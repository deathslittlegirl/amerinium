from ctypes import util
from importlib.resources import contents
import random
from tkinter import Variable, dialog
from turtle import speed

from click import command
import amatomic as ama
import amplanets
from time import sleep

from amplanets import Piscea

location = Piscea
location_name = Piscea.name



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
     

class wallet: 
    
    name = "Beartech Money Packager"
    
    size = 2222
    process_delay = 3
    money = 0
    
    
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

class Inv:

    max_space = 36
    up_price = 45

    location.materials[0] = 0
    location.materials[1] = 0
    location.materials[2] = 0

    transfer_rate = 3
    
    def sell():
        while True:
            for heaven in location.materials[0], location.materials[1], location.materials[2]:
                wallet.money += ama.Amerinium.price // ama.Amerinium.flux
                print("Wallet:", wallet.money)
                sleep(ama.Amerinium.transfer_rate)
                
                
        
        
    
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
        
    


class Miner: 
    
    name = "LSP-1000"
    
    strength = 3
    speed = 3
    
    def mining():
        print("Mining", location_name + "...")
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

class IT:

    utility = [ 'mine', 'scan', 'travel', 'automine', 'sell' ]
    diag = [ 'health', 'shield', 'inventory', 'wallet' ]
    offense = [ 'a', 'scan', 'sh', 'ff' ]
    off_sp = [ 'sp.a', 'cat',  'aim' ] # cat = capture
    
    
    command = ""

    while command != "kill":
        
        command = input("司令官V0.0.2: ")
        
        while command == utility[2]:
            zyX = input("X, Y: ")

            if zyX == amplanets.Piscea.code:
                location = Piscea
                location_name = Piscea.name
                amplanets.Piscea.arrival()
                command = ""
            
            else:
                command = ""
            
        while command == utility[0]:
            Miner.mining()
            command = ""
            
        while command == diag[0]:
            print("Health:", PS.health)
            command = ""
            

        while command == diag[1]:
            print("Shield:", PS.shield.density)
            command = ""
        
        while command == utility[4]:
            Inv.sell()
            command = ""
        
        else:
            pass
        
