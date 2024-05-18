import mysql.connector
import time


db_host = "sql6.freesqldatabase.com"
db_name = "sql6705813"
db_user = "sql6705813"
db_password = "U1FBjqe7kf"



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


    temp_ = 33434
    time_ = time.time()
    # print(time_)
    data = [temp_, time_]


    # sql_query = f"INSERT INTO temp_and_time (temp_instant, time_instant) VALUES (%s, %s); "  # Replace with your desired table
    # cursor.execute(sql_query, data)
    # connection.commit()


    sql_query = f"select * from temp_and_time;"
    cursor.execute(sql_query)

    result = cursor.fetchall()

    # Print the results (optional, you can process them further)
    # for row in result:
    #     print(row)


    cursor.close()
    connection.close()

    return result

cloud_engine()






