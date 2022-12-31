import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''create table Cars(ID INT,TEXT text,price INT)''')
print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',52127)")
cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
cur.execute("INSERT INTO Cars VALUES(4,'Volva',29000)")
cur.execute("INSERT INTO Cars VALUES(5,'Bentley',35000)")
cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
cur.execute("INSERT INTO Cars VALUES(7,'Bummer',41400)")
cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
con.commit()
print("values in table car inserted.")
