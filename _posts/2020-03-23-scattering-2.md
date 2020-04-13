---
layout: post
title: "Julia in Practice: Building Scattering.jl from Scratch (2)"
subheadline: "The shape of scattering peaks and essential Julia language features"
description: "In this post we implement a submodule peak.jl to model the shape of the scattering peaks."
author: lyx
date: 2020-03-23
modified: 2019-04-09
image:
    feature: false
    twitter: scattering2/all-L.png
categories: [Research, Software]
tags: [Julia, Scattering.jl, Scattering Theory]
show_meta:
    info: true
---

In this post we will implement a submodule, `peak.jl`, to model the shape of scattering peaks. Essential Julia language features will be introduced along the development of the submodule. You shall learn types, constructors, functions, methods, functors, modules, testing, and benchmarking after reading this post.

<!--more-->

{% include toc.md panel=true %}

## Shape of the Scattering Peak
For a perfect periodic lattice, *i.e.* a single crystal, as will be derived in later posts, the shape of the scattering peak has the form

$$
\begin{equation}
    L(x) = \frac{\sin^2(Nx/2)}{N^2\sin^2(x/2)}
\end{equation}\label{eq:L-raw}
$$

where $N$ is number of unit cells which also determines the grain size of a single crystal. As the number of unit cells increases, more cells interfere constructively and the scattering peak becomes sharper. The trend has been shown in Figure 1. Note that we have shifted the peak position to $x=2$ since in scattering the peak position is always positive.

<figure class="image">
    <img src="{{ site.url }}/images/scattering2/raw-L.svg" alt="The shape of the scattering peak." width="500px">
    <figcaption>Figure 1. The shape of the scattering peak described by Eq.\eqref{eq:L-raw}.</figcaption>
</figure>

Note that $N$ in the denominator of $L(x)$ is introduced to normalize the function. Although the function oscillates strongly  beyond  the  central  lobe, these oscillations  are  usually insignificant and can be safely  ignored for common crystal grain size ($N$ > 50). In practice, however, it is more convenient to choose other non-oscillating peak shapes to simulate the actual one. Gaussian and Lorentzian peaks are two popular choices. The Gaussian peak is defined as

$$
\begin{equation}
    L(x) = \frac{2}{\pi\delta}\exp\left( -\frac{4x^2}{\pi\delta^2} \right)
\end{equation}\label{eq:L-gauss}
$$

where the peak width (full-width at half-maximum, $h$) depends on the parameter $\delta$ as $h = \sqrt{\pi\ln2}\delta$. Note that we use a specialized form for the Gaussian distribution to be compatible with the following introduced generalized peak. The Lorentzian peak is

$$
\begin{equation}
    L(x) = \frac{\delta/2\pi}{x^2 + (\delta/2)^2}
\end{equation}\label{eq:L-loren}
$$

where the peak width is simply $h = \delta$. A more generalized peak shape function has been proposed in the literature[^Yager2013], which can be seen as a mixture of the Gaussian and Lorentzian peaks. It has the form

$$
\begin{equation}
    L(x) = \frac{2}{\pi\delta} \prod_{n=0}^{\infty} \left( 1 + \frac{\gamma_{\nu}^2}{(n+\nu/2)^2}\frac{4x^2}{\pi^2\delta^2} \right)^{-1}
\end{equation}\label{eq:L-general}
$$

where the parameter is a ratio of gamma functions

$$
\begin{equation}
     \gamma_{\nu} = \sqrt{\pi}\frac{\Gamma[(\nu+1)/2]}{\Gamma(\nu/2)}
\end{equation}\label{eq:gamma-nu}
$$

Its peak width is also $h = \delta$. The general peak shape has the property that it reduces to the Gaussian peak in the form of Eq.\eqref{eq:L-gauss} in the limit of $\nu \to \infty$, while it approaches to the Lorentzian peak in the form of Eq.\eqref{eq:L-loren} as $\nu \to 0$. Therefore, the parameter $\nu$ controls the shape of the generalized peak. This versatile peak shape allows one to account for the various contributions to peak broadening (instrumental resolution, grain size, grain shape, microstrain).

## Implementation
Now we will dive into the implementation details. We will use this opportunity to introduce some core language features about Julia. You will see that it is quite neat to use Julia to do the work.

