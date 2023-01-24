# views.py
from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from django.db import connection

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
        cnx = mysql.connector.connect(user='root', password='123', host='3.75.212.110', database='rishabh')
        cursor = cnx.cursor()

        # Insert the data into the database
        cursor.execute("INSERT INTO rvtable (fname, lname, email, dob, gender, address, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (fname, lname, email, dob, gender, address, password))

        # Close the connection
        cnx.commit()
        cursor.close()
        cnx.close()

        return HttpResponse('User registered successfully!')

    return render(request, 'register.html')
    
def fetch_data(request):
    cursor = connection.cursor()
    cursor.execute('select * from rvtable')
    row=cursor.fetchall()
    return render(request,'fetch_data.html',{'row':list(row)})

def delete(request):
    id = request.GET['id']
    cursor = connection.cursor()
    cursor.execute("delete from rvtable where email = '"+id+"'")
    row = cursor.fetchall()
    msg="the data has been deleted"
    cursor.execute('select * from rvtable')
    row=cursor.fetchall()

    return render(request,'fetch_data.html',{'row':list(row),'message':msg})

def update(request):
   
    fname=request.GET['fname']
    lname=request.GET['lname']
    email=request.GET['email']
    dob=request.GET['dob']
    gender=request.GET['gender']
    address=request.GET['address']
    password=request.GET['password']

    cursor=connection.cursor()
    #update the data
    cursor.execute("update rvtable set fname='"+fname+"',lname='"+lname+"', email='"+email+"', dob='"+dob+"' , gender='"+gender+"',address='"+address+"' , password='"+password+"' where email='"+email+"' ")
    msg="Record updated successfully."
    cursor.execute('select * from rvtable')
    row=cursor.fetchall()
   
    return render(request,'fetch_data.html',{'row':list(row),'message':msg}) 