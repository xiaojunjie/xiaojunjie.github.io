---
title: Linux
layout: cs
---

## IO  

### 标准IO  
具有一定的可移植性。标准IO库处理很多细节。例如缓存分配，以优化长度执行IO等。标准的IO提供了三种类型的缓存。  

- 全缓存：当填满标准IO缓存后才进行实际的IO操作。  
- 行缓存：当输入或输出中遇到新行符时，标准IO库执行IO操作。  
- 不带缓存：stderr  

### 文件IO  
不带缓存的IO（unbuffered I/O), 每个read，write都调用内核中的一个系统调用。  
也就是一般所说的低级I/O——操作系统提供的基本IO服务，与os绑定，特定于Unix平台。  

### 区别  
- 标准I/O默认采用了缓冲机制，比如调用fopen函数，不仅打开一个文件，而且建立了一个缓冲区（读写模式下将建立两个缓冲区），还创建了一个包含文件和缓冲区相关数据的数据结构(FILE \*)。
- 低级I/O一般没有采用缓冲，需要自己创建缓冲区，不过其实在linux系统中，都是有使用称为内核缓冲的技术用于提高效率，读写调用是在内核缓冲区和进程缓冲区之间进行的数据复制。
- 使用标准IO就不需要自己维护缓冲区了，标准IO库会根据stdin/stdout来选择缓冲类型，也就是说当你使用标准IO的时候，要清楚它的stdin/stdou是什么类型以及其默认的缓冲模式，如果不合适，你需要用setvbuf先设置，再使用，例如协同进程的标准输入和输出的类型都是管道，所以其默认的缓冲类型是全缓冲的，如果要使用标准IO，就需要现设置行缓冲。
- 对于文件IO，只要你自己能维护好缓冲区，完全可以不用标准IO。  
- 从名字上来区分，文件I/O主要针对文件操作，读写硬盘等，标准I/O，主要是打印输出到屏幕等。因为他们设备不一样，文件io针对的是文件，标准io是对控制台，操作的是字符流。对于不同设备得特性不一样，必须有不同api访问才最高效。 

## 进程  

### wait和waitpid  
- wait会令调用者阻塞直至某个子进程终止；  
- waitpid则可以通过设置一个选项来设置为非阻塞，另外waitpid并不是等待第一个结束的进程而是等待参数中pid指定的进程。  
- waitpid中pid的含义依据其具体值而变：  
　　pid==-1 等待任何一个子进程，此时waitpid的作用与wait相同  
　　pid >0   等待进程ID与pid值相同的子进程  
　　pid==0   等待与调用者进程组ID相同的任意子进程  
　　pid<-1   等待进程组ID与pid绝对值相等的任意子进程  
- waitpid提供了wait所没有的三个特性：  
　　1 waitpid使我们可以等待指定的进程  
　　2 waitpid提供了一个无阻塞的wait  
　　3 waitpid支持工作控制  

### vfork  
子进程与父进程共享数据段.  vfork()保证子进程先运行，在她调用exec或\_exit之后父进程才可能被调度运行。如果在调用这两个函数之前子进程依赖于父进程的进一步动作，则会导致死锁。  

### 守护进程  
守护进程是运行在后台的一种特殊进程, 不受终端控制，Linux系统的大多数服务器就是通过守护进程实现的。一个守护进程的父进程是init进程。  

- 创建子进程，父进程退出  
- 在子进程中创建新会话 setsid()  
- 改变当前目录 chdir("/");    
- 重设文件权限掩码  umask(0);      
- 重定向文件描述符  dup2(open("/dev/null"),0~2)  


## 编译运行  

### ELF文件  

section 是被链接器使用的，但是 segments 是被加载器所使用的。加载器会将所需要的 segment 加载到内存空间中运行。 

- 可重定位的对象文件(Relocatable file)(没有segments)  
这是由汇编器汇编生成的 .o 文件。后面的链接器(link editor)拿一个或一些 Relocatable object files 作为输入，经链接处理后，生成一个可执行的对象文件 (Executable file) 或者一个可被共享的对象文件(Shared object file)。我们可以使用 ar 工具将众多的 .o Relocatable object files 归档(archive)成 .a 静态库文件。
- 可执行的对象文件(Executable file)   
- 可被共享的对象文件(Shared object file)  

这些就是所谓的动态库文件，也即 .so 文件。  


在ELF文件里面，每一个 sections 内都装载了性质属性都一样的内容，比方： 

- .text section 里装载了可执行代码；  
- .data section 里面装载了被初始化的数据；  
- .bss section 里面装载了未被初始化的数据；  
- 以 .rec 打头的 sections 里面装载了重定位条目；  
- .symtab 或者 .dynsym section 里面装载了符号信息；  
- .strtab 或者 .dynstr section 里面装载了字符串信息； 
- 其他还有为满足不同目的所设置的section，比方满足调试的目的、满足动态链接与加载的目的等等。  

把带有相同属性(比方都是只读并可加载的)的 section 都合并成所谓 segments(段)。最重要的是三个 segment：代码段，数据段和堆栈段。  

### 程序启动过程
- 内核创建新进程  
- 往这个新进程的进程空间 加载代码段和数据段  
- 加载进动态连接器 (/lib/ld-linux.so)的代码段和数据。  
- 内核将控制传递给动态链接库里面的代码。动态连接器加载应用程序所需要使用的各种动态库。  
- 动态连接器将控制传递给main函数。  

### 过程链接表（PLT）  

### 全局偏移量表（GOT）  

### 开机流程  
- 加载BIOS的硬件信息与进行自我测试，并依据设置取得第一个可启动设备；  
- 读取并执行第一个启动设备内MBR（主引导分区）的Boot Loader（即是gurb等程序）；  
- 依据Boot Loader的设置加载Kernel，Kernel会开始检测硬件与加载驱动程序；  
- 在硬件驱动成功后，Kernel会主动调用init进程（/sbin/init），而init会取得runlevel信息；  
- init执行/etc/rc.d/rc.sysinit文件来准备软件的操作环境（如网络、时区等）；  
- init执行runlevel的各个服务的启动（script方式）；  
- init执行/etc/rc.d/rc.local文件；  
- init执行终端机模拟程序mingetty来启动login程序，最后等待用户登录。  

## 工具  
- ldd 查看程序依赖库    
- lsof list of open file   
- ps Process Status  
- pstack 跟踪进程栈  
- strace 跟踪进程中的系统调用  
- ipcs 查询进程间通信状态  
- vmstat 监视虚拟内存使用情况  
- iostat 监视I/O子系统  
- sar 找出系统瓶颈的利器  
- ifstat 看网络带宽  
- netstat命令是一个监控TCP/IP网络的非常有用的工具，它可以显示路由表、实际的网络连接以及每一个网络接口设备的状态信息。-t tcp  
