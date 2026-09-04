---
permalink: /publications/
layout: page
title: Publications
description: "Journal articles, talks, posters, and theses from Polyorder Lab."
header-img: images/publications-0.jpg
comments: false
modified: 2026-09-04
breadcrumbs: true
---

<div class="publications-page">
<section class="publications-intro" aria-labelledby="publications-record-heading">
  <div>
    <h2 id="publications-record-heading">A record of methods, models, and materials</h2>
    <p>Journal articles are listed as a chronological research index. Talks, posters, and theses follow as supporting collections.</p>
  </div>
  <div class="pub-profiles" aria-label="Publication profiles and downloads">
    <a href="https://orcid.org/0000-0001-9374-5981" class="profile-badge orcid" target="_blank" rel="noopener">ORCID</a>
    <a href="https://scholar.google.com/citations?user=TcKXbCoAAAAJ&amp;hl=en" class="profile-badge scholar" target="_blank" rel="noopener">Google Scholar</a>
    <button class="profile-badge bibtex-download" onclick="downloadAllBibtex()" type="button">Download all BibTeX</button>
  </div>
</section>

<nav class="pub-toc" aria-label="Publication collections">
  <a href="#journal-articles">Journal articles</a>
  <a href="#presentations-and-posters">Presentations and posters</a>
  <a href="#thesis">Theses</a>
</nav>

<section class="pub-section" id="journal-articles" aria-labelledby="journal-articles-heading">
  <header class="pub-section-heading">
    <h2 id="journal-articles-heading">Journal articles</h2>
    <p>{{ site.data.journal | size }} publications</p>
  </header>

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
      <article class="pub-record">
        <div class="pub-year-marker" aria-label="Published in {{ article.year }}">{{ article.year }}</div>
        <div class="pub-record-body">
          <h3 class="pub-title">{{ article.title }}</h3>
          <div class="pub-authors">
          {% for author in article.author %}
            <span class="{{ author.role }}">{{ author.family }}, {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}{% unless forloop.last %}; {% endunless %}</span>
          {% endfor %}
          </div>
          <div class="pub-info">
            <span class="pub-journal">{{ article.journal.abbreviation }}</span>
            <span class="pub-volume">{{ article.volume }}</span>{% if article.page %}, <span class="pub-page">{{ article.page }}</span>{% endif %}.
            {% if article.language != 'english' %}<span class="pub-lang">In {{ article.language }}</span>{% endif %}
          </div>
          <div class="pub-actions" aria-label="Actions for {{ article.title | escape }}">
            {% if article.URL %}<a href="{{ article.URL }}" class="pub-doi-link">DOI</a>{% endif %}
            {% if article.fulltext %}<a title="Download full text" href="{{ site.url }}/downloads/journal/{{ article.fulltext }}" class="pdf-link">PDF</a>{% endif %}
            <div class="cite-wrapper">
              <button class="cite-btn" onclick="toggleCiteMenu(this)" type="button">Copy citation</button>
              <div class="cite-menu">
                <div class="cite-menu-title">Citation style</div>
                <button onclick="copyCitation(this, 'acs')" type="button">ACS</button>
                <button onclick="copyCitation(this, 'aip')" type="button">AIP</button>
                <button onclick="copyCitation(this, 'aps')" type="button">APS</button>
              </div>
            </div>
            <button class="bibtex-btn" onclick="copyBibtex(this)" type="button">Copy BibTeX</button>
          </div>
        </div>
      </article>
    </li>
  {% endfor %}
  </ol>
</section>

<section class="pub-section pub-section-secondary" id="presentations-and-posters" aria-labelledby="presentations-heading">
  <header class="pub-section-heading">
    <h2 id="presentations-heading">Presentations and posters</h2>
    <p>{{ site.data.meeting | size }} records</p>
  </header>
  <ol class="pub-list">
  {% for presentation in site.data.meeting %}
    <li class="pub-item">
      <article class="pub-record">
        <div class="pub-year-marker">{{ presentation.year }}</div>
        <div class="pub-record-body">
          <h3 class="pub-title">{{ presentation.title }}</h3>
          <div class="pub-authors">
          {% for author in presentation.author %}
            <span class="{{ author.role }}">{{ author.family }}, {{ author.given_initial }}{% unless forloop.last %}; {% endunless %}</span>
          {% endfor %}
          </div>
          <div class="pub-info"><span class="pub-journal">{{ presentation.source }}</span>, <span class="pub-city">{{ presentation.city }}</span>.</div>
          {% if presentation.fulltext %}<div class="pub-actions"><a title="Download presentation" href="{{ site.url }}/downloads/meeting/{{ presentation.fulltext }}" class="pdf-link">Download</a></div>{% endif %}
        </div>
      </article>
    </li>
  {% endfor %}
  </ol>
</section>

<section class="pub-section pub-section-secondary" id="thesis" aria-labelledby="thesis-heading">
  <header class="pub-section-heading">
    <h2 id="thesis-heading">Theses</h2>
    <p>{{ site.data.thesis | size }} records</p>
  </header>
  <ol class="pub-list">
  {% for thesis in site.data.thesis %}
    <li class="pub-item">
      <article class="pub-record">
        <div class="pub-year-marker">{{ thesis.year }}</div>
        <div class="pub-record-body">
          <h3 class="pub-title">{{ thesis.title }}</h3>
          <div class="pub-authors">
          {% for author in thesis.author %}
            <span class="{{ author.role }}">{{ author.family }}, {{ author.given_initial }}</span>
          {% endfor %}
          </div>
          {% for advisor in thesis.advisor %}<div class="pub-advisor">{{ advisor.role }}: {{ advisor.family }}, {{ advisor.given_initial }}</div>{% endfor %}
          <div class="pub-info"><span class="pub-journal">{{ thesis.source }}</span>, <span class="pub-publisher">{{ thesis.publisher }}</span>. {% if thesis.language != 'english' %}<span class="pub-lang">In {{ thesis.language }}</span>{% endif %}</div>
          {% if thesis.fulltext %}<div class="pub-actions"><a title="Download thesis" href="{{ site.url }}/downloads/thesis/{{ thesis.fulltext }}" class="pdf-link">Download</a></div>{% endif %}
        </div>
      </article>
    </li>
  {% endfor %}
  </ol>
</section>
</div>
