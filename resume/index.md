---
title: 简历
layout: resume
date: 2018年6月12日

#job: 软件工程师
face: img/head.png
username: 肖俊杰
# pdf: 肖俊杰.pdf

study-info:
    base: 肖俊杰 / 男 / 25岁
    education0: 本科 / 西安电子科技大学 / 信息安全
    education1: 硕士 / 西安电子科技大学 / 电路与系统
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
#    - title: 北京-海知智能·软件工程师（2017.6 - 2017.8）
#      content: 海知智能(https://ruyi.ai)专注于人工智能交互系统，为客户提供自然语言理解和开放知识图谱的技术接口。我负责数据的爬取、清洗、入库工作，对各种反爬策略有深入的了解，能够处理复杂数据。最后还对爬虫框架进行改进，更好地满足公司的业务需求。
#      img:
#
    - title: 北京-去哪儿网·Web工程师（2016.1 - 2016.2）
      content: 在技术部实习两个月，参与“用户订单系统”维护和开发，主要是负责前端数据处理，用avalon重构前端模块，完成“用户订单系统”的升级。实习期间，我的编程能力能到了很大的提高，能够独立解决一些复杂的web工程问题。
      img:

    - title: 上海-携程网·软件工程师（2015.7 - 2015.9）
      content: 携程“自由行”研发部实习两个月，主要的任务是负责对前端数据接口的封装，基于nodejs的事件驱动模型进行数据处理。这期间我对MVC架构有深入的了解，并学会了团队合作开发和企业级应用的发布、更新及维护。
      img:

project:
    - title: 量子深度神经网络的研究与应用  (2018.5至今)
      content: 我提出了一种方法可以使计算机针对不同的图像分类任务自动化构建CNN，其中的创新点于我提出的一种编码策略将整个CNN结构及其超参完全映射于量子粒子群优化算法（QPSO）的搜索空间中，通过QPSO的量子进化策略不断搜索CNN结构和参数，最终使计算机在无任何人工经验的干涉下以比较小的计算代价构建出一个比较好的CNN。
    - title: Tiny Web Server  (2017.9至今)
      content: 生产者-消费者模式，主线程监听得到请求任务并推入队列，线程池的线程竞争提到任务后accpet请求，然后通过各种handler处理，最终响应请求。C++手动实现每个功能，包括日志、线程池、Http解析等等，无任何第三方库。通过不断地挖坑与填坑，可以夯实自己的计算机基础。
      img:
      demo:
#      source: https://github.com/xiaojunjie/tiny

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

competition:
    - 2018-华为软件精英挑战赛·西北赛区二等奖
    - 2015-第26届中国大学生计算机设计大赛·全国二等奖
    - 2013-第25届“星火杯”大学生课外学术科技作品竞赛中获三等奖

scholarship:
    - 2013~2014 校三等奖学金
    - 2014~2015 校三等奖学金
    - 2016~2017 校一等奖学金

current: 我正在努力打好基础，我觉得扎实的基本功远比掌握一些技能重要。
future: 我性格沉静，爱编程爱计算机。无论将来发展如何，我都希望自己能不忘初心。
---
