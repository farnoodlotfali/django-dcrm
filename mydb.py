
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursorObj = database.cursor()


cursorObj.execute(" CREATE DATABASE elderco")

print("done")