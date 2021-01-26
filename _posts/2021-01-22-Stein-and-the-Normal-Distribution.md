---
layout: post
title: "Stein and the Normal Distribution"
date: 2021-01-22 19-32-07 +0000
category: blog
tags: 
---


Hello and happy 2021!

Inspired from this
[tweet](https://twitter.com/docmilanfar/status/1312936010393640961?s=20), I
wanted to understand the basics of Stein’s characterization of the Normal
distribution.

With Stein's idea, we can identify the distribution of a random variable by
checking that it satisfies some condition in expectation. For example, for the
standard normal, we have that $$X\sim N(0,1)$$ if and only if for all $$f$$ with
$$E[f']<\infty$$ we have:

$$\mathbb{E}[xf(x)-f'(x)]=0.$$

The operator $$Af:=xf-f'$$ is then called the Stein operator and we can rewrite
the result with this operator as: $$\mathbb{E}_{P}[Af]=0$$ for all $$f\in C^1_b$$ iff
$$P$$ is $$N(0,1)$$.

This operator is not unique as we can always add P-measure zero parts; see
$$Bf:=xf-f'+x$$ which satisfies

$$\mathbb{E}[Bf]=\mathbb{E}[Af]+\mathbb{E}[x]=\mathbb{E}[Af].$$

How can we show $$A$$ characterises the standard Normal? A key identity is that
the probability density function (PDF) of the $$N(0,1)$$ satisfies $$P'+xP=0$$. So,
if $$P$$ is indeed the PDF of the standard normal, then applying integration by
parts to $$E_{P}[f']$$ and using the differential equation gives us Stein's
formula.

Now, if $$P$$ is the PDF of any other distribution and it satisfies Stein's
formula for all $$f\in C^1_b$$, then integration by parts on $$E_{P}[f']$$ leads us
back to the $$P'+xP=0$$. That ODE is separable with solution $$P\propto
\exp(-x^2/2)$$, which, up to the normalisation, is the PDF of the standard
normal!

This strategy of deriving an ODE for the density function, getting its weak form
by multiplying with a smooth function $$f$$ and integrating can be repeated to get
[Stein
operators](https://en.wikipedia.org/wiki/Stein%27s_method#The_Stein_operator)
for other distributions, e.g., the exponential, etc.


