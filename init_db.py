import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def init_db():
    # DB情報の取得
    dsn = os.environ.get("DATABASE_URL")
    # DBに接続
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('schema.sql', encoding='utf-8') as f:
        sql = f.read()
    # SQLを実行
    cur.execute(sql)
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる
    conn.close()


def insert_db(name, age):
    # DB情報の取得
    dsn = os.environ.get("DATABASE_URL")
    # DBに接続
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    sql = f"INSERT INTO users (name, age) VALUES (%s, %s);"
    # SQLを実行
    cur.execute(sql, (name, age))
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる
    conn.close()


def all_users():
    dsn = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql = "SELECT * FROM users;"
    cur.execute(sql)
    users = cur.fetchall()
    conn.commit()
    conn.close()

    return users


def main():
    # init_db()
    insert_db("Dan", 33)
    users = all_users()

    print(users)


if __name__ == '__main__':
    main()
