# Let us say your expense for every month are listed below,
# January = 2200
# February = 2350
# March = 2600
# April = 2130
# May = 2190

# Create a list to store these monthly expenses and using that find out,
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


January = 2200
February = 2350
March = 2600
April = 2130
May = 2190


months = ['January', 'February', 'March', 'April', 'May']
expenses = [2200, 2350, 2600, 2130, 2190]

#! 1. In Feb, how many dollars you spent extra compare to January?
# a = int(input('Enter starting month: '))
# b = int(input('Enter ending month: '))
# diff = 0.00

# for i in range(len(months)):
#     if(a > b):
#         diff = expenses[a-1] - expenses[b-1]
#     else:
#         diff = expenses[b-1] - expenses[a-1]
# print(f"The difference in expense  is: ", diff)


#! 2. Find out your total expense in first quarter (first three months) of the year.
# sum = 0
# for i in range(3):
#     sum += expenses[i]

# print(sum)


#! 3. Find out if you spent exactly 2000 dollars in any month
# month = 0
# for i in range(len(months)):
#     if expenses[i] == 2000:
#         month = i
# if(month == 0):
#     print('No any month found ')
# else:
#     print('Month is :', month)

#! 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
months.append('June')
expenses.append(1980)

#! 5. You returned an item that you bought in a month of April and
#! got a refund of 200$. Make a correction to your monthly expense list
#! based on this

index = str(input('Enter the month: '))
amt = int(input('Enter the amount :'))

for i in range(len(months)):
    if months[i].lower() == index.lower():
        expenses[i] = expenses[i] - amt
print(expenses)
