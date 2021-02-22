import sqlite3
conn = sqlite3.connect("ku.db")
cursor = conn.cursor()
sql = """Create table biaoge(
    id int,
    name text,
    gender text)"""
cursor.execute(sql)
cursor.close
conn.close