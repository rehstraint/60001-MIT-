# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:55:14 2024

@author: korea
"""
r = 0.04
current_savings = 0.0
number_of_months = 0


annual_salary = float(input('Please enter your Annual Salary: '))
portion_saved = float(input('Please enter the % of your salary to save, as a decimal: '))
monthly_savings = (annual_salary / 12) * portion_saved

total_cost = float(input('The cost of your dream home: '))
portion_down_payment = .25
down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    current_savings += monthly_savings + ((current_savings * r) / 12)
    number_of_months += 1
    
print('Number of months: {}' .format(number_of_months))