#!/usr/local/bin/python3
# NAME: NESTOR ALVAREZ
# FILE: spam.py
# DATE: 20160731
# DESC: Final shenanigans

class Spam:
    total_cost = []
    items_count = []
    removed = []

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.total_cost.append(cost)
        self.items_count.append(1)

    def rename(self, name):
        self.name = name

    def cost_change(self, cost):
        self.removed.append(self.cost)
        self.cost = cost
        self.total_cost.append(cost)

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    @classmethod
    def get_total_cost(self):
        return sum(self.total_cost) - sum(self.removed)

    @classmethod
    def get_items_count(self):
        return sum(self.items_count)


    

def __main__():
    print("#" * 28,"\n", "Testing...1, 2, 3...testing!\n", "#" * 28, "\n", sep="")
    print("#" * 37,"\n", "Creating//Initializing 5 Spam objects\n", "#" * 37, "\n", sep="")
    spam1 = Spam("Soap", 2.99)
    spam2 = Spam("Conditioner", 4.79)
    spam3 = Spam("Shampoo", 4.29)
    spam4 = Spam("Luffa", 1.50)
    spam5 = Spam("Toothpaste", 1.99)

    print("#" * 27,"\n", "Printing all 5 Spam objects\n", "#" * 27, "\n", sep="")
    print(spam1.get_name(), spam1.get_cost())
    print(spam2.get_name(), spam2.get_cost())
    print(spam3.get_name(), spam3.get_cost())
    print(spam4.get_name(), spam4.get_cost())
    print(spam5.get_name(), spam5.get_cost(), "\n")


    print("#" * 49,"\n", "Testing accessor methods: total_cost, items_count\n", "#" * 49, "\n", sep="")
    print("Total Cost: ", Spam.get_total_cost())
    print("Item Count: ", Spam.get_items_count())
    print("Total Cost: ", spam1.get_total_cost())
    print("Item Count: ", spam1.get_items_count())

    spam1.rename("Toothbruch")
    spam1.cost_change(1.99)
    print(spam1.get_name(), spam1.get_cost())

    print("#" * 34,"\n", "Instance count should be unchanged\n", "#" * 34, "\n", sep="")
    print("#" * 43,"\n", "Total cost should change after modification\n", "#" * 43, "\n", sep="")

    print("Total Cost: ", Spam.get_total_cost())
    print("Item Count: ", Spam.get_items_count())
    print("Total Cost: ", spam1.get_total_cost())
    print("Item Count: ", spam1.get_items_count())
    


if __name__ == '__main__':
    __main__()


    
