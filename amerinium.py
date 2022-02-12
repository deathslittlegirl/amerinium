import random
from tkinter import Variable
from turtle import speed
import amatomic as ama
import amplanets
from time import sleep

from amplanets import Piscea

location = Piscea
location_name = Piscea.name

class IT:

    util = [ 'mine', 'scan', 'travel', 'automine' ]
    diag = [ 'health', 'shield', 'inventory', 'wallet' ]
    location = ""
    
    def command():
        command = input("Command: ")
        if command != "":
        
        else:
            continue
    

class Shield1:
    
    name = "TH DOS 20"
    density = 35
    d_up = 32
    price = 35
    surface = "ribbed, transient"
    
     
class enemyShield:
    
    name = "TH DOS 20"
    density = 35
    d_up = 32
    price = 35
    surface = "ribbed, transient"
     

class Wallet: 
    
    size = 2222
    process_delay = 3
    
    
class lsCannon:
    
    name = "AW MK II"
    
    
    # Normal Mode
    dmg = random.randrange(2, 20)
    crit = random.randrange(14, 23)
    price = 40
    
    
    # Super Mode, needs locked_on = True
    locked_on = False
    super_dmg = random.randrange(18, 30)
    super_crit = random.randrange(18, 48)
    super_price = 60
    
class ESP:
     
    health = 100
    armor = 50
    shield = Shield1()
    weapon = lsCannon()

    def shield_dmg():
        
        if enemyShield.density < 0:
            ESP.armor_sw()
        
        else:
            enemyShield.density -= 3.5
    
    def armor_sw():
        
        if random.randint(1, 100) == 45:
            ESP.armor -= random.randrange(2, 4)
        else:
            ESP.armor -= random.randrange(4, 10)
        
    def dmg_ps():
        
        if ESP.armor == 0: 
            ESP.health -= 10
        
        else:
            ESP.armor_sw()

class Inv:

    max_space = 36
    up_price = 45
    contents = 0

    Piscea.materials[0] = 0
    Piscea.materials[1] = 0
    Piscea.materials[2] = 0
    

class Miner: 
    
    name = "LSP-1000"
    
    strength = 3
    speed = 3
    
    def mining():
        print("Mining", location_name, "...")
        sleep(2)
        for n in range(0, Inv.max_space):
            flip = [ 'a', 'b', 'c' ]

            if random.choice(flip) == 'a':
                location.materials[0] += Miner.strength
                print(location.materials[0], location.materials_name[0], "collected.")
                sleep(Miner.speed)
                if location.materials[0] == Inv.max_space:
                    break
                    

            elif random.choice(flip) == 'b':
                location.materials[1] += Miner.strength
                print(location.materials[1], location.materials_name[1], "collected.")
                sleep(Miner.speed)
                if location.materials[1] == Inv.max_space:
                    break
            
            
            elif random.choice(flip) == 'c':
                location.materials[2] += Miner.strength
                print(location.materials[2], location.materials_name[2], "collected.")
                sleep(Miner.speed)
                if location.materials[2] == Inv.max_space:
                    break

            else:
                continue
        
        
            
            



    
class PS:

    health = 100
    armor = 50
    shield = Shield1()
    inventory = Inv()
    weapon = lsCannon()

    
    
    def shield_dmg():
        
        if Shield1.density < 0:
            PS.armor_sw()
        
        else:
            Shield1.density -= 3.5
    
    def armor_sw():
        
        if random.randint(1, 100) == 45:
            PS.armor -= random.randrange(2, 4)
        else:
            PS.armor -= random.randrange(4, 10)
        
    def dmg_ps():
        
        if PS.armor == 0: 
            PS.health -= 10
        
        else:
            PS.armor_sw()    
            
# IT.command
# util = [ 'mine', 'scan', 'travel', 'automine' ]
# diag = [ 'health', 'shield', 'inventory', 'wallet' ]

    if IT.command() == IT.diag[0]:
        print("Health:", health)  
    
    if IT.command() == IT.diag[1]:
        print("Shield:", shield.density)
    
    if IT.command() == IT.util[2]:
        zX = input("X, Y: ")
        
        
        if zX == amplanets.Piscea.code:
            location = amplanets.Piscea.name
            amplanets.Piscea.arrival()
            
    if IT.command() == IT.util[0]:
        Miner.mining()


        

           



            