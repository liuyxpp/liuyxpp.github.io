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

## ubuntu

- Find the current working directory of a process with a PID, say 1234

```console
$ pwdx 1234
/home/lyx/simulation/pujiang/ab3_a/f0.4/xN20

$ lsof -p 1234 | grep cwd
/home/lyx/simulation/pujiang/ab3_a/f0.4/xN20
```

- Find processes using a name

```console
$ ps -ef | grep lyx
```

- Count the lines of a input source

```console
$ ps -ef | grep lyx | wc -l
Number of processes has keyword lyx (which happened to be my user name on the server) 
```

- NVidia GPU stats
  
```console
$ nvidia-smi
A brief summary of all Nvidia devices

$ nvidia-smi -L
GPU 0: <information about gpu 0>
GPU 1: <information about gpu 1>
GPU 2: <information about gpu 2>
GPU 3: <information about gpu 3>

$ nvidia-smi stats -d gpuUtil
display the gpu usage (similar to CPU usage, in percentage) repeatedly for every device.
```