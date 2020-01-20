---
layout: post
title: "Rewriting the Kullback-Leibler with an integral transform"
date: 2020-01-20 16-58-15 +0000
category: blog
tags: 

---

I recently heard of this nice integral representation of the logarithm in 1912.05812v1 by Neri Merhan and Igar Sason. Most ideas in this post are from there. The transform is:
$$
\log(x)=\int_{0}^{\infty}\frac{e^{-t}-e^{-tx}}{t}dt.
$$
This can be shown by using $$\log(x)=\int_{1}^{x}1/t\cdot dt$$ along with $$\frac{1}{x}=\int_{0}^{\infty}e^{-xu}du$$. It all becomes more interesting when we take an expectation though:
$$
\mathbb{E}[\log(X)]=\int_{0}^{\infty}\frac{e^{-t}-\mathbb{E}[e^{-tX}]}{t}dt
$$
This allows us to express the expectation of the logarithm in terms of the moment generating function of $$X$$. For instance, if $$X$$ is normal, then such a representation will probably be simpler. It is not obvious that it will help with computation, but it does suggest that we can use stuff like concentration bounds for expectations of logarithms. 

It’s fun to apply the same idea to the KL. 
$$
R(Q|P)=\int Q(x) \log \frac{Q(x)}{P(x)}dx.
$$
For simplicity, let $w(x):=\log\frac{Q(x)}{P(x)}$. Then, from (2):
$$
\mathbb{E}_Q[\log w]=\int_{0}^{\infty}\frac{e^{-t}-\mathbb{E}_Q[e^{-tw}]}{t}dt.
$$

(4) is a different way to express the KL divergence. It’s not particularly useful as is (to my eyes), as the MGF of $$w$$ is a tough cookie to compute. However, with a lower bound to the MGF we could get an upper bound to the KL that is not trivial. 