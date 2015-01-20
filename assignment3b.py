import sqlite3

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	reply_set={"AVG":"SELECT AVG(num) FROM numbers",
				"MAX":"SELECT MAX(num) FROM numbers",
				"MIN":"SELECT MIN(num) FROM numbers",
				"SUM":"SELECT SUM(num) FROM numbers"}

	user_command=""
	while user_command != "EXIT":
		user_command=str(raw_input("Enter AVG, MAX, MIN, SUM or EXIT")).upper()
		try:
			c.execute(reply_set[user_command])
			print c.fetchone()[0]

		except KeyError:
			if user_command == "EXIT":
				print
				print "See You Next Time~"

			else:
				print
				print "ENTER SOMETHING VALID YOU SCUM!!"

