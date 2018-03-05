---
layout: page
title: Research Interests
description: "Polymer Physics &amp; Numerical Algorithms."
header-img: images/research-1.jpg
comments: false
modified: 2018-03-02
---

I mainly work in the field of soft matter physics, dedicating efforts to understand the physics of polymers and biological macromolecules.

## Polymer Field-Theoretic Study
-----

<figure class="third">
    <img src="{{ site.url }}/images/research/bcc.png" alt="">
    <img src="{{ site.url }}/images/research/hex.png" alt="">
    <img src="{{ site.url }}/images/research/gyroid.png" alt="">
</figure>

The self-consistent field theory (SCFT), as the most accurate theory at the mean-field level, has become a standard technique in practice for studying microphase separations of block copolymers. Composition fluctuations become more and more important with the derease of the invariant degree of polymerization or invariant polymer concentration. While mean-field theories, such as SCFT, breaks down in this circumstance, beyond mean-field theories, such as Gaussian approximation, one-loop theory and complex Langevin simulation, are developed to study the fluctuation corrections to the mean-field theory.

### Topics

* The microphase-separated nanostructures in confined polymer systems
* Directed self-assembly and defect removal processes.
* Beyond mean-field theories for polymer solutions and block copolymers
* The phase behavior of weakly charged polymer solutions

### Research Notes

* [A Quick Guide to the Self-Consistent Field Theory in Polymer Physics]({% post_url 2014-05-26-scft-guide %})
* [Lecture Notes in Polymer Physics]({% post_url 2014-05-26-pp-notes %})

## Ultrathin Film Polymer Crystallization
-----

<figure>
    <img src="{{ site.url }}/images/research/peo.png" alt="">
</figure>

Ordering and crystallization of polymeric chains with regular chemistry structure is one of the most striking phenomena in con-densed matter physics.
The process of polymer crystallization is a transition from a randomly coiled state to a perfectly ordered state. During this process a hierarchy of ordered structure develops, which in turn controls the physical properties of the polymer materials. In bulk, spherulites are the most common superstruc-tures observed when crystallizing from melt, while single crystals and dendrites can be grown from dilute solutions. Recently, polymer crystallization under spatial confinement, especially in thin (thickness less than 1000 nm) and ultrathin (thickness less than 100 nm) films on solid substrates, has attracted increasing attention. The objective to study polymer crystal-lization confined in ultrathin films is twofold:

1. to develop new technologies and to enhance device performance;
2. to provide new evidence to better understand the nature of polymer crystal-lization.

### Topics

* Pattern formation of ultrathin film polymer crystallization.
* Thickening behavior of thin monolayer crystals.

## Scientific Software Development
-----

As an important part of my research, I have developed several computational software packages and implemented numerical algorithms to perform computational tasks encountered along research.

Programming languages involved: `C/C++` and `Python`. Transition to `Julia` Planned.

### Software Packages

* [Polyorder]({{ site.url }}/software/)
* [Gyroid]({{ site.url }}/software/)
* [PyDiagram]({{ site.url }}/software/)
* [NGPy]({{ site.url }}/software/)
* [mpltex]({{ site.url }}/software/)

### Numerical Algorithms

* Chebyshev collocation method for SCFT calculations of confined polymers.
* Pseudo-spectral method for SCFT calculations.
* Multigrid method for SCFT calculations of charged polymers.
* Off-lattice Monte-Carlo simulation of polymer crystal growth.
* Phase-field simulations of thin film polymer crystal growth.

### Research Notes

* [Test PolyFTS with Polyorder]({% post_url 2015-04-14-polyfts-test %})
* [Polyorder Configuration File]({% post_url 2015-04-06-polyorder-config %})
* [Simpson's Rule and Other Fourth-Order Quadrature Formulas]({% post_url 2014-09-11-simpson %})
* [mpltex: A Tool for Creating Publication-Quality Plots]({% post_url 2014-09-09-mpltex %})
