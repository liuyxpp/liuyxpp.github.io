---
permalink: /software/
layout: page
title: Software
description: "A set of open source projects developed by Yi-Xin Liu research group."
header-img: images/software-1.jpg
comments: false
modified: 2025-12-04
breadcrumbs: true
css: /assets/css/page.css
---

<div class="software-intro">
  <div class="intro-text">
    Scientific software development plays a central role in our research group. Along with the ongoing research, we have developed various scientific computing software to carry out the actual tasks. The software are coded in various programming languages, such as Julia, C/C++, Python, Matlab, and Fortran. Currently, we are almost exclusively using Julia for new projects.
  </div>
  <figure class="intro-image">
    <img src="{{ site.url }}/images/software.png" alt="Software ecosystem diagram">
  </figure>
</div>

<p class="software-subtitle">Some listed software are open sourced. More will be open sourced as they become mature. Please check our <a href="https://github.com/liuyxpp" target="_blank">github.com account</a> for the latest updates.</p>

<div class="toc-section">
  <div class="toc-nav">
    {% assign grouped_software = site.data.software | group_by: "category" %}
    {% for group in grouped_software %}
      <a href="#{{ group.name | slugify }}" class="toc-pill{% if forloop.first %} active{% endif %}">
        {% if group.name == "Scientific Computing" %}
          <svg class="toc-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>
        {% elsif group.name == "Utility" %}
          <svg class="toc-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
        {% elsif group.name == "Legacy" %}
          <svg class="toc-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        {% endif %}
        <span>{{ group.name }}</span>
        <span class="toc-count">{{ group.items | size }}</span>
      </a>
    {% endfor %}
  </div>
</div>

<div class="software-grid">
  {% assign grouped_software = site.data.software | group_by: "category" %}
  {% for group in grouped_software %}
    <div class="category-section" id="{{ group.name | slugify }}">
      <h2 class="category-title">{{ group.name }}</h2>
      <div class="card-container">
        {% for software in group.items %}
          <div class="software-card{% if software.highlight %} highlighted{% endif %}">
            <div class="card-header">
              <h3>{{ software.name }}</h3>
              {% if software.language %}
                <span class="lang-badge lang-{{ software.language | downcase | replace: '+', 'plus' | replace: '/', '-' }}">{{ software.language }}</span>
              {% endif %}
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
                <div class="card-links">
                  {% for link in software.links %}
                    <a href="{{ link.url }}" target="_blank" class="link-pill">
                      {% if link.text contains "GitHub" %}
                        <svg class="link-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                      {% elsif link.text contains "Documentation" or link.text contains "Doc" %}
                        <svg class="link-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                      {% elsif link.text contains "PyPI" %}
                        <svg class="link-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                      {% elsif link.text contains "app" or link.text contains "website" %}
                        <svg class="link-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                      {% else %}
                        <svg class="link-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                      {% endif %}
                      {{ link.text }}
                    </a>
                  {% endfor %}
                </div>
              {% endif %}
            </div>
          </div>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>
<script src="{{ site.url }}/assets/js/software.js"></script>
