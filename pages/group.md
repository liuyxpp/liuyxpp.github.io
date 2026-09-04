---
permalink: /group/
layout: page
title: Group
description: "People developing theory, algorithms, and software for ordered soft materials."
comments: false
modified: 2026-09-04
breadcrumbs: true
content_width: wide
hide_description: true
compact_header: true
---

<div class="group-page">
  <section class="group-section" aria-labelledby="principal-investigator">
    <h2 class="group-section-title" id="principal-investigator">Principal investigator</h2>
    {% for member in site.data.group.principle_investigator %}
    <article class="pi-profile">
      <figure class="pi-profile__portrait">
        <img src="{{ site.url }}/{{ member.image }}" alt="Portrait of {{ member.name }}">
      </figure>
      <div class="pi-profile__body">
        <h3>{{ member.name }}</h3>
        <div class="member-bio">{{ member.bio | markdownify }}</div>
        <div class="profile-actions">
          <a href="{{ site.url }}{{ member.bio_link }}">Biography</a>
          <a href="{{ site.url }}/cv/">Curriculum vitae</a>
          <a href="{{ site.url }}/publications/">Publications</a>
        </div>
      </div>
    </article>
    {% endfor %}
  </section>

  <section class="group-section" aria-labelledby="current-members">
    <h2 class="group-section-title" id="current-members">Current members</h2>

    <div class="member-roster">
      {% for member in site.data.group.graduate_students %}
      <article class="member-profile">
        <p class="member-profile__role">Graduate researcher</p>
        <h3>{{ member.name }}</h3>
        {% if member.period %}<p class="member-profile__period">Joined {{ member.period }}</p>{% endif %}
        <div class="member-profile__description">{{ member.description | markdownify }}</div>
      </article>
      {% endfor %}

      {% for member in site.data.group.undergraduate_students %}
      <article class="member-profile">
        <p class="member-profile__role">Undergraduate researcher</p>
        <h3>{{ member.name }}</h3>
        {% if member.period %}<p class="member-profile__period">Joined {{ member.period }}</p>{% endif %}
        <div class="member-profile__description">{{ member.description | markdownify }}</div>
      </article>
      {% endfor %}
    </div>
  </section>

  <aside class="join-panel" aria-labelledby="join-polyorder">
    <h2 id="join-polyorder">Join the group</h2>
    <p>Master's · Doctoral · Postdoctoral · Undergraduate</p>
    <a class="join-panel__action" href="mailto:{{ site.owner.email }}">Contact Prof. Liu</a>
  </aside>

  <section class="group-section group-section--alumni" aria-labelledby="alumni">
    <h2 class="group-section-title" id="alumni">Alumni</h2>
    <ol class="alumni-list">
      {% for member in site.data.group.alumni %}
      <li class="alumni-record">
        <div class="alumni-record__identity">
          <h3>{{ member.name }}</h3>
          {% if member.period %}<p>{{ member.period }}</p>{% endif %}
        </div>
        <div class="alumni-record__description">{{ member.description | markdownify }}</div>
      </li>
      {% endfor %}
    </ol>
  </section>
</div>
