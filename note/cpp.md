---
title: C++
layout: cs
---

## 关键字
- const函数不能修改任何非静态成员  
- const函数内要修改变量需要声明该变量为mutable  
- volatile是防止编译器优化变量，常用于signal handler或者mmap时  

- static_cast 向上转换  
- dynamic_cast 向下转换  
- const_cast 转const

{% highlight C++ %}
Rect::Rect:text("asd") // 直接构造函数进行初始化
{
    text = "abc"; //赋值，非初始化
    // text的default构造函数会将其先初化然后才能进入Rect函数作为域，赋值时再copy构造等于"abc"
}
{% endhighlight %}

- static成员初始化顺序无法确定  
- no-static成员初始化顺序由定义时顺序决定  
- 对空class，构造器默认为其补充default构造，copy造构，operator =构造 ，析构。注意，是按需补充，编译器检测到哪些将被使用才补充
- copy构造要在derived中“初始化”base，derived(const derived& a):base(a){}否则derived会被base的default构造初始化  
- operator=构造中要调用base的，base::operator=()  
- 对于某个类对象，a=b假如ab不同类，先调用构造实例化b(隐式)，然后operaor=, 除非其构造用explicit禁止这种隐式转换行为
除了=，其operator也一样。  

- base 声明纯virtual, virtual ~Base() = 0 也要在class外给出定义，否则derived中琏接base析构会报错  

- 析构中抛出异常可能导致不明确行为，特别是几个对象一起抛，e.g.vector<Class>结束时  
- 解决方法，让调用者主动去执行这个风险行为，然后析构再检测，如果用户不自觉那就不管，catch error就扔了  
- base构造和析构中不能调用virtual，否则derived构造中会调用base构造，进而调用的会是base的virtual函数，因为derived成员未初始化，编译肯定不允许调用derived的  

- string和vector可以连续赋值，a=b=c  


## 指针  
- auto_ptr指针 a=b;此时b为被置空  
- shared_ptr指针不会  
- shared_ptr会有循环引用问题。weak_ptr p = shared_ptr; 不会增加引用，通过lock来往回shared_ptr或者NULL  
- 智能指针是通过delete删除，所以不能用来搞数组 shared_ptr<char*>(new char[8])  
- shared_ptr注意循环引用， weak_prt  

se函数，其他同名异参的函数无法再被继承（即使是都是virtual），也不建议去重载Base，否则继承就没意义。重载virtual可以实现多态有意义。可以在Derived中声明 using Base::fun，然后可以求同存异;

virtual含有默认参数也不要重载，virtual是多态，但默认参不是，重载后还是base的默认参。