### Types
The shape of the scattering peak is fully specified by two parameters, $\nu$ and $\delta$. When $\nu$ is bigger than a threshold value $\nu_{max}$, we use the Gaussian peak to approximate the generalized peak. And when $\nu$ is smaller than a threshold value $\nu_{min}$, we use the Lorentzian peak instead of the generalized peak. Therefore, we have to implement three **types** of peaks, which is natural to define a Julia `type` for each one. And they shall all inherit from an `abstract type` that unifies the interface to produce a specific peak shape.

In Julia, we can define an *abstract* type as

{% highlight julia linenos %}
abstract type ScatteringPeak end
{% endhighlight %}

Now we can define a *concrete* Gaussian peak type inherited from it as

{% highlight julia linenos %}
struct GaussianPeak <: ScatteringPeak
    σ::Real # the variance
    μ::Real # the mean value, i.e. the position of the peak
end
{% endhighlight %}

The first line states that the `GaussianPeak` type is inherited from the `ScatteringPeak` denoted by the symbol `<:`. Note that a concrete type such as `GaussianPeak` should be defined using a keyword `struct` other than `type`. The type has two fields, `σ` and `μ`. Here we plan to use the standard expression of the Gaussian peak:

$$
\begin{equation}
    L(x) = \frac{1}{\sqrt{2\pi}\sigma}\exp\left[ -\frac{(x-\mu)^2}{2\sigma^2} \right]
\end{equation}\label{eq:gauss}
$$

Thus, we have to do a conversion between eq.\eqref{eq:L-gauss} and eq.\eqref{eq:gauss} using $\delta = \sqrt{\frac{8}{\pi}}\sigma$ and $\mu=0$.

Similarly, we can define a Lorentzian type

{% highlight julia linenos %}
struct LorentzianPeak <: ScatteringPeak
    δ::Real # the peak width
    μ::Real # the center of the peak
end
{% endhighlight %}

and a generalized peak type

{% highlight julia linenos %}
struct GeneralizedPeak <: ScatteringPeak
    δ::Real # the variance
    ν::Real # the mean value, i.e. the position of the peak
    γν::Real # = √π * Γ[(ν+1)/2] / Γ(ν/2)
    γνhalf::Real # = Γ(ν/2)
end
{% endhighlight %}

Note that besides `δ` and `ν`, we have two more fields `γν` and `γνhalf` which store precomputed parameters in eq.\eqref{eq:gamma-nu} to save some time for later computations.

### Constructors
Just as in `C++`, a **constructor** is a special function that use the type name as its name and create an instance of that type (instantiate an instance). Julia provides default constructors for all user-defined types, which accept the equal number of arguments as the number of its fields. Sometimes, however, it is convenient to custom our own constructors. Julia allows unlimited number of constructor for a type. For example, for the `GaussianPeak` type, the mean value parameter $\mu$ is commonly set to 0, so it is convenient to provide a constructor which takes only one arguments which provides the value of $\sigma$:

{% highlight julia linenos %}
function GaussianPeak(σ::Real, μ::Real=0)
    @assert(σ > 0, "The variance must be positive.")
    new(σ, μ)
end
{% endhighlight %}

Now, we can initiate an instance as

{% highlight julia linenos %}
p = GaussianPeak(0.1)
{% endhighlight %}

Using default constructor, we have to do the following

{% highlight julia linenos %}
p = GaussianPeak(0.1, 0.0)
{% endhighlight %}

Our own constructor also checks the value of $\sigma$, ensuring its value is positive. We can write a similar constructor for the `LorentzianPeak` type.

Constructors like above are put outside of the definition of its corresponding type. They are **outer constructors**. When only outer constructors are presented for a type, the default constructor provided by Julia is still working. However, sometimes it is better to disable the default constructor when we don't want user to provide values for some fields explicitly. For example, the fields `γν` and `γνhalf` both depend on another field `ν`. To ensure the consistency in the instance, we don't want users of our package to initialize the `GeneralizedPeak` type using the default constructor. To this end, we can define an **internal constructor** which will override the default one:

{% highlight julia linenos %}
struct GeneralizedPeak <: ScatteringPeak
    δ::Real # the variance
    ν::Real # the mean value, i.e. the position of the peak
    γν::Real # = √π * Γ[(ν+1)/2] / Γ(ν/2)
    γνhalf::Real # = Γ(ν/2)
    function GeneralizedPeak(δ::Real, ν::Real)
        @assert(δ > 0, "The peak width must be positive.")
        @assert(ν > 0, "The peak shape parameter must be positive.")
        γνhalf = gamma(ν/2)
        γν = √π * gamma((ν+1)/2) / γνhalf
        new(δ, ν, γν, γνhalf)
    end
