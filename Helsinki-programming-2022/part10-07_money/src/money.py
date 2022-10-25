# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        if self.__euros == another.__euros and self.__cents == another.__cents:
            return True
        return False

    def __lt__(self, another):
        if self.__euros < another.__euros or self.__euros == another.__euros and self.__cents < another.__cents:
            return True
        return False

    def __gt__(self, another):
        if self.__euros > another.__euros or self.__euros == another.__euros and self.__cents > another.__cents:
            return True
        return False

    def __ne__(self, another):
        if self.__euros != another.__euros and self.__cents != another.__cents:
            return True
        elif self.__euros == another.__euros and self.__cents != another.__cents:
            return True
        elif self.__euros != another.__euros and self.__cents == another.__cents:
            return True
        return False

    def __add__(self, another):
        eur = self.__euros + another.__euros
        cen = self.__cents + another.__cents
        if cen >= 100:
            eur += 1
            cen -= 100
        sum = Money(eur, cen)
        return sum

    def __sub__(self, another):
        if self.__cents < another.__cents:
            temp_euros = self.__euros - 1
            temp_cents = self.__cents + 100
        else:
            temp_euros = self.__euros
            temp_cents = self.__cents    

        eur = temp_euros - another.__euros
        cen = temp_cents - another.__cents

        # print("self.cents: ", self.cents)
        # print("another.cents: ", another.cents)  
        # print("temp_euros: ", temp_euros)
        # print("temp_cents: ", temp_cents)      
        # print(eur)
        # print(cen)

        if eur < 0 or cen < 0:
            raise ValueError(f"a negative result is not allowed")
        resta = Money(eur, cen)
        return resta

########################################        
if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)