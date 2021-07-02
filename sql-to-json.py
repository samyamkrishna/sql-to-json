import json
import psycopg2

# db connection setting
conn_string = "host='localhost' dbname='<your-db-name>' user='<your-user-id>' password='<your-password>'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

# for json path, root (<columnname>), gives you the data in json format
cursor.execute("SELECT * FROM <your_table_name> for json path, root (<columnname>)")
rows = cursor.fetchall()

# write the results into a json file
with open("your_json_file.json", "w") as f:
    f.write(rows)

# close db connection
conn.close()
