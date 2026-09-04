---
permalink: /software/
layout: page
title: Software
description: "Open-source tools for polymer field theory, numerical methods, and scientific workflows."
hide_description: true
compact_header: true
comments: false
modified: 2026-09-04
breadcrumbs: true
content_width: wide
---

<div class="software-page">
<nav class="software-directory" aria-label="Software categories">
  {% assign grouped_software = site.data.software | group_by: "category" %}
  {% for group in grouped_software %}
    <a href="#{{ group.name | slugify }}" class="toc-pill{% if forloop.first %} active{% endif %}">
      <span>{{ group.name }}</span>
      <span class="toc-count" aria-label="{{ group.items | size }} projects">{{ group.items | size }}</span>
    </a>
  {% endfor %}
  <a class="software-directory__source" href="https://github.com/liuyxpp" target="_blank" rel="noopener">GitHub repositories</a>
</nav>

<div class="software-grid">
  {% assign grouped_software = site.data.software | group_by: "category" %}
  {% for group in grouped_software %}
    <section class="category-section{% if group.name == 'Legacy' %} category-section-legacy{% endif %}" id="{{ group.name | slugify }}" aria-labelledby="{{ group.name | slugify }}-heading">
      <header class="category-heading">
        <h2 class="category-title" id="{{ group.name | slugify }}-heading">{{ group.name }}</h2>
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

              {% if software.features.size > 0 or software.installation %}
                <details class="software-details">
                  <summary>{% if software.installation %}Capabilities and installation{% else %}Capabilities{% endif %}</summary>
                  <div class="software-details__content">
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
                  </div>
                </details>
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

<script src="{{ site.url }}/assets/js/software.js?v=20260904-software-compact"></script>
