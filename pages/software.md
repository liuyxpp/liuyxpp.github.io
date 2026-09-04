---
permalink: /software/
layout: page
title: Software
description: "Open-source tools for polymer field theory, numerical methods, and scientific workflows."
header-img: images/software-1.jpg
comments: false
modified: 2026-09-04
breadcrumbs: true
---

<div class="software-page">
<section class="software-intro" aria-labelledby="software-ecosystem-heading">
  <div class="intro-text">
    <h2 id="software-ecosystem-heading">Software is part of the method</h2>
    <p>We build the numerical tools used in our research, from polymer architecture models and field-theoretic solvers to phase-diagram and publication workflows. New scientific projects are developed primarily in Julia; earlier C++, Python, Matlab, and Fortran projects remain available as part of the group’s technical record.</p>
    <p>Open-source releases appear here as they mature. Development activity and source repositories are also available on <a href="https://github.com/liuyxpp" target="_blank" rel="noopener">GitHub</a>.</p>
  </div>
  <figure class="intro-image">
    <img src="{{ site.url }}/images/software.png" alt="Diagram of the Polyorder scientific software ecosystem">
  </figure>
</section>

<nav class="software-directory" aria-label="Software categories">
  {% assign grouped_software = site.data.software | group_by: "category" %}
  {% for group in grouped_software %}
    <a href="#{{ group.name | slugify }}" class="toc-pill{% if forloop.first %} active{% endif %}">
      <span>{{ group.name }}</span>
      <span class="toc-count" aria-label="{{ group.items | size }} projects">{{ group.items | size }}</span>
    </a>
  {% endfor %}
</nav>

<div class="software-grid">
  {% assign grouped_software = site.data.software | group_by: "category" %}
  {% for group in grouped_software %}
    <section class="category-section{% if group.name == 'Legacy' %} category-section-legacy{% endif %}" id="{{ group.name | slugify }}" aria-labelledby="{{ group.name | slugify }}-heading">
      <header class="category-heading">
        <h2 class="category-title" id="{{ group.name | slugify }}-heading">{{ group.name }}</h2>
        {% if group.name == "Scientific Computing" %}
          <p>Research-grade tools for modeling, simulation, and analysis.</p>
        {% elsif group.name == "Utility" %}
          <p>Focused packages for visualization and research communication.</p>
        {% elsif group.name == "Legacy" %}
          <p>Earlier projects retained for reference; these are not the basis of current development.</p>
        {% endif %}
      </header>

      <div class="card-container">
        {% for software in group.items %}
          <article class="software-card software-entry{% if software.name == 'Polyorder.jl' %} software-entry-flagship{% elsif software.highlight %} highlighted{% endif %}" id="{{ software.name | slugify }}">
            <div class="card-header">
              <div>
                <h3>{{ software.name }}</h3>
                {% if software.name == "Polyorder.jl" %}<p class="software-role">Flagship SCFT platform</p>{% endif %}
              </div>
              <div class="software-meta">
                {% if group.name == "Legacy" %}<span class="software-status">Legacy</span>{% endif %}
                {% if software.language %}<span class="lang-badge lang-{{ software.language | downcase | replace: '+', 'plus' | replace: '/', '-' }}">{{ software.language }}</span>{% endif %}
              </div>
            </div>

            <div class="card-body">
              <p class="description">{{ software.description }}</p>

              {% if software.features.size > 0 %}
                <div class="features">
                  <ul>
                    {% for feature in software.features %}
                      <li>{{ feature }}</li>
                    {% endfor %}
                  </ul>
                </div>
              {% endif %}

              {% if software.installation %}
                <div class="installation">
                  <h4>Installation</h4>
                  {{ software.installation | markdownify }}
                </div>
              {% endif %}

              {% if software.links.size > 0 %}
                <div class="card-links" aria-label="{{ software.name }} links">
                  {% for link in software.links %}
                    <a href="{{ link.url }}" target="_blank" rel="noopener" class="link-pill">{{ link.text }}</a>
                  {% endfor %}
                </div>
              {% endif %}
            </div>
          </article>
        {% endfor %}
      </div>
    </section>
  {% endfor %}
</div>
</div>

<script src="{{ site.url }}/assets/js/software.js"></script>
