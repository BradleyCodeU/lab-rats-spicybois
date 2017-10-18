from room import Room
from flashlight import Flashlight
from character import Enemy
from container import Container
from weight_machine import Weight
<<<<<<< HEAD
from gun import Gun
=======
from gun import Gun
=======
 
from weight_machine import Weight
 
from gun import Gun
 
>>>>>>> fadcdd4afe2171cff6c53c3f64bd34f8c092434f
>>>>>>> 0a8f3017f74368652774a776a94c1804cd0b0a3c

heldItems = []
myHealth = 50
visitedRooms = []

# ********************************* SET UP THE ROOMS *********************************

# Shop (East Room)
#
# Room descriptions should include interactive containers like CABINET, CARDBOARD BOX, SHOEBOX, and LOCKED CONTAINER
shop = Room("Shop","A dark crypt, skulls surround you and give you an eerie feeling. Growls echo along the walls, as you search for things. There is a CABINET above a dirty sink, A CARDBOARD BOX in the corner, and A SHOEBOX under the sink.")

# The Shop has a CABINET object that contains/hides 2 interactive items: a fork and a health potion
# Once this container is open, the interactive items will no longer be hidden in the container
shop.cabinet = Container("cabinet above the sink",["a fork","health potion"])
# The Shop has a CARDBOARD BOX object that contains/hides 1 interactive item, a bitten cookie
# Once this container is open, the interactive items will no longer be hidden in the container
shop.cardboardbox = Container("a cardboard box in the corner",["cookie"])
# The Shop has a SHOEBOX object that contains/hides 2 interactive items: a kinfe and soap
# Once this container is open, the interactive items will no longer be hidden in the container
shop.shoebox = Container("shoebox under the sink",["a knife","soap"])
# Create an interactive item that's show in a room (not hidden in a container) with create_room_item()
shop.create_room_item("rat")

# Small Office
#
smalloffice = Room("Small Office","A dark room with a mess of books and papers covering the desk. There is some mail and an ozon.ru PACKAGE. You can READ a book. You can look in the DESK.")
smalloffice.desk = Container("desk",["battery","envelope"])
smalloffice.package = Container("ozon.ru package",["sheet of bubble wrap","porcelain figurine of a bear","red flashlight"])
smalloffice.create_room_item("guinea pig")
redFlashlight = Flashlight("red",0,False)

# Laboratory
#
lab = Room("Laboratory","A bright room with sunlight shining through windows secured by prison bars. There is a messy SHELF on the north wall.")
# The lab has a SHELF object that contains 3 interactive items. Shelf gets a third argument because you'd say ON the shelf, not IN the shelf
lab.shelf = Container("shelf",["brass key","spork","yellow flashlight"],"on")
lab.create_room_item("rat")
yellowFlashlight = Flashlight("yellow",1,True)

# Supply Closet
#
supplycloset = Room("Supply Closet","A small dark room with a musty smell. On one side is a filing CABINET and a large plastic BIN. On the other side is a SHELF with supplies and a SHOEBOX.")

#Armory Room
#
armory = Room("Armory Room","A dark open room that has a stinky stench. A glimmer catches your eye and you find a PISTOL. you find some other weapons but they are all broken.")
<<<<<<< HEAD
armory.create_room_item("gun")
=======
<<<<<<< HEAD
=======
 
>>>>>>> fadcdd4afe2171cff6c53c3f64bd34f8c092434f
newGun = Gun("New","Pistol",0)
>>>>>>> 0a8f3017f74368652774a776a94c1804cd0b0a3c

#Ammo
#
ammo = Room("Ammo Room","A dark room with a shelf in it. There is ammo on the shelf.")
ammo.create_room_item("bullets")
<<<<<<< HEAD

=======
       
>>>>>>> fadcdd4afe2171cff6c53c3f64bd34f8c092434f
#Fitness Room
#
fitnessroom = Room("Fitness Room","A small room with sets of weights and cardio equipment fit for a king! In the back, there is a large LOCKER, which appears to be unlocked. There is also a squat rack with a set of WEIGHTS you can LIFT")
fitnessroom.locker = Container("locker",["fitness magazine", "5 pound dumbell"])
squatrack = Weight("Holds bar in a position used to initiate a squat, an exercise used to improve core strength.", 50)

<<<<<<< HEAD
=======

 
>>>>>>> fadcdd4afe2171cff6c53c3f64bd34f8c092434f
# Create a fake room called locked that represents all permenently locked doors
#
locked = Room("locked","")

# Connect rooms. These are one-way connections.
<<<<<<< HEAD
shop.link_room(locked, "EAST")
shop.link_room(smalloffice, "SOUTH")
shop.link_room(fitnessroom, "WEST")
shop.link_room(armory, "NORTH")
supplycloset.link_room(smalloffice, "EAST")
smalloffice.link_room(shop, "NORTH")
smalloffice.link_room(lab, "EAST")
smalloffice.link_room(locked, "SOUTH")
smalloffice.link_room(supplycloset, "WEST")
lab.link_room(locked, "SOUTH")
lab.link_room(smalloffice, "WEST")
armory.link_room(shop, "SOUTH")
current_room = shop
armory.link_room(shop, "SOUTH")
fitnessroom.link_room(shop, "EAST")
current_room = shop
=======
<<<<<<< HEAD
 
=======
>>>>>>> 0a8f3017f74368652774a776a94c1804cd0b0a3c

