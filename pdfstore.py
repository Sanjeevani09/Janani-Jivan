import mysql.connector

# Open the PDF file in binary mode
with open('E:/sem2/Project_JananiJivan/JananiJivan/static/Govt. Schemes.pdf', 'rb') as file:
    # Read the binary data from the file
    pdf_data = file.read()

# Encode the binary data as Base64
# base64_data = base64.b64encode(pdf_data)

# Decode the Base64 data to a string (optional)
# base64_string = base64_data.decode('utf-8')

# print(base64_string)

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='collegedb'
)

# Insert the PDF data into the database using parameterized query
try:
    cursor = connection.cursor()

    # Insert PDF data into the database table
    cursor.execute("INSERT INTO pdf_files (id, file_name, file_data) VALUES (%s, %s, %s)", ('1','Govt Schemes.pdf', pdf_data)) 
    
    connection.commit()
    print("PDF inserted into database successfully")
    
except mysql.connector.Error as error:
    print("Error inserting PDF into MySQL database:", error)
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()