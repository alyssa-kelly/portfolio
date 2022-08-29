import budget
from budget import create_spend_chart

food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
business = budget.Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)



create_spend_chart([business, food, entertainment])
