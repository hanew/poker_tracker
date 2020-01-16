#!/usr/bin/python3

import pymysql
import datetime

# Open database connection
# db = pymysql.connect("localhost","root","coenjit1","sys" )

# function that executes a sql select query
# function input: query
# function output: rows returned

# biggest winner

def get_biggest_winner():
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	query = "SELECT max(net_gain) as biggest_winner from poker_app"

	try:		
		# execute SQL query using execute() method.
		cursor.execute(query)
		results = cursor.fetchone()
		net_gain = results[0]
		print ("biggest winnings = %4.2f" % (net_gain))
		print(cursor.rowcount, "record returned.")

	except:
		print ("Error: unable to fetch data")

def fixnetgain():
	mycursor = db.cursor()
	sql = "UPDATE poker_app SET net_gain = (cash_out - buy_in) WHERE net_gain = 0"

	mycursor.execute(sql)

	db.commit()

	print(mycursor.rowcount, "record fixed.\n")


def select_all():
	db = pymysql.connect("localhost","root","coenjit1","sys" )
	cursor = db.cursor(pymysql.cursors.DictCursor)
	query = "SELECT * from poker_app"

	cursor.execute(query)

	rows = cursor.fetchall()
	db.close()
	#print(rows)
	return rows

def insert_row(buyin, cashout, location, bigblind, littleblind, startime, endtime):
	db = pymysql.connect("localhost","root","coenjit1","sys" )

	mycursor = db.cursor()
	
	sql = "INSERT INTO poker_app(buy_in, cash_out, net_gain, location, big_blind, little_blind, startime, endtime) values(%s, %s, %s, %s, %s, %s, %s, %s)"
	val = (buyin, cashout, (cashout)-(buyin), location, bigblind, littleblind, startime, endtime)
	mycursor.execute(sql, val)

	db.commit()

	print(mycursor.rowcount, "record inserted.\n")
	mycursor.close()
	db.close()
	return mycursor.rowcount

def delete_row(startime):
	cursor = db.cursor()
	sql = "DELETE FROM poker_app WHERE startime = %s"
	adr = (startime)

	mycursor.execute(sql, adr)
	db.commit()

	print(mycursor.rowcount, "record inserted.\n")

#fixnetgain()

#db.close()

	