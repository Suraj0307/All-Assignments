from flask import Flask,request,jsonify,render_template
import pickle
app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home_page():
    prediction=None
    mp = pickle.load(open('model',"rb"))
    if request.method=='POST':
        user_input1=int(request.form.get('input1'))
        user_input2 = int(request.form.get('input2'))
        user_input3 = float(request.form.get('input3'))
        user_input4 = float(request.form.get('input4'))

        print(user_input1,user_input2)
        prediction=mp.predict([[user_input1,user_input2
                                ,user_input3,user_input4]])
    return render_template("index.html",prediction=prediction)







# @app.route('/via_postman',methods=['POST'])
# def math_operation_via_postman():
#     if (request.method=='POST'):
#         operation=request.json["operation"]
#         num1=int(request.json['num1'])
#         num2=int(request.json['num2'])
#         if (operation=='add'):
#              r=num1+num2
#             result ='The sum of '+str(num1) +'and'+str(num2) +"is "+str(r)
#
#
#         if (operation=='subtract'):
#             r=num1-num2
#             result ='The subtaction of '+str(num1) +'and'+str(num2) +"is "+str(r)
#
#         if (operation=='multiply'):
#             r=num1*num2
#             result ='The multiplication of '+str(num1) +'and'+str(num2) +"is "+str(r)
#
#         if (operation=='divide'):
#             r=num1/num2
#             result ='The Division of '+str(num1) +'and'+str(num2) +"is "+str(r)
#         return jsonify(result)
#
#
# @app.route('/via_postman',methods=['POST'])
# def math_operation_via_postman():
#     if (request.method=='POST'):
#         operation = request.json["operation"]
#         num1 = int(request.json['num1'])
#         num2 = int(request.json['num2'])
#         if (operation == 'add'):
#             r = num1 + num2
#         result = 'The sum of ' + str(num1) + 'and' + str(num2) + "is " + str(r)
#
#         if (operation == 'subtract'):
#             r = num1 - num2
#             result = 'The subtaction of ' + str(num1) + 'and' + str(num2) + "is " + str(r)
#
#         if (operation == 'multiply'):
#             r = num1 * num2
#             result = 'The multiplication of ' + str(num1) + 'and' + str(num2) + "is " + str(r)
#
#         if (operation == 'divide'):
#             r = num1 / num2
#             result = 'The Division of ' + str(num1) + 'and' + str(num2) + "is " + str(r)
#         return jsonify(result)
#

if __name__=='__main__':
    app.run(debug=True)