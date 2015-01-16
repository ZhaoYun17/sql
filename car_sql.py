# import the motherfucker sqlite3
import sqlite3

# create a mfking database file in the folder
conn = sqlite3.connect("cars.db")

# make the db file alive!
cursor = conn.cursor()

# Do something on it!
cursor.execute("""CREATE table Inventory
	(Make TEXT, Model TEXT, Quantity INT)
	""")

# close the database like you would any other files
conn.close()