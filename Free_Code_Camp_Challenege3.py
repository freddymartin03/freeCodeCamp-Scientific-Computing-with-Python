class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total = total + item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = "{:.2f}".format(item["amount"]).rjust(7)
            items += f"{description}{amount}\n"
            total += item["amount"]
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    total_withdrawals = 0
    category_names = []
    spent_percentages = []

    for category in categories:
        withdrawals = 0
        for item in category.ledger:
            if item["amount"] < 0:
                withdrawals = withdrawals - item["amount"]
        total_withdrawals = total_withdrawals + withdrawals
        category_names.append(category.name)
        spent_percentages.append(withdrawals)

    for i in range(len(spent_percentages)):
        spent_percentages[i] = int((spent_percentages[i] / total_withdrawals) * 10) * 10

    chart = "Percentage spent by category\n"
    for percentage in range(100, -10, -10):
        chart += str(percentage).rjust(3) + "| "
        for spent_percentage in spent_percentages:
            if spent_percentage >= percentage:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max([len(name) for name in category_names])
    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i != max_name_length - 1:
            chart += "\n"
    create_spend_chart = chart

    return create_spend_chart
