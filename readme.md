# deploy #

1. python虚拟环境创建
```
python3 -m venv venv
source venv/bin/activate

```
2. 安装第三方依赖库
```
pip install -r requirements.txt
```

3. 数据库
创建数据库
```
create database ansible_cmdb default charset utf8mb4
```

修改数据库配置: ansible_cmdb/settings.py

4. 迁移数据库
```
python manage.py makemigrations
python manage.py migrate
```

5. 创建管理员账号:
```
python manage.py createsuperuser
```

6. 启动web服务：
```
python manage.py runserver 0.0.0.0:9999
```

7. ansible准备
inventory编写: etc/hosts
ssh免密登录
测试:ansible all -m ping -i etc/hosts

8. 采集
```
python manage.py fact
```

9. 定时采集
添加采集到cron(每4小时执行一次)
/var/spool/cron/root
```
0 0 */4 * * /root/codes/ansible_cmdb/venv/bin/python /root/codes/ansible_cmdb/manage.py fact > /dev/null &
```

10. web查看