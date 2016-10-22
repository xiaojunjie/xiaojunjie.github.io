---
layout: post
title: 机器学习
categories: note
tags: coursera
---

[斯坦福大学公开课](//coursera.org/learn/machine-learning)

## 介绍

- 监督学习：把样本分成具体的类，如邮件分类。
- 无监督学习：把样本分成若干类，不知道各类特性，如百度新闻分类

## 线性回归
- 方案：h(x) = θ'X
- 代价函数：J(θ) = 1/2m * sum[ (h(x) - y)^2 ]
- 梯度下降： θ = θ - a/m*( θ‘X - Y )'X

## 正规方程
- θ = inv(X'X)X'Y 
- 求逆O(n^3),适用于n<10000
- 正规方程仅用了线性回归

## 逻辑回归
- 方案：h(x) = 1/[1+exp(-θ'X)]
- 代价函数：  
  if y=1 	**-log(h(x))**    
  if y=0	 **-log(1-h(x))**
- 梯度下降： θ = θ - a/m*( θ‘X - Y )'X

---


