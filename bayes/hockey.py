#!/usr/bin/python
#--*-- coding: utf-8


import thinkbayes


USE_SUMMARY_DATA = True

class Hockey(thinkbayes.Suite):
    """Represents hypotheses about the scoring rate for a team"""

    def __init__(self, name=""):
        """Initializes the Hockey object.
        name: string
        """
        if USE_SUMMARY_DATA:
            # prior based on each tema's average goals scored
            mu = 2.8
            sigma = 0.3
        else:
            # prior based on each pair-wise match-up
            mu = 2.8
            sigma = 0.85

        pmf = thinkbayes.MakeGaussianPmf(mu, sigma, 4)
        thinkbayes.Suite.__init__(self, pmf, name=name)



    def UpdateSet(self, dataset):
        for data in dataset:
            for hypo in self.Values():
                print("hypo: {}".format(hypo))
                like = self.Likelihood(data, hypo)
                self.Mult(hypo, like)
        return self.Normalize()

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.
        Evaluates the Poisson PMF for lambda and k.

        hypo: goal scoring rate in goals per game
        data: goals scred in one period
        """
        lam = hypo 
        k = data 
        like = thinkbayes.EvalPoissonPmf(k, lam)
        return like


        lam = hypo 
        k = data 
        like = EvalPoissonPmf(lam, k)
        return like
