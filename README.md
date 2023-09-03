
# Sweettalk-Django4.2


## 一、项目介绍

1. Django：Django是一套用于 Web 应用程序开发的具有高效灵活、扩展性强和安全可靠的强大开发工具,是Python开发网站的 Web 应用程序首选框架。Django运用DRY（Don’t Repeat Yourself）设计理念，采用 MTV（Model-Template-View）架构模式，提供了强大数据库和后台功能，突出代码可重用和可维护性和最佳实践性，通过提供许多内置功能和现成的解决方案，使得Python 程序开发人员可轻松完成网站大部分内容设计，具有开发快捷、部署方便、可重用性高和维护成本低等诸多优势。

2. MTV架构模式：M 代表模型（Model），负责业务对象和数据库的关系映射(ORM)；T 代表模板 (Template)，负责如何把页面展示给用户(html)；V 代表视图（View），负责业务逻辑，并在适当时候调用Model和Template。

3. 项目概述：在前后端分离的网站设计中，后端开发人员主要负责网站功能和数据库设计，这就离不开数据库读写、数据表之间的数据关联等内容。此开源项目以商品入库和查询为应用，运用Django架构和Python工具开发了一套开源程序，实现了商品信息（品类和详细信息）入库和查询系统的基础Django 项目开发。通过对该项目的学习，你可以体验Django环境搭建、数据表的创建，将商品信息入库存储，并通过相应条件的数据过滤与查询，获取所需的商品品类或者商品详细信息的程序实现流程。掌握虚拟环境构建、项目创建、数据表的使用（构建、合并、查询、序列化）、基于函数编程/APIview编程/自定义函数的三种编程模式、admin 后台管理、路由配置等功能的实现方法，体悟整个Web 应用的生命周期，并形成进行类似Django项目开发能力。该项目内容是Django项目后端开发者很好入门基础课程。


## 二、项目亮点

1. 提供清晰简洁的教学文档和匹配的课后习题。

2. 项目开发过程中会涉及到设计、开发、调试、部署等多个动手环节，这将使你熟悉整个 Web 应用的生命周期。

3. 基于Django框架的高效性、开放性和灵活性，通过项目架构理解和开发实践，可在此基础上进行Django的项目自主开发和进一步拓展。

[学习地址] https://joe-2002.github.io/sweettalk-django4.2/

## 三、项目受众

1. 开发人员和程序员：Django 是一个流行的 Web 框架，许多开发人员和程序员选择使用它来快速构建可扩展的 Web 应用程序。无论是有经验的开发人员还是初学者，Django 都提供了一个强大且易于使用的平台来创建功能丰富的网站和应用。

2. 学生和教育机构：许多大学、学院和教育机构将 Django 作为教学的一部分，因为它简单易懂，同时又涵盖了 Web 开发的各个方面。学生可以通过学习 Django 来获得实际的编程经验，并将其应用到项目中。

3. 创业者和企业家：对于有创业想法或开设在线业务的人来说，Django 是一个理想的选择。它提供了一个稳定、可靠且高效的开发平台，可以帮助他们快速构建起自己的网站或应用程序，并提供必要的功能和工具来支持业务的发展。

4. Web 设计师和 UI/UX 设计师：尽管 Django 是一个后端框架，但在开发过程中，与前端设计师和 UI/UX 设计师密切合作是非常重要的。Django 提供了与前端技术（如 HTML、CSS 和 JavaScript）的无缝集成，并允许设计师将设计和用户体验融入到 Web 应用中。

## 四、基本信息

1. 学习周期：8 天，每天平均花费时间 1~3 小时不等，根据个人学习能力和基础不同而有所浮动。

2. 学习形式：理论学习 + 练习

3. 人群定位：可以零基础入门

4. 难度系数：容易

备注：需要 Python 基础

