# 基本イメージ
FROM python:3.8-slim

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のコピーとインストール
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# アプリケーションのコピー
COPY . /app

# Streamlitの実行コマンド
CMD streamlit run --server.port $PORT app.py