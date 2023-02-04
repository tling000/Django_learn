![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Django_learn
Djandoの学習用

# Requirements
Python3.10
```python
asgiref==3.6.0
Django==4.1.6
sqlparse==0.4.3
tzdata==2022.7
```

# Preparations
## 1. settings_local.pyファイルの作成
"settings_local_sample.py"ファイルを同ディレクトリに"settings_local.py"としてコピーする。
## 2. SECRET_KEYの再生成
下記コマンドを実行する。
```bash
python secret_key_regenerate.py
```
出力された文字列を"settings_local.py"内のパラメータ"SECRET_KEY"の値としてペーストする。
```python
SECRET_KEY = "[ペースト位置]"
```

# Tests
下記コマンドを実行する。
```bash
python manage.py runserver
```
Webブラウザで下記アドレスへアクセスすると、Top page(Hello World!)が表示される。  
<http://127.0.0.1:8000/>
![Top-page](https://user-images.githubusercontent.com/84237053/216761933-61634d47-135d-4c9b-8f57-792e6e0574bf.png)

