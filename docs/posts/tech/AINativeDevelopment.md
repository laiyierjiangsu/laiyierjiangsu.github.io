---
title: AI-Native
date:
  created: 2025-11-23
  updated: 2025-12-07
categories:
  - 技术
tags:
  - AI 

---

# 什么是AI原生开发？
&ensp;&ensp;最近公司也在推AI, AI是每个员工的必修课。对于程序员来说AI更是未来必须掌握的技能。在用了两个月的cursor之后，工作效率明显提升：

-  a.对不熟悉的业务代码，cursor能帮你快速入门； 
-  b.对比较封闭的模块，cursor可以快速的帮你进行重构； 
-  c对于版本中的bug,cursor可以给出修复建议； 
-  d.日常一些常见的工作流，可以通过cursor帮你用c++快速的开发一些小工具。 

但这些远不够，Calude Code的工作流， skills ,mcp , rag这些可以帮助到我的日常开发吗？ 我不知道，但是我知道AI能够对我的帮助肯定不止这些，抱着拿着锤子找钉子的态度，先系统的学习下AI原生开发是什么吧。

<!-- more -->
## AI开发者集成成熟度模型

![alt text](https://github.com/laiyierjiangsu/blog_image/blob/master/posts/AINative/ai-module.png?raw=true)


# 编程工具

## Claude Code

第一个体验的产品是Claude Code ， 一个CLI的工具，与Cursor的区别是：
 1.命令行代表着更多的权限，可以调用更多系统原生的工具，无需通过mcp tool来提供额外的能力；
 2.Cursor,Codex更多的是集中于代码开发，受限于IDE,但是AI未来的应用场景会是系统本身就是一个巨大的AI入口，所有的工具都有AI驱动，AI原生变成对于未来可能更重要。
 3.搭载anthopic自家的sonnet 4.5 ,速度和效果都是最好的。

## Codex

 购买了ChatGpt的订阅，自带的codex , 并且也退出了命令行，cli + code-5.1-max,相对于sonnet 4.5,其速度比较慢，但是最终出来的效果还是比较令人满意的。

## Cursor

 Cursor是公司帮忙订阅的，如果开auto,在某些情况下效果不太令人满意，但是选择好的模型，比如sonnet-4.5-opus-high，你会发现20美元可能你一个问题都解决不了。


# 模型
好用的话，肯定还是Anthopic自家的claude sonnet模型，然后是openai的code 模型。 google gemini3 据说也不错，但目前来看也并没有对sonnet和codex形成断崖式的领先。 而且这几个模型在国内访问都需要付出点精力的，想体验的话可以通过openrouter等平台。
## OpenRouter
- 由于国内无法访问openai, claude code等原生模型，但对这些原生模型的体验也是不可或缺的，我选择用[OpenRouter](https://openrouter.ai/) + [Claude Code Proxy](https://github.com/laiyierjiangsu/claude-code-proxy) 来进行转发。 OpenRouter支持微信付费，不像google和openai付费需要国外的银行卡。
- OpenRouter使用过程中，虽然市面上所有的大模型都可以用，如果是平常测试，尽了使用免费的模型或者便宜的模型， 像anthropic最新的模型claude-opus-4.5，我用来查询天气，他的价格是haiku的十倍，未来如何用更少的token来完成需求，应该也是个工程学的问题。
![openroterbill](https://github.com/laiyierjiangsu/blog_image/blob/master/posts/AINative/openrouter-bill.png?raw=true)
- Claude-code-proxy是个开源项目，用来将Anthropic的API请求转换为Open API格式的请求，实现两者兼容。直接使用的时候， 服务会报错。我用cursor帮忙修改了些代码，可以使用了。神奇的体验，用一个AI来帮助另一个AI工作。
## [月之暗面](https://www.moonshot.cn/)
- K2模型最新出的，薅羊毛弄了一个月的会员，天然支持Claude Code，用起来体验不错，很多时候比豆包的体验要好，有些问题的答案进入比GPT5的答案更好，不能理解，目前是国内平替。
## [智谱AI](https://open.bigmodel.cn/)
- GLM系列大模型从社区来看，性价比是最高的，目前还没开，等k2到期开一个体验下。

# 技巧总计
## SDD（规范驱动开发）
- [github-spec-kit](https://github.com/github/spec-kit)
- [Spec-driven development with AI: Get started with a new open source toolkit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)

codex、claude、cusor 无一例外都有自己的一些机制去保存一些上下文，比如claude.md, mdc,agents.md，这些文件都会先制定一些规范，在每次会话开启的时候，先通过规范线建立约束，这样生成的代码跟贴合项目实际。

## Skill
Claude Code率先提出了skill的概念，现在codex也支持了，而cursor中这个概念叫做command，就是通过一个描述文档，规定一些输入，然后描述好对这些输入如何处理，给出指定输出。 这样的话，对于一些重复性的工作，可以直接用对应的skill来完成。 这样的好处是：
- 避免每次新开一个会话都要重新输入上下文
- skill可以在多个项目间共享

## MCP
使用一些定义好的服务，这个需要谨慎，突破了本地仓库的安全限制。

## Sub-Agent
把复杂的任务plan,生产to-do list，由sub-agent的并行的去完成。

# 应用场景
目前我对AI的应用场景还不太多，大概是下面几个：
- 日常知识查询： 这类需求国内的模型基本都能满足，Kimi的k2 模型体验非常好。
- 编程： vibe coding主要用于一些小工具的开发，真正的线上项目使用AI来帮助缩小scope，review mr。 Cursor + codex是我目前的组合，看起来够用了。
- 英语口语练习：入职外企之后，感觉口语表达很重要，用Gpt 的语音对话来学习口语，还是非常不错的。

# 未来
- AI原生开发，感觉更多的还是需求驱动，所以如何发掘出那些需要AI来赋能的项目，这个能力（创意？？） 就变得非常稀缺，实现反而变得简单了；
- 目前精力还是在职工作，使用mcp , sub-agent这些高端技巧的机会还是不多，但我觉得未来肯定会有这种场景的
- 未来如果更深度的使用AI，就可能大量的消耗token,那如何用更少的token来完成同样的任务， 这就变成了一个工程学的问题，需要关注这方面的进展。
- AI 帮我们编程的时候，我们该做些什么来保证心流的状态呢？
- AI 的能力不断突破，现有的网络安全体系可能会被挑战，未来肯定会有更多的网络安全问题出现（加密货币被盗）
