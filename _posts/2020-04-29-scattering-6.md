---
layout: post
title: "Julia in Practice: Building Scattering.jl from Scratch (6)"
subheadline: "Form factor of a homogeneous sphere"
description: "In this post we will first coin the term form factor for arbitrary particles by generalizing the idea of the atomic form factor. We then derive an analytical expression for the form factor of a homogeneous sphere. The functionality is implemented in two submodules: scatterer.jl and formfactor.jl."
author: lyx
date: 2020-04-29
modified: 2020-04-29
image:
    feature: false
    twitter: scattering6/Iq_sphere_ylog.png
categories: [Research, Software, Tutorial]
tags: [Julia, Scattering.jl, scattering theory, form factor]
show_meta:
    info: true
---

In this post we will first coin the term *form factor* for arbitrary particles by generalizing the idea of the atomic form factor. We then derive an analytical expression for the form factor of a homogeneous sphere. The functionality is implemented in two submodules: `scatterer.jl` and `formfactor.jl`. These two modules will be gradually extended by adding more types of particles as the project goes on.

<!--more-->

{% include toc.md panel=true %}

## Form Factor

In this section will generalize the strategy described in the [previous post]({% post_url 2020-04-23-scattering-5 %}) to arbitrary *particles* consisting of any type of building blocks, such as electrons, atoms, molecules, complexes, polymers, nanoparticles, *etc.*, as long as they themselves can be viewed as basic building blocks of the sample. We will see that such generalization eventually lead to the concept of *form factor*. Just as we call the amplitude of the x-ray scattering from an atom as *atomic form factor*, we will term the amplitude of the x-ray scattering from any particle as the **form factor** of the particle and denoted as $F(\vq)$. Note that, however, this quantity is usually termed as form factor amplitude in the literature. And the quantity $F(\vq)F^*(\vq)$ is instead termed as the form factor. _Throughout this project, we will stick to the convention that $F(\vq)$ is called form factor._

### General formula

The strategy presented in the [previous post]({% post_url 2020-04-23-scattering-5 %}) demonstrates that the amplitude of the x-ray scattering from multiple atoms can be derived from the amplitude of the scattering from its building blocks, *i.e.* a single atom, which in turn can be derived from the amplitde of the scattering from its building blocks, *i.e.* a single electron. It seems that there is a recursive relation between these amplitudes. To see it clearly, we shall rewrite the *normalized* amplitude of the x-ray scattering from a single electron as

$$
\begin{equation}
    F_e(\vq) = \frac{A_e}{A_0} = b_e = \int d\vr\; \rho_e(\vr) e^{-i\vq\cdot\vr}
\end{equation}\label{eq:Fe}
$$

where $b_e$ is the scattering length of an electron. And $\rho_e(\vr)$ is the scattering length density distribution of an electron which is

$$
\begin{equation}
    \rho_e(\vr) = F_0 \delta(\vr).
\end{equation}\label{eq:rhoe}
$$

where $F_0=b_e$ and $\delta(x)$ is a delta function. The *normalized* amplitude of the x-ray scattering from a single atom can also be rewritten as

$$
\begin{equation}
    F_a(\vq) = \frac{A_a}{A_0} = \int d\vr\; \rho_a(\vr) e^{-i\vq\cdot\vr}
\end{equation}\label{eq:Fa}
$$

where $\rho_a(\vr)$ is the scattering length density distribution of the atom, which is defined as

$$
\begin{equation}
    \rho_a(\vr) = F_e n_e(\vr).
\end{equation}\label{eq:rhoa}
$$

where $n_e(\vr)$ is the number density of the electrons within an atom. The *normalized* amplitude of the x-ray scattering from a *particle* (multiple atoms in a certain volume) consisting of $M$ types of atoms can be rewritten as

$$
\begin{equation}
    F_p(\vq) = \frac{A_p}{A_0} = \int d\vr\; \rho_p(\vr) e^{-i\vq\cdot\vr}
\end{equation}\label{eq:Fp}
$$

where $\rho_p(\vr)$ is the scattering length density distribution of the particle, which is defined as

