---
title: Windows Kernel Programing
date:
  created: 2025-09-02
  updated: 2025-09-06
categories:
  - 技术
tags:
  - Windows 

---

# Windows 核心编程
&ensp;&ensp;最近工作需要，需要Windows系统的一些编程知识，这些知识10年前做端游的时候曾经使用过，现在Windows7已经被淘汰，Win11成为主流，之前的知识也要与时俱进，想来是需要总结下相关的知识,年纪大了，方便自己将来记忆: 

- Windows核心API 
- 常见调试工具的使用 



<!-- more -->
# Windows 核心编程
##  多进程通信
### 调试器的两种不同Attach方式，导致获取子进程的退出码时存在差异
[示例代码](https://github.com/laiyierjiangsu/windows_kernal_programing)
启动client.exe会通过CreateProcess创建子进程，并通过函数返回的句柄来检测子进程的状态，通过procexp64.exe观察下进程树，
### 方式1：通过Gflags指定调试器
![Gflagsconfig](https://raw.githubusercontent.com/laiyierjiangsu/blog_image/refs/heads/master/posts/WindowsPrograming/gflags_config.png)

程序启动后，查看进程树,可以看到client的子进程是调试器，这个时候如果持有createprocess返回的进程句柄是调试器的，并不是server.exe的，而是调试器的句柄。
![create_process_tree](https://raw.githubusercontent.com/laiyierjiangsu/blog_image/refs/heads/master/posts/WindowsPrograming/create_process_tree.png)  
通过windbg产看, windbg用的是Create的方式创建的调试进程：

![create_windbg_status](https://raw.githubusercontent.com/laiyierjiangsu/blog_image/refs/heads/master/posts/WindowsPrograming/create_windbg_status.png) 
### 方式2： 关闭Gflags，用调试器Attach进程
进程树和windbg的状态如下,server直接是client的子进程

![attach_process_tree](https://raw.githubusercontent.com/laiyierjiangsu/blog_image/refs/heads/master/posts/WindowsPrograming/attach_process_tree.png) 

![attach_windbg_status](https://raw.githubusercontent.com/laiyierjiangsu/blog_image/refs/heads/master/posts/WindowsPrograming/attach-windbg-status.png) 
### 总结
<span style="color:red">如果有需求要缓存createProcess返回的信息来做进一步的处理，一定要小心调试器带来的侵入影响。<span>

# Window平台常见调试工具
## Gflags
## Windbg
&ensp;&ensp;之前做有过一段时间端游，一直用windbg解决外网的crash问题，后来用unity了，就再也没碰过了，最近新公司需要用，发现两个问题，一是windbg有了新的版本，源码调试更加友好，加了很棒的特性，比如说TimeTravelDebugging; 二是发现我很多常用的命令都记得了，只能去爬官网文档。这篇文章不会用来记录用来记录windbg使用过程中碰到的一些问题，作为我自己未来可以一直更新的自用手册。
 
 &ensp;&ensp; **RTFM** :[官方文档](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) 永远是最全的，随时通过关键字进行查询；有些命令可能一开始无法找到对应的文档，你可能通过AI查到，也可能通过咨询同事得到，在解决完问题之后，回到文档中找到对应的章节复习下，记录在这里，下次使用的时候会更加得心应手的。

- .formats:查看一个数字的其他进制格式；
