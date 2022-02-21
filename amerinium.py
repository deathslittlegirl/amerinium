
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
        wallet.bank = wallet.money
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


    ataxia = location.materials[0]
    eden = location.materials[1]
    japan = location.materials[2]

    def sell():

        print("ÆFLX -->", ama.Amerinium.flux)

        while True:

            if Inv.ataxia <= 0:
                print("Nothing to sell.")
                sleep(2)


            elif Inv.eden <= 0:
                print("Nothing to sell.")
                sleep(2)


            elif Inv.japan <= 0:
                print("Nothing to sell.")
                sleep(2)

            else:
                break

            # For every number of materials that player possesses, that material is sold for its price and depleted by 1.

            for n in Inv.ataxia, Inv.eden, Inv.japan:

                if n == Inv.ataxia:
                    Inv.ataxia -= 1
                    wallet.money += economy.price_one

                elif n == Inv.eden:
                    Inv.eden -= 1
                    wallet.money += economy.price_two

                elif n == Inv.japan:
                    Inv.japan -= 1
                    wallet.money += economy.price_three

                print("財布:", "Æ" + str(wallet.money))

                sleep(wallet.process_delay)

            if wallet.money >= wallet.size:
                sleep(wallet.process_delay)
                print("Wallet full, depositing Amerinium to bank.")
                sleep(1)
                wallet.deposit()



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

    strength = random.randint(2, 5)
    speed = random.randint(3, 7)

    def mining():
        print("Mining", location_name + "...")
        sleep(2)
        for n in range(0, 25):
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

    name = "Midnight Bliss™️ E-Shop"
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

        if wallet.money >= Shop.shield_up:
            wallet.money -= Shop.shield_up
            sleep(2)
            PS.shield.density = PS.shield.density * 2
            print("SHI:", str(PS.shield.density))

    def inv_upgrade():

        if wallet.money >= Shop.inv_up:
            wallet.money -= Shop.inv_up
            sleep(2)
            PS.inventory.max_space = PS.inventory.max_space * 2
            print("INV:", str(PS.inventory.max_space))

    def health_upgrade():

        if wallet.money >= Shop.health_up:
            wallet.money -= Shop.health_up
            sleep(2)
            PS.health = PS.health * 1.5
            print('+::', str(PS.health))

    def money_upgrade():

        if wallet.money >= Shop.wallet_up:
            wallet.money -= Shop.wallet_up
            sleep(2)
            wallet.size = wallet.size * 1.3
            print("$$$: Expanded to Æ", str(wallet.size))


class IT:

    utility = [ 'mine', 'scan', 'travel', 'automine', 'sell' ]
    shop = [ 'shop', '++', 'shi+', 'inv+', '$$$+' ]
    diag = [ 'health', 'shield', 'inventory', 'wallet' ]
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

        while command == shop[0]:
            print('Logging on...')
            sleep(2)
            Shop.online()
            Shop.listing()
            command = ""

        while command == shop[1]:
            print("Upgrading", PS.name + "'s", 'health')
            Shop.health_upgrade()

        while command == shop[2]:
            print("Upgrading", Shield1.name)
            Shop.shield_upgrade()

        while command == shop[3]:
            print("Upgrading inventory...")
            Shop.inv_upgrade()

        while command == shop[4]:
            print("Upgrading", wallet.name)
            Shop.money_upgrade()

        while command == "clear":
            os.system('clear')
            command = ""



        else:
            pass
