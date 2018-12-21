---
layout: post
title: "Bounds on joint probabilities - Part I"
date: 2018-06-29 12-31-22 +0100
category: blog 
tag:  
---

Here are some notes on bounding joint probability distributions. Enjoy! This was
converted from $$\LaTeX$$ with pandoc, so typos, missing figures, etc., to be expected. 

Consider the binary random variables $$X_1, \ldots, X_n$$ following the
distribution $$P$$. For some collection of values, say,
$$x_1, \ldots, x_n$$, we are interested in computing
$$P(X_1=x_1,\ldots, X_n=x_n)$$.

There is rich literature on bounding joint probabilities, say, $$P(X_1,X_2,X_3)$$, if one has of
knowledge of the marginals, $$P(X_i),$$ $$i=1,2,3$$, $$ P(X_{i},X_j)$$,
$$i\neq j$$, or of the moments of the marginal distributions. Some
examples of such inequalities follow below.

When the bounds only use $$P(X_i)$$, we will say that they utilize
*first-order* information. Similarly, if $$P(X_i, X_j)$$ are used in the
bounds, they are of second-order, then third-order, etc.

Bonferroni inequalities
-----------------------

We start with a classical result, inspired from the inclusion-enclusion
formula, known as the *Bonferroni* 
inequalities [@galambos1977bonferroni]. The notation $$X^c$$ corresponds
to the negation of the $$X$$ variable, i.e., if $$X=x$$, $$X^c=1-x$$ for
$$x\in \{0,1\}$$. First, we define:

$$\begin{aligned}
  S_1&:=\sum_{i}P(X_i^c),\\
  S_k&:=\sum_{1\leq i_1< \ldots < i_k\leq n} P(X_{i_1}^c,\ldots, X_{i_k}^c),\\\end{aligned}
$$
  
Then, for every odd $$k$$ in $$\{1,\ldots, n\}$$: 

$$
\begin{aligned}
  P(X_1,\ldots, X_n)&\geq 1 -\sum_{j=1}^{k} (-1)^{j-1}S_j.
\end{aligned}
$$
  
We can also get an upper bound for every even $$k$$:

$$\begin{aligned}
  P(X_1,\ldots, X_n)&\leq 1 -\sum_{j=1}^{k} (-1)^{j-1}S_j.\end{aligned}$$
  
By the inclusion-exclusion formula, the inequalities become equalities
when $$k=n$$. Thus, the inequalities can be made sharper by including more
marginals. However, the upper (and lower) bounds don’t necessarily
become sharper monotonically as $$k$$ increases; see work
by [@schwager1984bonferroni]. Also, although the inequalities are valid
for all $$k$$, they can be uninformative, that is, smaller than zero or
greater than one.

Frechet bounds
--------------

An alternative upper bound for the joint is the Frechet-type bound:

$$
\begin{aligned}
  \label{eq:frechet}
 P(X_1,\ldots, X_n)\leq \min_{i}P(X_i).
 \end{aligned}
 $$ 
 
This can be
simply derived by observing that, for any $$i$$,

$$P(X_1,\ldots, X_n)=P(X_1,\ldots,X_{i-1},X_{i+1},\ldots, X_n|X_i)P(x_i)\leq P(X_i)$$

and then picking the tightest bound. We can also include terms like
$$P(X_i,X_j)$$ to the upper bound, if known, to get an even tighter bound.
As an upper bound, this may be more suitable than the Bonferroni bound;
it is always a valid probability and can be tight when dealing with rare
events. Like the Bonferroni bound, this is distribution-independent.

Now, if all we know about the $$X_i$$ are the $$P(X_i)$$, then the tightest
bounds[^1] we can get are:

$$\begin{aligned}
\label{eq:frechet-first}
 \max\{0,1-\sum_i(1-P(X_i))\} \leq P(X_1,\ldots, X_n)\leq \min_{i} P(X_i).\end{aligned}$$

The lower bound comes from the first Bonferroni lower bound. However, it
can be further sharpened by adding second-order information, that is,
some of the $$P(X_i^c,
X_j^c)$$, as discussed by [@hochbergsome]. One example of such a
sharpening is known as the *Kounias* inequality: 

$$\begin{aligned}
\label{eq:kounias}
 1-\sum_{i}(1-P(X_i))+\max_j \sum_{i\neq j}P(X_i^c,X_j^c)\leq P(X_1,\ldots, X_n).\end{aligned}$$

This can be further sharpened by replacing the max term in by

$$\sum_{i,j:(i,j)\in T} P(X_i^c, X_j^c),$$

where $T$ is the maximal
spanning tree, i.e., the tree that maximizes the sum of the
probabilities[^2]. The new bound then is:

$$\begin{aligned}
\label{eq:wolfe}
 1-\sum_{i}(1-P(X_i))+\sum_{i,j:(i,j)\in T} P(X_i^c, X_j^c)\leq P(X_1,\ldots, X_n).\end{aligned}$$

This bound was first derived in work by [@hunter1976upper] and has been
subsequently generalized to work with more events via the construction
of multi-trees; see work by [@bukszar2001upper].

Multiplicative bounds
---------------------

In some cases, multiplicative bounds, that is,

$$P(X_1,\ldots X_n)\geq P(X_1)\ldots P(X_n),$$ 

may also be applicable when the random variables show positive association; see work
by [@esary1967association] for details on that. Those bounds are easier
to apply and often tighter but may not always be correct as they are
distribution dependent. Especially for Bernoulli variables, Theorem 4.
in [@esary1967association] shows that association of the
$$X_1,\ldots, X_n$$ implies only that 

$$\begin{aligned}
P(X_1=1,\ldots, X_n=1)&\geq P(X_1=1)\ldots P(X_n=1),\\
P(X_1=0,\ldots, X_n=0)&\geq P(X_1=0)\ldots P(X_n=0).\end{aligned}$$


