---
permalink: /research/
layout: page
title: Research
description: "Theory, algorithms, and software for polymer self-assembly, confinement, and crystallization."
hide_description: true
compact_header: true
header-img: images/research-1.jpg
comments: false
modified: 2026-09-04
breadcrumbs: true
content_width: wide
---

<div class="research-page">

<header class="research-lede">
  <div class="research-lede__copy">
    <p class="research-kicker">Research themes</p>
    <h2>Polymer order, from equations to structures</h2>
    <p>We connect polymer field theory, numerical algorithms, and experiment to
    understand how molecular architecture and processing conditions select
    ordered, aperiodic, and crystalline states.</p>
  </div>
  <a class="research-record-link" href="{{ site.url }}/publications/">
    <strong>{{ site.data.journal | size }}</strong>
    <span>journal articles<br>with full-text PDFs</span>
  </a>
</header>

<nav class="research-topic-index" aria-label="Research topics">
  <a href="#algorithms"><span>Algorithms</span><small>Field theory and solvers</small></a>
  <a href="#architectures"><span>Architectures</span><small>Phase behavior and design</small></a>
  <a href="#interfaces"><span>Interfaces</span><small>Confinement and DSA</small></a>
  <a href="#fluctuations"><span>Fluctuations</span><small>Aperiodic matter</small></a>
  <a href="#crystallization"><span>Crystallization</span><small>Thin films and chain folding</small></a>
  <a href="#software"><span>Software</span><small>Open computational workflows</small></a>
</nav>

<section class="research-topic" id="algorithms" aria-labelledby="algorithms-heading">
  <header class="research-topic__heading">
    <p class="research-topic__domain">Theory and computation</p>
    <h2 id="algorithms-heading">Field theory and numerical algorithms</h2>
  </header>
  <div class="research-topic__body">
    <div class="research-topic__copy">
      <p>We develop field-theoretic models and algorithms for polymer
      self-assembly in bulk, under confinement, and in multicomponent systems.
      High-order propagator solvers, real-space electrostatics, and
      phase-equilibrium methods make demanding calculations more accurate and
      reusable across physical models.</p>
      <p>Our newest published approach represents polymer architectures as
      graphs. Graph isomorphism and hierarchical subtree decomposition identify
      equivalent propagators, reducing repeated work for complex noncyclic
      chains.</p>
      <p class="research-direction"><strong>Current direction</strong> Solver
      acceleration, lower memory demand, and general formulations for more
      complex architectures and mixtures.</p>
    </div>
    <figure class="research-topic__figure">
      <img src="{{ site.url }}/images/news/toc-small-cjps-2025.png" alt="Graphical overview of the effective chemical potential framework for polymer phase equilibrium">
      <figcaption>TOC graphic: one thermodynamic framework connects canonical
      calculations to phase-equilibrium conditions.</figcaption>
    </figure>
  </div>
  {% include research-paper-list.html files="cjps202601.pdf,cjps202501.pdf,cjps201801.pdf,jcp201401.pdf,ma201101.pdf" %}
</section>

<section class="research-topic" id="architectures" aria-labelledby="architectures-heading">
  <header class="research-topic__heading">
    <p class="research-topic__domain">Molecular design</p>
    <h2 id="architectures-heading">Polymer architectures and phase behavior</h2>
  </header>
  <div class="research-topic__body">
    <div class="research-topic__copy">
      <p>Chain connectivity is a design variable. We study how topology,
      composition, conformational asymmetry, blending, and segregation compete
      to select mesostructures and reorganize phase diagrams.</p>
      <p>Systematic studies of miktoarm stars revealed recurring phase-diagram
      topologies. More recent graph-enhanced SCFT turns architecture itself into
      a searchable space and predicts stability windows for complex phases,
      including the PtS structure.</p>
      <p class="research-direction"><strong>Current direction</strong> Moving
      from prescribed architectures toward screening highly branched chains,
      multicomponent blends, and structures selected by target properties.</p>
    </div>
    <figure class="research-topic__figure">
      <img src="{{ site.url }}/images/news/toc-small-cm-2024.png" alt="Graphical abstract for automated polymer architecture screening and phase identification">
      <figcaption>Graphical abstract: architecture generation, automated phase
      identification, and free-energy comparison form a discovery loop.</figcaption>
    </figure>
  </div>
  {% include research-paper-list.html files="cm202401.pdf,cjps202501.pdf,jcp202101.pdf,ma201101.pdf" %}
</section>

<section class="research-topic" id="interfaces" aria-labelledby="interfaces-heading">
  <header class="research-topic__heading">
    <p class="research-topic__domain">Films and surfaces</p>
    <h2 id="interfaces-heading">Confinement, interfaces, and directed self-assembly</h2>
  </header>
  <div class="research-topic__body">
    <div class="research-topic__copy">
      <p>Interfaces do more than bound a polymer film: they select domain
      orientation, reshape free-energy barriers, and control how defects
      disappear. Our soft-confinement model separates surface preference from
      surface softness, while studies of polymer brushes identify distinct
      surface states across attractive and repulsive interactions.</p>
      <p>String-method calculations resolve competing pathways for removing
      lamellar defects. More recent work recasts directing-template design as a
      machine-learning problem, connecting interfacial physics with inverse
      design while retaining forward simulation for validation.</p>
      <p>A complementary study of solution-processed organic films traced
      composition waves propagating from kinetically frozen surface mesophases
      during solvent evaporation.</p>
    </div>
    <figure class="research-topic__figure">
      <img src="{{ site.url }}/images/research/inverse_dsa.png" alt="Graphical abstract for machine-learning-assisted inverse design of directed self-assembly templates">
      <figcaption>TOC graphic: a learned inverse map proposes directing
      templates, which are then checked by SCFT or experiment.</figcaption>
    </figure>
  </div>
  {% include research-paper-list.html files="acsami202301.pdf,afm202301.pdf,ma201801.pdf,gfzxb201802.pdf,cjps201802.pdf,jcp201601.pdf" %}
