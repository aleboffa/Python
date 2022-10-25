# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"


    def __eq__(self, another):
        if self.day == another.day and self.month == another.month and self.year == another.year:
            return True
        return False

    def __lt__(self, another):
        if self.year < another.year:
            return True 
        if self.year == another.year and self.month < another.month:
            return True
        if self.year == another.year and self.month == another.month and self.day < another.day:
            return True
        return False 

    def __gt__(self, another):
        if self.year > another.year:
            return True 
        if self.year == another.year and self.month > another.month:
            return True
        if self.year == another.year and self.month == another.month and self.day > another.day:
            return True
        return False 

    def __ne__(self, another):
        if self.year != another.year:
            return True 
        if self.year == another.year and self.month != another.month:
            return True
        if self.year == another.year and self.month == another.month and self.day != another.day:
            return True
        return False 

    def __add__(self, another):
        temp_day = self.day + another
        otro_day = temp_day
        temp_month = self.month 
        otro_month = temp_month
        temp_year = self.year 
        if temp_day > 30:
            otro_day = temp_day % 30
            temp_month += int(temp_day / 30)
#            temp_year += int(temp_month / 12)
        
        if temp_month > 12:
            helper = int(temp_month / 12)
            if helper > 1:
                temp_year += helper 
                otro_month = temp_month - 12*helper
            else:
                otro_month = temp_month
            if otro_month > 12:
                helper = int(temp_month / 12)
                if helper >= 1:
                    temp_year += helper 
                    otro_month = temp_month - 12*helper
                else:
                    otro_month = temp_month

        else:
            otro_month = temp_month     


        sum = SimpleDate(otro_day, otro_month, temp_year)
        return sum

    # def __sub__(self, another):
    #     if self.__cents < another.__cents:
    #         temp_euros = self.__euros - 1
    #         temp_cents = self.__cents + 100
    #     else:
    #         temp_euros = self.__euros
    #         temp_cents = self.__cents    

    #     eur = temp_euros - another.__euros
    #     cen = temp_cents - another.__cents

if __name__ == "__main__":
#    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(1, 12, 1999)

 #   d3 = d1 + 3
    d4 = d2 + 150

 #   print(d1)
    print(d2)
 #   print(d3)
    print(d4) # debe ser 1.5.2000