# 利用Mkdocs搭建个人博客
## 准备
- [参考教程](https://squidfunk.github.io/mkdocs-material/);
-  腾讯云申请域名，并通过cname指向github pages 地址;
-  未当前仓库申请一个访问token,并配置环境变量MKDOCS_GIT_COMMITTERS_APIKEY用于获取文档的更新信息
- 当前仓库为所有网页相关的代码;
- blog_image 作为图床使用，避免当前仓库冗余，额外增加发布时间;
- giscus_comment 评论仓库;
- webHow 测试html基础的语法;


## 构建
### Mac
####  vscode的teminal, 创建环境，方便调试

~~~
    //创建环境
    blogs % python3 -m venv venv 
    blogs % source venv/bin/activate

    # mac把当前的ssh-key添加到agent
    eval "$(ssh-agent -s)"
    kill -9  pid
    ssh-add -L
    ssh-add --apple-use-keychain ~/.ssh/github   

    //查看服务器正在运行的程序端口
    netstat -ntlp 

    //构建
    mkdocs build -v
    //本地服务
    mkdocs serve -v
    // 发布
    mkdocs gh-deploy

~~~

## 发布流程
- develop分支开放， 本地测试
- develop 发布， 外网测试
- merge代码至main分支， 发布，外网测试
 