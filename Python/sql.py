import MySQLdb

connection = MySQLdb.connect(
    host="obermayer",
    port=3306,
    db="aircondition",
    user="air", passwd="air"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM tasks ")
results = cursor.fetchall()
for items in results:
    print items[0]
