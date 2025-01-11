---
permalink: /group/
layout: page
title: Group Members
description: "Group members: a list of current group members and alumni."
header-img: images/research-1.jpg
comments: false
modified: 2025-01-10
breadcrumbs: true
---

## Principle Investigator
-----

{% for member in site.data.group.principle_investigator %}
<div class="pi-card">
  <div class="pi-info">
    <h3>{{ member.name }}</h3>
      <div class="member-bio">{{ member.bio | markdownify }}</div>
    <a href="{{ site.url }}{{ member.bio_link }}" class="member-link">View Biography →</a>
  </div>
  <div class="pi-photo">
    <img src="{{ site.url }}/{{ member.image }}" alt="{{ member.name }}">
  </div>
</div>
{% endfor %}

## Graduate Students
-----

_Master, PhD, and postdoc positions are open for application!_

<div class="member-grid">
{% for member in site.data.group.graduate_students %}
  <div class="member-card">
    <div class="member-info">
      <h4>{{ member.name }}</h4>
      {% if member.period %}<p class="member-period">{{ member.period }}</p>{% endif %}
      <div class="member-description">{{ member.description | markdownify }}</div>
    </div>
  </div>
{% endfor %}
</div>

## Undergraduate Students
-----

_Welcome undergraduate students to join our research group! Please contact Prof. Liu to make an appointment for interview._

<div class="member-grid">
{% for member in site.data.group.undergraduate_students %}
  <div class="member-card">
    <div class="member-info">
      <h4>{{ member.name }}</h4>
      {% if member.period %}<p class="member-period">{{ member.period }}</p>{% endif %}
      <div class="member-description">{{ member.description | markdownify }}</div>
    </div>
  </div>
{% endfor %}
</div>

## Alumni
-----

<div class="member-grid">
{% for member in site.data.group.alumni %}
  <div class="member-card">
    <div class="member-info">
      <h4>{{ member.name }}</h4>
      {% if member.period %}<p class="member-period">{{ member.period }}</p>{% endif %}
      <div class="member-description">{{ member.description | markdownify }}</div>
    </div>
  </div>
{% endfor %}
</div>
