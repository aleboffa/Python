# Write your solution here:
class Task:
    id = 0
    def __init__(self, description: str, programmer: str, workload: int ):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def is_finished(self):
        if self.finished == True:
            return True
        else:
            return False

    def mark_finished(self):
        self.finished = True
        return self.finished

    def __str__(self):
        if self.finished:
            terminado = "FINISHED"
        else:
            terminado = "NOT FINISHED"
        return f"{Task.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {terminado} "

class OrderBook(Task):
    def __init__(self):
        self.orders = []        

    def add_order(self, description, programmer, workload):
        datos = Task((description), (programmer), (workload))
        self.orders.append(datos)
        Task.id += 1
        
    def all_orders(self):
        return self.orders

    def programmers(self):
        lista = []
        for order in self.orders:
            lista.append(order.programmer)
        lista = list(set(lista))
        return lista

    def mark_finished(self, id: int):
        pass

    def finished_orders(self):
        pass

    def unfinished_orders(self):
        pass

    def status_of_programmer(self, programmer: str):
        pass

# 1 program hello world Eric 3
# 1: program hello world (3 hours), programmer Eric NOT FINISHED
# False
# 1: program hello world (3 hours), programmer Eric FINISHED
# True
# 2: program webstore (10 hours), programmer Adele NOT FINISHED
# 3: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)