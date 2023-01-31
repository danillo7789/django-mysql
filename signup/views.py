from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import mysql.connector as sql
# declare firstname, lastname, sex, emailail, password as global variables
firstname = ''
lastname = ''
sex = ''
email = ''
password = ''

def signup(request):
    global firstname, lastname, sex, email, password
    if request.method == 'POST':
        mysql = sql.connect(host='localhost', user='root', passwd='Boltudan@1', database='firstproject')
        cursor = mysql.cursor()
        passedInData = request.POST
        for key, value in passedInData.items():
            if key == 'first_name':
                firstname = value
            if key == 'last_name':
                lastname = value
            if key == 'sex':
                sex = value
            if key == 'email':
                email = value
            if key == 'password':
                password = value

        formValues = "insert into users values('{}', '{}', '{}', '{}', '{}')".format(firstname, lastname, sex, email, password)
        cursor.execute(formValues)
        mysql.commit()

    return render(request, 'signup_page.html')


def home(request):
    return render(request, 'home.html')

# def signup(request):
#     form = UserCreationForm()
#     # if request.user.is_authenticated:
#     #     return redirect('')
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
    
#     return render(request, 'signup_page.html', {'form': form})
