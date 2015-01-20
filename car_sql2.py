# Add table call orders
# containing "make", "model", and "order_date" YYYY-MM-DD
# Add 15 records with separte order_date
# Output the car make and model
# then output the quantity
# then output the order dates

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("""CREATE TABLE orders (make TEXT, model TEXT, order_date TEXT)""")

	theorders=[
				('Ford','T999','1991-08-07'),
				('Ford','Fiesta','1993-03-18'),
				('Toyota','Altis','1988-9-06'),
				('Ford','T999','1996-04-07'),
				('Toyota','Camry','2003-06-23'),
				('Toyota','Camry','1997-01-07'),
				('Ford','T999','2005-05-05'),
				('Ford','T999','2011-07-22'),
				('Ford','T999','1999-10-10'),
				('Ford','Mustang','2001-01-27'),
				('Ford','T999','1991-08-07'),
				('Ford','Fiesta','2007-12-25'),
				('Toyota','Camry','2014-04-02'),
				('Toyota','Altis','2001-05-05'),
				('Toyota','Altis','1993-11-07'),
				('Ford','T999','1992-02-02'),
				]

	c.executemany("INSERT INTO orders VALUES(?,?,?)",theorders)

	c.execute("""SELECT orders.make, orders.model, Inventory.Quantity, orders.order_date
				FROM orders, Inventory
				WHERE orders.model=Inventory.model 
				ORDER BY orders.order_date ASC""")

	rows = c.fetchall()

	for r in rows:
		print r[0],r[1]
		print "Quantity in Inventory: " + str(r[2])
		print "Order date: " + r[3]
		print
