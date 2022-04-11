import re


class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0.0

    def __str__(self):
        # Title
        self.total = 0
        self.title = '*' * (int(30 - len(self.category)) // 2) + self.category + '*' * (
                int(30 - len(self.category)) // 2) + '\n'
        self.display = self.title
        for specs in self.ledger:
            self.catamount = re.split(r'\s+|[,":]\s*', str(specs))
            self.space = ' ' * (
                        30 - len(specs["description"][0:23]) - len(str('{0:.2f}'.format(float(specs["amount"])))))
            self.line = f'{specs["description"][0:23]}{self.space}{float(specs["amount"]):.2f}'
            self.display += self.line + '\n'
            self.total += float(self.catamount[1])
        self.display += f"Total: {self.total:.2f}"

        return self.display

    def deposit(self, amount: float, description=''):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += self.amount

    def withdraw(self, negamount: float, negdescription=''):
        self.negamount = negamount
        self.negdescription = negdescription
        self.spent = 0
        if self.check_funds(self.negamount):
            self.ledger.append({'amount': -negamount, 'description': negdescription})
            self.balance -= self.negamount
            self.spent += self.negamount
            return True
        else:
            return False

    def get_balance(self):

        return self.balance

    def transfer(self, transfer_amount: int, budget_other_category):
        self.transfer_amount = transfer_amount
        self.budget_other_category = budget_other_category
        if self.check_funds(self.transfer_amount):
            self.withdraw(self.transfer_amount, f'Transfer to {budget_other_category.category}')
            budget_other_category.deposit(self.transfer_amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        self.check_fund = amount
        if self.balance >= self.check_fund:
            return True
        else:
            return False


def create_spend_chart(category_list):
    tot_spent = 0
    avg_spent = []
    for category in category_list: tot_spent += category.spent;
    for category in category_list:
        avg_spent.append(int((category.spent / tot_spent) * 100))

    title_display = 'Percentage spent by category\n'
    tiret = '    ' + '-' * (1 + 3 * len(category_list)) + '\n'

    # Writing printing

    letters = []
    lines = []
    space = '     '
    category_display = ''
    maxl = None

    for category in category_list:
        letters.append(list(category.category))

    for letter in letters:
        if maxl is None or maxl < len(letter):
            maxl = len(letter)

    for _ in range(maxl):
        line = ''
        for i in range(len(letters)):
            try:
                line += letters[i][_] + '  '
            except:
                line += '   '
        lines.append(line)

    for i in range(len(lines)):
        if i==(len(lines)-1):
          category_display += space + lines[i] 
        else:
          category_display += space + lines[i] + '\n'

    # Showing percent

    lines_percent = []
    o_display = ''

    for i in range(10, -1, -1):
        line_percent = ''
        for _ in range(len(letters)):
            n = _
            if avg_spent[n] >= i * 10:
                if _ == 0:
                    if len(str(i * 10)) != 3:
                        line_percent += ' ' * (3 - len(str(i * 10))) + str(i * 10) + '| o  '
                    else:
                        line_percent += str(i * 10) + '| o  '
                else:
                    line_percent += 'o  '

            else:
                if _ == 0:
                    if len(str(i * 10)) != 3:
                        line_percent += ' ' * (3 - len(str(i * 10))) + str(i * 10) + '|    '
                    else:
                        line_percent += str(i * 10) + '|    '
                else:
                    line_percent += '   '

        lines_percent.append(line_percent)

    for i in range(len(lines_percent)):
        o_display += lines_percent[i] + '\n'

    graph = ''
    graph += title_display + o_display + tiret + category_display

    return graph

    