end
{% endhighlight %}

With above definition, we can only initiate a `GeneralizedPeak` instance using

{% highlight julia linenos %}
p = GeneralizedPeak(0.1, 1.0)
{% endhighlight %}

and following attempt will fail

{% highlight julia linenos %}
p = GeneralizedPeak(0.1, 1.0, 0.0, 0.0)
{% endhighlight %}

### Functions
It is useful to provide a unified interface to create a correct `ScatteringPeak` instance based on the values of $\delta$ and $\nu$. We can write a function for this purpose

{% highlight julia linenos %}
function peak(δ::Real, ν::Real)
    if ν < 0.01
        LorentzianPeak(δ)
    elseif ν > 200
        σ = √(π/8) * δ
        GaussianPeak(σ)
    else
        GeneralizedPeak(δ, ν)
    end
end
{% endhighlight %}

It accepts two real numbers and returns a correct `ScatteringPeak` instance accordingly. Note that we have set $\nu_{min}=0.01$ and $\nu_{max}=200$. Also a conversion has been done for the `GaussianPeak` instance in line 5.

### Tests
We can verify the `peak` in the Julia REPL

{% highlight julia linenos %}
julia> p = peak(0.1, 1.0);
julia> typeof(p)
# GeneralizedPeak
{% endhighlight %}

There is also a very useful package, `Test.jl`, which provides functionalities to facilitate the testing work. We can perform a test as

{% highlight julia linenos %}
julia> using Test
julia> p = peak(0.1, 1.0);
julia> @test typeof(p) isa GeneralizedPeak
# Test Passed
{% endhighlight %}

In the above, we first import the `Test` package use `using` keyword. Then `@test` macro is used to verify that the instance created by the `peak` function is a `GeneralizedPeak` peak as expected (since $\nu_{min} < \nu = 1.0 < \nu_{max}$).

### Methods
Now it is time for us to add the essential part of each type: to actually create a peak. We shall use Julia `method`s. A `method` is a special function whose arguments are marked with explicit types. A `function` can have many `method`s. Therefore, a method can be viewed as a specific instance of a function.

{% highlight julia linenos %}
peakshape(p::LorentzianPeak, x) = @. (p.δ/(2π)) / ((x-p.μ)^2 .+ (p.δ/2)^2)
peakshape(p::GaussianPeak, x) = @. exp(-(x-p.μ)^2/(2p.σ^2)) / (√(2π)*p.σ)
peakshape(p::GeneralizedPeak, x; tol::Real=1e-4, nmax::Integer=2000) = [compute_single_point(p, x[i], tol, nmax) for i in 1:length(x)]
{% endhighlight %}

Above codes define three methods all named `peakshape` for three types of scattering peak, respectively. Note that the keyword `function` can be omitted when the function body can be written in one line (one-liner). This greatly reduces the redundancy of the code and make the code looks extremely clean. The `@.` macro broadcast all operations to every elements of an array-like object. The implementation of `compute_single_point` will be presented in the following subsection.

Using these `peakshape` methods, we can now compute any type of scattering peaks, such as:

{% highlight julia linenos %}
julia> p = peak(0.1, 1.0);
julia> q = collect(0.001:0.001:4.0);
julia> qhkl = 2.0;
julia> qs = q .- qhkl;
julia> peakshape(p, qs)
# produce a generalized peak with its peak locates at q = 2.0
{% endhighlight %}

The Julia compiler first deduces the type of instance `p`, which is `GeneralizedPeak` in the above example. Then it will dispatch it to the correct version of the `peakshape` method, which is the third one in the example.

We can compare these types of scattering peaks by plotting them together as shown in Figure 2.

<figure class="image">
    <img src="{{ site.url }}/images/scattering2/all-L.svg" alt="" width="500px">
    <figcaption>Figure 2. A comparison of various scattering peaks.</figcaption>
</figure>

It is obvious that the `GeneralizedPeak` is indeed a mixture of other two types.

### Functors
Methods are associated with types, so it is possible to make any arbitrary Julia object "callable" by adding methods to its type. Such "callable" objects are sometimes called *functors*. Since the only  functionality of the `ScatteringPeak` type is computing the peak shape, the functor fits this use case perfectly. For example, we can define functors as

{% highlight julia linenos %}
(p::ScatteringPeak)(x) = peakshape(p, x)
{% endhighlight %}

The functor is a function without name and its only argument is a type instance. Now we can compute the peak simply using

{% highlight julia linenos %}
julia> p(qs)
{% endhighlight %}

