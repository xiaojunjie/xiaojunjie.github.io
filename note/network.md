---
title: 计算机网络
layout: cs
---

## 七层模型简述  

###  应用层(APDU)  
- DHCP(udp):ip地址分配  
- DNS(udp)www→ ip   
- ping，在icmp中藏有当前时间，目标主机原物返回，相减  
- Traceroute， 递增TTL发包，端口不可达，开始时一直收超时包，直到收到端口不可达说明到目的地了  

### 表示层(PPDU)  
加密解密压缩 JPEG ASII  

### 会话层(SPDU)  
进程间数据传输的建立恢复, RPC NFS  

### 传输层(报文)  
端到端，一台主机上的进程发出的包，如何到达目的主机上的某个进程。  

### 网络层(包)  
每一个网络分组如何到达目的主机，而不管目的主机如何处理。  
- ARP:ip→ mac   
- RARP:mac→ ip  
- NAT:公网ip→ 私网ip  
- ICMP:  ip不可靠，需要ICMP帮忙，网络通不通，报文是否可达  
- A 0  B10 C110 D1110 E1111  

### 链路层(帧)
- 目的mac-源mac-协议类型-数据，以太网内网络包的传输。  
- VPN协议，交换器switch 基于MAC识别  
- 交换式以太网特点a) 扩展了网络带宽。b) 分割了网络冲突域   
- 数据链路层协议，滑动窗口  
- 停止等待  size=1对1  
- 后退N(GBN) ，类似指令流水，不一定等待前一条执行完才到下一条。只计时第一个，超时整个size重发。size=n对1 。n=2^k-1  
- 选择重发 ，计时整个size，接收端非按序拿到包，缓存。包中要含有序号才能排序。Size = 2^(k-1)  超出size后接收端难区分新旧包  

### 物理层(bit)  
集线器hub, IEE802.3 CLOCK RJ45 

## TCP  

### 序列号、确认应答、超时重传

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

### select  
- fds拷到内核，对监听的所有fd创建共同的wait_entry(callback)（for当前进程，一个fd有多个wait_entry from processes）  
- 遍历一遍fds后调用schedule_timeout等待被唤醒  
- 有事件时被callback唤醒（wait_entry会被移除），遍历收集再return。超时时被计算器回调唤醒    
{% highlight C++ %}
copy(fds);
create wait_entry(callback) for fds;
for(;;){
    for(fd:fds);
    poll_schedule_timeout();// 被计算器回调唤醒, 或callback唤醒
}
{% endhighlight %}

### epoll  
- fds通过共享内存(mmap)常驻  
- epoll_ctl(ADD) 对fd创建wait_entry_sk(callback)，并加入sleep_list中  
- epoll_wait 遍历ready_list后，将callback放入single_epoll_wait_list，调用schedule_timeout等待被唤醒  
- 有事件时wait_entry_sk将fd放入ready_list（wait_entry_sk会被移除），并调用single_epoll_wait_list里面的callback去遍历ready_list收集返回，callback会被移除。  
- epoll_wait.ET 一进来ready_list不空肯定有事件(IN)，收集后立即删除。  
- epoll_wait.LT 一进来ready_list不空可能没有事件，可能是上次遗留（每次收集会重新入队），此时才真正去除，然后等待被唤醒   
- [LT vs ET](https://cloud.tencent.com/developer/article/1005481): 兼容poll,编程方便,减少EAGAIN系统调用  

### write  
- 接收端receive buffer满了，通过流控和差控阻止发送端发送  
- 阻塞模式下，发送端等到send buffer足够时才回返; 如果接收端close，能填多少是多少，return填的量，再次write时 connection reset by peer  
- 非阻塞模式下，return -1, EAGAIN  
- 收到对方的FIN仅意味着对方不会再send  

### RST  
当一端进程异常退出时，OS会代发FIN，当再收到消息时会以RST回应，对方面对RST若再发就会被其OS的SIGPIPE（停止）   
- 建立连接的SYN到达某端口，但是该端口上没有正在 监听的服务。  
- TCP收到了一个根本不存在的连接上的分节。  
- 请求超时。 使用setsockopt的SO_RCVTIMEO选项设置recv的超时时间。接收数据超时时，会发送RST包   


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
server把公钥给ca认证后拿到证书给client, ca给server时要用ca自己的私钥给证书加密附在证书尾  
RSA  
N = 3x5, r=欧拉(2)x欧拉(4)=1x2，选择e(=1) <r，er互质，d=e关于r的逆元  
(N,e) 公  
(N,d) 私  


