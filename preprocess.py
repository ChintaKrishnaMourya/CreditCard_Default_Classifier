from utils.logs import log_message
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from collections import Counter
from sklearn.preprocessing import StandardScaler
import pickle

cleanpath = "./Logs/cleaning.log"
log_message("Data Cleaning and Preprocessing has started", cleanpath )

df = pd.read_csv(r".\Data\Raw_data\UCI_Credit_Card.csv")


try:
    df.drop("ID", axis=1, inplace =True)
    log_message("ID column has dropper", cleanpath)
    df.rename(columns={'PAY_0': 'PAY_1', 'default.payment.next.month':'DEFAULT'},inplace=True)
    log_message("PAY_0 and default.payment.next.month are renamed to PAY_1 and DEFAULT", cleanpath)
    df.drop_duplicates(inplace=True)   #Dropped Duplicates
    log_message("Duplicates removed", cleanpath)
    df["EDUCATION"].replace([0,5,6],4, inplace=True)
    df["MARRIAGE"].replace(0,3, inplace=True)
    log_message("Unspecified values in education and marriage have been transformed", cleanpath)
    for i in range(1,7):
        df[f"PAY_{i}"].replace([0,-2],-1, inplace=True)
    log_message("Unspecified values in PAY_1,2,3,4,5,6 have been transformed", cleanpath)

except Exception as e:
    log_message(f"Some error has occured in cleaning part : {e}")

try:
    log_message("Divided dataset to X and y. X==> Features, y==> Target", cleanpath)
    X= df.drop("DEFAULT",axis=1)
    y=df["DEFAULT"]
    log_message("Using SMOTE to balance the dataset", cleanpath)
    log_message(f'Original dataset shape is {Counter(y)}',cleanpath)
    sm= SMOTE()
    X_res,y_res = sm.fit_resample(X,y)

    log_message(f'Resampled dataset shape is {Counter(y_res)}', cleanpath)

except Exception as e:
    log_message(f"Some error has occured in SMOTE part : {e}", cleanpath)

try:
    log_message("Scaling has started", cleanpath)
    scale = StandardScaler()
    X_scaled = scale.fit_transform(X_res)
    log_message("Scaled the data as X_scaled", cleanpath)
except Exception as e:
    log_message(f"Some error has occured in Scaling part: {e}", cleanpath)

try:
    log_message("Saving the SCALE object. Will use this Scale object for scaling the user_input later", cleanpath)
# save the scaler object to a file
    path = '.\Models\scaler.pkl'
    with open(path, 'wb') as f:
        pickle.dump(scale, f)
    log_message("Saved the scale object in Models\scaler.pkl ", cleanpath)

except Exception as e:
    log_message(f"Some error in saving the model : {e}", cleanpath)

try:
    log_message("Saving the cleaned Data", cleanpath)
    X_cleaned = pd.DataFrame(X_scaled, columns= X.columns)
    y_cleaned = pd.DataFrame(y_res, columns=["DEFAULT"])

    cleaned_data= pd.concat([X_cleaned,y_cleaned],axis=1,ignore_index=False)

    # save the cleaned_data DataFrame to a CSV file in the custom folder
    cleaned_data.to_csv('.\Data\CleanData.csv', index=False)
    log_message("Saved the cleaned data in Data\cleanedData\CleanData.csv", cleanpath)
except Exception as e:
    log_message(f"Some error in saving the cleaned Data : {e}", cleanpath)