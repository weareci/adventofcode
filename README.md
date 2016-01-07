Advent of Code
==============
Advent of Code is a series of small programming puzzles for a variety of
skill levels. It is good for both beginners who are first learning and
even for experts who need to keep their skills sharp.

Read the fill about section from the site itself:
http://adventofcode.com/about

What is this repository?
------------------------
This repository includes **solutions** to the problems for Advent of Code.
I am including the solutions with detailed comments here to help see how
a professional software developer may go about solving these problems.

**Before looking at the answers, try to find the solution yourself.**

Learning how to code is all about making mistakes, banging your head in
frustration, and perserverance. But learning how to code is also about
learning from others, which is why there are solutions in here.

What language should I use?
---------------------------
You should use either Python or Ruby. Solutions for both have been
included here. If you have never used either of these languages, spend
some time on [codecademy](https://www.codecademy.com/) learning either
one.

Don't worry about choosing the wrong language.  Programming languages
are all very similar to each other and once you have learned a few, it
is very easy to pick up a new language. You cannot choose a wrong
language.

It personally took me about 3-6 years to become proficient in my first
language, 1-2 years in my second, 3-6 months for my third, and each
language after that is now usually about a month or two. In fact,
learning my second programming language helped me learn my first
programming language better.

How is this repository structured?
----------------------------------
The repository has a folder for each day and a README.md describing the
problem. The scripts are written in a way that you can answer both the
initial problem and the expanded problem.

The Python solution has a `.py` extension while the Ruby solution has a
`.rb` extension.

There is an `input.txt` file in every directory. This is the input **I**
received when solving the problem. It is included just to show how the
program works.

What if I don't understand something?
-------------------------------------
Ask! Send an email to one of your coaches and ask if they have time to
explain some part of what the code does.

How do I run the programs?
--------------------------
You can run these programs on Windows, Mac OS X, or Ubuntu. At the
moment, the easiest way to run them is to use the command line. If you
have never used a command line before, you should try the lesson on the
command line in [codecademy](https://www.codecademy.com/).

If you are on a Chromebook, you cannot run these on your computer.
While Chromebooks are very cheap, they are not useful for programming.

Windows
=======
Download [Git](https://git-scm.com/).

If you want to use Python, download [Python
2](https://www.python.org/downloads/windows/).

If you want to use Ruby, the official project doesn't provide easy
installation instructions for Windows. You can use
[RubyInstaller](http://rubyinstaller.org/downloads/) to more easily
install Ruby.

Afterwards, open the `Git Shell` program using the `Start` menu (it
should have been installed by Git). Afterwards, run the following:

```bash
$ git clone git://github.com/weareci/adventofcode
$ cd adventofcode
$ python day1/main.py < day1/input.txt
```

Each line starts with a dollar sign (`$`) and ends with pushing `ENTER`
or `RETURN`.

After performing these commands the first time, you only have to `cd`
into `adventofcode`.

Mac OS X
========
Git is already installed on your computer. Open
`Applications/Utilities/Terminal`. Afterwards, run the following:

```bash
$ git clone git://github.com/weareci/adventofcode
$ cd adventofcode
$ python day1/main.py < day1/input.txt
```

Each line starts with a dollar sign (`$`) and ends with pushing `ENTER`
or `RETURN`.

After performing these commands the first time, you only have to `cd`
into `adventofcode`.

Ubuntu
======
You can also use other versions of Linux, but Ubuntu is the most common.

In Ubuntu, all of the tools except `git` are already installed. Open a
terminal and run the following:

```bash
$ sudo apt-get install -y git
$ git clone git://github.com/weareci/adventofcode
$ cd adventofcode
$ python day1/main.py < day1/input.txt
```

Each line starts with a dollar sign (`$`) and ends with pushing `ENTER`
or `RETURN`.

After performing these commands the first time, you only have to `cd`
into `adventofcode`.
