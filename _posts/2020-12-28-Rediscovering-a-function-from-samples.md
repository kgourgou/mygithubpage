---
layout: post
title: "Rediscovering a function from samples"
date: 2020-12-28 18-06-27 +0000
category: blog
tags: 
---


A friend shared this nice problem with me. Suppose you have a fixed function, $$f$$, and a family of probability distributions, defined by, say, prob. density functions, $$P_t$$, $$t \in A$$. If we know $$E_t=E_{P_t}[f]$$ for every $$t\in A$$, can we recover $$f$$?

Clearly the answer depends on both how rigid $$f$$ is and the family $$P_t$$. We can cast this problem as a functional analysis problem by defining $$k(x,t)=P_t(x)$$ to be a kernel and the expectation to be an integral transform. Then the question becomes: is there an inverse kernel, say, $$k^{-1}(x,t)$$, such that
$$
\int k^{-1}(x,t)E(t)dt=f(x)?
$$
When does that exist and when is it unique? Hints can be taken from the Laplace transform, i.e., $$P_t(x)\propto e^{-tx}$$ - up to a normalizing constant this is the just the exponential distribution. In general, this can be a hard problem though. 



## Fredholm equations

If we know $$E_t=E_{P_t}[f]$$ for every $$t\in A$$, can we recover $$f$$? Formally, we have the equation:
$$
E(t)=\int k(x,t)f(x)dx.
$$
This equation is called a **Fredholm Equation of the first kind** (cause it doesn't have an "eigenvalue" component). Formally, the integral should also have limits. 



## Practical stuff

If we assume the existence of an inverse kernel, how can we approximate it? One idea — which is also kind of a standard approach — is to fix a set of orthonormal basis functions, describe everything in terms of them, and then resolve them to arrive to a linear algebra problem. 
