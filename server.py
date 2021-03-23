from flask import Flask, request, send_from_directory, render_template, Response, jsonify
import datetime
import os
app = Flask(__name__)


import pymysql.cursors
import pymysql



@app.route('/store', methods=['POST'])
def index():
    message = request.json.get("message")
    now = datetime.datetime.now()
    try:
        # https://stackoverflow.com/a/34503728/1320619
        # Connect to the database
        connection = pymysql.connect(host="141.136.33.223",
                                     user='timepcou_site',
                                     password=os.environ["code"],
                                     db='timepcou_devopchallenge',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `store` (`message`, `timestamp`) VALUES (%s, %s)"
            cursor.execute(sql, (message, now))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()
    return jsonify({})


if __name__ == "__main__":
    app.run(port=8008, host="0.0.0.0")
