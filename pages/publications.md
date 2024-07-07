---
permalink: /publications/
layout: page
title: My Publications
description: "A list of my publications: journal articles, presentations, posters, and thesis."
header-img: images/publications-0.jpg
comments: false
modified: 2024-07-07
breadcrumbs: true
---

{% include toc.md panel=true %}

## Journal Articles
-----

<!--
<div itemscope itemtype="https://schema.org/Person"><a itemprop="sameAs" content="https://orcid.org/0000-0001-9374-5981" href="https://orcid.org/0000-0001-9374-5981" target="orcid.widget" rel="me noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">https://orcid.org/0000-0001-9374-5981</a></div>
-->

<div markdown="0">
    <a href="https://orcid.org/0000-0001-9374-5981" class="btn btn-info">ORCID: 0000-0001-9374-5981</a>
    <a href="https://scholar.google.com/citations?user=TcKXbCoAAAAJ&hl=en" class="btn btn-info">Google Scholar</a>
</div>

<div class='panel-pub'>
<ol reversed>
{% for article in site.data.journal %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ article.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }}, {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    </li>
{% endfor %}
</ol>
</div>

## Presentations and Posters
-----

<div class='panel-pub'>
<ol>
{% for presentation in site.data.meeting %}
    <li>
    <div class="title">
    <span class="title">{{ presentation.title }}</span>
    {% if presentation.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/meeting/{{ presentation.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in presentation.author %}
        <span class='{{ author.role }}'>{{ author.family }}, {{ author.given_initial }}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ presentation.source }} </span><span class="city">{{ presentation.city }}, </span><span class="year">{{ presentation.year }}.</span>
    </div>
    </li>
{% endfor %}
</ol>
</div>

## Thesis
-----

<div class='panel-pub'>
<ol>
{% for thesis in site.data.thesis %}
    <li>
    <div class="title">
    <span class="title">{{ thesis.title }}</span>
    {% if thesis.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/thesis/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in thesis.author %}
        <span class='{{ author.role }}'>{{ author.family }}, {{ author.given_initial }}</span>
    {% endfor %}
    </div>
    {% for advisor in thesis.advisor %}
        <span class='advisor'>{{ advisor.role }}: {{ advisor.family }}, {{ advisor.given_initial }}</span>
    {% endfor %}
    <div class="pubinfo">
    <span class="source">{{ thesis.source }} </span><span class="publisher">{{ thesis.publisher }}, </span><span class="year">{{ thesis.year }}.</span>{% if thesis.language != 'english' %}<span class="language"> (In {{ thesis.language }})</span>{% endif %}
    </div>
    </li>
{% endfor %}
</ol>
</div>
