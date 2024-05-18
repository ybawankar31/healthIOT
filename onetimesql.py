import mysql.connector
import time

# Database connection details
# db_host = "sql6.freesqldatabase.com"
# db_name = "sql6705813"
# db_user = "sql6705813"
# db_password = "U1FBjqe7kf"

db_host = "localhost"
db_name = "healthiot"
db_user = "root"
db_password = "root"

temp_ = 33434

# Connect to the database
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

# Create a cursor object to execute queries
cursor = connection.cursor()

# Define the SQL query to fetch data
for i in range(10):
    time.sleep(1)
    data = (temp_, time.time())
    sql_query = f"INSERT INTO temperature (temp, time_) VALUES (%s, %s); "  # Replace with your desired table

    # Execute the query
    cursor.execute(sql_query, data)

       

# Close the cursor and connection
cursor.close()
connection.close()








#************************************************************************
# import mysql.connector
# import random
# import threading
# import time

# # Database connection details
# db_host = "localhost"
# db_name = "healthiot"
# db_user = "root"
# db_password = "root"

# # Table name
# table_name = "temperature"

# # Function to insert data in a separate thread
# def insert_data(connection, cursor):
#     while True:
#         temp = round(random.uniform(10.0, 30.0), 2)  # Generate random temperature
#         current_time = time.time()  # Get current time
#         data = (temp, current_time)

#         # SQL INSERT statement (prepared statement)
#         sql_insert = f"INSERT INTO {table_name} (temp, time) VALUES (%s, %s)"

#         try:
#             cursor.execute(sql_insert, data)
#             connection.commit()  # Commit changes to the database
#             print(f"Data inserted: Temp = {temp:.2f}, Time = {current_time:.2f}")
#         except mysql.connector.Error as err:
#             print("Failed to insert data:", err)
#         time.sleep(1)  # Sleep for 1 second before next insertion

# # Connect to the database
# try:
#     connection = mysql.connector.connect(
#         host=db_host,
#         database=db_name,
#         user=db_user,
#         password=db_password,
#     )
# except mysql.connector.Error as err:
#     print("Failed to connect:", err)
#     exit()

# # Create a cursor object
# cursor = connection.cursor()

# # Create a thread object for data insertion
# data_thread = threading.Thread(target=insert_data, args=(connection, cursor))
# data_thread.start()  # Start the thread

# # Keep the main thread running (e.g., for your UI)
# # ... your main application logic here ...

# # Close the cursor and connection (when the main thread is done)
# cursor.close()
# connection.close()
