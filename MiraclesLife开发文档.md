# 数据库的使用

## 安装redis后在安装目录下打开powrshell或cmd

## 启动redis：在powershell或cmd中输入```redis-server.exe redis.windows.conf```,```redis.windows.conf```为配置文件，可根据需要宣告

## 连接redis：在powershell或cmd中输入```redis-cli --raw -h 127.0.0.1 -p 6379 -a 12345```。注：```--raw```目的是为了防止中文乱码，```-h```为redis监听的ip，```-p```为监听端口，```-a```，为数据库密码

## 相关配置请在```redis.windows.conf```进行更改
