# simple_fab
Some Fabric tools

目前只有自用的SpringBoot打包上传启动 & Thrift Service文件远程生成工具，将会添加更多……

## 自用的SpringBoot打包上传启动：
 ***maven 需要在plugins节点下添加***:
 
 ```xml
 <plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <configuration>
      <executable>true</executable>
    </configuration>
  </plugin>
  ```
  

  > 进入到simple_fab目录下
  
  > $ cd jar
  
  > fab -f booty.py release
  
  或者指定带有 @task 装饰的方法名，例：
  
  > fab -f booty.py pack
  
  
## Thrift Service文件远程生成工具，解决开发机安装的各种痛苦和版本不同的问题
  
  > $ cd thrift
  
  > fab -f gen.py gen:idl_path=/Users/xiaolei/abc-service.thrift
  
  远程host上必须安装 thrift 生成工具
  
  **注意：生成前会删除远程服务器上所有之前生成的文件！**
