# AutoBitcoin
## 项目简介
一个自动化比特币交易平台。

## 开发准备
* 开发工具
pycharm（建议）
通过pycham开发的时候，安装依赖库需要配置代理，通过pycharm的git拉取或者提交代码的时候需要取消代理。
* Git 全局配置
```
git config --global user.name  "your_rtx_name"
git config --global user.email "your_rtx_name@tencent.com"
```
* Git 代理配置（取消代理）
```
git config --global --unset http.proxy
git config --global --unset https.proxy
```
* 拉取代码
```
http://git.code.oa.com/teg-apd-bitcoin/AutoBitcoin.git
```
* 创建分支
```
git checkout -b your_branch_name
```
* 将主分支代码合并到自己的分支
```
git pull
git merge master
注意：如果有冲突，切记要谨慎解决。
```
* 将本地分支代码提交到仓库
```
git push origin your_branch_name
注意：在提交代码之前一定要先pull,解决冲突后再提交。
```
* 合并代码至master分支
在项目主页点击branch，找到自己的分之，点击merge,按照操作提示提交合并代码的Pull Request,为了防止代码合并问题，建议多指定几个代码审阅人。
* 友情提示
    * 建议使用pycharm开发，通过pycharm嵌入的git进行代码的拉取、合并、更新
    * 尽量不要在别人的代码文件中开发，减少冲突
    * 及时的更新（pull）、提交（push）、合并（pull request）你的代码

## 项目依赖
在开发的过程中，我们难免会使用第三方的库，比如后台开发框架django，机器学习相关的numpy、scipy等，如有使用到，请在下注明库名以及版本。其他同学在开发的时候安装即可。
* django 2.0.7
* mysqlclient 1.3.13

## 项目模块

### AutoBitcoin模块

`AutoBitcoin`模块是django模板生成的模块，主要包含项目的设置、路由、网管等配置
* settings.py 项目配置
* urls.py 路由配置
* wsgi.py 网关
这个模块我们只需要在`urls.py`编写路由信息即可，例如：
```
    path('', bit_views.home),
```
### BitcoinDealer模块
`BitcoinDealer`也是通过django生成的模块，这个模块使我们项目具体实现的一个应用，具体的业务逻辑、数据库连接都在这一层实现
* views.py 主要的业务逻辑、控制器
* models.py 数据库model操作的封装，一个简易的ORM

### BitcoinSDK模块
封装对比特币交易网站api访问接口

### PricePrediction模块
价格预测实现

### TradingStrategy模块
交易策略的实现
