# Tutorial releases

> Tutorial has to be versioned because we should be able to give translators information that the tutorial has significant changes that affect all the languages and that they need to make additional translation changes (or at least check if the tutorial requires changes).

## Naming convention
The releases should be named in a sepcific pattern:
vX.Y.Z+YYYYMMDD

This gives us the ability to tell at what stage and what specific DG event has the tutorial changed.

Z - small changes, typos, we shouldn't really change it, in our case it should be 0 all the time

Y - changes that make a bigger difference but don't change the whole project structure

X - changes that are or may be backwards incompatible, like introducing gitbook 2.0.0 or changing the whole approach of the tutorial

## Creating releases 
A great reference about creating releases can be found on GitHub, and we should use it:
https://help.github.com/articles/creating-releases/

## Changelog.md
I am generating Changelog.md automatically with [GitHub Changelog Generator](https://github.com/skywinder/github-changelog-generator) but we should decide whether we are only writing down the most important changes in the release notes.
