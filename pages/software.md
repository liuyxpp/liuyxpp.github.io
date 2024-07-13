---
permalink: /software/
layout: page
title: Software
description: "A set of open source projects developed by Yi-Xin Liu research group."
header-img: images/software-1.jpg
comments: false
modified: 2024-07-07
breadcrumbs: true
---

Scientific software development plays a central role in our research group. Along with the ongoing research, we have developed various scientific computing software to carry out the actual tasks. The software are coded in various programming languages, such as Julia, C/C++, Python, Matlab, and Fortran. Currently, we are almost exclusively using Julia for new projects.

<figure class="first">
    <img src="{{ site.url }}/images/software.png" alt="">
</figure>

Some listed software are open sourced. More will be open sourced as they become mature. Please check our [github.com account](https://github.com/liuyxpp) for the latest updates.

<div markdown="0">
    <a href="{{ site.url }}/software/#polyorderjl" class="btn btn-danger">Polyorder.jl</a>
    <a href="{{ site.url }}/software/#scatteringjl" class="btn btn-danger">Scattering.jl</a>
    <a href="{{ site.url }}/software/#phasediagramjl" class="btn btn-danger">PhaseDiagram.jl</a>
</div>

<div markdown="0">
    <a href="{{ site.url }}/software/#polymerjl" class="btn btn-success">Polymer.jl</a>
    <a href="{{ site.url }}/software/#polymerarchitecturejl" class="btn btn-success">PolymerArchitecture.jl</a>
    <a href="{{ site.url }}/software/#cubichermitesplinejl" class="btn btn-success">CubicHermiteSpline.jl</a>
</div>

<div markdown="0">
    <a href="{{ site.url }}/software/#makiepublicationjl" class="btn btn-warning">MakiePublication.jl</a>
    <a href="{{ site.url }}/software/#polymerarchitecturemakiejl" class="btn btn-warning">PolymerArchitectureMakie.jl</a>
    <a href="{{ site.url }}/software/#mpltex" class="btn btn-warning">mpltex</a>
</div>

<div markdown="0">
    <a href="{{ site.url }}/software/#polyorder" class="btn btn-light">PolyOrder</a>
    <a href="{{ site.url }}/software/#cheb" class="btn btn-light">cheb++</a>
    <a href="{{ site.url }}/software/#gyroid" class="btn btn-light">gyroid</a>
    <a href="{{ site.url }}/software/#pydiagram" class="btn btn-light">pydiagram</a>
    <a href="{{ site.url }}/software/#scftpy" class="btn btn-light">scftpy</a>
    <a href="{{ site.url }}/software/#chebpy" class="btn btn-light">chebpy</a>
    <a href="{{ site.url }}/software/#ngpy" class="btn btn-light">ngpy</a>
</div>


## Scientific Computing Software & Packages

### Polyorder.jl
-----

Polyorder.jl is a pure Julia implementation of polymer self-consistent field theory, which is a successor of the C++ library [Polyorder]({{ site.url }}/software/#polyorder).

#### Features

* Support arbitrary noncyclic chain architectures.
* Support modern acceleration algorithms, such as Anderson mixing, GMRES, etc.
* Support all 1D, 2D, and 3D unit cells.
* Support specify all 1D, 2D, and 3D space groups.
* Support optimization of unit cell shape and size with advanced algorithms, such as variable cell shape optimization, etc.
* Support RPA analysis.
* Support arbitrary number of species and components, e.g. polymer solutions, polymer blends, etc.

### Scattering.jl
-----
Scattering.jl is a Julia package for computing scattering and diffraction of nanoparticles. The package is general in the sense that the scatterer can be either atoms, nano-particles, clusters of nano-particles, or even macro items, depending on the characteristic length scale you are focusing on.

#### Features

* Form factor of single particle.
* Form factor, structure factor, and scattering curves of a collection of particles and crystals.
* Translation, rotation, and symmetry operation on particles.
Unit cell and space group.

### PhaseDiagram.jl
-----

PhaseDiagram.jl is a Julia package for computing phase diagrams of block copolymers and their blends and solutions. For two- or multi-component systems, coexistence boundaries in addition to the phase boundaries will be computed. This package will ultimately replace [PyDiagram]({{ site.url }}/software/#pydiagram).

#### Features

* Computing phase diagrams for microphase separations of polymers.
* Computing phase diagrams for macrophase separations of polymer blends and solutions.

### Polymer.jl
-----

Polymer.jl defines a common interface to describe a polymer system. It is designed to be used in conjunction with other packages, such as [Polyorder.jl]({{ site.url }}/software/#polyorderjl), [Scattering.jl]({{ site.url }}/software/#scatteringjl), and [PhaseDiagram.jl]({{ site.url }}/software/#phasediagramjl).

#### Installation
This package is open sourced and registered in Julia General Registry. It can be installed in the Julia REPL as

```julia
julia > ]
pkg> add Polymer
```

The source code is available at [github.com](https://github.com/liuyxpp/Polymer.jl).

### PolymerArchitecture.jl
-----
PolymerArchitecture.jl provides a graph representation of the polymer architecture. To construct a graph representation, polymer systems should be described by the [Polymer.jl]({{ site.url }}/software/#polymerjl).

<!--Based on such representation, equivalent sub-architectures and semi-equivalent sub-architectures of a non-cyclic block copolymer chain can be identified automatically. Equivalent sub-architectures and semi-equivalent sub-architectures are useful for reducing the computational cost of polymer field-theoretic simulations.-->

### CubicHermiteSpline.jl
-----
CubicHermiteSpline.jl is a naive implementation of cubic Hermite spline interpolation for 1D data points in pure Julia. Currently, the 1st order gradient should be given by the user. It is most useful when the gradient happens to be available. When the function to be interpolated is smooth and the accuracy of the gradients is high, the cubic Hermite spline interpolation should perform extremely well. A demonstration of the power of this interpolation can be found here.

#### Features

* Univariate cubic Hermite spline interpolation for 1D data points (regular and irregular grids are both supported).
* Gradient (1st order derivative) of the interpolation. (New in version 0.2.0)
* Bivariate cubic Hermite spline interpolation for 2D data points (regular and irregular grids are both supported). (New in version 0.3.0)

#### Installation
This package is open sourced and registered in Julia General Registry. It can be installed in the Julia REPL as

```julia
julia > ]
pkg> add CubicHermiteSpline
```

The source code is available at [github.com](https://github.com/liuyxpp/CubicHermiteSpline.jl).

## Utility Software & Packages

### MakiePublication.jl
-----
[MakiePublication.jl](https://github.com/liuyxpp/MakiePublication.jl) is a Julia package for producing publication quality figures based on [Makie.jl](https://github.com/JuliaPlots/Makie.jl). It aims to provide equivalent functionalities as the Python package [mpltex](https://github.com/liuyxpp/mpltex).

Read the [full documentation here](http://www.yxliu.group/MakiePublication.jl/dev/).

#### Features

- Provide a collection of custom themes for journal publishers: ACS, APS, RSC.
- Custom theme for making figures suitable for web pages.
- 15 color palettes based on well-known quality color schemes with special tweaked ordering for scientific publishing. (since v0.3.0)
- Support hollow markers. (since v0.3.1)

### PolymerArchitectureMakie.jl
-----
PolymerArchitectureMakie.jl visualizes `BlockCopolymer` and `BlockCopolymerGraph` objects Based on GraphMakie.jl. It is designed to be used in conjunction with other packages, such as [PolymerArchitecture.jl]({{ site.url }}/software/#polymerarchitecturejl).

### mpltex
-----

`mpltex` is a python package for creating publication-quality plots using matplotlib. Inspired by [Olga Botvinnik](http://olgabotvinnik.com/)'s python package [prettyplotlib](https://github.com/olgabot/prettyplotlib).
`mpltex` now has **75 stars** and has been **forked 18** times at [github.com](https://github.com)!

#### Features

- Create plots for American Chemical Society.
- Create plots for presentation slides.
- Create plots for webpages.
- The color cycle is replaced by Tableau classic 10 color scheme which looks less saturated and more pleasing to eyes.
- enable cycle line styles and a selected set of line markers including hollow type markers.

#### Getting Started

- [Reading the tutorial]({% post_url 2014-09-09-mpltex %})

#### Links

- [mpltex source code](https://github.com/liuyxpp/mpltex)
- [mpltex PyPI page](https://pypi.python.org/pypi/mpltex)

## Legacy Software & Packages

### Polyorder
-----

`PolyOrder` is a C++ library which aims to ease the development of polymer self-consistent field theory (SCFT) programs. This software is deprecated and replaced by [Polyorder.jl]({{ site.url }}/software/#polyorderjl).

#### Features

* Flexibility. All components can be replaced.
* Extensibility. The OO design enables one add new features smoothly.
* Non-orthogonal unit cell calculations are supported.
* Weakly charged polymers are supported natively.

#### Getting Started

* [Introduction to the PolyOrder project]({{ site.url }}/downloads/polyorder20120628.pdf)
* [Configuration file format]({% post_url 2015-04-06-polyorder-config %})

<!--
### Links

* [PolyOrder source code](https://github.com/liuyxpp/polyorder)
-->

### cheb++
-----

`cheb++` is a C++ library which implements a set of functions dealing with Chebyshev polynomials.

#### Features

* Compute chebyshev differential matrix
* Compute derivatives of Chebyshev expanded functions
* Compute Clenshaw-Curtis quadrature
* Compute 1D interpolation based on Chebyshev-Gauss-Lobatto grid
* Work with `PolyOrder` seamlessly

#### Links

* [cheb++ source code](https://github.com/liuyxpp/cheb)

### scftpy
-----

`scftpy` is a python package for performing polymer self-consistent field theory calculations.

#### Features

* New features are experimented here before implemented in `PolyOrder`
* SCFT simulations of confined polymers.
* SCFT simulations of polymer brushes.

#### Links

* [scftpy source code](https://github.com/liuyxpp/scftpy)

### chebpy
-----

`chebpy` is a python package for spetral methods of PDEs based on Chebyshev series.

#### Features

* New features are experimented here before implemented in `cheb++`
* Chebyshev series construction
* Fast Chebyshev transform
* Chebyshev differentiation
* Chebyshev interpolation
* Chebyshev quadrature
* Chebyshev applications in solution of PDEs

#### Links

* [chebpy source code](https://github.com/liuyxpp/chebpy)

### PyDiagram
-----

`PyDiagram` is a python package for generating phase diagrams from results output by polymer field-theoretic simulations. PyDiagram also provides functions for analysis of simulation results.

#### Features

- Processor: support Polyorder and PolyFTS output files, and a general dgm file containing all simulation results.
- Plotter: provide plots of raw, invalid, phase boundary, and standard phase diagrams.
- Analyzer: the trend of the free energy, stretch-free cell size, and accuracy.
- A project configuration file provides full control of the processor, plotter, and analyzer.

<!--
### Links

- [PyDiagram source code](https://github.com/liuyxpp/pydiagram)
- [PyDiagram PyPI page](http://pypi.python.org/pypi/pydiagram)
-->

### Gyroid
-----

`gyroid` is a python package that generates *symmetry adapted basis functions* based on the space group of a unit cell.

#### Features

- Support 1D, 2D and 3D symmetry groups.
- Has a structure renderer.
- Prepare input data for polyorder.
- Install with pip/easy_install
- Well documented.

#### Links

- [Gyroid source code](https://github.com/liuyxpp/gyroid)
- [Gyroid PyPI page](https://pypi.python.org/pypi/gyroid)
- [Gyroid documentation](http://packages.python.org/gyroid/)

### NGPy
-----

`NGPy` is a web application that enable online performing and analyzing Monte-Carlo simulation on nucleation and growth phenomena. It can be also used as a web framework to develop your own web applications.

#### Features

- Run multiple simulation instances.
- Analyze simulation data online.
- Retrieve result data online.
- Install with pip/easy_install

#### Links

- [NGPy source code](https://github.com/liuyxpp/ngpy)
- [NGPy PyPI page](https://pypi.python.org/pypi/ngpy)
- [NGPy documentation](http://pypi.python.org/pypi/ngpy)
