class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.category.center(30, "*") + "\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = []

    # Calculate total spending
    total_spending = sum(category.get_balance() - category.ledger[0]["amount"] for category in categories)

    # Calculate percentage spent in each category
    for category in categories:
        percentage = ((category.get_balance() - category.ledger[0]["amount"]) / total_spending) * 100
        percentage = int(percentage // 10) * 10  # Round down to the nearest 10
        spendings.append(percentage)

    # Build the chart
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for spending in spendings:
            chart += "o" if spending >= i else " "
            chart += "  "
        chart += "\n"

    # Add the horizontal line
    chart += "    -" + "---" * len(categories) + "\n"

    # Add category names vertically
    max_len = max(len(category.category) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            chart += category.category[i] if i < len(category.category) else " "
            chart += "  "  # Add an extra space for better readability
        chart += "\n"

    return chart.strip()+"  "
