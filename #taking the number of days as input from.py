#taking the number of days as input from the user
days=int(input("Enter the number of days: "))

#taking a variable named "penny" and initialising it with 1
penny=1

#taking a variable named "dollar" and initialising it with 0.01
dollar=0.01

#taking a variable named "total" to calculate the total pay
total = 0

#using for loop
for day in range(1, days+1):
  
    #calculating the total
    total += dollar
  
    #printing the pay per each day
    print("Day number : {} Salary in pennies : {} Salary in dollars : $ {}".format(day, penny, dollar))
  
    #calculating the penny per day
    penny *= 2
  
    #calculating the penny amount in dollars
    dollar=penny*0.01
  
#printing the total pay earned
print("Total pay earned: $ %.2f"%total)
