{% comment %}
	Usage:
		{% include toc.md %}
	Set to show panels by default in _config.yml, can be overridden with
		{% include toc.md panel=true %}
		{% include toc.md panel=false %}
	Use <a href="#toc">{{ site.data.language.go_toc }}</a> to navigate.
	Use {: .no_toc } after a heading (##...) on a new line to exclude it from TOC.
{% endcomment %}
{% if include.panel or site.kramdown.toc_panel %}{% assign show_panel = true %}{% else %}{% assign show_panel = false %}{% endif %}
{% if show_panel %}<div id="toc" class="panel radius" markdown="1">{% endif %}
## Table of Contents
{:{% unless show_panel %}#toc{% endunless %}.no_toc}
*  Auto generated table of contents
{:toc}
{% if show_panel %}</div>{% endif %}
