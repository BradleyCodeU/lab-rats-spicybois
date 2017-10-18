class Weight():
    def __init__(self, machine_name, machine_description, weight):
        self.machine_name = machine_name
        self.machine_description = machine_description
        self.weight = weight
        self.HP_per_rep = 10

    def get_weight(self,weight):
        return self.weight
        
    def get_machine_name(self,machine_name):
        return self.machine_name

    def get_HP_per_rep(self,HP_per_rep):
        return self.HP_per_rep

    def set_weight(self,newWeight):
        self.weight = newWeight

    def set_HP_per_rep(self,newHP_per_rep):
        self.HP_per_weight = newHP_per_rep

        
        
    
        
