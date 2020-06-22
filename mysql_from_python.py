import os
import datetime
import pymysql

# Get username from Gitpod
username = os.getenv('USER')

connection = pymysql.connect(host="localhost",
                             user=username,
                             password="",
                             db="Chinook")

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['jim', 'fred', 'Bob']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)
        
        connection.commit()
finally:
    # close the connnection
    connection.close()
