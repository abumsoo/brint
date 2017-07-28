# Turn all expenses and income into daily terms
# in order to get a daily budget
allowance = 1000.00 / 30
wage = 12.00
hours_fortnight = 20
tax_rate = 0.11
save_rate = 0.15

expenses = {
  "rent" => 745.00,
  "internet" => 38.00,
  "energy" => 30.00,
  "groceries" => 200.00,
  "phone" => 30.00,
}

expenses.each do |key, value|
  expenses[key] = value / 30
end

revenue = wage * hours_fortnight
tax = revenue * tax_rate
saving = (revenue - tax) * save_rate
fortnight_income = revenue - tax - saving
daily_income = fortnight_income / 14

profit = allowance + daily_income - expenses.values.sum
puts "Daily Revenue: #{(allowance + daily_income).round(2)}"
puts "Leftover: #{profit.round(2)}"

puts daily_income.round(3)
