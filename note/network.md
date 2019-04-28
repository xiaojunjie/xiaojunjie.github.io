---
title: 计算机网络
layout: cs
---

## 七层模型简述  

###  应用层  
- DHCP(udp):ip地址分配  
- DNS(udp)www→ ip   
- ping，在icmp中藏有当前时间，目标主机原物返回，相减  
- Traceroute， 递增TTL发包，端口不可达，开始时一直收超时包，直到收到端口不可达说明到目的地了  

### 表示层  
加密解密压缩  

### 会话层  
进程间数据传输的建立恢复  

### 传输层  
端到端，一台主机上的进程发出的包，如何到达目的主机上的某个进程。  

### 网络层  
每一个网络分组如何到达目的主机，而不管目的主机如何处理。  
- ARP:ip→ mac   
- RARP:mac→ ip  
- NAT:公网ip→ 私网ip  
- ICMP:  ip不可靠，需要ICMP帮忙，网络通不通，报文是否可达  
- A 0  B10 C110 D1110 E1111  

### 链路层  
- 目的mac-源mac-协议类型-数据，以太网内网络包的传输。  
- VPN协议，交换器switch 基于MAC识别  
- 交换式以太网特点a) 扩展了网络带宽。b) 分割了网络冲突域   
- 数据链路层协议，滑动窗口  
- 停止等待  size=1对1  
- 后退N(GBN) ，类似指令流水，不一定等待前一条执行完才到下一条。只计时第一个，超时整个size重发。size=n对1 。n=2^k-1
选择重发 ，计时整个size，接收端非按序拿到包，缓存。包中要含有序号才能排序。Size = 2^(k-1)
超出size后接收端难区分新旧包  

### 物理层  
集线器hub 

## TCP  

### 流量控制  
滑动窗口动态调整大小  

###­拥塞控制   
- 慢启:x2      
- 拥塞避免: ++  
- 快重传: count==3 || timeout   
- 快恢复: 阈值和窗口都 等于当前窗口的一半，++  

### 3握4挥  
![TCP]({{ site.storage  }}/assets/dist/img/tcp3.png)  
![TCP]({{ site.storage  }}/assets/dist/img/tcp4.png)  

### 与UDP比较  
- UDP无连接，没有拥塞控制，可能丢失，所以不可靠  
- TCP面向字节流，TCP把数据看成一连串无结构的字节流；UDP是面向报文的  
- TCP点到点的；UDP一对一，一对多，多对一和多对多  

## Socket 

![TCP]({{ site.storage  }}/assets/dist/img/accept.png)  

- listen  
listen某个端口后，这个端口的SYN队列和ACCEPT队列就弄好。1.1步骤客户端的SYN包到达了服务器后，内核会把这一信息放到SYN队列（即未完成握手队列）中，同时回一个SYN+ACK包给客户端。一段时间后，2.1步骤中客户端再次发来了针对服务器SYN包的ACK网络分组时，内核会把连接从SYN队列中取出，再把这个连接放到ACCEPT队列（即已完成握手队列）中。而服务器在第3步调用accept时，其实就是直接从ACCEPT队列中取出已经建立成功的连接套接字而已.
SYN队満就丢弃新的，ACCEPT队列满了导致SYN出不来。  
- int listen(int sockfd, int backlog);backlog是队列长度  
- select  查找，1024, copy
- [epoll](https://cloud.tencent.com/developer/article/1005481)  不查找，mmap, 中间件，ET/LT, ET要非阻塞  


## HTTP  

### 字段  
- cache: Expires 时间点， max-age时间差(优先，但ie9-不支持）)  

### 版本区别  
- 1.0  每次都经过三次握手和慢启动  
- 1.1  host, 持续连接, 提出pipeline想法但会线头阻塞   
- 2.0 解决1.x的线头阻塞，多路复用一个TCP连接，每路以stream（header帧，data帧）传输  
- pipeline 一个TCP连接上多个HTTP

### FTP  
- 除了二进制，还能以acsii传输  
- 没有流水线，两个连接（指令和数据）不持久，无代理，头部信息少  
- 单个文件ftp,多个http快  

### HTTPS  
RSA  
N = 3x5, r=欧拉(2)x欧拉(4)=1x2，选择e(=1) <r，er互质，d=e关于r的逆元  
(N,e) 公  
(N,d) 私  


