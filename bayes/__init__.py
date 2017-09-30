#!/usr/bin/python
#--*-- coding: utf-8


import matplotlib.pyplot as plt


def showLine(suite):
    x, y = zip(*suite.Items())
    plt.plot(x, y)
    plt.show()


def showMuli(suites):
    for suite in suites:
        x, y = zip(*suite.Items())
        plt.plot(x, y)
    plt.show()