where `p` is a `<:ScatteringPeak` instance and `qs` is an array of $x$ values.

### Benchmark and Performance
To compute a generalized peak, we have to evaluate an infinite product series in Eq.\eqref{eq:L-general}. By doing some numerical experiments, we learn that the series converges fast near and far away from the peak, but it converges much slower in between (around peak shoulder). So we have to allow the number of terms varying during computation. A tolerance is set to control the minimum number of terms for each $x$ value. The implementation is given below

{% highlight julia linenos %}
function compute_single_point(p::GeneralizedPeak, q::Real; tol::Real=1e-4, nmax::Integer=2000)
    c = 2/(p.δ*π)
    s = c
    s_prev = 0.0
    ds = 1.0
    n = 0
    while ds > tol && n < nmax
        s_prev = s
        t1 = (p.γν/(n+p.ν/2))^2
        t2 = (c * q)^2
        s /= (1 + t1*t2)
        ds = abs(s - s_prev)
        n += 1
    end
    s
end
{% endhighlight %}

This is the only computation intensive method in this submodule. To ensure its performance, we can run some benchmarks. Julia core provides a `@time` macro which can estimate the computation time of a method. However, its results are known to be disturbed by environment settings. So it is not quite reliable. The `BenchmarkTools.jl` package, on the other hand, provide a reliable macro `@btime` that isolates the environment. We can check out the performance of our code by running

{% highlight julia linenos %}
julia> using BenchmarkTools
julia> p = peak(0.1, 1.0);
julia> @btime compute_single_point($p, 0.2)
# 11.xx μs (xx allocations: xx bytes)
{% endhighlight %}

Julia also provides a macro `@code_warntype` which helps us to identify the *type instability* issue. Using `@code_warntype`, it shows that our current implementation of `compute_single_point` is not optimized.

{% highlight julia linenos %}
julia> @code_warntype compute_single_point(p, 0.2)
# pseudo codes presented here.
{% endhighlight %}

From the output of above `@code_warntype`, we can observe that Julia compiler cannot infer the types of `c`, `s`, `s_prev`, and `ds` due to the lack of type information of `p.δ`. To solve this issue, we should re-define `GaussianPeak`, `LorentzianPeak` and `GeneralizedPeak` to accept a type parameter which defines the type of their internal fields. For example,

{% highlight julia linenos %}
struct GaussianPeak{T<:Real} <: ScatteringPeak
    σ::T # the variance
    μ::T # the mean value, i.e. the position of the peak
end
{% endhighlight %}

We should also update its constructor

{% highlight julia linenos %}
function GaussianPeak(σ::T, μ::T=zero(T)) where {T<:Real}
    @assert(σ > 0, "The variance must be positive.")
    new{T}(σ, μ)
end
{% endhighlight %}

After all refactoring work is done, we re-run `@code_warntype` and will notice that all types are inferred by the compiler successfully. Using `@btime` to benchmark again, we will notice that the running time is only 207 ns which is 50 times faster!

## Modules
The above codes are organized into a submodule and put in a single file named `peak.jl`

{% highlight julia linenos %}
module Peak

using SpecialFunctions # for gamma function

# all other codes ...

end
{% endhighlight %}

We use the `gamma` function in the `SpecialFunctions.jl` package to compute the $\Gamma$ function in Eq.\eqref{eq:gamma-nu}.

We will create a new file `Scattering.jl` to organize all its submodules and export Julia objects.

{% highlight julia linenos %}
module ScatteringPeak

include("peak.jl")

using .Peak: ScatteringPeak, GaussianPeak, LorentzianPeak, GeneralizedPeak, peak
export ScatteringPeak, GaussianPeak, LorentzianPeak, GeneralizedPeak
export peak

end
{% endhighlight %}

Currently, only the `Peak` submodule is included and exported.

## Usage
Now we can generate a peak using the `Scattering.jl` package as follows

```console?lang=julia
julia> using Scattering
julia> p = peak(0.1, 1.0);
julia> qs = collect(0.001:0.001:4.0) .- 2.0
julia> p(qs) # peak is generated here
```

## Acknowledgements
This work is partially supported by the General Program of the National Natural Science Foundation of China (No. 21873021).

## References

[^Yager2013]: Yager, K. G.; Zhang, Y.; Lu, F.; Gang, O. Periodic Lattices of Arbitrary Nano-Objects: Modeling and Applications for Self-Assembled Systems. *J. Appl. Crystallogr.* **2013**, *47*, 118–129.

