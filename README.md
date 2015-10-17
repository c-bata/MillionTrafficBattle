# Flask API

## Migration

- http://flask-migrate.readthedocs.org/en/latest/

```
$ python manage.py db --help
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```


## Flask-Script

- http://tell-k.hatenablog.com/entry/2012/01/22/005625
- http://flask-script.readthedocs.org/en/latest/


runserverはdefaultで入ってる。
debugもTrueにしてくれてるみたい。portとかは引数で指定できる。詳しくはhelp見る。

shell
- http://flask-script.readthedocs.org/en/latest/#shell


## Profiling

- http://blog.zoncoen.net/blog/2013/11/12/werkzeug-wsgi-application-profiler/
- http://docs.python.jp/3.4/library/profile.html


## Flask application examples

- https://github.com/miguelgrinberg/flasky
- https://github.com/miguelgrinberg/api-pycon2015
- https://github.com/c-bata/Katudon


## Tips

- Blueprint: http://qiita.com/Alice1017/items/a6b6500e60f2a0334e44

# Implementation

## User authentication

```
>>> from flask_api.models import User
>>> u = User()
>>> u.password='cat'
>>> u.password
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/masashi/PycharmProjects/million_traffic_battle/flask_api/models.py", line 13, in password
    raise AttributeError('password is not a readable attribute')
AttributeError: password is not a readable attribute
>>> u.password_hash
'pbkdf2:sha1:1000$pjsh7cVO$33e723c78dfe39b49ade0c7b5db8f034bdd6d31e'
>>> u.verify_password('cat')
True
>>> u.verify_password('cats')
False
```

