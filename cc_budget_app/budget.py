class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
    
    def __str__(self):
        # title line string: 30 chars
        name_length = len(self.category)
        n = (30 - name_length) // 2
        
        # formatting asterisks for odd vs even number of characters
        if name_length % 2 != 0:
            title_string = '{0}{1}{2}'.format(n * '*', self.category, (n + 1) * '*')
        else:
            title_string = '{0}{1}{2}'.format(n * '*', self.category, n * '*')
    
        # ledger lines
        ledger_string = ''
        for transaction in self.ledger:
            description = transaction['description']
            if len(description) > 23:
                description = description[0:23]
            description = description.ljust(23)
            
            amount = '{:.2f}'.format(transaction['amount'])
            if len(amount) > 7:
                amount = amount[0:7]
            amount = amount.rjust(7)
            
            # adding new line if it's not the last transaction
            if transaction != self.ledger[-1]:
                ledger_string += description + amount + '\n'
            else:
                ledger_string += description + amount
        
        #total line
        total_line = 'Total: {0}'.format(self.get_balance())
        
        return title_string + '\n' + ledger_string + '\n' + total_line
        
    def get_balance(self) -> float:
        total = 0
        if self.ledger != []:
            for transaction in self.ledger:
                total += transaction['amount']
        return total
    
    def deposit(self, amount: float, description: str=''):
        """
        Accepts an amount and (optional) description. 
        The method should append an object to the
        ledger list in the form of {"amount": amount,
        "description": description}.
        """
        self.ledger.append({'amount' : amount, 'description' : description})
    
    def check_funds(self, amount: float):
        """
        Method that accepts an amount as an argument.
        It returns False if the amount is greater than the
        balance of the budget category and returns True
        otherwise. This method should be used by both the
        withdraw method and transfer method.
        """
        total = self.get_balance()
        enough = True
        if amount > total:
            enough = False
        return enough
        
    def withdraw(self, amount: float, description: str=''):
        """
        Similar to the deposit method, but the amount
        passed in should be stored in the ledger as a 
        negative number. If there are not enough funds, 
        nothing should be added to the ledger. This method
        should return True if the withdrawal took place,
        and False otherwise.
        """
        if self.check_funds(amount) == False:
            enough = False
        else:
            amount *= -1
            self.ledger.append({'amount' : amount, 'description' : description})
            enough = True
        return enough

    def transfer(self, amount: float, category):
        """
        Method that accepts an amount and another budget
        category as arguments. The method should add a
        withdrawal with the amount and then add a deposit
        to the other budget category with the amount. If
        there are not enough funds, nothing should be added to
        either ledgers. This method should return True if
        the transfer took place, and False otherwise.
        """
        if self.check_funds(amount) == False:
            transfer_occurred = False
        else:
            self.withdraw(amount, 'Transfer to {0}'.format(category.category))
            category.deposit(amount, 'Transfer from {0}'.format(self.category))
            transfer_occurred = True
        return transfer_occurred

def create_spend_chart(categories):
    # creating list of spent amounts per category
    spent_amounts = []
    descriptions = []
    for category in categories:
        descriptions.append(category.category)
        spent = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                spent += abs(transaction['amount'])
        spent_amounts.append(round(spent, 2))            
    total_spent = round(sum(spent_amounts), 2)

    # calculating percentages of total & rounding down to nearest 10
    spent_amounts = [round((x / total_spent) * 100, 2)for x in spent_amounts]
    spent_amounts = [int((x // 10) * 10) for x in spent_amounts]

    # spend chart creation
    header = 'Percentage spent by category\n'
    graph = ''
    for value in reversed(range(0, 101, 10)):
        graph += str(value).rjust(3) + '|'
        for percent in spent_amounts:
            if percent >= value:
                graph += " o "
            else:
                graph += "   "
        graph += " \n"
    dashes = (' ' * 4) + ('-' * ((len(categories) * 3) + 1)) + '\n'
    max_length = len(max(descriptions, key = len))
    
    footer = ' ' * 4
    for i in range(max_length):
        for name in descriptions:
            if i < len(name):
                footer += ' ' + name[i] + ' '
            else:
                footer += ' ' * 3
        footer += ' \n' + (' ' * 4)
    remove = "\n    "
    footer = footer[:-len(remove)]  
    spend_chart = header + graph + dashes + footer
    print(spend_chart)