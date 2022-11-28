from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import mysql.connector as sql

fn = ''
ln = ''
em = ''
ne = ''
mes=''


# Create your views here.
def contact(request):
    global fn, ln, em,ne,mes
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="pass", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "fname":
                fn = value
            if key == "lname":
                ln = value
            if key == "email":
                em = value
            if key == "need":
                ne = value
            if key == "mes":
                mes = value

        c = "insert into contact Values('{}','{}','{}','{}','{}')".format(fn, ln, em,ne,mes)
        cursor.execute(c)
        m.commit()

    return render(request, 'contact.html')
