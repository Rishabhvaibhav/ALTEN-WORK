from django.shortcuts import render
from django.http import JsonResponse
import mysql.connector

# Create your views here.

def my_api_function(request):
    # Do some processing here

    data = {
    '4661': 'Pritam',
    '4662': 'Shashank',
    '4663': 'Rishabh',
    '4664': 'Aashu',
    '4665': 'Prastuta',
    '4666': 'Triveni',
    } 
    return JsonResponse(data)

def phpmyadmin_data(request):
    # Connect to the database
    mydatabase = mysql.connector.connect(
        user='root',
        password='123', 
        host='3.75.212.110', 
        database='rishabh'
    )

    # Create a cursor object
    cursor = mydatabase.cursor()

    # Execute a SELECT statement to retrieve data from the "mytable" table
    cursor.execute("SELECT * FROM rvtable")

    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Close the cursor and the connection
    cursor.close()
    mydatabase.close()

    # Convert the rows to a list of dictionaries
    data = [dict(zip([key[0] for key in cursor.description], row)) for row in rows]

    # Return the data as a JSON response
    return JsonResponse(data, safe=False)


