import mysql.connector
import time
import sensor_code
import importlib
from queue import Queue

db_host = "sql12.freesqldatabase.com"
db_name = "sql12707409"
db_user = "sql12707409"
db_password = "RGDhTdT1Iz"



# Connect to the database
def cloud_engine():
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
        importlib.reload(sensor_code)
        data_to_push = sensor_code.sensor_data_queue1.get(timeout= 3)[0]
        time_to_push = sensor_code.sensor_data_queue1.get(timeout= 3)[1]
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

        
representation_value_cloud = Queue()

def cloud_to_window():
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

        # data_to_push = sensor_code.sensor_data_queue1.get(timeout= 3)[0]
        # time_to_push = time.time()
        # # print(time_)
        # data = [data_to_push, time_to_push]


        # sql_query = f"INSERT INTO temp_and_time (temp_instant, time_instant) VALUES (%s, %s); "  # Replace with your desired table
        # cursor.execute(sql_query, data)
        # connection.commit()


        sql_query = f"select * from temp_and_time order by temp_instant limit 1;"
        cursor.execute(sql_query)

        result = cursor.fetchall()
        representation_value_cloud.put(result, timeout=3)

        # Print the results (optional, you can process them further)
        # for row in result:
        #     print(row)


        cursor.close()
        connection.close()

        time.sleep(1)

        













