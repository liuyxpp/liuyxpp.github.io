---
layout: post
title: "Tutorial and A Template for Blogging with the LYX Jekyll Theme"
subheadline: "Write beautiful math and code intensive blog posts"
description: Code blocks, math equations, images, TOC, Alert boxes, etc.
author: lyx
date: 2020-04-13
modified: 2020-04-13
image:
    feature: false
    twitter: 20200413/twitter.png
categories: [Software, Tutorial]
tags: [template, Jekyll, theme, blog]
show_meta:
    info: true
---

An abstract or a summary of the blog post should be put here. This paragraph, before the excerpt mark, also goes before the TOC. The excerpt mark we choose in the LYX theme is `<!--more-->`, which can be configured in <samp>_config.yml</samp>.

<!--more-->

{% include toc.md panel=true %}

## Heading

Headings starts from `##` instead of common `#`, which is reserved for the title of the blog post. All headings can be linked via their short name (spaces replaced by hypens `-`): [Math Equations](#math-equations).

## Front Matter

The front matter of a post page source file is a collection of `YAML` options enclosed by `--`. The front matter controls how Jekyll builds this current post. Available options are:

* `layout`: should always be `post` for publishing a blog post.
* `title`: the title of the blog post.
* `subheadline`: subtitle of the blog post, which will be displayed above the tile with smaller font and all capitalized characters.
* `description`: a short summary of the blog post. It shows under the title on page `/blog/`.
* `teaser`: shorter than `description`, which highlights the key point of the blog post. I shows under the title on this blog post.
* `author`: the short name should be provided, which is defined in <samp>_data/authors.yml</samp>
* `date`: the original publishing date of the blog post, which can be different than the date in the filename of this blog post.
* `modified`: the date when the blog post was modified.
* `image.feature`: whether to display a image header for the blog post. Absent or valued `false` when present of the `feature` keyword will disable the image header.
* `image.twitter`: for Twitter card.
* `categories`: a list of categories, can be one.
* `tags`: a list of tags, can be one or none.
* `comments`: show `utterences` comments by default. Absent of `comments` will show comments. To disable comments, set `comments: false` explicitly.
* `show_meta.info`: if `true`, show information including author, date, categories, and tags.
* `math`: include a list of user defined LaTeX commands/macros by default. To disable, set `math: false`.

## TOC

Table of contents can be displayed by adding the following line to the blog post:

{% highlight liquid linenos %}
{% raw %}{% include toc.md panel=true %}{% endraw %}
{% endhighlight %}

## Math Equations

Math equations is rendered by `MathJax`. Here is an example of inline math equation $\pi^2/6 = \sum_{n=1}^{\infty} 1/n^2$. And display math equation is written as

$$
\begin{equation}
    Z_0(q) = \frac{1}{q^2} \sum_{\lbrace hkl \rbrace} \abs{\sum_j\ensemble{F_j(\mM_j\cdot\vq_{hkl})}_d\exp[2\pi i(x_jh + y_jk + z_jl)]}^2 L(q - q_{hkl})
\end{equation}
$$

All display math equations are numbered automatically. Adding `\label{a_label_describes_this_equation}` to the end of the math block to be cited later, such as

$$
\begin{equation}
    L(x) = \frac{1}{\sqrt{2\pi}\sigma}\exp\left[ -\frac{(x-\mu)^2}{2\sigma^2} \right]
\end{equation}\label{eq:gauss}
$$

Multiline display equation is also possible:

$$
\begin{equation}
\begin{split}
    \vr' &= p - o' \\
         &= p - o + o - o' \\
         &= \vr - (o' - o).
\end{split}
\end{equation}\label{eq:split}
$$

Now cite the Gaussian distribution equation using `\eqref{eq:guass}` eq.\eqref{eq:gauss}.

Above equations use some user defined `LaTeX` commands. To disable it, add `math: false` to the front matter. Check out the predefined macros at <samp>_include/latex_commands.html</samp>, and you can modify it freely as you like.

## Codes

### Code blocks

There are two kinds of code blocks:

* Kramdown fencing code blocks enclosed by <code>```</code>.
* Liquid code blocks using {% raw %}`{% highlight %}{% endhighlight %}`{% endraw %}.

Unfortunately, Jekyll processes these code blocks differently and outputs incompatible `HTML` contents, leading to serious issues. In general, one should use Jekyll code blocks for better syntax highlighting. However, there will be sometimes that it is more convenient to use fencing code blocks. The LYX Jekyll theme handles this situation carefully, see <samp>_sass/_syntax.scss</samp>. The rendered code blocks should have little visual differences.

Note that due to fencing blocks lack the `data-lang` attribute in their corresponding `HTML` codes, we use a dirty hack using `CSS` to display language name on the code block panel. Only a few languages are supported. Check out which language is supported in <samp>_sass/_syntax.scss</samp>, adding more as you wish.

Line numbers are displayed by default in fencing code blocks which cannot be disabled. If you don't want to display line numbers, use Liquid code blocks instead.

`Julia` syntax highlighting using fencing code blocks:

```julia
struct GeneralizedPeak <: ScatteringPeak
    δ::Real # the variance
    ν::Real # the mean value, i.e. the position of the peak
    γν::Real # = √π * Γ[(ν+1)/2] / Γ(ν/2)
    γνhalf::Real # = Γ(ν/2)
end
```

`Julia` syntax highlighting using Liquid code blocks with line numbers:

{% highlight julia linenos %}
struct GeneralizedPeak <: ScatteringPeak
    δ::Real # the variance
    ν::Real # the mean value, i.e. the position of the peak
    γν::Real # = √π * Γ[(ν+1)/2] / Γ(ν/2)
    γνhalf::Real # = Γ(ν/2)
end
{% endhighlight %}

`Julia` syntax highlighting using Liquid code blocks without line numbers:

{% highlight julia %}
struct GeneralizedPeak <: ScatteringPeak
    δ::Real # the variance
    ν::Real # the mean value, i.e. the position of the peak
    γν::Real # = √π * Γ[(ν+1)/2] / Γ(ν/2)
    γνhalf::Real # = Γ(ν/2)
end
{% endhighlight %}

`Output` as `Markdown` syntax highlighting using fencing blocks:

{% highlight markdown linenos %}
Translation{Float64}([1.0, 2.0, 3.0])
{% endhighlight %}

`Console` syntax highlighting using fencing code blocks

```console?lang=julia
julia> f(x, y) = x + y
julia> f(2, 3)
5
julia> f(3, 4)
7
```

`Console` syntax highlighting using Liquid code blocks

{% highlight console linenos %}
julia> f(x, y) = x + y
julia> f(2, 3)
5
julia> f(3, 4)
7
{% endhighlight %}

Note that since we can not set the `lang=julia` as in fencing code blocks, the Liquid code blocks will not highlight the codes after `julia>` as `Julia`, but as general `console` codes.

### Inline codes

* File extensions with `<code>`: `.css`, `.js`, `.html`
* Paths and file names with `<samp>`: <samp>lib/code/path/file.name</samp>
* Liquid-like code may need some escaping: {%raw%}`{{tag}}`{%endraw%}
* Fencing code blocks' ticks can be output like this: ````<code>```</code>```` &rarr; <code>```</code>.
* Don't be lazy with `alternative`/`code`/`formatting`.

## Images

* Centered: use `.center`
* Align left without text around: use nothing
* Align left with text right: use `.alignleft`
* Align right with text left: use `.alignright`

![image alt]({{ site.url }}/images/scattering3/alibi_translation.png){:width="300px" .center}

## Citations

Here is an reference example.[^Yager2013]

## Quotes

Here's a <q>short quotation</q> which is in the middle of a sentence.

> This is a long quotation by someone, normal markdown formatting rules apply:
  **strong**, *em*, _em_, ***strong em***, <b>html bold</b>, `code`, <kbd>kbd</kbd>, <samp>samp</samp>, <ins>ins</ins>, <del>del</del>
  <cite>TWiStErRob</cite>

Another block quotes:

> <samp>Program output text</samp> <cite>output from [file.name](http://sources.com/path/to/file.name#line=123) in [library](http://library.com/)</cite>

## Alert Boxes

All `alert`s support markdown and their names are all lowercase, because they're used as CSS classes, for example TODO is `alert todo=`. The <q>TODO:</q> prefix is not automatically inserted, it's for name calling only here.

{% include alert alert='Alert:
    This is like any normal markdown, even when used from non-markdown context:
    **strong**, *em*, _em_, ***strong em***, <b>html bold</b>, `code`, <kbd>kbd</kbd>, <samp>samp</samp>, <ins>ins</ins>, <del>del</del>.' %}

{% include alert warning='Warning: call out a caveat that is easy to trigger
    This is like any normal markdown, even when used from non-markdown context:
    **strong**, *em*, _em_, ***strong em***, <b>html bold</b>, `code`, <kbd>kbd</kbd>, <samp>samp</samp>, <ins>ins</ins>, <del>del</del>.' %}

{% include alert info='Info: supplementary information, for example links to further reading or documentation.
    This is like any normal markdown, even when used from non-markdown context:
    **strong**, *em*, _em_, ***strong em***, <b>html bold</b>, `code`, <kbd>kbd</kbd>, <samp>samp</samp>, <ins>ins</ins>, <del>del</del>.' %}

{% include alert tip='Tip: call out something non-trivial that could help.
    This is like any normal markdown, even when used from non-markdown context:
    **strong**, *em*, _em_, ***strong em***, <b>html bold</b>, `code`, <kbd>kbd</kbd>, <samp>samp</samp>, <ins>ins</ins>, <del>del</del>.' %}

{% include alert success='Success:
    This is like any normal markdown, even when used from non-markdown context:
    **strong**, *em*, _em_, ***strong em***, <b>html bold</b>, `code`, <kbd>kbd</kbd>, <samp>samp</samp>, <ins>ins</ins>, <del>del</del>.' %}

{% include alert text='Text:
    This is like any normal markdown, even when used from non-markdown context:
    **strong**, *em*, _em_, ***strong em***, <b>html bold</b>, `code`, <kbd>kbd</kbd>, <samp>samp</samp>, <ins>ins</ins>, <del>del</del>.' %}

{% include alert todo='TODO: reminder to myself that something needs to be done here
    This is like any normal markdown, even when used from non-markdown context:
    **strong**, *em*, _em_, ***strong em***, <b>html bold</b>, `code`, <kbd>kbd</kbd>, <samp>samp</samp>, <ins>ins</ins>, <del>del</del>.' %}

{% include alert terminal='Terminal:<br/>
    This is like any normal markdown, even when used from non-markdown context:
    **strong**, *em*, _em_, ***strong em***, <b>html bold</b>, `code`, <kbd>kbd</kbd>, <samp>samp</samp>, <ins>ins</ins>, <del>del</del>.' %}

## Formatting

*[abbr]: abbreviation

* Belonging words should have `&nbsp;` between to prevent wrapping: Yi-Xin&nbsp;Liu.
* Long list of alternatives should have `<wbr>` between them to allow wrapping: this&nbsp;one<wbr>/that&nbsp;one<wbr>/other&nbsp;thing.
* Use `<del>` to <del>strike text out</del>.
* Use `<samp>` for sample output: <samp>Exit code: 1</samp>.
* Use `<samp>` for math: <samp>4&nbsp;people &times; 5&nbsp;days = 20&nbsp;man hours</samp>.
* Use `<var>` for something representing a number: <var>your age</var> times.
* Use `<mark>` for callout <mark>Grammar&nbsp;Nazis</mark>.
* Use `<mark>` for UI elements: Press <mark>Next</mark> to proceed.
* Use `<abbr>` to show an abbreviation: <abbr title="shortended text">shot</abbr>, but it's not necessary if the abbr is defined in markdown.
* Custom colors using `<span style="color:orange">colored content</span>` when referencing something highlighted on an image: <span style="color:orange">Save button</span>.

## Acknowledgements

The LYX Jekyll theme adopts features from

* The HPSTR Jekyll Theme by [Michael Rose](https://github.com/mmistakes)
* The Clean Blog Theme by [David Miller](https://github.com/davidtmiller/).
* The [TWiStErRob Blog](http://www.twisterrob.net) Theme by [Róbert Sándor Papp](https://github.com/TWiStErRob/twisterrob.github.io).

## References

[^Yager2013]: Yager, K. G.; Zhang, Y.; Lu, F.; Gang, O. Periodic Lattices of Arbitrary Nano-Objects: Modeling and Applications for Self-Assembled Systems. *J. Appl. Crystallogr.* **2013**, *47*, 118–129.
