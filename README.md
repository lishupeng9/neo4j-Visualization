# query_neo4j_flask
## 项目简介
 此项目是简单的neo4j查询可视化，使用Flask框架，通过vis.js可视化到前端
## 注意事项
 具体的cypher语句写在app.py中的get_data()，最后返回的一定要是json格式，如果要使用vis.js展示节点的话，边（links）的定义一定要具备id，from，to这三个属性，缺一不可，缺少一个则无法正确定位到节点之间的关系。
## 运行方法
* 切换到neo4j安装目录的bin目录下，使用cmd命令，输入neo4j.bat console 启动neo4j数据库
![image](/img/neo4j的启动.png)
* 运行app.py 在localhost:5000下即可查看页面
![image](/img/启动app.py.png)
![image](/img/可视化的展示.png)
