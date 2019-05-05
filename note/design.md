---
title: 设计模式
layout: cs
---
## 行为

### 观察者模式
MVC,M观察目标，V观察者，C中简，本质就是观察者注册回调函数

### 策略模式
排序有很多种方法，每种方法都是一种策略，由用户根据数据情况new an object of sort, 把object作为一个策略对象的主要成员，用这个策略对象进行排序。

### 工厂模式
- 简单：使用时不具体去new对象，只是参数到工厂类，工厂类中进行判断再new，然后return。
- 工厂：把不对方法分配到不同工厂子类中，由工厂子类去new，比如快排归到快排工厂类。
- 抽象：把多个方法分到同一个工厂子类，比如稳定工厂子类。每个工厂子类包含多个方法。

## 结构

### 装饰者模式
为对象动态添加功能。比如一个HttpRequest对象起初只有一个string对象，把通过赋值构造传入HttpRequest1生成一个新对象，HttpRequest1在print_header多提取cache字段，HttpRequest2的print_header多提取了Host字段，通过不断地装饰，原对象的print_header方法可以输出更多肉容

### 代理模式
封装被代理对象并限制外界对被代理对象的访问,把通过赋值构造传入HttpProxy生成一个代理对象，而非HttpRequest对象，所以不能再传下去，代理对象可以使print_header多提取cache字段，然后就没了，它是功能的组合，而非像装饰者的聚合。

### 模板方法模式
把子类共有的方法抽出作为模板，剩下的各自实现。

### 外观模式
服务端打包一群接口成为一个新接口，对客户端隐藏细节，便于调用。

### 适配器模式
客户端对接口的重新包装，wcharts和其他，适配器对客户端这边接口固定，对服务端这边随机应变。

### 桥接模式
自己去设计，在设计初期，定义好客户端和服务端的接口，后期加需求用到第三方组件才考虑适配器模式，因为先前的接口已经定型了，必须包装第三方的。

## 创建

### 建造者模式
一个Response由多个部分建造而成，建造方法很多，每个方法都是一个builder，通过更换builder可以很方便生成不同的response。将一个复杂对象的构建与它的表示分离.

### 单例模式  
{% highlight C++ %}
//C++0X以后，要求编译器保证内部静态变量的线程安全性，可以不加锁
class Singleton
{
    private:
        Singleton() {  };
        ~Singleton() {  };
        Singleton(const Singleton&);
        Singleton& operator=(const Singleton&);
    public:
        static Singleton& getInstance()
        {
            static Singleton instance; 
            return instance;

        }

};
{% endhighlight %}

### 命令模式
对socket有read,write,close行为，每个行为针对socket都实现一个execute方法，socket是其成员，将各个行为推入队列等待被执行。  


