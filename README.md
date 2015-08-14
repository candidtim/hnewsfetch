# Hacker News Top Stories for the terminal

This simple tool fetches latest top stories from [Hacker News](https://news.ycombinator.com/) and displays them in
the termial's standard output. For example, combined with "cowsay" it looks like:

![hnfetch](https://raw.githubusercontent.com/candidtim/hnewsfetch/gh-pages/img/hnfetch.png)

Most terminal emulators will let you click on the links, which will take you to the story itself, or the comments.


## How to use

This script is kept simple intentionally and can be simply copied anywhere on the file system and executed with Python.
It only requires bare bones Python 3 and doesn't depend on any external library (see 'Speed it up' section below though).
On Linux/MacOS it is recommended to grant it an "execution" permission and put into `$PATH`:

    $ wget https://raw.githubusercontent.com/candidtim/hnewsfetch/master/hnfetch.py -O hackernews
    $ chmod +x hackernews
    $ ./hackernews

Much improved user experience is achieved when combined with [cowsay](https://en.wikipedia.org/wiki/Cowsay):

    $ hackernews | cowsay -n

Make sure `-n` option is specified for cowsay, or cowsay will fail to print the message correctly.

(Hint: cowsay is normally available for any popular Linux distribution. For example, on Debian/Ubuntu install it with
`sudo apt-get install cowsay`)

I like adding it to my `.bashrc` - this way it shows me one of the latest top stories every time I open new terminal
window. The obvious drawback however is that this way there is some delay before the prompt is open, due to the time it
takes to request the REST service to fetch the story. See next section however!


### Speed it up

Note that if `urllib3` is installed and is available for Python, this tool will benefit of it and will be about twice
as fast. With my internet connection for example, it takes about 800 msec to get the story with `urllib3` installed,
as opposed to 1300 msec when using Python's standard `urllib`. This small performance improvement might be handy if
this is used in `.bashrc` for example.

[`urllib3`](https://github.com/shazow/urllib3) is often already installed in most Linux distributions


### Selecting stories

By default, the tool will display a random story from current top 10 stories. It is possible to adjust it:

Select random story from current top 42:

    $ hackernews -n 42

Show only the top story (should work unless someone proves `randint(1,1)` being something different from 1):

    $ hackernews -n 1

Select stories from "newest stories" instead or "top stories":

    $ hackernews --newest


## Why?

Because I'm a fan of `fortune | cowsay`, but got bored with fortune's fortunes. Being also a fan of 'Hacker News', I
thought that this is a nice way to keep up to date with latest top news.


## How it works

It uses nice and easy [Hacker News API](https://github.com/HackerNews/API)


## Copying

Copyright (c) 2015 candidtim

[The MIT License (MIT)](http://opensource.org/licenses/MIT)

![Open Source Initiative](http://opensource.org/files/osi_logo_100X133_90ppi_0.png)
