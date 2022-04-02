from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.
def driverhistory(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM userInfo WHERE email = %s", [request.POST['email']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO userInfo VALUES (%s, %s, %s, %s)"
                        , [request.POST['email'], request.POST['firstName'], request.POST['lastName'],
                           request.POST['username']  ])
                return redirect('index')    
            else:
                status = 'Customer with ID %s already exists' % (request.POST['email'])


    context['status'] = status
 
    return render(request, "app/driverhistory.html", context)

def driverinterface(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM userInfo WHERE email = %s", [request.POST['email']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO userInfo VALUES (%s, %s, %s, %s)"
                        , [request.POST['email'], request.POST['firstName'], request.POST['lastName'],
                           request.POST['username']  ])
                return redirect('index')    
            else:
                status = 'Customer with ID %s already exists' % (request.POST['email'])


    context['status'] = status
 
    return render(request, "app/driverinterface.html", context)

def driverlogin(request):
    """Shows the main page"""
    context = {}
    status = ''
    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM userInfo WHERE email = %s", [request.POST['email']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO userInfo VALUES (%s, %s, %s, %s)"
                        , [request.POST['email'], request.POST['firstName'], request.POST['lastName'],
                           request.POST['username']  ])
                return redirect('driverinterface')    
            else:
                status = 'Customer with ID %s already exists' % (request.POST['email'])
   
    return render(request, "app/driverlogin.html", context)    
    
def homepage(request):
    """Shows the main page"""
    context = {}
    status = ''
    context['status'] = status
 

    return render(request,"app/homepage.html",context)

def signup(request):
    """Shows the main page"""
    context = {}
    status = ''
    context['status'] = status
 

    return render(request,"app/signup.html",context)

def index(request):
    """Shows the main page"""

    ## Delete customer
    if request.POST:
        if request.POST['action'] == 'delete':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM userInfo WHERE email = %s", [request.POST['email']])

    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM userInfo ORDER BY email")
        userInfo = cursor.fetchall()

    result_dict = {'records': userInfo}

    return render(request,'app/index.html',result_dict)

# Create your views here.
def view(request, email):
    """Shows the main page"""
    
    ## Use raw query to get a customer
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM userInfo WHERE email = %s", [email])
        customer = cursor.fetchone()
    result_dict = {'userInfo': customer}

    return render(request,'app/view.html',result_dict)

# Create your views here.
def add(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM userInfo WHERE email = %s", [request.POST['email']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO userInfo VALUES (%s, %s, %s, %s)"
                        , [request.POST['email'], request.POST['firstName'], request.POST['lastName'],
                           request.POST['username']  ])
                return redirect('index')    
            else:
                status = 'Customer with ID %s already exists' % (request.POST['email'])


    context['status'] = status
 
    return render(request, "app/add.html", context)

# Create your views here.
def edit(request, email):
    """Shows the main page"""

    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM userInfo WHERE email = %s", [email])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE userInfo SET email = %s, firstName = %s, lastName = %s, username = %s"
                    , [request.POST['email'], request.POST['firstName'], request.POST['lastName'],
                        request.POST['username'], email ])
            status = 'Customer edited successfully!'
            cursor.execute("SELECT * FROM userInfo WHERE email = %s", [email])
            obj = cursor.fetchone()


    context["obj"] = obj
    context["status"] = status
 
    return render(request, "app/edit.html", context)