>>>>>>> fadcdd4afe2171cff6c53c3f64bd34f8c092434f
# Set up characters
dmitry = Enemy("Dmitry", "A smelly zombie")
dmitry.set_speech("Brrlgrh... rgrhl... brains...")
dmitry.set_weaknesses(["FORK","SPORK","KNIFE"])
supplycloset.set_character(dmitry)

# This is a procedure that simply prints the items the player is holding and tells them if they can do something with that item
def playerItems():
    # Print out the player's Held Items and let player know if they can USE an item to fight a character or something
    if len(heldItems) == 1:
        print("You are holding a "+heldItems[0])
        print("You can DROP "+heldItems[0].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name)
    elif len(heldItems) >= 2:
        print("Your hands are full. You must drop something before you can pick anything else up.")
        print("You are holding a "+heldItems[0]+" and a "+heldItems[1])
        print("You can DROP "+heldItems[0].upper()+" or DROP "+heldItems[1].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name+" or USE "+heldItems[1].upper())
    # ********************************* SPECIAL ITEM INTERFACES *********************************
    # If holding a special item, then display the item's interface with get_interface()
    if "red flashlight" in heldItems:
        redFlashlight.get_interface(heldItems,current_room)
    if "yellow flashlight" in heldItems:
        yellowFlashlight.get_interface(heldItems,current_room)

# This fuction checks the player's command and then runs the corresponding method
def checkUserInput(current_room,command,heldItems):
    # Convert it to ALL CAPS
    command = command.upper()
    # All possible user input commands go here
    print("\n")
    
    # ********************************* SPECIAL USER INPUT *********************************
    # If holding a special item, then check for that item's UI keywords with check_input()
    if "red flashlight" in heldItems and "RED FLASHLIGHT" in command:
        redFlashlight.check_input(command,heldItems,current_room)
    elif "yellow flashlight" in heldItems and "YELLOW FLASHLIGHT" in command:
        yellowFlashlight.check_input(command,heldItems,current_room)

    # ********************************* USE, TAKE, DROP *********************************
    # Use an item to fight an enemy
    elif "USE " in command and current_room.get_character() is not None:
        # command[4:] is used to get the characters typed after "USE "
        enemyHealth = current_room.character.fight(command[4:])
        if enemyHealth < 1:
            print(current_room.character.name+" is dead")
            current_room.remove_character() # If the enemy is dead, then remove them from the room
    # Take lets you pick up an item
    elif "TAKE " in command:
        # command[5:] is used to get the characters typed after "TAKE "
        heldItems = current_room.take_room_item(command[5:],heldItems)
    # Drop lets you set down an item
    elif "DROP " in command:
        # command[5:] is used to get the characters typed after "DROP "
        heldItems = current_room.add_room_item(command[5:],heldItems)
    # Talk and Fight aren't currently used in this version of the game, but could be implemented in your version of the game
    elif "TALK" in command and current_room.get_character() is not None:
        current_room.character.talk()
    elif "FIGHT" in command and current_room.get_character() is not None:
        current_room.character.talk()
    
    # ********************************* ROOM SPECIFIC USER INPUTS *********************************
    # Interactive containers look like this...   elif current_room.name == "Laboratory" and command == "SHELF"
    elif current_room.name == "Shop" and command == "CABINET":
        # Open kitchen.cupboard and concat each of the contents to the end of room_items
        current_room.room_items += shop.cabinet.open()
    # Can only open cabinet if holding a flashlight that isOn
    elif current_room.name == "Shop" and command == "SHOEBOX":
        # Open kitchen.cabinet and concat each of the contents to the end of room_items
        print("You check the shoebox and find a KNIFE and a SOAP")
        current_room.room_items += shop.shoebox.open()
    elif current_room.name == "Shop" and command == "CARDBOARD BOX":
        print("You check the cardboard box, but it's too dark to see if there is anything inside.")
    elif current_room.name == "Small Office" and command == "PACKAGE":
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        current_room.room_items += smalloffice.package.open()
    elif current_room.name == "Small Office" and command == "READ":
        print("POCCNR??? You can't read it. It's written is some strange Cyrillic script.")
    elif current_room.name == "Small Office" and command == "DESK" and "brass key" in heldItems:
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        print("You use the brass key to unlock the desk.")
        current_room.room_items += smalloffice.desk.open()
    elif current_room.name == "Small Office" and command == "DESK":
        print("The desk drawer is locked.")
    elif current_room.name == "Laboratory" and command == "SHELF":
        # Open lab.shelf and concat each of the contents to the end of room_items
        current_room.room_items += lab.shelf.open()
    elif current_room.name == "Fitness Room" and command == "LIFT WEIGHTS":
        myHealth += squatRack.get_HP_per_rep
        

    # ********************************* MOVE *********************************
    else:
        current_room = current_room.move(command,visitedRooms) # If it was none of those commands, assume it was a direction. Try to move.
    return current_room


#THE LOOP
while True:
    print("\n")
    # Print current room info
    myHealth = current_room.info(heldItems,myHealth,visitedRooms) # this returns myHealth cuz an enemy in the room could hurt you
    if myHealth <= 0:
        print("You died.\nGAME OVER")
        break
    # Print player items
    playerItems()
    # Get user input
    command = input("> ")
    # Check the user input
    current_room = checkUserInput(current_room,command,heldItems)
