# Alertover推送插件

## 使用方式

- 在HomeAssistant中建立以下路径: `homeassistant\custom_components\notify`
- 在notify文件夹下放入alert_over文件
- 注册

    1. 注册账户

    ![图片](https://www.alertover.com/static/imgs/pages/pic01.png)

    2. 以组织为单位管理成员，发送源，接收组添加组织然后邀请成员加入，在成员列表管理成员,并建立该组织下的发送源和接收组。发送源只能通知到同一组织下的接收组和成员

    ![](https://www.alertover.com/static/imgs/pages/pic02.png)

    3. 创建并管理你所在组织的发送源。在发送源列表添加组织中的发送源，确定后可以获取发送源对应ID，作为source用于代码中发送

    ![](https://www.alertover.com/static/imgs/pages/pic03.png)

    4. 创建并管理你所在组织的接收组。receiver可以为用户ID，可以为接收组ID，在接收组列表管理你的接收组

    ![](https://www.alertover.com/static/imgs/pages/pic04.png)

## 配置文件及自动化例程

### 配置
```yaml
notify:
  - name: my_notify
    platform: alert_over
    from_source: 发送人密钥
```

### 自动化

```yaml
- alias: weather publish
  trigger:
    at: '6:30'
    platform: time
  action:
    service: notify.my_notify
    data:
      title: 早安
      message: 'hello'

      target: 接收信息人密钥
```

