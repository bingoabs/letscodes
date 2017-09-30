#!/usr/bin/python
#--*-- coding: utf-8


import matplotlib.pyplot as plt


class Plot(object):
    def __init__(self, name="default_name"):
        self.name = name

    def Line(self, suite):
        items = sorted(suite.Items(), key=lambda item: item[0])
        x, y = zip(*items)
        plt.plot(x, y)
        plt.show()


    def MuliLine(self, suites):
        for suite in suites:
            items = sorted(suite.Items(), key=lambda item: item[0])
            x, y = zip(*items)

            plt.plot(x, y)

        plt.show()
