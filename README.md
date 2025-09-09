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
### Windows 
~~~
   #查看系统的python版本，推荐使用python3.9 ,否则某些库会缺失
   where python
   
   #创建环境
   python -m venv venv

   # 开启powershell权限
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

   # 激活环境
    #在Activate.ps1的添加环境变量部分新增代理，用到了google的部分服务
    $env:HTTP_PROXY = "127.0.0.1:7897"
    $env:HTTPS_PROXY = "127.0.0.1:7897"
    #设置系统环境变量用于获取git-committers，这个比较敏感，设置在系统的环境变量中
    MKDOCS_GIT_COMMITTERS_APIKEY

    执行：
    .\venv\Scripts\Activate.ps1
    检查环境变量是否ok:
    $env:HTTP_PROXY
    $env:HTTPS_PROXY 
    $env:MKDOCS_GIT_COMMITTERS_APIKEY

   #安装依赖: 1) 关闭代理； 2）禁用源码编译
   pip install --only-binary=:all: -r requirements.txt --proxy=http://127.0.0.1:7897 -i https://pypi.org/simple
   pip install --only-binary=:all: -r requirements.txt
   

   # 安装额外的插件
   pip install "mkdocs-material[imaging]"

   #指定私约测试ssh访问，注意github只允许git用户登录，其他的用户名会被拒绝
    ssh -Tv -i C:\Users\xxx\.ssh\id_rsa git@github.com
    

~~~
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
 