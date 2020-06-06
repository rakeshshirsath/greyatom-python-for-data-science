# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank = pd.read_csv(path)

#Code starts here
categorical_var = bank.select_dtypes(include='object')
print(categorical_var.shape)
numerical_var = bank.select_dtypes(include='number')
print(numerical_var.shape)

banks = bank.drop('Loan_ID',axis=1)
print(banks.shape)

print("number of null values are",banks.isnull().sum().values.sum())

bank_mode = banks.mode()
banks.fillna(bank_mode,inplace=True)
print("number of null values are",banks.isnull().sum().values.sum())

avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)

loan_approved_se = len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
percentage_se = 100 * loan_approved_se / 614
percentage_nse = 100 * loan_approved_nse / 614
print(percentage_se)
print(percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term = loan_term[loan_term>=25].count()
print("Big loan term is ",big_loan_term)

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.agg([np.mean])
print(mean_values)





