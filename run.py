#!/usr/bin/python
#--*-- coding: utf-8

from bayes import Plot
from bayes.hockey import *

suite1 = Hockey("bruins")
suite1.UpdateSet([0, 2, 8, 4])

suite2 = Hockey("canucks")
suite1.UpdateSet([1, 2, 1, 0])

# Plot().Line(suite1)
# Plot().Line(suite2)
Plot().MuliLine([suite1, suite2])