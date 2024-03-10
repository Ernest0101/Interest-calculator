import math

'''
1. The user will be asked to input if they want to calculate interest earnt on investment or home loan repayments on a bond
2. If they pick investment they will be asked to input the details of the investment
3. The user will now select if the investment has compound interest or simple interest set upon it
4 If it simple this will be calculated and presented
5. however if it is compound this will be calculated and isplayed
6. if it is a bond it will ask a different set of questions relating to this
7.then it will display the amount of bond repayments the user will have to pay

'''

type_of_investment = input(''' 

Investment - to calculate the amount the interest you' ll earn on your investment.
Bond - to calculate the amount you'll have to pay on your home loan.

Enter (Investment), or (Bond) :
''').capitalize()

inv_type_1 = "Investment".capitalize()
inv_type_2 = "Bond".capitalize()

interest_type1 = "simple".capitalize()
interest_type2 = " compound".capitalize()


if type_of_investment == inv_type_1:

    # variables used to calculate investment
    funds = float(input("How much money are you depositing? "))
    interest_rate = float(input("Enter your interest rate : "))
    length_invest = float(input("How many years do you plan to invest? "))

    interest = input(''' 
    Will the interest applied be Compound or Simple?
    Enter 'simple' or 'compound' interest: ''').capitalize()

    if interest == interest_type1:
        #variables used to calculate simple interest
        int_percen = interest_rate / 100
        simple_interest_calc = funds * (1 + int_percen * length_invest)
        simple_interest_calc_rounded = round(simple_interest_calc,2)
        interest_gain = (funds * int_percen) * length_invest
        interest_gain_rounded = round(interest_gain,2)
        print(f'''
        You will have £{simple_interest_calc_rounded} after your investment.
        You accrued £{interest_gain_rounded} in interest.
        ''')

    else:
        #variables used to calculate compound interest
        int_percen = interest_rate / 100
        compound_interest_calc = funds*(1+int_percen)**length_invest
        inter_rest_accrued = compound_interest_calc - funds
        rounded_compound = round(compound_interest_calc,2)
        rounded_interest_accrued = round(inter_rest_accrued,2)
        print(f'''
        You will have £{rounded_compound} after your initial investment.
        You have earned £{rounded_interest_accrued} in interest.
        ''')

elif type_of_investment == inv_type_2:
    #variables used to calculate repayments
    house_value = float(input("What is the present value of the house? "))
    repay_time = float(input("How many months do u plan to repay the bond? "))
    interest_r = float(input("What is your interest rate? "))
    inter_r_percen = interest_r / 100
    monthly_interest_rate = inter_r_percen / 12
    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-1 * repay_time))
    repay_rounded = round(repayment,2)
    print(f" You will have to pay  £{repay_rounded} per month. ")