$$
\begin{equation}
    \rho_p(\vr) = \sum_{\alpha=1}^{M} F_{a\alpha} n_{a\alpha}(\vr)
\end{equation}\label{eq:rhop}
$$

where $F_{a\alpha}$ is the normalized amplitude contributed by the atom of type $\alpha$, each is given by eq.\eqref{eq:Fa}, and $n_{a\alpha}(\vr)$ is the number density of the atom of type $\alpha$ within the particle. When the particle consists of only one type of atom, eq.\eqref{eq:rhop} is simply

$$
\begin{equation}
    \rho_p(\vr) = F_a n_a(\vr)
\end{equation}\label{eq:rhop2}
$$

It is now ready for us to explore the structure of the normalized amplitude of a particle. The building block of a particle is atoms. The building block of an atom is electrons. We can find the normalized amplitude of a particle using a top-down approach, by following the chain $F_p \to \rho_p \to F_a \to \rho_a \to F_e$, *i.e.* by using the above equations in a reverse order. Therefore, the normalized amplitude is a universal quantity that is associated to the scatterer we are looking at. In the literature, it is termed as the **form factor** of the scatterer, just as the *atomic form factor* for an atom.

Suppose a sample we are interested in consists of $M$ types of building blocks. Each building block can be any chemical or physical objects, such as electrons, atoms, molecules, complexes, polymers, nanoparticles *etc.*. Then the form factor of the sample can be written in a general form

$$
\begin{equation}
    F(\vq) = \frac{A}{A_0} = \int d\vr\; \rho(\vr) e^{-i\vq\cdot\vr}
\end{equation}\label{eq:F}
$$

where $\rho(\vr)$ is the scattering length density distribution of the sample which is given by

$$
\begin{equation}
    \rho(\vr) = \sum_{\alpha=1}^{M} F_{b\alpha} n_{b\alpha}(\vr)
\end{equation}\label{eq:rho}
$$

Here $n_{b\alpha}(\vr)$ is the number density of the $\alpha$th building block of the sample with its center located at position $\vr$. $F_{b\alpha}$ is the form factor of the $\alpha$th building block of the sample. *Note that, in general, $F_{b\alpha}$ is a function of $\vq$.* To find $F_{b\alpha}$ for each building block, we will use eq.\eqref{eq:F} and eq.\eqref{eq:rho} in a recursive manner.

The scattering intensity which is directly measured in experiments is the differential scattering cross section:

$$
\begin{equation}
    I(\vq) = \frac{J_\Omega}{J_0} = \frac{\abs{A}^2}{\abs{A_0}^2} = FF^*
\end{equation}\label{eq:I}
$$

By viewing eq.\eqref{eq:I}, we conclude that the **form factor** is the most fundamental quantity in scattering experiments, while the **structure factor** is a derived quantity from the form factor.

