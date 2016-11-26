---
layout: post
title: Algorithms 2.3-7
excerpt: 判断集合中是否有两个数的和等于某个给定整数
categories: note
tags: 算法
---
判断集合中是否有两个数的和等于某个给定整数  
{% highlight C++ %}
3 void quickSort(int s[], int l, int r) {
4     if (l < r) {
5       int i = l, j = r, x = s[l];
6         while (i < j) {
7             while(i < j && s[j] >= x) j--;
8             if(i < j) s[i++] = s[j];
9
10             while(i < j && s[i] < x) i++;
11             if(i < j) s[j--] = s[i];
12         }
13         s[i] = x;
14         quickSort(s, l, i - 1);
15         quickSort(s, i + 1, r);
16     }
17 }
{% endhighlight %}
{% highlight C++ %}
18 int find(int A[], int len, int x){
19         quickSort(A,0,len-1);
20         int i=0,j=len-1;
21         while(i<j) {
22                 if( A[i] + A[j] == x )
23                         return 1;
24                 else if( A[i] + A[j] < x )
25                         i++;
26                 else
27                         j--;
28         }
29         return 0;
30 }
{% endhighlight %}
