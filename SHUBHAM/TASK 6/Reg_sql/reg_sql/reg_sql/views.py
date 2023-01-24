# views.py
from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

def register(request):
    if request.method == 'POST':
        # Get the form data
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        password = request.POST.get('password')

        # Connect to the database
        cnx = mysql.connector.connect(user='root', password='123', host='3.71.188.197', database='rishabh')
        cursor = cnx.cursor()

        # Insert the data into the database
        cursor.execute("INSERT INTO rishabh (fname, lname, email, dob, gender, address, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (fname, lname, email, dob, gender, address, password))

        # Close the connection
        cnx.commit()
        cursor.close()
        cnx.close()

        return HttpResponse('User registered successfully!')

    return render(request, 'register.html')
    