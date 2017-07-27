#!/usr/local/bin/ruby24

allowance_month = 1000.00
wage = 12.00
hours_fortnight = 20
tax_rate = 0.11
save_rate = 0.15

revenue = wage * hours_fortnight
tax = revenue * tax_rate
saving = (revenue - tax) * save_rate
fortnight_income = revenue - tax - saving
daily_income = fortnight_income / 14

puts daily_income
