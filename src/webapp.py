from flask import Flask, render_template
from flask import *
from broken_calc import *
app = Flask(__name__)

result=0
flag=-1

@app.route('/',methods = ['POST', 'GET'])
def calc():
   global flag
   flag=flag+1
   try:
     var1 = request.form['var1']
     var2 = request.form['var2']
     calc_option = request.form['calc_option']
     if calc_option=='add':
         result=broken_add(int(var1),int(var2))
   except Exception,e:
     result=str(e)
   if flag==0:
       result=0
     
   return render_template('web_app.html',result=result)

if __name__ == '__main__':
   app.run()
