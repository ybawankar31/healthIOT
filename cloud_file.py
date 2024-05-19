import mysql.connector
import time
from sensor_code import sensor_data_queue

db_host = "sql12.freesqldatabase.com"
db_name = "sql12707409"
db_user = "sql12707409"
db_password = "RGDhTdT1Iz"



# Connect to the database
def cloud_engine():
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
    # print(time_)
    data = [sensor_data_queue.g, time_]


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

    return result

cloud_engine()






