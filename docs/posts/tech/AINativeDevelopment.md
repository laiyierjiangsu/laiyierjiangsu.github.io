---
title: AI-Native
date:
  created: 2025-11-23
  updated: 2025-11-23
categories:
  - 技术
tags:
  - AI 

---

# AI原生开发
&ensp;&ensp;最近公司也在推AI, AI是每个员工的必修课。对于程序员来说AI更是未来必须掌握的技能。在用了两个月的cursor之后，工作效率明显提升： a.对不熟悉的业务代码，cursor能帮你快速入门；b.对比较封闭的模块，cursor可以快速的帮你进行重构；c对于版本中的bug,cursor可以给出修复建议；d.日常一些常见的工作流，可以通过cursor帮你用c++快速的开发一些小工具。 但这些远不够，Calude Code的工作流， skills ,mcp , rag这些可以帮助到我的日常开发吗？ 我不知道，但是我知道AI能够对我的帮助肯定不止这些，抱着拿着锤子找钉子的态度，先系统的学习下AI原生开发是什么吧。

<!-- more -->

# AI-Native / Autonomous Integratio
## AI开发者集成成熟度模型

![alt text](https://github.com/laiyierjiangsu/blog_image/blob/master/posts/AINative/ai-module.png?raw=true)

## SDD

- [github-spec-kit](https://github.com/github/spec-kit)

- [Spec-driven development with AI: Get started with a new open source toolkit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)

# 实操
## AI Claude
第一个体验的产品是AI Claude， 一个CLI的工具，与Cursor和Codex的区别是：
 1.命令行代表着更多的权限，可以调用更多系统原生的工具，无需通过mcp tool来提供额外的能力；
 2.Cursor,Codex更多的是集中于代码开发，受限于IDE,但是AI未来的应用场景会是系统本身就是一个巨大的AI入口，所有的工具都有AI驱动，AI原生变成对于未来可能更重要。

### 模型
#### OpenRouter
- 由于国内无法访问openai, claude code等原生模型，但对这些原生模型的体验也是不可或缺的，我选择用[OpenRouter](https://openrouter.ai/) + [Claude Code Proxy](https://github.com/laiyierjiangsu/claude-code-proxy) 来进行转发。 OpenRouter支持微信付费，不像google和openai付费需要国外的银行卡。
- OpenRouter使用过程中，虽然市面上所有的大模型都可以用，如果是平常测试，尽了使用免费的模型或者便宜的模型， 像anthropic最新的模型claude-opus-4.5，我用来查询天气，他的价格是haiku的十倍，未来如何用更少的token来完成需求，应该也是个工程学的问题。
![openroterbill](https://github.com/laiyierjiangsu/blog_image/blob/master/posts/AINative/openrouter-bill.png?raw=true)
- Claude-code-proxy是个开源项目，用来将Anthropic的API请求转换为Open API格式的请求，实现两者兼容。直接使用的时候， 服务会报错。我用cursor帮忙修改了些代码，可以使用了。神奇的体验，用一个AI来帮助另一个AI工作。
### [月之暗面](https://www.moonshot.cn/)
- K2模型最新出的，薅羊毛弄了一个月的会员，天然支持Claude Code，用起来体验不错，很多时候比豆包的体验要好，有些问题的答案进入比GPT5的答案更好，不能理解，目前是国内平替。
### [智谱AI](https://open.bigmodel.cn/)
- GLM系列大模型从社区来看，性价比是最高的，目前还没开，等k2到期开一个体验下。