---
permalink: /about/
layout: page
title: About Prof. Yi-Xin Liu
description: A brief introduction of Prof. Yi-Xin Liu and this website.
header-img: images/about.jpg
comments: false
modified: 2025-02-09
breadcrumbs: true
---

<div class="about-page">

<div class="about-bio">
  <div class="bio-content" markdown="1">
Prof. Yi-Xin Liu (刘一新) is a [polymer physicist at Department of Macromolecular Science of Fudan University](https://polymer.fudan.edu.cn/e1/db/c31500a385499/page.htm) since 2012.
Before that, he was a Postdoctoral Research Fellow at Fudan University from 2009 to 2012.
He received his PhD in Polymer Physics from Peking University China in 2009 and my BSc from Nanjing University China in 2004.
He has spent two years (07/2014 - 07/2016) performing research, as a visiting researcher, in collaboration with Prof. Glenn H. Fredrickson in Materials Research Laboratory (MRL) at University of California, Santa Barbara, on the fields of computational polymer field theory and theoretical polymer physics.
His [Current research interests]({{site.url}}/research) lie in the area of soft matter physics and [scientific software]({{site.url}}/software), including polymer field theory (both mean-field and beyond mean-field) and related numerical algorithms, phase behavior and structures of block copolymers, polymer brushes and polyelectrolytes in bulk and under confinements, directed self-assembly, and ultrathin film crystallization.
He has published [30 research articles]({{site.url}}/publications) in peer reviewed journals.
  </div>
</div>

<div class="about-positions">
  <h2>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
    Affiliations
  </h2>
  <div class="position-grid">
    {% for position in site.data.positions %}
    <div class="position-card">
      <div class="position-info">
        <h3>{{ position.title }}</h3>
        <div class="position-details">
          {% if position.roles %}
            {% for role in position.roles %}
              <strong>{{ role.title }} ({{ role.dates }})</strong><br>
            {% endfor %}
          {% endif %}
          {{ position.department }}<br>
          {{ position.address }}<br>
          {{ position.location }}<br>
          {% if position.phone %}Office: {{ position.phone }}<br>{% endif %}
          {% if position.mobile %}Mobile: {{ position.mobile }}<br>{% endif %}
          Email: {{ position.email }}<br>
          {% if position.profiles %}
            Department profile: 
            {% for profile in position.profiles %}
              <a href="{{ profile.url }}">{{ profile.lang }}</a>
              {% unless forloop.last %}/{% endunless %}
            {% endfor %}
          {% endif %}
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<div class="about-cv">
  <a href="{{ site.url }}/cv/" class="cv-badge html" target="_blank">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
    View CV (HTML)
  </a>
  <a href="{{ site.url }}/downloads/CV.pdf" class="cv-badge pdf" target="_blank">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><polyline points="9 15 12 12 15 15"/></svg>
    Download CV (PDF)
  </a>
</div>

<div class="about-section" markdown="1">

## <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg> About This Website

{% include alert alert='Alert:
    please DO NOT publish your website before you remove all copyright materials!' %}

This website is the homepage of the Polyorder lab. **Yi-Xin Liu** is the copyright holder to all the contents published on this website except the underlying theme. If you wish to use any copyright material on this website, please contact me via the Email or address listed above to obtain a permission.

This website is designed for **math** and **code** intensive blogging, particularly suited for computational scientist. The main features are:

* Minimal visual components plus a responsive, paper-like, extremely clean appearance. Let visitors focus on the main content of a post.
* Beautiful Inline and display math equations rendered by [MathJax](https://www.mathjax.org/).
* Markdown code block fences are rendered with line numbers by default and with a carefully tweaked solarized light theme.
* Code blocks and its output look similar to Jupyter Notebook.
* Julia and Python REPL code blocks.
* Comments powered by [utterances](https://utteranc.es/).
* Pre-designed TOC and alerts.
* Support Twitter Card.
* Support per tag Atom feeds, see <samp>feed_julia.xml</samp> for an example.

It has been deployed to Github Pages at [http://liuyxpp.github.io](http://liuyxpp.github.io) with custom domain at [http://www.yxliu.group](http://www.yxliu.group).

</div>

<div class="about-section" markdown="1">

## <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg> Theme Credits & Usage

This website adopts features from
* The HPSTR Jekyll Theme by [Michael Rose](https://github.com/mmistakes)
* The Clean Blog Theme by [David Miller](https://github.com/davidtmiller/).
* The [TWiStErRob Blog](http://www.twisterrob.net) Theme by [Róbert Sándor Papp](https://github.com/TWiStErRob/twisterrob.github.io).

If you wish to use the Jekyll theme of this website, please follow the guidelines below:

1. Please give credit by starring [this project](https://github.com/liuyxpp/liuyxpp.github.io) and/or display this line on your website: <q>This website is powered by [LYX Jekyll theme](https://github.com/liuyxpp/liuyxpp.github.io)</q>.
2. Remove all personal materials and personal information about me (Yi-Xin Liu).
3. Remove all the contents in the following directories: `_posts`, `_drafts`, `_data`, `_site`, `CV`, `downloads`, `images`, `publications`, `research`, and `software`.
4. Modify the configuration file `_config.yml` to add your own personal information.
5. Add your contents.
6. Publish your website.

</div>

</div>
