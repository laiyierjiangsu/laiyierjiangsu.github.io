---
title: 程序探查器
date:
  created: 2025-09-03
  updated: 2025-09-03
categories:
  - 技术
tags:
  - 跨平台
  - 性能分析 
draft: true
---

# 程序探查器 
&ensp;&ensp; 最近到了新公司，发现Native的程序开发永远绕不开性能、异常检测等基础功能。 突然发现15年的软件开发，我都没有积累下一些自己的工具库，每次都要重新造轮子。所以就有了这个新的想法，未来三年的时间，我要自己实现一个跨平台的程序探查器，该探查器的目标：
- 跨平台：windows,mac
- CPU性能分析
- 内存分析
- 统一的Hook框架

<!-- more -->
# 第一期
- 跨平台
- windows: ETW
- windows: hook