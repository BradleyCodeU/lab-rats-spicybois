 class Chainsaw():
    def __init__(self,condition,model,gas):
        self.conditon = condition
        self.model = ripper
        self.gas = 0

    def get_interface(self,heldItems,current_room):
        if gas == 0 and "GAS" in heldItems:
            print("You can POUR GAS TO "+self.model())
        elif gas == 0:
            print("The tank is empty.")

    def check_input(self,command,heldItems,current_room):
        if command == "POUR GAS TO"+self.model() and self.gas == 0 and "gas" in heldItems:
            self.add_gas(heldItems)
