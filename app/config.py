import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Flaskの設定定数をまとめたクラスです。
    """
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'unko.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
