---
layout: post
title: "Tutorial on CubicHermiteSpline.jl"
subheadline: "Perform cubic Hermite spline interpolation in Julia"
description: "This is a tutorial on how to use the Julia package CubicHermiteSpline.jl, which performs a [cubic Hermite spline interpolation](https://en.wikipedia.org/wiki/Cubic_Hermite_spline) on an array of data points given that their associated gradients at each point are known in advance."
author: lyx
date: 2020-06-19
modified: 2020-08-25
image:
    feature: false
    twitter: CubicHermiteSpline/twitter.png
categories: [Software, Tutorial]
tags: [Julia, CubicHermiteSpline.jl, PhaseDiagram.jl, Algorithms]
show_meta:
    info: true
---

This is a tutorial on how to use the Julia package [CubicHermiteSpline.jl](https://github.com/liuyxpp/CubicHermiteSpline.jl), which performs a [cubic Hermite spline interpolation](https://en.wikipedia.org/wiki/Cubic_Hermite_spline) on an array of data points, $(x_i, y_i)$, given that their associated gradients, $k_i=(dy/dx)_i$, are known in advance.

New: v0.2.2 can now compute the 1st order derivative of the interpolated function.

<!--more-->

{% include toc.md panel=true %}

## Getting started

First, the package can be easily installed from the Julia REPL:

```console?lang=julia
julia> using Pkg
julia> Pkg.add("CubicHermiteSpline")
```

Or in the package mode (typing `]` in REPL):

```console?lang=julia
(v1.5) pkg> add CubicHermiteSpline
```

Then you can load the package:

```julia
using CubicHermiteSpline
import Plots
using Plots: plot, plot!
using LaTeXStrings
```

Plotting related packages are also loaded. Let's tweak the appearance of our plots:

```julia
Plots.default(size=(600, 370))
fntf = :Helvetica
titlefont = Plots.font(fntf, pointsize=12)
guidefont = Plots.font(fntf, pointsize=12)
tickfont = Plots.font(fntf, pointsize=9)
legendfont = Plots.font(fntf, pointsize=8)
Plots.default(fontfamily=fntf)
Plots.default(titlefont=titlefont, guidefont=guidefont, tickfont=tickfont, legendfont=legendfont)
Plots.default(minorticks=true)
Plots.default(linewidth=1.2)
Plots.default(foreground_color_legend=nothing)
Plots.default(legend=false)
```

Now we are ready to go.

## Example 1: interpolating cubic polynomial

The cubic polynomial of the form

$$
    f(x) = ax^3 + bx^2 + cx + d
$$

should be exactly interpolated by the cubic Hermite spline interpolation.

Below we use CubicHermiteSpline.jl to demonstrate this fact. First we define a typical cubic polynomial:

```julia
f(x) = x^3 - 3x^2 + 2x - 5;
```

Its gradient are available in an analytical form as

```julia
df(x) = 3x^2 - 6x + 2;
```

The exact cubic polynomial is evaluated at evenly spaced points.

```julia
a = 0.0
b = 2.5
x_exact = range(a, b, step=0.01);
y_exact = f.(x_exact);
k_exact = df.(x_exact);

plot(x_exact, y_exact)
```

The exact cubic polynomial is plotted.

```julia
xlabel = L"x"
ylabel = L"f(x)"
plot(x_exact, y_exact, xlabel=xlabel, ylabel=ylabel)
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_9_0.svg" alt="Cubic polynomial." width="600px">
</figure>

Generate a set of data points to be interpolated in the cubic polynomial curve on a evenly spaced grid:

```julia
x_input = range(a, b, step=0.5);
y_input = f.(x_input);
k_input = df.(x_input);
```

Create an interpolation instance:

```julia
spl = CubicHermiteSplineInterpolation(x_input, y_input, k_input);
```

Perform the actual cubic Hermite spline interpolation:

```julia
x_interp = range(a, b, step=0.01);
y_interp = spl(x_interp);
```

Plotting input data points, exact solution, and the interpolated result in a single plot shows that the interpolation is exact for cubic polynomials.

```julia
Plots.scatter(x_input, y_input, label="input data", legend=:topleft)
plot!(x_exact, y_exact, label="exact")
plot!(x_interp, y_interp, label="interpolated")
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_17_0.svg" alt="Interpolation on even grid." width="600px">
</figure>

Interpolate the gradients of the cubic polynomial

```julia
k_interp = spl(x_interp; grad=true);
```

The results are plotted.

```julia
Plots.scatter(x_input, k_input, xlabel=xlabel, ylabel=L"f'(x)", label="input data", legend=:topleft)
plot!(x_exact, k_exact, label="exact")
plot!(x_interp, k_interp, label="interpolated")
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_19_0.svg" alt="Interpolated gradients on even grid." width="600px">
</figure>

Do the interpolation again for data points on an irregular grid:

```julia
x_input = [a, 0.1, 0.6, 1.75, b];
y_input = f.(x_input);
k_input = df.(x_input);

spl = CubicHermiteSplineInterpolation(x_input, y_input, k_input);

x_interp = range(a, b, step=0.01);
y_interp = spl(x_interp);

Plots.scatter(x_input, y_input, label="input data", legend=:topleft)
plot!(x_exact, y_exact, label="exact")
plot!(x_interp, y_interp, label="interpolated")
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_21_0.svg" alt="Interpolation on uneven grid." width="600px">
</figure>

Also compute the 1st order derivative of the interpolated function.

```julia
k_interp = spl(x_interp; grad=true);

Plots.scatter(x_input, k_input, xlabel=xlabel, ylabel=L"f'(x)", label="input data", legend=:topleft)
plot!(x_exact, k_exact, label="exact")
plot!(x_interp, k_interp, label="interpolated")
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_22_0.svg" alt="Interpolated gradients on uneven grid." width="600px">
</figure>

## Example 2: interpolating smooth functions

Here we use the [spherical bessel function of the first kind](https://mathworld.wolfram.com/SphericalBesselFunctionoftheFirstKind.html):

$$
    j_1(x) = \frac{\sin x - x\cos x}{x^2}.
$$

Below we show that the cubic Hermite spline performs impressively well for interpolating such smooth functions.

```julia
g(x) = (sin(x) - x*cos(x)) / x^2;

# dg(x) = ((x^2 - 2) * sin(x) + 2x*cos(x)) / x^3;
dg(x) = (sin(x) - 2*g(x)) / x;

a = 0.01
b = 8.01
x_exact = range(a, b, step=0.01);
y_exact = g.(x_exact);

ylabel = L"g(x)"
plot(x_exact, y_exact, xlabel=xlabel, ylabel=ylabel)
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_27_0.svg" alt="spherical bessel function of the first kind." width="600px">
</figure>

Perform cubic Hermite interpolation on an even grid:

```julia
x_input = range(a, b, step=0.5);
y_input = g.(x_input);
k_input = dg.(x_input);

spl = CubicHermiteSplineInterpolation(x_input, y_input, k_input);

x_interp = range(a, b, step=0.01);
y_interp = spl(x_interp);

Plots.scatter(x_input, y_input, xlabel=xlabel, ylabel=ylabel, label="input data", legend=:topright)
plot!(x_exact, y_exact, label="exact")
plot!(x_interp, y_interp, label="interpolated")
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_31_0.svg" alt="Interpolation on even grid." width="600px">
</figure>

Compute the interpolated gradients of the target function.

```julia
k_interp = spl(x_interp; grad=true);

Plots.scatter(x_input, k_input, xlabel=xlabel, ylabel=L"g'(x)", label="input data", legend=:topright)
plot!(x_exact, k_exact, label="exact")
plot!(x_interp, k_interp, label="interpolated")
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_32_0.svg" alt="Interpolated gradients on even grid." width="600px">
</figure>

It can be seen from above plot that interpolation on data points and gradients works perfectly for known data points on a dense even grid.

Interpolate the function on an unevenly spaced grid:

```julia
x_input = [a, 0.6, 1.5, 3.4, 4.5, 5.0, 6.2, 7.5, b];
y_input = g.(x_input);
k_input = dg.(x_input);

spl = CubicHermiteSplineInterpolation(x_input, y_input, k_input);

x_interp = range(a, b, step=0.01);
y_interp = spl(x_interp);

Plots.scatter(x_input, y_input, xlabel=xlabel, ylabel=ylabel, label="input data", legend=:topright)
plot!(x_exact, y_exact, label="exact")
plot!(x_interp, y_interp, label="interpolated")
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_34_0.svg" alt="Interpolation on uneven grid." width="600px">
</figure>

The gradients of the target function can be also interpolated.

```julia
k_interp = spl(x_interp; grad=true);

Plots.scatter(x_input, k_input, xlabel=xlabel, ylabel=L"g'(x)", label="input data", legend=:topright)
plot!(x_exact, k_exact, label="exact")
plot!(x_interp, k_interp, label="interpolated")
```

<figure class="image">
    <img src="{{ site.url }}/images/CubicHermiteSpline/output_36_0.svg" alt="Interpolated gradients on uneven grid." width="600px">
</figure>

Note that the accuracy of the interpolation degrades near the extrema of the function if there is no input data point near that region.

## Available methods

- Interpolation

```julia
# `spl` is an instance of `CubicHermiteSplineInterpolation`.
# `x` can be a real number of an 1D array of real numbers.
# Following two methods are equivalent.
spl(x; grad=false)
interp(spl, x)
```

- Interpolated gradients

```julia
spl(x; grad=true)
grad(spl, x)
```

## Acknowledgements

- This work is partially supported by the General Program of the National Natural Science Foundation of China (No. 21873021) and Shanghai Pujiang Program (No. 18PJ1401200).