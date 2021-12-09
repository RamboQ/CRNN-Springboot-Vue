# 基于crnn实现的汉字印刷体识别课程大作业
## 此作业使用crnn来实现识别功能，并使用一个网页来展示
前端：vue 后端：springboot 算法：crnn   
crnn算法部分使用的是一个博客的代码：https://www.cnblogs.com/skyfsm/p/10345305.html 只做了一点小修改
## 环境
见requirment.txt; 这个环境是我anaconda创建的一个虚拟环境python版本为3.6 装的库是用pycharm看的
## IDE和运行
使用的是pycharm + IDEA写的程序，想看效果的话，运行crnn文件夹下的socket.py程序，打开算法部分的服务端socket,运行learnSpr(Springboot写的后端)后端和vue前端learnVue，就能在浏览器（仅测试过edge）看到新打开的窗口，注册登录后即可使用。  
注：注册功能需要使用自己的本地数据库，如mysql等; 不想使用数据库的话请自行在Vue前端修改绕过登录或删除登录界面。
## 结果展示
![image](https://user-images.githubusercontent.com/55075404/144846362-90e823dc-76de-4896-8d22-1c061b6163b8.png)
