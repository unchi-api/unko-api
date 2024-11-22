#アプリケーションの設定ファイル

import os

#現在のファイル（config.py）があるディレクトリの絶対パスを取得
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Flaskの設定定数をまとめたクラスです。
    """
    #SQLiteデータベースの接続先を指定
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'unko.db')}"
    #データベースの変更追跡機能を無効
    SQLALCHEMY_TRACK_MODIFICATIONS = False
