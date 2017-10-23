class Gun():
    def __init__(self,condition,model,ammo):
        self.conditon = condition
        self.model = model
        self.ammo = ammo

    def get_interface(self,ammo):
        if ammo == 0 and "BULLETS" in heldItems:
            print("You can LOAD BULLETS TO "+self.model())
        elif ammo == 0:
            print("You dont have ammo")
        if self.ammo > 0:
            print("You can REMOVE "+self.model)

    def check_input(self):
        if command == "LOAD BULLETS TO "+self.model() and self.ammo == 0 and "bullets" in heldItems:
            self.remove_bullets(heldItems)
        if command == "UNLOAD BULLETS "+self.model() and self.ammo > 0:
            self.add_bullets(heldItems)