如果觉得本项目中有错误，可以[点击这里](https://github.com/Joe-2002/sweettalk_django4.2/issues)提交你希望补充的内容，我们看到后会尽快进行补充。



## 五、DataWhale开源学习记录     
| 时间      | 人数 |
| ----------- | ------ |
| 2023年8月 | 55人 |
| 待定      |      |     

**共计55人**

## 六、学习线路

第一步：环境搭建

第二步：项目配置

第三步：数据模型实现（数据表创建与数据迁移）

第四步：Django内置后台管理（用户注册、登录和数据增删与修改）

第五步：数据查询程序实现

第六步：数据格式转换--序列化程序实现

第七步：自定义编程程序实现

第八步：路由配置

第九步：联合测试

## 七、学习建议

1. 在动手调试或者开发之前，认真阅读并理解该节课的学习文档和程序架构。

2. 基于学习周期有限，本项目仅提供了基于Djangojia基础学习内容。若学习过程中遇到一些卡点，涉及到一些拓展性或者关联性知识，鼓励你通过网络资源进行自主学习，这对进一步深入理解和驾驭本项目内容是非常有帮助的，也是我们终生学习素质的一次养成机会。

3. 在编辑器选项中，pycharm专业版更好，没有专业版，可以用社区免费版。如果对于没有使用过pyhcharm的新手来说，也可采用更为简洁的vscode作为暂时过度。

## 八 任务规划

### Task1：环境搭建与项目配置（Day1）

1. 环境创建: 安装Python、虚拟环境创建以及项目开发依赖包的安装

2. 项目框架创建： 创建项目文件夹及项目应用文件夹

3. 项目配置与测试： 通过settings.py 文件完成项目配置。通过对轻量级服务器进行连接测试。


### Task2：数据表构建与数据迁移与管理（Day2~Day3）--models.py的应用

1. 数据表常用字段和常用配置

2. 外键使用

3. 执行生成迁移脚本命令（python manage.py makemigrations）和迁移命令（python manage.py migrate）

4. 创建 admin 的超级管理员：在 admin 文件中引入数据表，注册数据表到 admin，进行数据增添、删减与修改操作（检查数据库内容进行测试）


### Task3: QuerySet 和 Instance应用（Day4~Day5）

1. 输出相关数据的数据类型，找出 QuerySet 和 Instance

2. 运用函数式编程尝试对数据进行增删查改等操作（编写程序并测试）

### Task4: Django Serialization（序列化）及APIView模式的编程实现（Day6）

1. 构建序列化（序列化单个字段、多个字段和所有字段）

2. 序列化的高级使用（序列化单个对象、序列化多个对象和序列关联对象（有外键））

3、使用 APIView进行序列化功能编程实现（编写程序并测试）

### Task5:Django-DRF(ModelViewSet)及自定义函数的使用（day7）

1. Django-DRF（ModelViewSet）简介

2. 使用 DRF（ModelViewSet）方法

3. 自定义函数的装饰器的掌握和使用（编写自定义函数并测试）


### Task6： DefaultRouter 的使用(day8)

1. 导入 DefaultRouter

2. 使用 DefaultRouter 注册 API

3. 将 API 导入项目路由配置中

4. 对整个项目进行综合调试

## 贡献者

项目负责人：[李柯辰](https://github.com/Joe-2002)

邮箱：likechen@linchance.com

<div>
<table border="0">
  <tbody>
    <tr align="center" >
      <td>
         <a href="https://github.com/Joe-2002"><img width="70" height="70" src="https://github.com/Joe-2002.png?s=40" alt="pic"></a><br>
         <a href="https://github.com/Joe-2002">李柯辰</a> 
        <p> 南京航空航天大学<br>江苏霖承科技有限公司</p>
      </td>
      <td>
         <a href="https://github.com/zhumengyu"><img width="70" height="70" src="https://github.com/zhumengyu.png?s=40" alt="pic"></a><br>
         <a href="https://github.com/zhumengyu">朱梦雨</a> 
        <p>南通理工学院<br>江苏霖承科技有限公司</p>
      </td>
      <td>
         <a href="https://github.com/Ethan-2004"><img width="70" height="70" src="https://github.com/Ethan-2004.png?s=40" alt="pic"></a><br>
         <a href="https://github.com/Ethan-2004">张海生</a>
         <p>南通师范高等专科学校<br>江苏霖承科技有限公司</p>
      </td>
    </tr>
  </tbody>
</table>
</div>

## 致谢

特别感谢 [@Sm1les](https://github.com/Sm1les)、[胡锐锋](https://github.com/Relph1119)对本项目的帮助与支持。

特别感谢以下为教程做出贡献的同学！

<a href="https://github.com/Joe-2002/sweettalk-django4.2/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Joe-2002/sweettalk-django4.2" />
</a>



## 项目地址

[点击这里](https://github.com/Joe-2002/sweettalk_django4.2)

## License
LinChance © 2023, sweettalk-django4.2 - Released under the GNU General Public License v3.0





