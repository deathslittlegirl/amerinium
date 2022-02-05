import random
from time import sleep

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
    
    size = 200
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
        
        if EPS.armor == 0: 
            ESP.health -= 10
        
        else:
            ESP.armor_sw()

class IT:
    
    util = [ 'mine', 'scan', 'travel', 'automine' ]
    diag = [ 'health', 'shield', 'inventory', 'wallet' ]
    command = input("Command: ")
    

class Inv:
    
    materials = 150
    max_space = 420
    up_price = 45

class Miner: 
    
    name = "LSP-1000"
    
    strength = 3
    speed = 3
    
    
class PS:
    health = 100
    armor = 50
    shield = Shield1()
    inventory = Inv()
    weapon = lsCannon()
    interface = IT()
    
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
            
     
    if IT.command == IT.diag[0]:
        print("Health:", health)  
    
    if IT.command == IT.diag[1]:
        print("Shield:", shield.density)
        
        




            