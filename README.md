# Allure Framework

## 1、官网文档教程
https://docs.qameta.io/allure-report/

## 2、环境准备，安装jdk
https://blog.csdn.net/panc_guizaijianchi/article/details/90634013

## 3、下载 allure-commandline并配置环境变量
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

## 3、检查安装是否成功
allure --version

## 4、安装pytest-allure插件
pip install allure-pytest

## 5、保存运行测试产生的xml文件
pytest --alluredir=./allure_results  
python -m  pytest --alluredir=./allure_results  

## 6、根据xml文件生成allure测试报告
allure serve ./my_allure_results