Note that, in some cases, such as polymers, the building blocks are highly correlated. Time average or ensemble average should be performed to obtain the scattering intensity. In these cases, the scattering intensity is proportional to the Fourier transform of the correlation function $\ensemble{n(\vr)n(\vr')}$, just as in the case of polymeric systems. Therefore, eq.\eqref{eq:I} is not applicable in these situations.

Also note that, in the polymer community, due to the fact mentioned above, the term *form factor* is commonly referred to the **square** of the normalized amplitude, which is proportional to the scattering intensity.

### Form factor of a homogeneous sphere

The simplest scatterer (except that of an electron which is just the scattering length $b_e$) is a homogeneous sphere. Here, the word <q>homogeneous</q> has a specific meaning that the scattering length density distribution $\rho(\vr)$ is a constant function across the whole volume of the sphere, $\rho(\vr)=\rho_0$. Note that it is only possible that the scattering angle should be quite small because $b_e \sim (1+\cos^22\theta)^{1/2}$ becomes a constant only in the limit of $\theta \to 0$. This is also the reason why the form factor of a homogeneous sphere is mostly interested and studied in the small-angle scattering (SAS) community. For small-angle x-ray scattering (SAXS) experiments, the radius of the sphere should be at least in nanoscale.

To compute the form factor of the homogeneous sphere, it is most convenient to use a spherical coordinate system $(r, \theta, \phi)$. We put the center of the sphere at the origin. The homogeneous sphere is spherical symmetric, which enables us choose its polar axis freely. The simplest choice is to let the direction of $\vq$ and the polar axis coincide. In such setup, we have

$$
    \vq \cdot \vr = qr\cos\theta
$$

And the form factor written in eq.\eqref{eq:F} is evaluated as

$$
\begin{split}
    F(q) &= 4\pi\int_0^R dr\; \rho_0r^2\frac{\sin(qr)}{qr} \\
         &= \frac{4\pi\rho_0}{q}\int_0^R dr\; r\sin(qr) \\
         &= -\frac{4\pi\rho_0}{q^2} \int_0^R dr\; rd\cos(qr) \\
         &= -\frac{4\pi\rho_0}{q^2} \left[ r\cos(qr)\rvert_0^R - \int_0^R dr\; \cos(qr) \right] \\
         &= -\frac{4\pi\rho_0}{q^2} \left[ R\cos(qR) - 0 - \frac{1}{q}\sin(qr)\rvert_0^R \right] \\
         &= -\frac{4\pi\rho_0}{q^2} \left[ R\cos(qR) - \frac{1}{q}\sin(qR) \right] \\
         &= 4\pi\rho_0 \frac{\sin(qR) - qR\cos(qR)}{q^3}
\end{split}
$$

or

$$
\begin{equation}
    F(q) = 3\rho_0V \frac{\sin(qR) - qR\cos(qR)}{(qR)^3}
\end{equation}\label{eq:Fsphere}
$$

where $V=4\pi R^3/3$ is the volume of the sphere. Note that the first line of the above equation directly adopts the result of eq.(35) derived in the [previous post]({% post_url 2020-04-23-scattering-5 %}). Noticing that the [spherical bessel function](https://mathworld.wolfram.com/SphericalBesselFunctionoftheFirstKind.html) of the first kind at order 1 is

$$
    j_1(z) = \frac{\sin z - z\cos z}{z^2}
$$

Inserting it into eq.\eqref{eq:Fsphere}, we have

$$
\begin{equation}
    F(q) = \rho_0V \frac{3j_1(qR)}{qR}
\end{equation}\label{eq:Fspherej1}
$$

And the intensity scattered by a single sphere is just

$$
\begin{equation}
    I(q) = \rho_0^2V^2 \left(\frac{3j_1(qR)}{qR}\right)^2
\end{equation}\label{eq:Isphere}
$$

## Implementation

We can compute the form factor of a particle using eq.\eqref{eq:F} and eq.\eqref{eq:rho}, given that the form factor and the number density distribution are known explicitly for its building blocks and all sub building blocks. We will call such particles **simple particles**. When at least one of these two quantities are *unknown* in explicit form, we will call it **complex particles**. Complex particles have internal structures and their building blocks correlate with each other. Special techniques have to be introduced to obtain the scattering of complex particles.

Examples of simple particles are atoms, basic geometric shapes with uniform scattering length density distribution (such as homogeneous spheres, cylinders, polyhedra, etc.), composite of non-interacting basic geometric shapes with uniform scattering length density distribution. Non-ineracting building blocks means their position and orientation are fixed. Composite particles consisting of simple particles are also simple particles if the number density distributions of each building block are known. Atoms are simple particles because the number density distribution of its building block which is the electron is available. We will see in the later posts that by using eq.\eqref{eq:F} and eq.\eqref{eq:rho}, we can easily compute the composite simple particles consisting of basic simple particles as their building blocks. It is a powerful insight. For example, the article by Senesi and Lee[^Senesi2015] becomes a special case of this approach.

Examples of complex particles are polymers and particles whose building blocks contain polymers. It is required to compute the correlation of the number density distribution of polymers' building blocks which are segments. Sometimes, analytical expression for the correlation of the number density distribution is available. Furthemore, for a correlated system, the correlation of the number density distribution is generally not equal to the square of the ensemble average of the number density distribution:

$$
\begin{equation}
    \ensemble{n(\vr)n(\vr')} \neq \ensemble{n(\vr)}^2
\end{equation}\label{eq:correlation}
$$

### scatterer.jl

Any matter that can scatter x-rays will have a form factor. We will first define an abstract type to represent all such matter.

```julia
abstract type AbstractScatterer end
```

Inheriting from it, two abstract types representing the sample and the particle are defined. The `AbstractSample` stands for the actual sample the experiment want to measure, while the `AbstractParticle` models the scattering components in the sample.

```julia
abstract type AbstractSample <: AbstractScatterer end
abstract type AbstractParticle <: AbstractScatterer end
```

According to our previous discussion, the particle is further categorized into following two types. The way of computing the form factors of these two types of particles are quite different.

```julia
abstract type SimpleParticle <: AbstractParticle end
abstract type ComplexParticle <: AbstractParticle end
```

The homogeneous sphere is a simple particle. We can define it as follows

```julia
struct Sphere{T <: Real} <: SimpleParticle
    R::Float64 # radius
    V::Float64 # volume
    ρ::Float64 # scattering length density
    Δρ::Float64 # = ρ - ρ_ambient
    origin::RVector{T}
    function Sphere(R::Real, ρ::Real, Δρ::Real, origin::RVector{T}) where {T<:Real}
        @argcheck R > 0 DomainError
        @argcheck ρ > 0 DomainError
        new{T}(R, 4π*R^3/3, ρ, Δρ, RVector(origin))
    end
end
```

Since the homogeneous sphere is isotropic, it is not necessary to have a field for its orientation.

### formfactor.jl

It is straightforward to implement a method to compute the form factor of a homogeneous sphere using eq.\eqref{eq:Fsphere}.

```julia
function formfactor_basic(s::Sphere, q::Real)
    qR = q * s.R
    return s.Δρ * s.V * 3 * sphericalbesselj(1, qR) / qR
end
```

Here the suffix `basic` denotes that the homogeneous sphere is a **basic** simple particle which means that it has no building block. The `sphericalbesselj` function has been implemented in the `SpecialFunctions.jl` [package](https://github.com/JuliaMath/SpecialFunctions.jl).

## Usage

The usage of above submodules is straightforward. First, we create a homogeneous sphere with radius $1.0$ and uniform scattering length density $\rho=15.0$, locating at the origin. Assume that the scattering length density of the ambient is $0$.

```console?lang=julia
julia> s0 = Sphere(1.0, 15.0, 15.0, [0.0, 0.0, 0.0])
Sphere{Float64}(1.0, 4.1887902047863905, 15.0, 15.0, [0.0, 0.0, 0.0])
```

The form factor of this sphere at a single $q$ is computed as

```console?lang=julia
julia> formfactor_basic(s0, 1.0)
56.76895855490903
```

The form factor of this sphere in a range of $q$ values are obtained using

```console?lang=julia
julia> F = [formfactor_basic(s0, q) for q in 0.01:0.01:10];
```

And the scattering intensity is readily computed

```console?lang=julia
julia> I = abs2.(F);
```

Then the form factor and scattering intensity are plotted and shown below.

<figure class="image">
    <img src="{{ site.url }}/images/scattering6/Fq_sphere.svg" width="500px">
</figure>

<figure class="image">
    <img src="{{ site.url }}/images/scattering6/Fq_sphere_ylog.svg" width="500px">
</figure>

<figure class="image">
    <img src="{{ site.url }}/images/scattering6/Iq_sphere.svg" width="500px">
</figure>

<figure class="image">
    <img src="{{ site.url }}/images/scattering6/Iq_sphere_ylog.svg" width="500px">
</figure>

## Acknowledgements

This work is partially supported by the General Program of the National Natural Science Foundation of China (No. 21873021).

## Reference

[^Senesi2015]: Senesi, A.; Lee, B. Scattering Functions of Polyhedra. J. Appl. Crystallogr. 2015, 48, 565–577.
