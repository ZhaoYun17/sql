# use COUNT()  calculate total number of orders for each make and model
# Output car's make and model
# output quantity
# output order count

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("SELECT * FROM inventory")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1]
		print "Quantity of car: " + str(r[2])
		c.execute("SELECT count(order_date) FROM orders WHERE model=?",(r[1],))
		print c.fetchone()[0]
		print