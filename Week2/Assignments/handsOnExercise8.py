# 8 Tip, Tax, Total

# Create the required variables

BILL_AMOUNT = float (input("Enter the amount for the food: "))    # Will enter the amount of bill prior to tip, and tax
PERCENT_TIP = float (input("Enter the tip(IN DEC) amount: "))     # Will enter tip amount in decimal(in this scenario, it is 18%)
SALES_TAX = .07                                                   # Sales tax is a constant, until changed

# Preform the calculations

TIP_TOTAL = BILL_AMOUNT * PERCENT_TIP                             # TOTAL AMOUNT OF TIP  
TAX_TOTAL = BILL_AMOUNT * SALES_TAX                               # TOTAL AMOUNT OF SALES TAX

TOTAL = BILL_AMOUNT + TIP_TOTAL + TAX_TOTAL                       # COMPLETE TOTAL OF BILL

# Output the results with required formatting

print(f'Bill Amount = ${BILL_AMOUNT:,.2f}')
print(f'Percent Sales Tax = {SALES_TAX:.0%}')
print(f'Total Tax = ${TAX_TOTAL:,.2f}')
print(f'Percent Tip Amount = {PERCENT_TIP:.0%}')
print(f'Total Tip Amount = ${TIP_TOTAL:,.2f}')


print(f'Total Amount = ${TOTAL:,.2f}')







