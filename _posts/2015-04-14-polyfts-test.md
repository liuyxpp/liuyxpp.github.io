---
layout: post
title: Test PolyFTS with Polyorder
author: Yi-Xin Liu
create: 2015-04-10
modified: 2015-04-14
image:
    feature: abstract-5.jpg
---

We will verify the [PolyFTS] calculation by comparing to the [Polyorder] results. The SCFT model we will test is miktoarm star block copolymer and homopolymer blends (AB3 + A). The density is not smeared in both [PolyFTS] and [Polyorder].

## 1 Settings

### 1.1 Common Settings

{% highlight yaml linenos %}
f:          0.4
phi_h:      0.3
xN:         18
Lx:         64
ds:         0.01
stop_tol:   1e-8
{% endhighlight %}

### 1.2 Polyorder Settings

{% highlight yaml linenos %}
MDE solver:             ETDRK4
SCFT updater:           Anderson mixing
seed:                   file
Cell size optimization: Brent
{% endhighlight %}

### 1.3 PolyFTS Settings

{% highlight yaml linenos %}
MDE solver:             ROS
SCFT updater:           SIS
seed:                   random numbers or file (for HEX)
Cell size optimization: variable cell
{% endhighlight %}

## 2 DIS

For disordered structure, it is not necessary to optimize the unit cell size. The unit cell size can be arbitrarily chosen to be 1.0. Also, we can use only one plane wave in 1D.

Software        | a     | H             | t
----------------|-------|---------------|-------
Polyorder       | 1.0   | 4.3848        | 0.00083
PolyFTS         | 1.0   | 4.384794      | 0.02
PolyFTS+smear   | 1.0   | 4.3848        | 0.01

## 3 LAM

### 3.1 Single Unit Cell Size

We choose the unit cell size to be 3.552616, which is the optimum value obtained by Polyorder.

#### Free Energy

Software        | a         | H             | t
----------------|-----------|---------------|-------
Polyorder       | 3.552616  | 4.1076304682  | 0.04
PolyFTS         | 3.552616  | 4.1076351249  | 1.84
PolyFTS+smear   | 3.552616  | 4.3615373785  | 1.97

### 3.2 Cell Size Optimization

Brent optimization in Polyorder preforms 3 SCFT simulations to find the initial points and 4 additional SCFT simulations to search the minimum. Variable cell SCFT simulations by PolyFTS takes 25,000 SCFT cycles, which is about 6 times more than the bare SCFT simulations.

Software        | a         | H             | t
----------------|-----------|---------------|-------
Polyorder       | 3.552616  | 4.1076304682  | 0.38
PolyFTS         | 3.556888  | 4.1076334133  | 11.24
PolyFTS+smear   | 4.083726  | 4.3477787568  | 32.38

## 4 HEX

### 4.1 Single Unit Cell Size

In Polyorder, we choose a rectangular unit cell whose side lengths are $$a$$ and $$b$$. The ratio $$b/a$$ is equal to $$\sqrt{3}$$. In PolyFTS we choose a rhombic unit cell with angle between side lengths being $$2\pi/3$$.

#### Free Energy

Software                | a         | H             | t
------------------------|-----------|---------------|-------
Polyorder               | 4.621005  | 4.1458955044  | 1.68
PolyFTS                 | 4.621005  | 4.1458949638  | 48.26
PolyFTS + Symmetrizer   | 4.621005  | 4.1458949635  | 32.50
PolyFTS + smear         | 4.621005  | 4.3556394360  | 6.28

#### Density Field

Software   | A                          | B
:---------:|:--------------------------:|:-----------------:
PolyFTS without symmetrizer  | <img src="{{ site.url }}/images/20150414/fix-minorA-density1.png" alt="" width="168px">   | <img src="{{ site.url }}/images/20150414/fix-minorA-density2.png" alt="" width="168px">
PolyFTS with symmetrizer  | <img src="{{ site.url }}/images/20150414/fix-sym-minorA-density1.png" alt="" width="112px">  | <img src="{{ site.url }}/images/20150414/fix-sym-minorA-density2.png" alt="" width="112px">
PolyFTS with smearing  | <img src="{{ site.url }}/images/20150414/smear-fix-sym-minorA-density1.png" alt="" width="112px">  | <img src="{{ site.url }}/images/20150414/smear-fix-sym-minorA-density2.png" alt="" width="112px">

### 4.2 Cell Size Optimization

In Polyorder we choose a rectangular unit cell, while in PolyFTS we choose a rhombic unit cell with angle between side lengths being $$2\pi/3$$.

Brent optimization in Polyorder preforms 3 SCFT simulations to find the initial points and 4 additional SCFT simulations to search the minimum. Variable cell SCFT simulations by PolyFTS with symmetrizer takes 63,000 SCFT cycles. Variable cell SCFT simulations by PolyFTS without symmetrizer takes 126,000 SCFT cycles.

#### Free Energy

Software                | a         | H             | t
------------------------|-----------|---------------|---------
Polyorder               | 4.621005  | 4.1458955044  | 13.35
PolyFTS                 | 4.621874  | 4.1458949237  | 1007.56
PolyFTS + Symmetrizer   | 4.622002  | 4.1458949227  | 496.81
PolyFTS + smear         | 4.949710  | 4.3534538770  | 1182.66

#### Density Field

Software   | A                          | B
:---------:|:--------------------------:|:-----------------:
PolyFTS without symmetrizer  | <img src="{{ site.url }}/images/20150414/vc-minorA-density1.png" alt="" width="168px">  | <img src="{{ site.url }}/images/20150414/vc-minorA-density2.png" alt="" width="168px">
PolyFTS with symmetrizer  | <img src="{{ site.url }}/images/20150414/vc-sym-minorA-density1.png" alt="" width="112px">  | <img src="{{ site.url }}/images/20150414/vc-sym-minorA-density2.png" alt="" width="112px">
PolyFTS with smearing  | <img src="{{ site.url }}/images/20150414/smear-vc-sym-minorA-density1.png" alt="" width="112px">  | <img src="{{ site.url }}/images/20150414/smear-vc-sym-minorA-density2.png" alt="" width="112px">

### 4.3 Discussion

For HEX phase, there are two kinds of structures: cylinder formed by specie A (HEX-A phase) and cylinder formed by specie B (HEX-B phase). In this particular case, HEX-A phase is more stable, despite that specie A's volume fraction is larger than that of specie B.

Using random initial fields, PolyFTS with symmetrizer can only produce HEX-B phase. To obtain HEX-A phase, one can switch the two columns corresponding to A and B fields in fields.dat and use the resulted file to initialize the PolyFTS + symmetrizer simulation.

## 5 Conclusion

1. Polyorder and PolyFTS agree very well within an error of about 1e-6.
2. Caution about the type A and type B phase of the HEX structure. Use corresponding field to initialize simulation.
3. Output and input field are all `SpeciesField`.

## Reference

- [Polyorder][polyorder]
- [PolyFTS][polyfts]

[polyorder]: http://ngpy.org/software/#polyorder
[polyfts]: http://polybot.mrl.ucsb.edu
