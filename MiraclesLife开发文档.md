# 注释规范

## 为了统一，多行注释统一使用```""```,字符串统一使用```''```表示


# 数据库的使用

## 安装redis后在安装目录下打开powrshell或cmd

## 启动redis：在powershell或cmd中输入```redis-server.exe redis.windows.conf```,```redis.windows.conf```为配置文件，可根据需要宣告

## 连接redis：在powershell或cmd中输入```redis-cli --raw -h 127.0.0.1 -p 6379 -a 12345```。注：```--raw```目的是为了防止中文乱码，```-h```为redis监听的ip，```-p```为监听端口，```-a```，为数据库密码

## 相关配置请在```redis.windows.conf```进行更改

## 为了防止初始化时redis数据库的大规模读写导致的数据库异常而使程序异常退出，请在redis配置文件```redis.windows.conf```中设置```stop-writes-on-bgsave-error yes```为```stop-writes-on-bgsave-error no```,注：产生意外的根本原因尚未彻底了解
