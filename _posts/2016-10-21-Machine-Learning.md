---
layout: post
title: 机器学习
categories: note
excerpt: 笔记内容只能保证我能看的懂，请不要查看
tags: coursera
---
<!-- {% include MathJax.html %} -->

[斯坦福大学公开课](//coursera.org/learn/machine-learning)  



## 介绍

- 监督学习：把样本分成具体的类，如邮件分类。
- 无监督学习：把样本分成若干类，不知道各类特性，如百度新闻分类  

## 线性回归
- 方案：h(x) = θ'X
- 代价函数：J(θ) = \frac{1}{2m} * sum[ (h(x) - y)^2 ]
- 梯度下降： θ = θ - \frac{a}/{m} *( θ‘X - Y )'X

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
- 分为多类时(y = 1 2 ... n)  
  y=1为1类，y=其他为另一类，共两类，即化为2类问题  
  最后各类均有θ，求max(h(x))的索引

## 过拟合  
- 方法  
	1.丢弃一些不能帮助我们正确预测的特征。  
	2.正则化(保留所有的特征,但是减少参数的大小)  
-  线性和逻辑  
  J = J + 入/2m*sum(θ) **θ不包含θ0**当不处罚θ0时  
  θ = (1-入/m)θ
  **θ0 = θ0**    
- 正规方程  
  θ = inv(X'X-入ones(n+1,n+1))X'Y **ones的（0,0）为0**  

## 神经网络
- 概念  
  基于[逻辑回归](./#逻辑回归)，多类。各类均有1个向量θ，同理最后求其max(概率)。特别之处在于中间有递归多次。  
  比如1000样本分成10类，按逻辑回归思路，一步到位，而神经网络会把其先分为500,再把500分成100,最后10.  
  **每步的样本输入为h(x)**,而非Xθ，否则经过多次递归肯定出错。  
  而逻辑回归只有一步 && h(x)单调增，故max(Xθ)效果同max(h(x))  
  当然，每步和输入的样本维度要+1  
  ![]({{ site.storage }}assets/dist/img/2016-10-27 16-49-51屏幕截图.png)  
  蓝圈x，红圈h(x)  

- 回归算法  
a1 -> z2 -> a2 -> z3
{% highlight matlab %}
a1 = [ones(m, 1) X]; %5000*401 1层准备输入2层
z2 = a1*θ1'; %5000*401 25*401   输入到2层的结果
a2 = [ones(m, 1) h(z2)]; %5000*26 2层准备输入3层
z3 = a2*θ2'; %5000*26 26*10  输入到3层的结果
out= h( z3 ); %5000*10  3层准备输出
{% endhighlight %}

{% highlight matlab %}
θ2_grad =  (h-y)'*a2/m;
sigma2 = ((h-y)*θ2(:,2:end)).*hGrad( z2 );
θ1_grad = sigma2'*a1/m;
{% endhighlight %}

{% highlight matlab %}
当中间有一层网络时，
θ2_grad可简单的看成 (a2*θ2-y)对θ2求导，结果为a2
θ1_grad可简单的看成h(a1*θ1)*θ2对θ1求导，结果为h'(a1*θ1)*θ2*θ1  
当中间有两层网络时，  
θ1_grad可简单的看成h(h(a1*θ1)*θ2)*θ3对θ1求导，结果为h'(h(a1*θ1)*θ2)*θ3*θ2*θ1*h'(a1*θ1)  
即h'(z3)*θ3*θ2*θ1*h'(z2)  
当中间3层时θ1_grad = h'(z4)*h'(z3)*h'(z2)*θ4*θ3*θ2*θ1
{% endhighlight %}

## 调参  

- 欠拟合  
入=0,维度=2  
![欠拟合]({{ site.storage }}assets/dist/img/ml-10-1.png)  
参数过少导致y值最终过大（欠拟合）  
![欠拟合]({{ site.storage }}assets/dist/img/ml-10-2.png)  
- 过拟合  
扩大x的维度，入=0,维度=9  
![过拟合]({{ site.storage }}assets/dist/img/ml-10-3.png)  
此时训练误差过小，过拟合  
![过拟合]({{ site.storage }}assets/dist/img/ml-10-4.png)  
- 调整入  
维度=9，样本数=max，入=1  
![调整入=1]({{ site.storage }}assets/dist/img/ml-10-6.png)
维度=9，样本数=max，遍历入，发现3最合适  
![调整入]({{ site.storage }}assets/dist/img/ml-10-5.png)   
