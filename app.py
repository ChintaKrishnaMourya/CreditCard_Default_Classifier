from flask import Flask,render_template, request, jsonify
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from utils.logs import log_message
import traceback


app = Flask(__name__)
log_file_path = "./Logs/prediction.log"

try:
    log_message("Running the app for prediction!!\n", log_file_path)

    with open(r"Models\scaler.pkl","rb") as fs:
        scaler = pickle.load(fs)
    log_message("Imported scaler object for scaling the input", log_file_path )  

    with open(r"Models\finalmodel.pkl","rb") as fm:
        model = pickle.load(fm)
    log_message("Imported model for predicting the input", log_file_path)

    @app.route('/', methods=['POST','GET'])
    def predict():
        if request.method=='POST':
            try:
                log_message("Taking the input from user", log_file_path)
                user_input = request.form

                limit_bal = float(user_input['limit_bal'])
                sex = int(user_input['sex'])
                education = int(user_input['education'])
                marriage = int(user_input['marriage'])
                age = int(user_input['age'])
                pay_1 = int(user_input['pay_1'])
                pay_2 = int(user_input['pay_2'])
                pay_3 = int(user_input['pay_3'])
                pay_4 = int(user_input['pay_4'])
                pay_5 = int(user_input['pay_5'])
                pay_6 = int(user_input['pay_6'])
                bill_amt1 = float(user_input['bill_amt1'])
                bill_amt2 = float(user_input['bill_amt2'])
                bill_amt3 = float(user_input['bill_amt3'])
                bill_amt4 = float(user_input['bill_amt4'])
                bill_amt5 = float(user_input['bill_amt5'])
                bill_amt6 = float(user_input['bill_amt6'])
                pay_amt1 = float(user_input['pay_amt1'])
                pay_amt2 = float(user_input['pay_amt2'])
                pay_amt3 = float(user_input['pay_amt3'])
                pay_amt4 = float(user_input['pay_amt4'])
                pay_amt5 = float(user_input['pay_amt5'])
                pay_amt6 = float(user_input['pay_amt6'])

                X = np.array([[limit_bal, sex, education, marriage, age, pay_1, pay_2, pay_3, pay_4, pay_5, pay_6,
                                bill_amt1, bill_amt2, bill_amt3, bill_amt4, bill_amt5, bill_amt6,
                                pay_amt1, pay_amt2, pay_amt3, pay_amt4, pay_amt5, pay_amt6]])
                log_message(f"Input given by user = {X}", log_file_path)

                X_scaled = scaler.transform(X)
                prediction = model.predict(X_scaled)
                log_message(f"Prediction is {prediction}",log_file_path)
                return render_template("Index.html",result=prediction[0])
            except Exception as e:
                log_message(f"An exception occurred: {str(e)}", log_file_path)
                traceback.print_exc()
                return render_template("Index.html",result="Invalid Input!")
        else:
            return render_template('Index.html')

except Exception as e:
    log_message(f"An exception occurred: {str(e)}", log_file_path)
    traceback.print_exc()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)