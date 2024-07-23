from flask import Flask
from bs4 import BeautifulSoup
import requests
import mysql.connector

app = Flask(__name__)

# Function to scrape the data from the website
def scrape_data():
    url = "https://www.maxhealthcare.in/blogs/indian-diet-plan-pregnancy"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.find('table')
    rows = table.find_all('tr')
    
    data = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    return data

# Function to insert scraped data into MySQL database
def insert_into_database(data):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='collegedb'
        )
        cursor = connection.cursor()

        for row in data:
            cursor.execute("INSERT INTO scrapedemo (WeekDays, PreBreakfast, Breakfast, MorningSnack, Lunch, EveningSnack, Dinner) VALUES (%s, %s, %s, %s, %s, %s, %s)", row)
        
        connection.commit()
        print("Data inserted successfully")
        
    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Flask route to scrape data and insert into database
@app.route('/scrape-and-insert')
def scrape_and_insert():
    data = scrape_data()
    insert_into_database(data)
    return "Data scraped and inserted into database successfully"

if __name__ == '__main__':
    app.run(debug=True)