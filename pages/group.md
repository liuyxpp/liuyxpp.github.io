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
<div class="container">
  <div class="row">
    <div class="col-md-4">
      <figure class="third">
        <img src="{{ site.url }}/{{ member.image }}" alt="" class="img-fluid">
      </figure>
    </div>
    <div class="col-md-4">
      <h4>{{ member.name }}</h4>
      <p>{{ member.bio }} See his biography <a href="{{ site.url }}{{ member.bio_link }}">here</a>.</p>
    </div>
  </div>
</div>
{% endfor %}

## Graduate Students
-----

_Master, PhD, and postdoc positions are open for application!_

{% for member in site.data.group.graduate_students %}
#### {{ member.name }}
{% if member.period %}_{{ member.period }}_{% endif %}

{{ member.description }}

{% endfor %}

## Undergraduate Students
-----

_Welcome undergraduate students to join our research group! Please contact Prof. Liu to make an appointment for interview._

{% for member in site.data.group.undergraduate_students %}
#### {{ member.name }}
{% if member.period %}_{{ member.period }}_{% endif %}

{{ member.description }}

{% endfor %}

## Alumni
-----

{% for member in site.data.group.alumni %}
#### {{ member.name }}
{% if member.period %}_{{ member.period }}_{% endif %}

{{ member.description }}

{% endfor %}
