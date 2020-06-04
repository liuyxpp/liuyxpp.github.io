---
permalink: /tips/
layout: page
title: Tips and Tricks for Settings and Configurations
description: Tips and tricks to maintain a development working environment for research.
comments: false
modified: 2020-04-30
breadcrumbs: true
---

Tips and tricks to maintain a development working environment for research.

## MacOS

- After upgrade or reinstall the MacOS, rerun following commands to install the command tools for xcode and others.

```console
$ xcode-select --install
```

- Check port 3413 is used by which application

```console
$ lsof -nP -i4TCP:3413 | grep LISTEN
```