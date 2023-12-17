import random

class machine_slot:
    _tablero = {"Cereza":0,
                   "Manzana":0, 
                   "Naranja":0, 
                   "Campana":0, 
                   "Melon":0, 
                   "Sandia":0, 
                   "Estrellas":0,
                   "77":0,
                   "Bar":0,
                   "Bar/Bar":0}
    
    def __init__(self, credits) -> None:
        self._credits = credits
        if self._credits > 999:
            self._credits = 999
        elif self._credits < 0:
            self._credits = 0
    

    def set_tablero(self, apuesta):
        if self._credits != 0:
            if self._tablero[f"{(list(self._tablero.keys())[apuesta])}"] < 9:
                self._tablero[f"{(list(self._tablero.keys())[apuesta])}"] += 1
                self.set_credits(-1)
            

    def set_credits(self,credits):
        self._credits += credits
        if self._credits > 999:
            self._credits = 999
        elif self._credits < 0:
            self._credits = 0
        
    def get_credits(self):
        return self._credits
    
    def confirm_bet(self)->bool:
        x = False
        for values in self._tablero.values():
            if values != 0:
                x = True
        return x
    
    def cobrar(self):
        if not self.confirm_bet():
            self._credits = 0
        
    
    def roulette(self):
        x = random.randint(0,21)
        prize = 0
        if x in [2,5,8,11,14,17,20]:
            if self._tablero["Cereza"] != 0:
                
                prize = self._tablero['Cereza']*2

        elif x in [1,10,16,19]:
            if self._tablero["Manzana"] != 0:
                
                prize = self._tablero['Manzana']*5
                
        elif x in [7,18]:
            if self._tablero["Naranja"] != 0:
                
                prize = self._tablero['Naranja']*10

        elif x in [15,0]:
            if self._tablero["Campana"] != 0:
                
                prize = self._tablero['Campana']*15
                
        elif x in [12,21]:
            if self._tablero["Melon"] != 0:
                
                prize = self._tablero['Melon']*20
                
        elif x == 9:
            if self._tablero["Sandia"] != 0:
                
                prize = self._tablero['Sandia']*25
                
        elif x == 13:
            if self._tablero["Estrellas"] != 0:
                
                prize = self._tablero['Melon']*30
                
        elif x == 6:
            if self._tablero["77"] != 0:
                
                prize = self._tablero['77']*40
                
        elif x == 3:
            if self._tablero["Bar"] != 0:
                
                prize = self._tablero['Bar']*50
                
        else:
            if self._tablero["Bar/Bar"] != 0:
                
                prize = self._tablero['Bar/Bar']*100
        
        return x, prize