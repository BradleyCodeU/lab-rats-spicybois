class HealthPotion():
    #Constructs a name, the amount in the potion, and if it is large or small
    def __init__(self, name, contain, category):
        self.name = name
        self.contain = contain
        self.category = category
    #Sets what kind of potion it is
    def get_potion_type(self):
        if self.category > 50:
            print("Congrats! You found a large potion! This heals for 50 health.")
        elif self.category < 50:
            print("A small potion heals for 25 helath.")
        else self.category == 0:
            print("Not your lucky day... there is no health potion...")

    #Sets the amount of the potion inside
    def get_amount(self):
        
        
        
        
            
            
        
