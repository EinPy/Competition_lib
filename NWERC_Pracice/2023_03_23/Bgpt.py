n = int(input()) # number of items
prices = list(map(int, input().split())) # list of prices

prices.sort() # sort the prices in ascending order

total_discount = 0 # initialize the total discount to zero

# calculate the total discount by going to the counter three items at a time
for i in range(n//3):
    total_discount += prices[3*i] # add the discount for the cheapest item
    total_discount += prices[3*i+1] # add the discount for the second cheapest item

# if there are any items left over, add them to the total discount
if n%3 == 1:
    total_discount += prices[-1]
elif n%3 == 2:
    total_discount += prices[-2] + prices[-1]

print(total_discount) # print the maximum discount