---
permalink: /publications/
layout: page
title: Publications
description: "A list of publications of Polyorder lab: journal articles, presentations, posters, and thesis."
header-img: images/publications-0.jpg
comments: false
modified: 2025-02-04
breadcrumbs: true
---

<div class="publications-page">

<div class="pub-toc">
  <h3 class="toc-title">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
    Contents
  </h3>
  <ul>
    <li><a href="#journal-articles">Journal Articles</a></li>
    <li><a href="#presentations-and-posters">Presentations and Posters</a></li>
    <li><a href="#thesis">Thesis</a></li>
  </ul>
</div>

<div class="pub-section" id="journal-articles">
  <h2>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
    Journal Articles
  </h2>

  <div class="pub-profiles">
    <a href="https://orcid.org/0000-0001-9374-5981" class="profile-badge orcid" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zM7.369 4.378c.525 0 .947.431.947.947s-.422.947-.947.947a.95.95 0 0 1-.947-.947c0-.525.422-.947.947-.947zm-.722 3.038h1.444v10.041H6.647V7.416zm3.562 0h3.9c3.712 0 5.344 2.653 5.344 5.025 0 2.578-2.016 5.025-5.325 5.025h-3.919V7.416zm1.444 1.303v7.444h2.297c3.272 0 4.022-2.484 4.022-3.722 0-1.847-1.163-3.722-3.916-3.722h-2.403z"/></svg>
      ORCID
    </a>
    <a href="https://scholar.google.com/citations?user=TcKXbCoAAAAJ&hl=en" class="profile-badge scholar" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5l4.838 3.94A8 8 0 0 1 12 9a8 8 0 0 1 7.162 4.44L24 9.5z"/></svg>
      Google Scholar
    </a>
  </div>

  <ol class="pub-list" reversed>
  {% for article in site.data.journal %}
    {% capture authors_str %}{% for author in article.author %}{{ author.family }}, {{ author.given_initial }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endcapture %}
    <li class="pub-item"
        data-title="{{ article.title | escape }}"
        data-authors="{{ authors_str | strip | escape }}"
        data-journal="{{ article.journal.abbreviation | escape }}"
        data-journal-full="{{ article.journal.fullname | escape }}"
        data-year="{{ article.year }}"
        data-volume="{{ article.volume }}"
        data-issue="{{ article.issue }}"
        data-page="{{ article.page }}"
        data-doi="{{ article.DOI }}">
      <div class="pub-title">
        {{ article.title }}
        {% if article.fulltext %}
          <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ article.fulltext }}" class="pdf-link">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          </a>
        {% endif %}
      </div>
      <div class="pub-authors">
      {% for author in article.author %}
        <span class="{{ author.role }}">{{ author.family }}, {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
      {% endfor %}
      </div>
      <div class="pub-info">
        <span class="pub-journal">{{ article.journal.abbreviation }}</span>
        <span class="pub-year">{{ article.year }},</span>
        <span class="pub-volume">{{ article.volume }},</span>
        <span class="pub-page">{{ article.page }}.</span>
        {% if article.language != 'english' %}<span class="pub-lang">(In {{ article.language }})</span>{% endif %}
      </div>
      <div class="pub-actions">
        {% if article.URL %}
        <a href="{{ article.URL }}" class="pub-doi-link">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          DOI
        </a>
        {% endif %}
        <div class="cite-wrapper">
          <button class="cite-btn" onclick="toggleCiteMenu(this)" type="button">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M6 17c-2 0-3-1-3-3v-3c0-2 1-3 3-3h1l1-3h2l-1 3c2 0 3 1 3 3v3c0 2-1 3-3 3H6z"/><path d="M15 17c-2 0-3-1-3-3v-3c0-2 1-3 3-3h1l1-3h2l-1 3c2 0 3 1 3 3v3c0 2-1 3-3 3h-3z"/></svg>
            Cite
          </button>
          <div class="cite-menu">
            <div class="cite-menu-title">Copy citation as:</div>
            <button onclick="copyCitation(this, 'acs')" type="button">ACS Style</button>
            <button onclick="copyCitation(this, 'aip')" type="button">AIP Style</button>
            <button onclick="copyCitation(this, 'aps')" type="button">APS Style</button>
          </div>
        </div>
      </div>
    </li>
  {% endfor %}
  </ol>
</div>

<div class="pub-section" id="presentations-and-posters">
  <h2>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
    Presentations and Posters
  </h2>

  <ol class="pub-list">
  {% for presentation in site.data.meeting %}
    <li class="pub-item">
      <div class="pub-title">
        {{ presentation.title }}
        {% if presentation.fulltext %}
          <a title="fulltext" href="{{ site.url }}/downloads/meeting/{{ presentation.fulltext }}" class="pdf-link">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          </a>
        {% endif %}
      </div>
      <div class="pub-authors">
      {% for author in presentation.author %}
        <span class="{{ author.role }}">{{ author.family }}, {{ author.given_initial }}; </span>
      {% endfor %}
      </div>
      <div class="pub-info">
        <span class="pub-journal">{{ presentation.source }}</span>
        <span class="pub-city">{{ presentation.city }},</span>
        <span class="pub-year">{{ presentation.year }}.</span>
      </div>
    </li>
  {% endfor %}
  </ol>
</div>

<div class="pub-section" id="thesis">
  <h2>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 2 3 3 6 3s6-1 6-3v-5"/></svg>
    Thesis
  </h2>

  <ol class="pub-list">
  {% for thesis in site.data.thesis %}
    <li class="pub-item">
      <div class="pub-title">
        {{ thesis.title }}
        {% if thesis.fulltext %}
          <a title="fulltext" href="{{ site.url }}/downloads/thesis/{{ thesis.fulltext }}" class="pdf-link">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          </a>
        {% endif %}
      </div>
      <div class="pub-authors">
      {% for author in thesis.author %}
        <span class="{{ author.role }}">{{ author.family }}, {{ author.given_initial }}</span>
      {% endfor %}
      </div>
      {% for advisor in thesis.advisor %}
        <div class="pub-advisor">{{ advisor.role }}: {{ advisor.family }}, {{ advisor.given_initial }}</div>
      {% endfor %}
      <div class="pub-info">
        <span class="pub-journal">{{ thesis.source }}</span>
        <span class="pub-publisher">{{ thesis.publisher }},</span>
        <span class="pub-year">{{ thesis.year }}.</span>
        {% if thesis.language != 'english' %}<span class="pub-lang">(In {{ thesis.language }})</span>{% endif %}
      </div>
    </li>
  {% endfor %}
  </ol>
</div>

</div>
