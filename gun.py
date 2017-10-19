class Gun():
    def __init__(self,condition,model,ammo):
        self.conditon = condition
        self.model = model
        self.ammo = 0

    def get_interface(self,heldItems,current_room):
        if ammo == 0 and "BULLETS" in heldItems:
            print("You can LOAD BULLETS TO "+self.model())
        elif ammo == 0:
            print("You dont have ammo")

    def check_input(self,command,heldItems,current_room):
        if command == "LOAD BULLETS TO "+self.model() and self.ammo == 0 and "bullets" in heldItems:
            self.add_bullets(heldItems)
        if 
