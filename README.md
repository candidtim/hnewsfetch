# Hacker News Top Stories for the terminal

This simple script fetches latest top stories from [Hacker News](https://news.ycombinator.com/) and displays them in
the termial's standard output. For example, combined with "cowsay" it looks like:

![hnfetch](https://raw.githubusercontent.com/candidtim/hnewsfetch/gh-pages/img/hnfetch.png)

Most terminal emulators will let you click on the links, which will take you to the story itself, or the comments.

## How to use

This script is kept simple intentionally and can be simply copied anywhere on the file system and executed with Python.
It only requires bare bones Python 3 and doesn't depend on any external library. On Linux/MacOS it is recommended to
grant it an "execution" permission and put into `$PATH`:

    $ wget https://raw.githubusercontent.com/candidtim/hnewsfetch/master/hnfetch.py -O hnfetch
    $ chmod +x hnfetch
    $ ./hnfetch

Much improved user experience is achieved when combined with [cowsay](https://en.wikipedia.org/wiki/Cowsay):

    $ hnfetch | cowsay -n

Make sure `-n` option is specified, or cowsay will fail to print the message correctly.

(Hint: cowsay is normally available for any popular Linux distribution. For example, on Debian/Ubuntu install it with
`sudo apt-get install cowsay`)

I like adding it to my `.bashrc` - this way it shows me one of the latest top stories every time I open new terminal
window. The obvious drawback however is that this way there is some noticeable delay before the prompt is open, due to
the time it takes to request the REST service to fetch the story.


## Why?

Because I'm a fan of `fortune | cowsay`, but got bored with fortune's fortunes. Being also a fan of 'Hacker News', I
thought that this is a nice way to keep up to date with latest top news.


## How it works

It uses nice and easy [Hacker News API](https://github.com/HackerNews/API)


## Copying

Copyright (c) 2015 candidtim

[The MIT License (MIT)](http://opensource.org/licenses/MIT)

![Open Source Initiative](http://opensource.org/files/osi_logo_100X133_90ppi_0.png)
