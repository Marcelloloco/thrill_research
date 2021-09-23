# Simple Thrill Project

This is a simple project using Thrill as a git submodule via CMake project files.

This repository was forked from https://github.com/thrill/tutorial-project to do research 
on Thrill and use it as a setup for an example project. The submodule for Thrill was changed to a fork of the core 
library, where changes could be made. Furthermore, the main.cpp was changed for the Word Count program written by 
Elsa Buchholz and was taken from https://github.com/elsabuchholz/parallel_algorithm_thrill. 

When cloning this repository, use the `--recursive` option:

```
git clone --recursive https://github.com/Marcelloloco/thrill_research.git
```

If you forgot that, then run `git submodule update --init --recursive` to get the missing repositories.

For more information, see https://project-thrill.org

Written 2018-10-24 Timo Bingmann
