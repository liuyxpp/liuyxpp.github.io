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

<div class="group-section">
  <h2 class="group-section-title">
    <svg class="section-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
    Principle Investigator
  </h2>

  {% for member in site.data.group.principle_investigator %}
  <div class="pi-card">
    <div class="pi-photo">
      <img src="{{ site.url }}/{{ member.image }}" alt="{{ member.name }}">
    </div>
    <div class="pi-info">
      <h3>{{ member.name }}</h3>
      <div class="member-bio">{{ member.bio | markdownify }}</div>
      <a href="{{ site.url }}{{ member.bio_link }}" class="member-link">
        View Biography
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </div>
  </div>
  {% endfor %}
</div>

<div class="group-section">
  <h2 class="group-section-title">
    <svg class="section-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
    Graduate Students
  </h2>
  <p class="group-notice">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
    Master, PhD, and postdoc positions are open for application!
  </p>

  <div class="member-grid">
  {% for member in site.data.group.graduate_students %}
    <div class="member-card">
      <div class="member-avatar">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      </div>
      <div class="member-info">
        <h4>{{ member.name }}</h4>
        {% if member.period %}<span class="member-period">{{ member.period }}</span>{% endif %}
        <div class="member-description">{{ member.description | markdownify }}</div>
      </div>
    </div>
  {% endfor %}
  </div>
</div>

<div class="group-section">
  <h2 class="group-section-title">
    <svg class="section-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 12 3 12 0v-5"/></svg>
    Undergraduate Students
  </h2>
  <p class="group-notice">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
    Welcome undergraduate students to join our research group! Please contact Prof. Liu to make an appointment for interview.
  </p>

  <div class="member-grid">
  {% for member in site.data.group.undergraduate_students %}
    <div class="member-card">
      <div class="member-avatar">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      </div>
      <div class="member-info">
        <h4>{{ member.name }}</h4>
        {% if member.period %}<span class="member-period">{{ member.period }}</span>{% endif %}
        <div class="member-description">{{ member.description | markdownify }}</div>
      </div>
    </div>
  {% endfor %}
  </div>
</div>

<div class="group-section">
  <h2 class="group-section-title">
    <svg class="section-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
    Alumni
  </h2>

  <div class="member-grid">
  {% for member in site.data.group.alumni %}
    <div class="member-card">
      <div class="member-avatar">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      </div>
      <div class="member-info">
        <h4>{{ member.name }}</h4>
        {% if member.period %}<span class="member-period">{{ member.period }}</span>{% endif %}
        <div class="member-description">{{ member.description | markdownify }}</div>
      </div>
    </div>
  {% endfor %}
  </div>
</div>
