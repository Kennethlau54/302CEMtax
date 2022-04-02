from flask import Flask,request,render_template,flash,redirect,url_for,session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
import unittest

ALLOWED_EXTENSIONS = {}

app = Flask(__name__)
@app.route('/')

@app.route('/single',methods=["GET","POST"])
def single():
    if request.method == "POST":
        try:
            self_income = int(request.values.get('selfincome'))
        except ValueError as err:
            return "please input correct value"
        if self_income == 0:
            return "no need pay"
        if self_income<0:
            return "please give a positive amount"

        if self_income <= 360000:
            selfmpf = int(self_income*0.05)
        else:
            selfmpf = 18000
        selfindiviual = 132000
        self_net_income = self_income -selfmpf- selfindiviual
        self_standard_income = self_income -selfmpf
        if self_net_income <0:
            self_net_income = 0
        elif self_net_income <= 50000:
            self_tax = int(self_net_income*0.02)
        elif self_net_income <=100000:
            self_tax = int(1000 + (self_net_income - 50000)*0.06)
        elif self_net_income <=150000:
            self_tax = int(1000 + 3000 + (self_net_income - 50000 - 50000)*0.10)
        elif self_net_income <=200000:
            self_tax = int(1000 + 3000 + 5000 + (self_net_income - 50000 - 50000 - 50000)*0.14)
        elif self_net_income >200000:
            self_tax = int(1000 + 3000 + 5000 + 7000 + (self_net_income - 50000 - 50000 - 50000 - 50000)*0.17)
        

        self_standard_tax = self_standard_income *0.15

        if self_tax > self_standard_tax:
            Tax_pay = self_standard_tax
        else:
            Tax_pay = self_tax

        return render_template('singleresult.html', self_standard_tax = self_standard_tax, Tax_pay = Tax_pay, self_tax = self_tax)
    return render_template('single.html')


@app.route('/married',methods=["GET", "POST"])
def married():
    if request.method == "POST":
        try:
            wife_income = int(request.values.get('wifeincome'))
        except ValueError as err:
            return "please input correct value in wife"
        if wife_income == 0:
            return "no need pay"
        if wife_income<0:
            return "please give a positive amount in wife"

        if wife_income <= 360000:
            wifempf = int(wife_income*0.05)
        else:
            wifempf = 18000

        selfindiviual = 132000

        wife_net_income = wife_income - wifempf - selfindiviual
        wife_standard_income = wife_income - wifempf
        if wife_net_income <0:
            wife_net_income = 0
        if wife_net_income <= 50000:
            wife_tax = int(wife_net_income*0.02)
        elif wife_net_income <=100000:
            wife_tax = int(1000 + (wife_net_income - 50000)*0.06)
        elif wife_net_income <=150000:
            wife_tax = int(1000 + 3000 + (wife_net_income - 50000 - 50000)*0.10)
        elif wife_net_income <=200000:
            wife_tax = int(1000 + 3000 + 5000 + (wife_net_income - 50000 - 50000 - 50000)*0.14)
        elif wife_net_income >200000:
            wife_tax = int(1000 + 3000 + 5000 + 7000 + (wife_net_income - 50000 - 50000 - 50000 - 50000)*0.17)
            

        wife_standard_tax = wife_standard_income *0.15

        if wife_tax > wife_standard_tax:
            Tax_wife_pay = wife_standard_tax
        else:
            Tax_wife_pay = wife_tax
        
        try:
            husband_income = int(request.values.get('husbandincome'))
        except ValueError as err:
            return "please input correct value in husband"
        if husband_income == 0:
            return "no need pay"
        if husband_income<0:
            return "please give a positive amount in husband"

        if husband_income <= 360000:
            husbandmpf = int(husband_income*0.05)
        else:
            husbandmpf = 18000

        selfindiviual = 132000

        husband_tax = 0

        husband_net_income = husband_income -husbandmpf- selfindiviual
        husband_standard_income = husband_income -husbandmpf
        if husband_net_income <0:
            husband_net_income = 0
        elif husband_net_income <= 50000:
            husband_tax = int(husband_net_income*0.02)
        elif husband_net_income <=100000:
            husband_tax = int(1000 + (husband_net_income - 50000)*0.06)
        elif husband_net_income <=150000:
            husband_tax = int(1000 + 3000 + (husband_net_income - 50000 - 50000)*0.10)
        elif husband_net_income <=200000:
            husband_tax = int(1000 + 3000 + 5000 + (husband_net_income - 50000 - 50000 - 50000)*0.14)
        elif husband_net_income >200000:
            husband_tax = int(1000 + 3000 + 5000 + 7000 + (husband_net_income - 50000 - 50000 - 50000 - 50000)*0.17)
        
        husband_standard_tax = husband_standard_income *0.15

        if husband_tax > husband_standard_tax:
            Tax_husband_pay = husband_standard_tax
        else:
            Tax_husband_pay = husband_tax
        
        total_pay = Tax_wife_pay + Tax_husband_pay
        total_income = wife_income + husband_income

        totalmpf = wifempf + husbandmpf


        totalindiviual = 264000

        total_net_income = total_income -totalmpf- totalindiviual
        total_standard_income = total_income -totalmpf
        if total_net_income <0:
            total_net_income = 0
        elif total_net_income <= 50000:
            total_tax = int(total_net_income*0.02)
        elif total_net_income <=100000:
            total_tax = int(1000 + (total_net_income - 50000)*0.06)
        elif total_net_income <=150000:
            total_tax = int(1000 + 3000 + (total_net_income - 50000 - 50000)*0.10)
        elif total_net_income <=200000:
            total_tax = int(1000 + 3000 + 5000 + (total_net_income - 50000 - 50000 - 50000)*0.14)
        elif total_net_income >200000:
            total_tax = int(1000 + 3000 + 5000 + 7000 + (total_net_income - 50000 - 50000 - 50000 - 50000)*0.17)
        
        total_standard_tax = total_standard_income *0.15

        if total_tax > total_standard_tax:
            Tax_total_pay = total_standard_tax
        else:
            Tax_total_pay = total_tax
        
        if Tax_total_pay > total_pay:
            Lowest_tax = total_pay
        else:
            Lowest_tax = Tax_total_pay
        
        return render_template('marriedresult.html', husband_standard_tax = husband_standard_tax, wife_standard_tax = wife_standard_tax, 
        Tax_husband_pay = Tax_husband_pay, Tax_wife_pay = Tax_wife_pay, husband_tax = husband_tax, wife_tax = wife_tax, total_pay = total_pay,
         total_tax = total_tax, Tax_total_pay = Tax_total_pay, total_standard_tax = total_standard_tax, Lowest_tax = Lowest_tax)
    return render_template('302tax.html')

if __name__ == '__main__':
    app.run(debug=True)
  
