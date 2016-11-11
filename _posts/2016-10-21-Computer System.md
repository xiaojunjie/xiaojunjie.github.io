---
layout: post
title: 计算机系统
categories: note
tags: 计算机
---

[深入理解计算机系统](//book.douban.com/subject/5333562/)

## 信息的表示和处理

## 程序的机器级表示
- 访问信息  
movb 8   字节
movw 16  字  
movl 32  双字  
movl 64  四字  
**用movl来表示双精度浮点数不会产生歧义，因为浮点数使用的是一组不同的指令和寄存器**

![IA32的整数寄存器](/assets/dist/img/2016-10-22 16-27-01屏幕截图.png)


movsbl 8->32 字符扩展  
movzbl 8->32 字符扩展(无符号时)

- 算术逻辑  
leal S,D  D<-&S  
leal 7(%eax,%eax,4)   
%eax %eax = %exa * 5 + 7  
左称补0 算术右移补符号 逻辑右移补0  
移位量为立即数或%cl  

for(int i=0;;)xorl %edx %edx  

乘法：  
imull S,D S×D->D  
imull D   D*%eax-> %edx %eax  

除法：  
idivl D  
if(signed) cltd  
else $0 -> %edx  
余%edx 商%eax

- 控制  
 [二进制数逆转](/note/csapp-3.23)  
 [整数除法](/note/divid/)  

- 函数调用  
![函数堆栈](/assets/dist/img/2016-11-01 16-45-37屏幕截图.png)  
**父函数**  
esp 指向参数1  
call 返回地址（call下条指令的地址）入栈  esp指向返回地址 pc指向子函数代码区  
**子函数**  
push ebp  把ebp的原先值（调用者的帧指针）入栈，esp指向"被保存的ebp",ebp仍指向父函数帧  
ebp = esp  ebp指向子函数帧  
esp -= n   esp向前跳，这根据子函数而定，ebp不动  
子函数代码  
esp = ebp  ebp回跳  
pop ebp  ebp指向父函数帧，esp指向“返回地址”  
ret 返回地址出栈，pc指向call下条指令的地址。esp指向“参数1”  

- 异质的数据结构  
windows： double,long double 要求8字节对齐  
linux： 8字节数据要求4字节对齐  

- 缓冲区溢出  
![函数堆栈](/assets/dist/img/2016-11-06 14-05-56屏幕截图.png)   
buf过长会覆盖返回地址，植入shellcode使返回地址为shellcode的地址。因为栈的随机化，故要“空操作雪橇”使shellcode变长。  
gcc的栈破坏检测会在buf前设置“金丝雀”，ret前检测，而其他局部变量移至buf后，使其一溢出就改动“金丝雀”  
硬件可以检测栈内容的可执行性  

- 64位  
![64位](/assets/dist/img/2016-11-07 14-38-18屏幕截图.png)  
movl会将高32位置0,故无需movzlq  
movzbl目的寄存器32位，效果同movl，将高32位置0。如addl将高32位置0,addw addb不会。  
而高->低,高字节可以无所谓
