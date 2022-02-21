import amatomic as ama
import random as rnd
from time import sleep

class Pleroma: 

    matter_d = ama.THC, ama.Psycilobin, ama.Dextromethorphan, ama.Diphenhydramine 
    matter_g = ama.Ammonia, ama.Helium, ama.Hydrogen, ama.Methane, ama.Sulfur
    matter_m = ama.Meteorite, ama.MR, ama.Junk 
    matter_s = ama.Femininium, ama.Angelium
    matter_sp = ama.Silver, ama.Gold, ama.Diamond, ama.Platinum

#def d_select():

       #for i in range(1, 25): 
           #drg = rnd.choice(Pleroma.matter_d)
           
          # if i == 8:
            #   drg = rnd.choice(Pleroma.matter_d)
         
class Piscea():
    
    name = "Piscea V"
    materials = [ ama.THC, ama.Femininium, ama.Diamond ]
    materials_name = [ ama.THC.name,  ama.Femininium.name, ama.Diamond.name ]
    materials_price = [ ama.THC.cost, ama.Femininium.cost, ama.Diamond.cost ]
    surface = "Watery, rainbow hue from multi-shifting, drug-addled atmosphere."
    smell = "Perfume-like, swathed in neptunian breeze, hard candy."
    rings = True
    breathable = True
    code = "34, 77"  # X, Y


    def arrival():
        print("You are now at", Piscea.name)



    


               



