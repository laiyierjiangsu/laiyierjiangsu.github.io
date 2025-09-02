---
title: Windows Kernel Programing
date:
  created: 2025-09-02
  updated: 2025-09-02
categories:
  - 技术
tags:
  - Windows 
draft: true
---

# Windows 核心编程

最近工作需要，需要Windows系统的一些编程知识，这些知识10年前做端游的时候曾经使用过，现在Windows7已经被淘汰，Win11成为主流，之前的知识也要与时俱进，所以开个新帖，总结下相关的知识。

<!-- more -->

# 多进程
## 通信
### 通过子进程的退出码获取相关状态
[示例代码](https://github.com/laiyierjiangsu/windows_kernal_programing)

### 命名管道