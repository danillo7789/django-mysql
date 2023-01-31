from django.shortcuts import render, redirect
import mysql.connector as sql

email = ''
password = ''

def loginPage(request):
    global email, password
    if request.method == 'POST':
        mysql = sql.connect(host='localhost', user='root', passwd='Boltudan@1', database='firstproject')
        cursor = mysql.cursor()
        passedInData = request.POST
        for key, value in passedInData.items():
            if key == 'email':
                email = value
            if key == 'password':
                password = value

        loginValues = "select * from users where email = '{}' and password = '{}' ".format(email, password)
        cursor.execute(loginValues)
        tee = tuple(cursor.fetchall())
        if tee == ():
            return render(request, 'error.html')
        else:
            # return render(request, 'welcome.html')
            return redirect('welcome')

    return render(request, 'login_page.html')



def welcome(request):
    return render(request, 'welcome.html')