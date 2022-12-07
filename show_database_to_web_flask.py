
import mysql.connector
from flask import Flask, render_template
#variabel
user = 'root'
password = ''
host = '127.0.0.1'
database = 'pizza'

class sql():
    def __init__(self, user, password, host, database) :
        self.config = mysql.connector.connect(
                                                host=host,
                                                user=user,
                                                passwd=password,
                                                database=database
                                            )

    def select(self, query, values):
        config = self.config
        mycursor = config.cursor()
        mycursor.execute(query, values)
        myresult = mycursor.fetchall()
        return myresult #ubah dari json


app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    table_names= "pizza4" 
    abc = sql(user, password, host, database)
    query = "SELECT * FROM {}".format(table_names)
    values = ()
    data = abc.select(query, values)
    return render_template('show_data.html', data = data)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
