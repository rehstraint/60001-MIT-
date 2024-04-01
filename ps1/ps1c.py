# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:32:40 2024

@author: korea
"""

total_cost = 1000000                                                                                        #total cost of home
portion_down_payment = 0.25                                                                                 #percentage of down payment
down_payment = total_cost * portion_down_payment                                                            #formula to get down payment
semi_annual_raise = .07                                                                                     #perctange of annual raises
annual_return = 0.04                                                                                        #percentage of annual return

starting_annual_salary = float(input('Enter your starting annual salary: '))                                #asks for starting annual salary input from user

one_hundred_dollars_as_epsilon = 100                                                                        #round off error 
steps_in_bisection_search = 0                                                                               #starting @ 0 allows to us to get most accurate answer
possible_to_pay_in_three_years = True                                                                       #parameters given by instructor 
max_portion_saved_as_integer = 10000                                                                        #maximum number given
min_portion_saved_as_integer = 0                                                                            #minimum number given
best_portion_saved_as_integer = max_portion_saved_as_integer                                                #gets maximum number to get best results

while True:
    steps_in_bisection_search += 1                                                                          #increase search by 1 to get accurate results
    annual_salary = starting_annual_salary                                                                  #simplifies term for easier readability/function
    best_portion_saved = best_portion_saved_as_integer / 10000                                              #simplifies term for easier readability/function
    monthly_savings = (annual_salary / 12) * best_portion_saved                                             #forumla to get monthly savings 
    
    current_savings = 0.0                                                                                   #starts @ 0 to assume you have no savings
    number_of_months = 0                                                                                    #starts @ 0 so you can see how many months it takes
    while number_of_months <= 36:                                                                           #while loop to see if you can get within 3 years and calculates the best savings rate
        current_savings += monthly_savings + ((current_savings * annual_return) / 12)
        number_of_months += 1
            
        if number_of_months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_savings = (annual_salary / 12) * best_portion_saved            
    
    if abs(current_savings - down_payment) <= one_hundred_dollars_as_epsilon:
        break
    
    if current_savings > down_payment:                                                                      #if loop to see if current savings is greater than the down payment to print a error to user
        max_portion_saved_as_integer = best_portion_saved_as_integer
    else:
        min_portion_saved_as_integer = best_portion_saved_as_integer
        
    if min_portion_saved_as_integer >= max_portion_saved_as_integer:
        possible_to_pay_in_three_years = False
        break
        
    best_portion_saved_as_integer = (max_portion_saved_as_integer + min_portion_saved_as_integer) // 2 
    

if possible_to_pay_in_three_years:                                                                          #if loop to print both outcomes
    print('Best savings rate: {}'.format(best_portion_saved))
    print('Steps in bisection search: {}'.format(steps_in_bisection_search))
else:
    print('It is not possible to pay the down payment in three years.')