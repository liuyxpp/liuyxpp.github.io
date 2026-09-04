---
permalink: /about/
layout: page
title: About Polyorder
description: "A computational polymer physics group at Fudan University."
comments: false
modified: 2026-09-04
breadcrumbs: true
content_width: wide
---

<div class="about-page">
  <section class="about-mission" aria-labelledby="about-mission-title">
    <div class="about-mission__statement">
      <h2 id="about-mission-title">From molecular architecture to ordered materials</h2>
      <p>Polyorder develops field-theoretic models, numerical algorithms, and scientific software for understanding how soft materials organize. The group works at the intersection of polymer physics and computational science.</p>
      <div class="about-actions">
        <a href="{{ site.url }}/research/">Explore our research</a>
        <a href="{{ site.url }}/software/">Use our software</a>
      </div>
    </div>
    <div class="about-mission__axes" aria-label="Polyorder research continuum">
      <span>Architecture</span>
      <span>Algorithms</span>
      <span>Morphology</span>
    </div>
  </section>

  <section class="about-profile" aria-labelledby="yi-xin-liu">
    <figure class="about-profile__portrait">
      <img src="{{ site.url }}/images/me.JPG" alt="Portrait of Prof. Yi-Xin Liu">
    </figure>
    <div class="about-profile__bio">
      <h2 id="yi-xin-liu">Prof. Yi-Xin Liu</h2>
      <p>Yi-Xin Liu (刘一新) is a polymer physicist in the Department of Macromolecular Science at Fudan University, where he has worked since 2012. He received his PhD in Polymer Physics from Peking University in 2009 and his BSc from Nanjing University in 2004.</p>
      <p>From 2014 to 2016, he was a visiting researcher in Prof. Glenn H. Fredrickson's group at the Materials Research Laboratory, University of California, Santa Barbara. His research spans polymer field theory, accelerated numerical methods, block-copolymer self-assembly, confinement, directed self-assembly, and polymer crystallization.</p>
      <div class="about-actions">
        <a href="{{ site.url }}/cv/">View CV</a>
        <a href="{{ site.url }}/downloads/CV.pdf">Download CV (PDF)</a>
        <a href="{{ site.url }}/publications/">View publications</a>
      </div>
    </div>
  </section>

  <section class="about-affiliations" aria-labelledby="affiliations">
    <h2 id="affiliations">Affiliations and contact</h2>
    <div class="affiliation-list">
      {% for position in site.data.positions %}
      <article class="affiliation-record">
        <div class="affiliation-record__identity">
          <h3>{{ position.title }}</h3>
          {% if position.roles %}
          <ul>
            {% for role in position.roles %}
            <li><strong>{{ role.title }}</strong><span>{{ role.dates }}</span></li>
            {% endfor %}
          </ul>
          {% endif %}
        </div>
        <address>
          {{ position.department }}<br>
          {{ position.address }}<br>
          {{ position.location }}<br>
          {% if position.phone %}Office: {{ position.phone }}<br>{% endif %}
          Email: <a href="mailto:{{ position.email }}">{{ position.email }}</a>
        </address>
        {% if position.profiles %}
        <p class="affiliation-record__profiles">
          Department profile:
          {% for profile in position.profiles %}
          <a href="{{ profile.url }}" rel="noopener">{{ profile.lang }}</a>{% unless forloop.last %}<span aria-hidden="true"> / </span>{% endunless %}
          {% endfor %}
        </p>
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </section>

  <p class="site-credit">This site supports math- and code-intensive research communication and is published with Jekyll on GitHub Pages. Theme and reuse details remain available in the project repository.</p>
</div>
