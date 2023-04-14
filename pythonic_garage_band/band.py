from abc import ABC, abstractmethod

class Musician(ABC):
    """
    An abstract base class representing a musician.

    Attributes:
        name (str): The name of the musician.
    """

    def __init__(self, name):
        """
        Initializes a new Musician object with the given name.

        Args:
            name (str): The name of the musician.
        """
        self.name = name

    @abstractmethod 
    def play_solo(self):
        """
        Abstract method to play a solo.
        """
        pass
    
    @abstractmethod 
    def get_instrument(self):
        """
        Abstract method to get the instrument played by the musician.

        Returns:
            str: The instrument played by the musician.
        """
        pass


class Guitarist(Musician):
    """
    A class representing a guitarist, which is a subclass of Musician.

    Attributes:
        name (str): The name of the guitarist.
        instrument (str): The type of instrument played by the guitarist (guitar).
    """
    def __init__(self, name):
        """
        Initializes a new Guitarist object with the given name.

        Args:
            name (str): The name of the guitarist.
        """
        self.instrument = 'guitar'
        super().__init__(name)

    def get_instrument(self):
        """
        Returns the type of instrument played by the guitarist.

        Returns:
            str: The type of instrument played by the guitarist (guitar).
        """
        return f'{self.instrument}'
    
    def __str__(self):
        """
        Returns a string representation of the guitarist.

        Returns:
            str: A string representation of the guitarist in the format "My name is {name} and I play {instrument}".
        """
        return f'My name is {self.name} and I play {self.instrument}'
    
    def __repr__(self):
        """
        Returns a string representation of the guitarist.

        Returns:
            str: A string representation of the guitarist in the format "Guitarist instance. Name = {name}".
        """
        return f'Guitarist instance. Name = {self.name}'
    
    def play_solo(self):
        """
        Plays a guitar solo.

        Returns:
            str: A string representing the guitar solo ("face melting guitar solo").
        """
        return f'face melting guitar solo'

    
class Bassist(Musician):
    """
    A class representing a bassist musician.

    Args:
        name (str): The name of the bassist.

    Attributes:
        instrument (str): The instrument played by the bassist.
        name (str): The name of the bassist.
    """

    def __init__(self, name):
        """
        Initializes a new Bassist object with the given name.

        Args:
            name (str): The name of the bassist.
        """
        self.instrument = 'bass'
        super().__init__(name)

    def get_instrument(self):
        """
        Gets the instrument played by the bassist.

        Returns:
            str: The instrument played by the bassist.
        """
        return f'{self.instrument}'

    def __str__(self):
        """
        Returns a string representation of the bassist.

        Returns:
            str: The string representation of the bassist.
        """
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        """
        Returns a string representation of the bassist.

        Returns:
            str: The string representation of the bassist.
        """
        return f'Bassist instance. Name = {self.name}'

    def play_solo(self):
        """
        Plays a bass solo.

        Returns:
            str: The bass solo played by the bassist.
        """
        return f'bom bom buh bom'

    
class Drummer(Musician):
    """
    A class representing a drummer.

    Attributes:
        name (str): The name of the drummer.
        instrument (str): The instrument played by the drummer, which is always "drums".
    """

    def __init__(self, name):
        """
        Initializes a new Drummer object with the given name.

        Args:
            name (str): The name of the drummer.
        """
        self.instrument = 'drums'
        super().__init__(name)

    def get_instrument(self):
        """
        Returns the instrument played by the drummer.

        Returns:
            str: The instrument played by the drummer, which is always "drums".
        """
        return f'{self.instrument}'
        
    def __str__(self):
        """
        Returns a string representation of the Drummer object.

        Returns:
            str: A string representation of the form "My name is <name> and I play drums".
        """
        return f'My name is {self.name} and I play {self.instrument}'
        
    def __repr__(self):
        """
        Returns a string representation of the Drummer object.

        Returns:
            str: A string representation of the form "Drummer instance. Name = <name>".
        """
        return f'Drummer instance. Name = {self.name}'
        
    def play_solo(self):
        """
        Plays a solo on the drums.

        Returns:
            str: A string representing the solo played by the drummer.
        """
        return f'rattle boom crash'

        
class Band:
    instances = []
    def __init__(self ,name ,members) :
        """
        A class representing a music band.
        param name: The name of the band.
        type name: str
        param members: A list of musicians in the band.
        type members: list
        """
        self.name = name
        self.members = members
        Band.instances.append(self)


    def __str__(self):
        """
        Returns a string representing the band.

        :return: A string containing the name of the band.
        :rtype: str
        """
        return f'Hi, we are {self.name} and we are a band'
    
    def __repr__(self):
        """
        Returns a string representation of the Band object.

        :return: A string representation of the Band object.
        :rtype: str
        """
        return f'{self.members} instance. Name = {self.name}'
    
    def play_solos(self):
        """
        Calls the play_solo method of each member of the band.

        :return: A list of strings representing the solos played by each band member.
        :rtype: list
        """
        members = []
        for member in self.members:
            members.append(member.play_solo())
        return members
    
    @classmethod
    def to_list(cls):
        """
        Returns a list of all Band instances.

        return: A list of all Band instances.
        return type: list
        """
        return cls.instances
    

    

    



        

        

        
    
    
    

        

    
    


     


