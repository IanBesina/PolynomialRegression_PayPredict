# This Python Program will predict the likelihood of a customer being able to pay his/her accounts, 
# based on existing information on customers in general.
# Using the principles of POLYNOMIAL REGRESSION
# This requires a CSV output of a spreadsheet file on existing customers, 
# with columns for the Customer Name (or codename), Pricing Scheme applied, Payment Terms, Product Purchased, 
# Item Quantity, and Paid on Time 
# (The "Paid on Time" column can be determined by comparing the date of payment vs. the due date of Payment Terms )
# needed to be installed is Python 3, as well as to run the following commands to install Python libraries
# pip install pandas
# pip install numpy
# pip install matplotlib
# pip install scikit-learn
# Also, please feel free to modify the determining factors, to serve your own purpose.
# Happy customizing!


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures

# enter test data in the following order: 
# Customer, PricingScheme,  PaymentTerms, Product, ItemQuantity, PaidOnTime
testCustomer = 10
testPricingScheme = 'Thirty_Days'
testPaymentTerms = 30
testProduct = 241
testItemQuantity = 5



# reviewed Python functions and tried it here
def PaidOnTime(Customer, PricingScheme, PaymentTerms, Product, ItemQuantity):
    # loading dataset
    data = pd.read_csv("/home/whatever/Downloads/CustSales.csv")

    # Convert words to numbers
    dataset.PricingScheme = dataset.PricingScheme.replace(to_replace=['Thirty_Days', 'Forty-five_Days', 'Ninety_Days'], value=[0, 1, 2])
    dataset.PaidOnTime = dataset.PaidOnTime.replace(to_replace=['NO', 'YES'], value=[0, 1])
    y = data.iloc[:, -1].values

    # include polynomial terms up to degree 2 and use it to fit model
    polytwodeg = PolynomialFeatures(degree=2)
    xpoly = polytwodeg.fit_transform(X)
    model = LinearRegression()
    model.fit(xpoly, y)

    # get the test data and fit them to the polynomial
    xtestdata = polytwodeg.fit_transform([[Customer, PricingScheme, PaymentTerms, Product, ItemQuantity]])
    yprediction = model.predict(xtestdata)
    
    # reviewed float formatting and tried it here
    formatted_yprediction = "{:.2f}".format(yprediction[0])
    print("Chances of being paid ('0' for unpaid, '2' for paid early or on time): ", formatted_yprediction)

PaidOnTime(Customer, PricingScheme, PaymentTerms, Product, ItemQuantity)