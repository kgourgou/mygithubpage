---
layout: post
title: "A computable lower bound for the KL from Hammersley-Chapman-Robbins inequality"
date: 2020-12-28 17-43-32 +0000
category: blog
tags: 
---


I first read of this bound from: 

```
Nishiyama, T., 2019. A New Lower Bound for Kullback-Leibler Divergence Based on Hammersley-Chapman-Robbins Bound. arXiv:1907.00288 [cs, math, stat].
```

The following notes are not very polished, but present the general idea. I hope they are useful.

The strategy of the paper is quite nice; first, Nishiyama shows that if we have two distributions $$P,Q$$ and define the mixture $$R_t(x):=P(x)+t(Q(x)-P(x)), t\in [0,1]$$, then: 

$$\frac{d}{dt}D_a(P|R_t)=\frac{1-a}{t}D_a(P|R_t)+\frac{1+a}{t}D_{a+1}(P|R_t),$$

for any $$a$$ and $$D_a$$ being the alpha-divergence. Setting $$a=1$$ leaves us with the KL divergence and $$\chi^2$$, which recovers the nice identity:

$$\frac{d}{dt}KL(P|R_t)=\frac{1}{t}\chi^2(P|R_t).$$

Now, fix a function $$f$$ for which $$E_Q, E_P, V_P, V_{R_t}$$ (expectations and variances) are finite and $$V_{R_t}>0$$ for all $$t\in [0,1]$$. Then, applying the HCR inequality gives: 



$$\frac{d}{dt}KL(P|R_t)\geq \frac{(E_{R_t}-E_P)^2}{tV_{R_t}}.$$



Integrating the above in $$[0,1]$$ gives the result of the paper as 
$$\int_0^1 KL(P|R_t)dt=KL(P|Q).$$



We can also show that

$$KL(P|Q)=\int_0^1 \frac{\chi^2(P|R_t)}{t}dt=\int_0^1 t\int_{\Omega}\frac{(Q-P)^2}{P+t(Q-P)}dxdt.$$

Assuming everything exists, we can exchange the integrals (ala. Fubini) and then expand the $$t$$ function around $$t=1$$ to introduce the chi-square divergence:

$$KL(P|Q)=\chi^2(P|Q)+...$$




## Actual lower bound

The lower bound is:

$$KL(P|Q)\geq \int_0^1\frac{(E_{R_t}-E_P)^2}{tV_{R_t}}dt,$$

where the integral depends on $$E_P, E_Q, V_P, V_Q$$ and can be computed analytically and written as a sum of logarithms (by using partial fractions). 



# Tighter lower-bounds

Starting from the equality:

$$KL(P|Q)=\int_0^1 \frac{\chi^2(P|R_t)}{t}dt$$

we can derive tighter lower bounds for the KL. First, we write the variational representation of  $$\chi^2$$ 

$$\chi^2(P|R_t)=\sup_{h}\left \{ 2E_P[h]-E_Q[h^2]-1\right \}.$$

Suppressing the family of functions leads to lower bounds of chi-square and thus to lower bounds of $$KL(P|Q)$$. The HCR bound can be derived by considering the class of first degree polynomials: $$ax+b$$.  
