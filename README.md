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
