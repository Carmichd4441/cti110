# Calculating profit from sales
# 9/26/2018
# CTI-110 P2T1 - Sales Prediction
# De'Ante Carmichael


# Get the projected total sales.
totalSales = float(input("Enter the projected sales: "))

# Calculate the profit as 23 percent of total sales.
profit = totalSales * .23

# Display the profit.
print ("The profit is $", format(profit, ",.2f"))
