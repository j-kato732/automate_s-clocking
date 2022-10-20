# automate_s-clocking
s-clockingの打刻自動化

# 実行環境
- Google Chrome
    - 106.0.5249.119（Official Build） （x86_64）
- Python
    - 3.9.12
- Selenium
    - 4.5.0

# 前提
以下がインストールされていること
- Google Chrome
  - Google Chromeのバージョンが106以外の場合は、バージョンに合わせてdriverを変更すること
- python3
- Selenium

# 使用方法
1. git pull
2. config.iniにログイン情報を入力
3. automate.pyを実行。

出勤時
```
$ python3 automate.py in
```

退勤時
```
$ python3 automate.py out
```