</section>

<section class="research-topic" id="fluctuations" aria-labelledby="fluctuations-heading">
  <header class="research-topic__heading">
    <p class="research-topic__domain">Beyond mean field</p>
    <h2 id="fluctuations-heading">Fluctuations and aperiodic matter</h2>
  </header>
  <div class="research-topic__body">
    <div class="research-topic__copy">
      <p>Not every soft-matter state can be understood from a single mean-field
      minimum. Complex-Langevin field simulations show how thermal fluctuations
      qualitatively reshape the phase diagram of miktoarm-star
      copolymer–homopolymer blends.</p>
      <p>These simulations recover a fluctuation-stabilized bricks-and-mortar
      mesophase between microphase and macrophase separation. Near the
      order–disorder transition, the state is aperiodic rather than a
      conventionally ordered crystal.</p>
    </div>
    <figure class="research-topic__figure">
      <img src="{{ site.url }}/images/research/bm-toc.png" alt="TOC graphic showing the bricks-and-mortar phase region and simulated aperiodic morphologies">
      <figcaption>TOC graphic: thermal fluctuations stabilize a
      bricks-and-mortar region absent from the mean-field phase diagram.</figcaption>
    </figure>
  </div>
  {% include research-paper-list.html files="ma201701.pdf" %}
</section>

<section class="research-topic" id="crystallization" aria-labelledby="crystallization-heading">
  <header class="research-topic__heading">
    <p class="research-topic__domain">Structure and kinetics</p>
    <h2 id="crystallization-heading">Polymer crystallization and hierarchical order</h2>
  </header>
  <div class="research-topic__body">
    <div class="research-topic__copy">
      <p>Ultrathin polymer films provide a real-space view of nucleation,
      metastability, chain folding, and lamellar reorganization. In situ AFM,
      nucleation theory, and phase-field modeling resolved competing
      crystallization pathways in low-molecular-weight PEO and the
      nucleation-and-growth mechanism of lamellar thickening.</p>
      <p>Related studies of liquid-crystalline and dynamic helical polymers show
      how confinement, chain architecture, and folding generate hierarchical
      order across several length scales. Together, this work forms an
      important experimental and theoretical foundation of the group.</p>
    </div>
    <figure class="research-topic__figure">
      <img src="{{ site.url }}/images/research/peo-thickening-toc.jpg" alt="TOC graphic contrasting uniform and nucleation-and-growth pathways for PEO crystal thickening">
      <figcaption>TOC graphic: local domains nucleate and grow during lamellar
      thickening rather than the crystal thickening uniformly.</figcaption>
    </figure>
  </div>
  {% include research-paper-list.html files="ma202101.pdf,gfzxb201801.pdf,ma201103.pdf,ccr201001.pdf,ma200901.pdf" %}
</section>

<section class="research-topic research-topic--software" id="software" aria-labelledby="software-heading">
  <header class="research-topic__heading">
    <p class="research-topic__domain">Research infrastructure</p>
    <h2 id="software-heading">Scientific software and open workflows</h2>
  </header>
  <div class="research-topic__body">
    <div class="research-topic__copy">
      <p>We turn models and algorithms into open, inspectable computational
      workflows. Graph-based model construction, automated phase recognition,
      distributed architecture screening, and reusable Julia packages connect
      physical questions to calculations that can be repeated and extended.</p>
      <p>Polyorder.jl is the central SCFT platform. Polymer.jl and
      PolymerArchitecture.jl describe chain topology; PhaseDiagram.jl handles
      coexistence calculations; and specialized numerical libraries accelerate
      transforms, symmetry-aware calculations, and publication workflows.</p>
      <p class="research-direction"><strong>Current direction</strong>
      Integrating model definition, solvers, phase recognition, and provenance
      into one coherent computational environment.</p>
    </div>
    <figure class="research-topic__figure">
      <img src="{{ site.url }}/images/news/toc-small-cjps-2024.png" alt="TOC graphic for scattering-based automated identification of ordered polymer phases">
      <figcaption>TOC graphic: scattering patterns and reflection conditions
      provide an automated route from computed fields to phase labels.</figcaption>
    </figure>
  </div>
  <nav class="research-software-links" aria-label="Selected research software">
    <a href="{{ site.url }}/software/#polyorder-jl">Polyorder.jl</a>
    <a href="{{ site.url }}/software/#polymer-jl">Polymer.jl</a>
    <a href="{{ site.url }}/software/#polymerarchitecture-jl">PolymerArchitecture.jl</a>
    <a href="{{ site.url }}/software/#phasediagram-jl">PhaseDiagram.jl</a>
    <a href="{{ site.url }}/software/#crystallographicfft-jl">CrystallographicFFT.jl</a>
  </nav>
  {% include research-paper-list.html files="cjps202601.pdf,cm202401.pdf,cjps202401.pdf" %}
</section>

</div>
