#!/usr/bin/env python
# encoding: utf-8

def colorprint(text, colour="green"):
    colours = dict(
        zip(["black", "red", "green",
             "yellow", "blue", "magenta",
             "cyan", "white"], range(30, 38)
        )
    )

    print "\x1b[1;%(colour)sm%(text)s\x1b[0m" % {
        "colour": colours[colour], "text": text,
    }

def warning(text):
    colorprint(text, "yellow")

def error(text):
    colorprint(text, "red")

def success(text):
    colorprint(text, "green")

def info(text):
    colorprint(text, "blue")
