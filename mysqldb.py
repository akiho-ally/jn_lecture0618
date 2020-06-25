from flask import *
import pymysql.cursors

pymysql.install_as_MySQLdb()
app = Flask(__name__)

cursor = pymysql.connect(host="localhost", user="root", db="lamplecture_homework").cursor()
cursor.execute(
    'SELECT * FROM users;')
data = cursor.fetchall()


@app.route("/")
def index():
    return jsonify({cursor.description[i][0]: data[0][i]
                    for i in range(0, len(data[0]))})


if __name__ == "__main__":
    app.run(port=8000)
