from flask import Flask, render_template, url_for, request, send_file
import mysql.connector
import io

app = Flask(__name__)

# Function to retrieve data from the database
def get_data_from_database():
    data = []
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='collegedb'
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM scrapedemo")
        data = cursor.fetchall()
        
    except mysql.connector.Error as error:
        print("Error retrieving data from MySQL table:", error)
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    return data

# Function to retrieve PDF data from MySQL database
def get_pdf_data_from_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='collegedb' 
        )
        cursor = connection.cursor()

        # Select PDF data from the database table
        cursor.execute("SELECT file_data FROM pdf_files WHERE id = 1")
        pdf_data = cursor.fetchone()[0]  # There's only one row for the PDF file

        return pdf_data
        
    except mysql.connector.Error as error:
        print("Error retrieving PDF data from MySQL database:", error)
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Route to serve the PDF file
@app.route('/download_pdf', methods=['GET'])
def download_pdf():
    if request.method == 'GET':
        # Retrieve PDF data from the database
        pdf_data = get_pdf_data_from_database()
        if pdf_data:
            # Serve the PDF file as a response
            return send_file(
                io.BytesIO(pdf_data),
                mimetype='application/pdf',
                as_attachment=True,
                download_name='Govt_Schemes.pdf'
            )
        else:
            return 'PDF not found'
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dietplanner.html')
def dietplanner():
    data = get_data_from_database()
    return render_template('dietplanner.html', data = data)

@app.route('/telemedicine.html')
def telemedicine():
    return render_template('telemedicine.html')

if __name__ == '__main__':
    app.run(debug=True)