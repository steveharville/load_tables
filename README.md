# insert_multiple_csv
Use cx-Oracle in Python to bulk load arbitrary tables using csv files

I recently got a request to load hundreds of database tables in a day and a half using csv files our developers created. I considered using SQL Loader but I didn't want to spend the time understanding the table structure and creating the control file for each table. Another alternative was to use SQL Developer to import the csv files. That goes against my nature because it would be a manual, repetitive and error prone process.

The csv files were fairly small so plain inserts would work. I looked at writing a BASH script to generate the insert statements and it became very complex very quickly. PL/SQL was an option too but I ruled it out because of the requirement to read flat files. I have been using the Python cx-Oracle module recently so I decided to write a Python script for this task. 

Python turned out to be the right choice and the script was very easy to write. The only tricky part was recognizing the date fields. Those are unquoted like a numeric field but contain literals like JAN,FEB, etc. Python and cx-Oracle handled everything with a minimum of effort on my part.

Create the csv files in a dedicated subdirectory like : tablename.csv. The first row of each csv file must contain the column names. The script truncates the target table before inserting the csv records. Any double quoted field is considered a literal and unquoted fields are numeric except date fields which must have the format 01-JAN-16.

Link to blog post : https://steveharville.wordpress.com/2016/05/02/use-cx-oracle-in-python-to-bulk-load-arbitrary-tables-using-csv-files/
