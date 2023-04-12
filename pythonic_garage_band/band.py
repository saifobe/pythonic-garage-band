from abc import ABC, abstractmethod

class Musician:
    def __init__(self ,name) :
        self.name = name
        
        
        
    @abstractmethod 
    def play_solo(self):
        pass
    
    @abstractmethod 
    def get_instrument(self):
        pass

class Guitarist(Musician):
    def __init__(self ,name) :
        self.instrument = 'guitar'
        super().__init__(name)

    def get_instrument(self):
        return f'{self.instrument}'
    
    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'
    
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    
    def play_solo(self):
        return f'face melting guitar solo'
    
class Bassist(Musician):
    def __init__(self ,name ) :
        self.instrument = 'bass'
        super().__init__(name)
    
    def get_instrument(self):
        return f'{self.instrument}'
    
    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'
    
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    
    def play_solo(self):
        return f'bom bom buh bom'
    
class Drummer(Musician):
        def __init__(self ,name) :
            self.instrument = 'drums'
            super().__init__(name)

        def get_instrument(self):
            return f'{self.instrument}'
        
        def __str__(self):
            return f'My name is {self.name} and I play {self.instrument}'
        
        def __repr__(self):
            return f'Drummer instance. Name = {self.name}'
        
        def play_solo(self):
            return f'rattle boom crash'
        
class Band:
    instances = []
    def __init__(self ,name ,members) :
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f'Hi, we are {self.name} and we are a band'
    
    def __repr__(self):
        return f'{self.members} instance. Name = {self.name}'
    
    def play_solos(self):
        members = []
        for member in self.members:
            members.append(member.play_solo())
        return members
    
    @classmethod
    def to_list(cls):
        return cls.instances
    

    

    



        

        

        
    
    
    

        

    
    


     


