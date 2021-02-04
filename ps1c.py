'''
To simplify things, assume:

1. Your semi­annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%)  
3. The down payment is 0.25 (25%) of the cost of the house 
4. The cost of the house that you are saving for is $1M.
You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
the required down payment.

'''

#Getting inputs
annual_salary = float(input("Enter the starting salary: "))
annual_salary_original = annual_salary
#initalizing variables
semi_annual_raise = .07
r = .04
total_cost = 1000000
portion_saved = 1
i=0
max = 1
min = 0

def initialise():
    global months
    months = 0
    global portion_down_payment
    portion_down_payment = .25*total_cost
    global current_savings
    current_savings = 0
    global annual_salary
    annual_salary = annual_salary_original

initialise()
if annual_salary*3<portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
    raise SystemExit
    
while True:
    current_savings *= (1+r/12)
    current_savings += (annual_salary/12)*portion_saved
    months += 1
    if months % 6 == 0:
        annual_salary *= (1+semi_annual_raise)
    if abs(current_savings - portion_down_payment) <=100 and months == 36:
        break
    elif months == 36: 
        if (current_savings - portion_down_payment) < 0: #saving less, increase rate
            min = portion_saved
            portion_saved += (max-min)/2
            portion_saved = round(portion_saved ,5)
            i+=1
            initialise()
        else: #saving too much, reduce rate
            max = portion_saved
            portion_saved -= (max-min)/2
            portion_saved = round(portion_saved,5)
            i+=1
            initialise()

print("Best savings rate: ",round(portion_saved,4))
print("Steps in bisection search: ",i)
