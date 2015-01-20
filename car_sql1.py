# INSERT data and SELECT data

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	addition = [('Ford','Mustang',3),
		('Ford','Fiesta',2),
		('Toyota','Altis',1),
		('Toyota','Camry',5),
		('Ford','T500',9)]

	c.executemany("INSERT INTO Inventory VALUES (?,?,?)", addition)

	c.execute("SELECT * FROM Inventory")

	rows= c.fetchall()

	for row in rows:
		print row[0],row[1],row[2]

	c.execute("UPDATE Inventory SET Quantity=5 WHERE Model='Altis'")
	c.execute("UPDATE Inventory SET Model='T999' WHERE Model='T500'")

	c.execute("SELECT * FROM Inventory WHERE Make='Ford'")

	rows=c.fetchall()

	for row in rows:
		print row[0],row[1],row[2]


