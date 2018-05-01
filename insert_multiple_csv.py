# copyright 2016 Steve Harville
import cx_Oracle
import csv
import datetime
import os
 
r = connection = cx_Oracle.connect('steveharville/secretpassword@ora_db')
print r
r = cursor = connection.cursor()
print r
schema='STEVEHARVILLE'
for csvfile in os.listdir(os.getcwd()):
    if csvfile.endswith(".csv") or csvfile.endswith(".CSV"): 
	tablename=csvfile.rsplit('.',1)[0].upper()
        print csvfile
	print tablename 
	cursor.execute('truncate table ' + schema + '.' + tablename)
	reader = csv.reader(open(csvfile), delimiter=',')
	L = []
	column_list=''
	value_list=''
	first_row = next(reader)
	column_string = ','.join(first_row).translate(None,'"')
	insert_string='insert into ' + schema + '.' + tablename + ' (' + column_string + ') values ('
	val_list=[]
	for i in range(1,len(first_row)+1):
		val_list.append(':'+ str(i))
	value_string=','.join(val_list)
	insert_string += value_string + ')'
	for row in reader:
		for index,col in enumerate(row):
			col_tr = col
			if col_tr:
				if col_tr[0] != '"' :
					try:
						col_tr=datetime.datetime.strptime(col_tr,'%d-%b-%y')
					except ValueError:
						continue
			row[index] = col_tr	
		L.append(row)
 	cursor.prepare(insert_string)
 	cursor.executemany(None, L)
 	print 'Inserted: ' + str(cursor.rowcount) + ' rows.'
 	connection.commit()
        continue
    else:
        continue
 
cursor.close()
connection.close()
#
