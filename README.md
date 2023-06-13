# reactPy-sample
reactPyで作成したアプリケーションです。
以下に詳細を記載しています。


### reactPy(gitHub)
https://github.com/reactive-python/reactpy

### 必要なライブラリ
- reactPy
- reactPy-router
```
pip install reactPy reactPy-router
```
※python、fastapi,uvicornはインストール済みの状態で環境で作成しています。
適宜追加をお願いします。

### アプリケーション起動
ホットリロードなし
```
python view.py
```
ホットリロードあり
```
uvicorn view:app --reload
```