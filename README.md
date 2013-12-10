# newslint

A linter for detecting bias, subjectivity, and inaccuracy in news clippings.

A little project to lint a block of text to see how newsworthy, objective, sensationalist, pundit-prone, etc. it is.  It comes from my interest in reading the news and identifying political bait.  And it was enabled by the excellent joblint project originally done in JavaScript by [Rowan Manning](https://github.com/rowanmanning/joblint).

## Run

Type `python newslint.py "[block of text]"` at a console to lint it.  You will get a log report of errors, warnings, and notices along with what rules were found when linting the clipping.

## Credits

This is a Python modification/translation of Rowan Manning's excellent JavaScript package, `joblint`:

https://github.com/rowanmanning/joblint

My Python fork of Rowan's repo is at:

https://github.com/Xeus/joblint_python
