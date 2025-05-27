class Restaurant:
    def _order1(self, food):
        print(f"Order placed: Food = {food}")

    def _order2(self, food, drink):
        print(f"Order placed: Food = {food}, Drink = {drink}")

    def _order3(self, food, drink, dessert):
        print(f"Order placed: Food = {food}, Drink = {drink}, Dessert = {dessert}")

    def order(self, *args):
        methods = {
            1: self._order1,
            2: self._order2,
            3: self._order3
        }
        method = methods.get(len(args))
        if method:
            return method(*args)
        raise TypeError("No matching method for given number of arguments.")

# Example usage
r = Restaurant()
r.order("Burger")
r.order("Pizza", "Soda")
r.order("Pasta", "juice", "Cake")



class BankAtm:
    def withdraw(self, *args):
        labels = ["AccountNumber", "Amount", "password"]
        if not 1 <= len(args) <= 3:
            raise TypeError("Withdrawal must have 1 to 3 items (accountnumber, amount, password).")

        items = [f"{label} = {value}" for label, value in zip(labels, args)]
        print("Withdrawal: " + ", ".join(items))

# Example usage
bank = BankAtm()
bank.withdraw("SV0000567")
bank.withdraw("SV0000456", 45000)
bank.withdraw("SV0000389", 85000, 1234)