import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("SELECT * FROM inventory")

	rows = c.fetchall()

	for r in rows:
		print r[1]
		print """c.execute("SELECT count(order_date) FROM orders WHERE model=?",({}))""".format(r[1])
		c.execute("SELECT count(order_date) FROM orders WHERE model='Kancil'")
		print c.fetchone()[0]
		print