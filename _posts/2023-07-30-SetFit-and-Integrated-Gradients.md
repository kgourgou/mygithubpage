---
layout: post
title: "SetFit and Integrated Gradients"
date: 2023-07-30 11-19-39 +0100
category: blog 
tags: 
---

I'm a fan of both SetFit and integrated gradients, so I wrote this tiny library to combine them. The code is available [here](https://github.com/kgourgou/setfit-integrated-gradients) under MIT license for further hacking by others. I'm fixing bugs, but otherwise not actively maintaining it. 

## What is SetFit ?

It's a [language-model-tuning paradigm ](https://huggingface.co/blog/setfit) for few-shot learning with language models without using prompts. It relies on contrastive learning and the authors published a really nice library that makes the method plug & play with sentence-transformers. 

I have been contributing some time to that library on Github as well. 

## What are integrated gradients ?

[Integrated gradients (IG)](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients) are a method for attributing the output of a neural network to its inputs. It was first developed to explain the output of image classifiers, but it can be used for any model that takes a vector as input. 

It occured to me by building this that there are various places one could perturb to apply IG and that the perturbation path probably also matters a lot. 
