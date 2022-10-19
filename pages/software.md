---
permalink: /software/
layout: page
title: Software
description: "A set of open source projects developed by Yi-Xin Liu research group."
header-img: images/software-1.jpg
comments: false
modified: 2022-06-30
breadcrumbs: true
---

Scientific software development plays a central role in my research. Along with my research, I have developed various scientific computing software to carry out the actual task. The software are coded in various programming languages, such as C/C++, Julia, Python, Matlab, and Fortran. Most software listed here are open source software.

<div markdown="0">
    <a href="https://github.com/liuyxpp" class="btn btn-info">View source codes at github.com</a>
</div>

<div markdown="0">
    <a href="{{ site.url }}/software/#polyorder" class="btn btn-success">PolyOrder</a>
    <a href="{{ site.url }}/software/#gyroid" class="btn btn-success">gyroid</a>
    <a href="{{ site.url }}/software/#pydiagram" class="btn btn-success">pydiagram</a>
    <a href="{{ site.url }}/software/#scftpy" class="btn btn-success">scftpy</a>
    <a href="{{ site.url }}/software/#chebpy" class="btn btn-success">chebpy</a>
</div>

<div markdown="0">
    <a href="{{ site.url }}/software/#mpltex" class="btn btn-success">mpltex</a>
    <a href="{{ site.url }}/software/#MakiePublication.jl" class="btn btn-success">MakiePublication.jl</a>
    <a href="{{ site.url }}/software/#ngpy" class="btn btn-success">ngpy</a>
</div>

## Polyorder
-----

`PolyOrder` is a C++ library which aims to ease the development of polymer self-consistent field theory (SCFT) programs.

### Features

* Flexibility. All components can be replaced.
* Extensibility. The OO design enables one add new features smoothly.
* Non-orthogonal unit cell calculations are supported.
* Weakly charged polymers are supported natively.

### Getting Started

* [Introduction to the PolyOrder project]({{ site.url }}/downloads/polyorder20120628.pdf)
* [Configuration file format]({% post_url 2015-04-06-polyorder-config %})

<!--
### Links

* [PolyOrder source code](https://github.com/liuyxpp/polyorder)
-->

## cheb++
-----

`cheb++` is a C++ library which implements a set of functions dealing with Chebyshev polynomials.

### Features

* Compute chebyshev differential matrix
* Compute derivatives of Chebyshev expanded functions
* Compute Clenshaw-Curtis quadrature
* Compute 1D interpolation based on Chebyshev-Gauss-Lobatto grid
* Work with `PolyOrder` seamlessly

### Links

* [cheb++ source code](https://github.com/liuyxpp/cheb)

## scftpy
-----

`scftpy` is a python package for performing polymer self-consistent field theory calculations.

### Features

* New features are experimented here before implemented in `PolyOrder`
* SCFT simulations of confined polymers.
* SCFT simulations of polymer brushes.

### Links

* [scftpy source code](https://github.com/liuyxpp/scftpy)

## chebpy
-----

`chebpy` is a python package for spetral methods of PDEs based on Chebyshev series.

### Features

* New features are experimented here before implemented in `cheb++`
* Chebyshev series construction
* Fast Chebyshev transform
* Chebyshev differentiation
* Chebyshev interpolation
* Chebyshev quadrature
* Chebyshev applications in solution of PDEs

### Links

* [chebpy source code](https://github.com/liuyxpp/chebpy)

## PyDiagram
-----

`PyDiagram` is a python package for generating phase diagrams from results output by polymer field-theoretic simulations. PyDiagram also provides functions for analysis of simulation results.

### Features

- Processor: support Polyorder and PolyFTS output files, and a general dgm file containing all simulation results.
- Plotter: provide plots of raw, invalid, phase boundary, and standard phase diagrams.
- Analyzer: the trend of the free energy, stretch-free cell size, and accuracy.
- A project configuration file provides full control of the processor, plotter, and analyzer.

<!--
### Links

- [PyDiagram source code](https://github.com/liuyxpp/pydiagram)
- [PyDiagram PyPI page](http://pypi.python.org/pypi/pydiagram)
-->

## Gyroid
-----

`gyroid` is a python package that generates *symmetry adapted basis functions* based on the space group of a unit cell.

### Features

- Support 1D, 2D and 3D symmetry groups.
- Has a structure renderer.
- Prepare input data for polyorder.
- Install with pip/easy_install
- Well documented.

### Links

- [Gyroid source code](https://github.com/liuyxpp/gyroid)
- [Gyroid PyPI page](https://pypi.python.org/pypi/gyroid)
- [Gyroid documentation](http://packages.python.org/gyroid/)

## NGPy
-----

`NGPy` is a web application that enable online performing and analyzing Monte-Carlo simulation on nucleation and growth phenomena. It can be also used as a web framework to develop your own web applications.

### Features

- Run multiple simulation instances.
- Analyze simulation data online.
- Retrieve result data online.
- Install with pip/easy_install

### Links

- [NGPy source code](https://github.com/liuyxpp/ngpy)
- [NGPy PyPI page](https://pypi.python.org/pypi/ngpy)
- [NGPy documentation](http://pypi.python.org/pypi/ngpy)

## mpltex
-----

`mpltex` is a python package for creating publication-quality plots using matplotlib. Inspired by [Olga Botvinnik](http://olgabotvinnik.com/)'s python package [prettyplotlib](https://github.com/olgabot/prettyplotlib).
`mpltex` now has **75 stars** and has been **forked 18** times at [github.com](https://github.com)!

### Features

- Create plots for American Chemical Society.
- Create plots for presentation slides.
- Create plots for webpages.
- The color cycle is replaced by Tableau classic 10 color scheme which looks less saturated and more pleasing to eyes.
- enable cycle line styles and a selected set of line markers including hollow type markers.

### Getting Started

- [Reading the tutorial]({% post_url 2014-09-09-mpltex %})

### Links

- [mpltex source code](https://github.com/liuyxpp/mpltex)
- [mpltex PyPI page](https://pypi.python.org/pypi/mpltex)

## MakiePublication.jl

[MakiePublication.jl](https://github.com/liuyxpp/MakiePublication.jl) is a Julia package for producing publication quality figures based on [Makie.jl](https://github.com/JuliaPlots/Makie.jl). It aims to provide equivalent functionalities as the Python package [mpltex](https://github.com/liuyxpp/mpltex).

Read the [full documentation here](http://www.yxliu.group/MakiePublication.jl/dev/).

### Features

- Provide a collection of custom themes for journal publishers: ACS, APS, RSC.
- Custom theme for making figures suitable for web pages.
- 15 color palettes based on well-known quality color schemes with special tweaked ordering for scientific publishing. (since v0.3.0)
- Support hollow markers. (since v0.3.1)
