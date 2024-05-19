import mysql.connector
import time
from sensor_code import sensor_data_queue

db_host = "localhost"
db_name = "healthiot"
db_user = "root@localhost"
db_password = "root"



# Connect to the database
def edge_engine():
    while True:
        try:
            connection = mysql.connector.connect(
                host=db_host,
                database=db_name,
                user=db_user,
                password=db_password,
            )
        except mysql.connector.Error as err:
            print("Failed to connect:", err)
            exit()

        cursor = connection.cursor()


        data_to_push = sensor_data_queue.get(timeout= 3)
        time_to_push = time.time()
        # print(time_)
        data = [data_to_push, time_to_push]


        sql_query = f"INSERT INTO temp_and_time (temp_instant, time_instant) VALUES (%s, %s); "  # Replace with your desired table
        cursor.execute(sql_query, data)
        connection.commit()


        # sql_query = f"select * from temp_and_time;"
        # cursor.execute(sql_query)

        result = cursor.fetchall()

        # Print the results (optional, you can process them further)
        # for row in result:
        #     print(row)


        cursor.close()
        connection.close()

        time.sleep(1)

edge_engine()
        







