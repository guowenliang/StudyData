首先你得注册一个自己的GitHub账号，注册网址：https://github.com/join



有了自己的账号以后，就可以进行登录，开始创建一个新的项目



创建一个新的项目，填写项目名称，描述



创建完成之后，跳转到下面的页面，下面红框中的网址要记住，在后面上传代码的时候需要使用



接下来，我们需要先下载Git，这里最好下载最新版本的Git，这里附上我下载的Git2.6.2的网址：https://git-scm.com/downloads，安装时如果没有特殊需求，一直下一步就可以了，安装完成之后，双击打开Git Bash



出现以下界面：



第一步：cd进入你放项目文件的地址，我的地址在D:\MYFILE\graduation\study\项目程序



第二步：输入git init

如下图所示，这个意思是在当前项目的目录中生成本地的git管理（会发现在当前目录下多了一个.git文件夹）



第三步：输入git add .     

这个是将项目上所有的文件添加到仓库中的意思，如果想添加某个特定的文件，只需把.换成这个特定的文件名即可。




第四步输入git commit -m "first commit"，表示你对这次提交的注释，双引号里面的内容可以根据个人的需要
改。


这里如果出现以下内容，则需要你输入自己的账号或名字



用上面提示的代码输入自己的邮箱或名字



再输入git commit -m "first commit"时就会成功



第五步输入git remote add origin https://自己的仓库url地址（上面有说到） 将本地的仓库关联到github上，
这里宝宝输入的是git remote add origin https://github.com/Vivianyuwei/Fabric-defect-classification-based-on-WLD.git

最后一步，输入git push -u origin master，这是把代码上传到github仓库的意思。

执行完后，如果没有异常，会等待几秒，然后跳出一个让你输入Username和Password 的窗口，你只要输人github的登录账号和密码就行了。
————————————————
版权声明：本文为CSDN博主「夏雨薇安」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/m0_37725003/article/details/80904824