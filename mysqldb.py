import MySQLdb
import json


conn = MySQLdb.connect(
user='root',
# passwd='root',
host='localhost',
db='lamplecture_homework')


#usersテーブル
query = "SELECT * FROM users"

cursor = conn.cursor(MySQLdb.cursors.DictCursor)
cursor.execute(query)
data = cursor.fetchone()
conn.close()
print(json.dumps(data, indent=4))

# {
#     "id": 1,
#     "name": "Akiho Iwata",
#     "KG": "d-hacks",
#     "login_name": "akiho"
# }
