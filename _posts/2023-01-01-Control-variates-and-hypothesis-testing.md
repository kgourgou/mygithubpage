---
layout: post
title: "Control variates and hypothesis testing"
date: 2023-01-01 16-42-22 +0200
category: blog
tags:
---


I haven’t looked at this in a while, so thought I would revise a bit.

To start with, I have a variable, say, $$Y\sim P$$. Given data from this variable, $$y_i$$, we can estimate the mean
$$
E[Y]\approx S_N=\frac{1}{N}\sum_{i=1}^{N}y_i.
$$
The estimator we all know and use. It’s unbiased, but it may have large variance, which means that for a fixed N, most random sums could fall away from $$E[Y]$$. What can we do to improve on this?

One idea is to introduce a new variable, $$X$$. Then, we adjust the data as

$$y'_i=y_i+a(x_i-E[x_i]),$$

where $$a$$ is some parameter that we can pick later. What's the advantage of this? First, this adjustment doesn't change the mean:
$$E[Y']=E[Y]+a(E[X]-E[X])=E[Y].$$
So an estimator based on $$Y'$$ is unbiased. Not bad.

What is the variance of this new estimator?

$$\mathrm{Var}[Y'] = \mathrm{Var}[Y] + a^2\mathrm{Var}[X] + 2\mathrm{Cov}[Y,aX].$$

Now the first two terms are non-negative. However, the last one can be negative as long as $$X$$ and $$Y$$ have negative correlation. For instance, picking $$X=-Y$$,

$$\mathrm{Var}[Y'] = \mathrm{Var}[Y] + \mathrm{Var}[Y] - 2\mathrm{Cov}[Y,Y] = 0,$$

which is the best possible variance. Realistically, we are back to where we started if we set $$X=-Y$$, however if we have other variables that are close to $$-Y$$, then this idea can get quite useful (and dramatically reduce variance).


## In hypothesis testing

Why would all this be useful for hypothesis testing?

To conduct it, we first split the population to two groups, traditionally called the "treatment" and "control". We have intervened on the treatment group in some way, say via a variable $$Z$$, and we wish to understand whether the magnitude of $$E[Y_T-Y_C]$$ (this is also called the average treatment effect (ATE)) is due to $$Z$$ or random chance.

Suppose that the difference is indeed due to $$Z$$. If we use data to estimate $$E[Y_{T}-Y_{C}]$$, the estimator can have variance and that will affect how small an effect we can confidently separate from random chance.

We are now thinking about the "*power* " of a hypothesis test, and there are at least three ways to improve our situation from here:

1. Give up on the small effect size and go for a larger one.
2. Get more $$Y_T, Y_C$$ data for the estimator, i.e., make the groups larger.
3. Use other covariates, $$X$$, to reduce the variance of the ATE estimator. Only covariates that are independent of the way the groups are split can be used, for example pre-experiment data.

Now we can discuss two ways to increase the power of the test by using 3.


### CUPED and CUPAC

You can find implementations of [CUPED and CUPAC in this notebook](https://github.com/kgourgou/cupac_cuped_control_variates/blob/main/cuped_cupac.ipynb).

CUPED stands for "Controlled-Experiment using Pre-experiment data"; see Deng, Xu, Kohavi, Walker, 2013.

At its core, CUPED is a proposal for how to use pre-experiment data with control variates to reduce the variance of the ATE estimator. The authors propose using any covariates that we have before the experiment took place, $$X_i$$, $$i=1,\ldots, n$$, as well as past values of $$Y$$ to fit a linear model:
$$\hat{Y}=X\beta +\epsilon$$

Then, we can use the linear model to get predictions for the $$Y$$ variables in the control and experiment groups and adjust the true values as
$$Y'_T=Y_{T}-(\hat{Y}_T-E[\hat{Y}_T]),$$
and similarly for $$Y_C$$. Instead of the original ATE, we will then construct an estimator for $$E[Y'_T-Y'_C]$$ which, because of our control variates method, will have smaller variance!

CUPAC, aka., Control Using Predictions As Covariates, introduced by DoorDash's engineering, [Li, Tang, and Bauman](https://doordash.engineering/2020/06/08/improving-experimental-power-through-control-using-predictions-as-covariate-cupac/), takes this one step further: there's nothing special about using a linear model. One can use a more expressive ML model, get a closer fit to $$Y$$, and reduce variance further.


