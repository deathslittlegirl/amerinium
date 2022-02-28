 # idk wtf these are but im scared to delete them
from ctypes import util
from importlib.resources import contents
from click import command

# things i recognize

import random
import os

# game files

import amatomic as ama
import amplanets
from time import sleep

from amplanets import Piscea

location = Piscea
location_name = Piscea.name


class economy:

    price_one = location.materials_price[0] / ama.Amerinium.flux
    price_two = location.materials_price[1] / ama.Amerinium.flux
    price_three = location.materials_price[2] / ama.Amerinium.flux

class Shield1:

    name = "TH DOS 20"
    density = 35
    d_up = 32
    surface = "ribbed, transient"


class enemyShield:

    name = "TH DOS 20"
    density = 35
    d_up = 32
    surface = "ribbed, transient"


class wallet:

    name = "Beartech Money Packager"

    size = 10
    process_delay = random.randint(3, 5)
    money = 0
    bank = 0

    def deposit():
        print('Initiating deposit of +', str(wallet.money))
        sleep(wallet.process_delay)
        wallet.bank = wallet.bank + wallet.money
        print("Æ: +" + str(wallet.money))
        wallet.money = 0

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

    max_space = 18

    location.materials[0] = 0
    location.materials[1] = 0
    location.materials[2] = 0

    m_one = location.materials[0]
    m_two = location.materials[1]
    m_three = location.materials[2]

    box = location.materials[0], location.materials[1], location.materials[2]

    def sell():

        print("Determining ÆFLX...")
        ama.Amerinium.fluxflip()
        sleep(2)

        print("ÆFLX:", ama.Amerinium.flux)

        while True:

            # For every number of materials that player possesses, that material is sold for its price and depleted by 1.

            for i in Inv.m_one, Inv.m_two, Inv.m_three:

                if i == Inv.m_one:
                    print(location.materials_name[0], "-1/" + str(Inv.m_one))
                    Inv.m_one -= 1
                    wallet.money += economy.price_one

                elif i == Inv.m_two:
                    print(location.materials_name[1], "-1/" + str(Inv.m_two))
                    Inv.m_two -= 1
                    wallet.money += economy.price_two

                elif i == Inv.m_three:
                    print(location.materials_name[2], "-1/" + str(Inv.m_three))
                    Inv.m_three -= 1
                    wallet.money += economy.price_three

                print("財布:", "Æ" + str(wallet.money))

                sleep(wallet.process_delay)

            if wallet.money == wallet.size:
                sleep(wallet.process_delay)
                print("Wallet full, depositing Amerinium to bank.")
                sleep(1)
                wallet.deposit()
                break

            else:
                break



class PS:

    health = 100
    armor = 50
    shield = Shield1()
    inventory = Inv()
    weapon = lsCannon()


    def shield_dmg():

        if Shield1.density <= 0:
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

    strength = random.randint(2, 3)
    speed = random.randint(3, 7)

    def mining():
        print("Mining", location_name + "...")
        sleep(2)
        for n in range(8):

            flip = [ 'a', 'b', 'c' ]

            if random.choice(flip) == 'a':
                if Inv.m_one == Inv.max_space:
                    return
                Inv.m_one += Miner.strength
                print(Inv.m_one, location.materials_name[0], "collected.")
                sleep(Miner.speed)


            elif random.choice(flip) == 'b':
                if Inv.m_two == Inv.max_space:
                    return
                Inv.m_two += Miner.strength
                print(Inv.m_two, location.materials_name[1], "collected.")
                sleep(Miner.speed)


            elif random.choice(flip) == 'c':
                if Inv.m_three == Inv.max_space:
                    return
                Inv.m_three += Miner.strength
                print(Inv.m_three, location.materials_name[2], "collected.")
                sleep(Miner.speed)



class PS:

    name = "Calcula I"
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


class Shop:

    name = "The Midnight Bliss™️ E-Shop"
    comfort_msg = "Welcome to " + name + "."

    # Upgrade Prices

    health_up = 100
    shield_up = 100
    inv_up = 42
    wallet_up = 60

    # Functions

    def online():
        print(Shop.comfort_msg)
        sleep(3)
        print("Æ", wallet.bank)
        sleep(2)


    def listing():
        print('++:', Shop.health_up) # Print health price
        sleep(2)
        print('shi+:', Shop.shield_up)
        sleep(2)
        print('inv+:', Shop.inv_up)
        sleep(2)
        print('$$$+:', Shop.wallet_up)

    def shield_upgrade():

        while wallet.bank >= Shop.shield_up:
            wallet.bank -= Shop.shield_up
            sleep(2)
            PS.shield.density = PS.shield.density * 2
            print("SHI:", str(PS.shield.density))
            break

    def inv_upgrade():

        while wallet.bank > Shop.inv_up:
            wallet.bank -= Shop.inv_up
            sleep(2)
            PS.inventory.max_space = PS.inventory.max_space * 2
            print("INV:", str(PS.inventory.max_space))
            break

    def health_upgrade():

        while wallet.bank >= Shop.health_up:
            wallet.bank -= Shop.health_up
            sleep(2)
            PS.health = PS.health * 1.5
            print('+::', str(PS.health))
            break

    def money_upgrade():

        while wallet.bank >= Shop.wallet_up:
            wallet.bank -= Shop.wallet_up
            sleep(2)
            wallet.size = wallet.size * 1.3
            print("$$$: Expanded to Æ", str(wallet.size))
            break


class IT:


    # Various commands

    utility = [ 'mine', 'scan', 'travel', 'automine', 'sell' ]
    shop = [ 'shop', '++', 'shi+', 'inv+', '$$$+' ]
    diag = [ 'health', 'shield', 'inventory' ]
    money = [ 'wallet', 'deposit' ]
    offense = [ 'a', 'scan', 'sh', 'ff' ]
    off_sp = [ 'sp.a', 'cat',  'aim' ] # cat = capture

    command = ""

    while command != "kill":

        command = input("司令官: ")

        while command == utility[0]:
            Miner.mining()
            command = ""

        while command == utility[2]:
            zyX = input("X, Y: ")

            if zyX == amplanets.Piscea.code:
                location = Piscea
                location_name = Piscea.name
                amplanets.Piscea.arrival()
                command = ""

            else:
                command = ""

        while command == utility[4]:
            Inv.sell()
            command = ""

        while command == diag[0]:
            print("Health:", PS.health)
            command = ""

        while command == diag[1]:
            print("Shield:", PS.shield.density)
            command = ""

        while command == money[1]:
            wallet.deposit()

        while command == shop[0]:
            print('Logging on...')
            sleep(2)
            Shop.online()
            Shop.listing()
            command = ""

        while command == shop[1]:
            print("Upgrading", PS.name + "'s", 'health')
            Shop.health_upgrade()
            command = ""

        while command == shop[2]:
            print("Upgrading", Shield1.name)
            Shop.shield_upgrade()
            command = ""

        while command == shop[3]:
            print("Upgrading inventory...")
            Shop.inv_upgrade()
            command = ""

        while command == shop[4]:
            print("Upgrading", wallet.name)
            Shop.money_upgrade()
            command = ""

        while command == "clear":
            os.system('clear')
            command = ""



        else:
            pass
