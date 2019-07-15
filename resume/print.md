---
title: 简历
layout: print

#job: 软件工程师
face: img/head.png
username: 肖俊杰
# pdf: 肖俊杰.pdf

study-info:
    base: 肖俊杰 / 男 / 25岁
    education0: 2013-2017 本科 / 西安电子科技大学 / 信息安全
    education1: 2017-2020 硕士 / 西安电子科技大学 / 电路与系统
    political: 共青团员
    native: 福建福州
    english: CET-6：507
    score: 均分84 排名7/40

contact-info:
    phone: 18020878508
    mail: 971308896@qq.com
    wechat: xiao-jun-jie
    qq: 971308896
    blog: xjjfly.com
    github: github.com/xiaojunjie

intern:
    - title: 北京-海知智能·软件工程师（2017.6 - 2017.9）
      content: 海知智能专注于人工智能交互系统，为客户提供自然语言理解和开放知识图谱的技术接口。我负责数据的爬取、清洗、入库工作，对各种反爬策略有深入的了解，能够处理复杂数据。最后还对爬虫框架Scrapy进行改进，更好地满足公司的业务需求。
      img:

    - title: 北京-去哪儿网·Web工程师（2016.1 - 2016.3）
      content: 在技术部实习两个月，参与“用户订单系统”维护和开发，主要是负责前端数据处理，用avalon重构前端模块，完成“用户订单系统”的升级。实习期间，我的编程能力能到了很大的提高，能够独立解决一些复杂的web工程问题。
      img:

    - title: 上海-携程网·软件工程师（2015.7 - 2015.9）
      content: 携程“自由行”研发部实习两个月，主要的任务是负责对前端数据接口的封装，基于nodejs的事件驱动模型进行数据处理。这期间我对MVC架构有深入的了解，并学会了团队合作开发和企业级应用的发布、更新及维护。
      img:

project:
    - title: 量子深度神经网络的研究与应用  (2018.5至今)
      content: 基于量子粒子群算法(QPSO)，我提出了一种新的编码方式将卷积神经网络(CNN)映射于QPSO的搜索空间中，通过改进的量子搜索策略使计算机能快速地自动化构建合适的CNN结构来处理不同的图像分类任务，其中的创新点于全程无需人工经验的干涉，并且充分发挥了量子的不确定性以降低计算代价。这是第一个用粒子群算法来构建CNN结构的完全自动化算法。
    - title: Tiny Web Server  (2017.9至今)
      content: 本项目为C++11编写的轻量级Web服务器，在不依赖第三方库的情况下实现基础的功能，包括使用有限状态机解析get请求，处理静态资源，实现异步日志，等等。主线程负责accept请求，线程池负责处理，线程皆基于Reactor模式，使用Epoll水平触发的IO多路复用技术，将阻塞点放在监控socket的epoll_wait调用上，通过事件驱动实现了线程的异步唤醒。
      img:
      demo:
      source: https://github.com/xiaojunjie/tiny

#    - title: 基于hadoop的学生上网行为分析（2015.6 - 2015.8）
#      content: 我们团队参加中国大学生计算机设计大赛，命题为《基于hadoop的学生上网行为分析》。我是负责数据可视化创新设计，不拘泥于传统单调的图表，而是采用地图插件，使后端数据动态展现出来。在数据处理上，通过封装前端的数据接口，完美地实现了前后端对接。通过这个项目使我对大量数据的交互处理以及数据可视化有进一步了解。
#      img:
#      demo:
#      source:

#    - title: 微信会员管理系统（2014.4 - 2014.9）
#      content: 使用PHP为“西安方圆羽毛球俱乐部”开发过微信平台及CMS，后端是基于角色的访问控制，定时自动更新比赛安排，通过微信平台向会员推送，后端通过数据统计分析，把报名结果呈现给管理员。系统在传统的MVC架构上提出了改进方案，以微信平台作为视图层，使系统跟微信平台更好地对接，降低系统的耦合度。
#      img:
#      demo:
#      source:

#    - title: 单片机的开发应用（2013.9 - 2014.3）
#      content: 我大一开始学习单片机，有半年多的开发经验。在这期间利用51单片机、时钟芯片、LCD显示屏制做了一个智能电子表，集成温度测控、智能报警等功能。后续我又做了一个“光立方”，用125个LED搭成一个立方体，通过C语言能使立方体呈现许多变化图形。
#      img:
#      demo:
#      source:

program:
    - language: 计算机组成原理
      detail:
        - 浮点运算，指令流水，中断，缓存。
    
    - language: 数据结构和算法
      detail:
        - 堆栈，队列，琏表，二叉树，哈希表，邻接矩阵。
        - sort, dfs, dp, greedy.
    
    - language: 操作系统
      detail:
        - CFS, IPC, FCB, LRU.
        - 死锁，缺页，零拷贝，IO模型。

    - language: 计算机网络
      detail:
        - "TCP/IP: 3握4挥11态, 流量控制，拥塞控制。"
        - "Socket:  select, epoll, listen, accept."
        - "Http(s):  非对称加密, 状态码，抓包分析."

Cplusplus:
    - RAII, rule of three, allocator, new operator, shared_ptr .
    - STL各容器的存储结构及时间复杂度

JavaScript:
    - 两年开发经验，熟悉闭包、原型琏等高级特性。
    - 对于Web前端的数据处理有一定的工程经验。

Python:
    - keras, matplotlib, numpy, scrapy
    - 丰富的爬虫经验，能应对绝大部分反爬策略。

Linux:
    - grep, find, netstat, ln, vim

security:
    - 熟悉XSS、CSRF、ClickJacking等web安全相关技术

competition0:
    - 2013-第25届“星火杯”大学生课外学术科技作品竞赛中获三等奖
    - 2015-第26届中国大学生计算机设计大赛·全国二等奖

competition1:
    - 2018-华为软件精英挑战赛·西北赛区二等奖

scholarship:
    - 2013~2014 校三等奖学金
    - 2014~2015 校三等奖学金
    - 2016~2017 校一等奖学金

current: 我正在努力打好基础，我觉得扎实的基本功远比掌握一些技能重要。
future: 我性格沉静，爱编程爱计算机。无论将来发展如何，我都希望自己能不忘初心。
paper: Evolving Deep Convolutional Neural Networks by Quantum Behaved Particle Swarm Optimization with Binary Encoding for Image Classification, Neurocomputing, accepted.
patent: 基于量子神经网络的手写体图片分类方法, 201910229053.3
---
