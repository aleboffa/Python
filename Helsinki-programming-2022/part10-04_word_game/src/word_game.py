# Write your solution here
from operator import truediv
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):

        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")
            respuesta = self.round_winner(answer1, answer2)

            if respuesta == 1:
                self.wins1 += 1
                print("player 1 won")
            elif respuesta == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            pass

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        p1 = 0
        p2 = 0
        vowels = "aeiou"
        for letra in player1_word:
            if letra in vowels:
                p1 += 1 
        for letra in player2_word:
            if letra in vowels:
                p2 += 1
        if p1 > p2:
            return 1
        elif p1 < p2:
            return 2
        else:
            pass

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        salir = False
        # your code for determining the winner goes here
        p1 = 0
        p2 = 0
        words = ["rock","paper","scissors"]
        if player1_word == "" or player2_word == "":
            salir = True
        if player2_word not in words:
            if player1_word in words:
                p1 += 1
            else:
                salir = True        
        if player1_word not in words:
            if player2_word in words:
                p2 += 1
            else:
                salir = True
        while salir == False:        
            if player1_word in words and player2_word in words:
                if player1_word == player2_word: # rock == rock ## paper == paper ## scissors == scissors
                    salir = True
                    break
                else:
                    if player1_word == "rock":
                        if player2_word == "paper":
                            p2 += 1 
                            salir == True
                            break
                        else:   # p2 == "scissors"
                            p1 += 1
                            salir == True
                            break
                    elif player1_word == "paper":
                        if player2_word == "rock":
                            p1 += 1
                            salir == True
                            break
                        else:   # p2 == "scissors"
                            p2 += 1
                            salir == True
                            break
                    elif player1_word == "scissors":
                        if player2_word == "rock":
                            p2 += 1
                            salir == True
                            break   
                        else:
                            # p2 == "paper"
                            if player2_word == "paper":
                                p1 += 1    #error test automatico endless bucle
                                salir == True
                                break
                    else:
                        salir == True
                        break
                salir == True
                break
            else:
                salir == True
                break
                    
        if p1 > p2:
            return 1
        elif p1 < p2:
            return 2
        else:
            pass

##############################
if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()