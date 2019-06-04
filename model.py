"""
 Commentaire principal
   sur deux lignes Special kind :-)
   
   
     Main abstraction for fruits
"""

class Fruit(object):
    def __init__(self):
        self.quantity = 0
        
        
    # Start of user code -> properties/constructors for Fruit class

    # End of user code
    def price(self):
        # Start of user code protected zone for price function body
        return 0.
        # End of user code	
    # Start of user code -> methods for Fruit class

    # End of user code


class Pomme(Fruit):
    pass
    # Start of user code -> properties/constructors for Pomme class

    # End of user code
    # Start of user code -> methods for Pomme class

    # End of user code

class Golden(Pomme):
    pass
    # Start of user code -> properties/constructors for Golden class

    # End of user code
    # Start of user code -> methods for Golden class

    # End of user code

class Poire(Fruit):
    pass
    # Start of user code -> properties/constructors for Poire class

    # End of user code
    # Start of user code -> methods for Poire class

    # End of user code

class BelleHelene(Poire):
    """
     <p>Pas trop de vanille mais beaucoup de chocolat.<br />
       Reste &agrave; voir ce que cela donne en go&ucirc;t...</p>
       
       <p>Fin des commentaires</p>
       
       <p>&nbsp;</p>
       
    """
    def __init__(self):
        self.cream = False
        self.vanilla = False
        
        
    # Start of user code -> properties/constructors for BelleHelene class
        self._cache = []

    # End of user code
    def price(self):
        # Start of user code protected zone for price function body
        return 0.
        # End of user code	
    # Start of user code -> methods for BelleHelene class

    def misc(self):
        pass
    # End of user code

class Williams(Poire):
    pass
    # Start of user code -> properties/constructors for Williams class

    # End of user code
    # Start of user code -> methods for Williams class

    # End of user code

class Reinette(Pomme):
    pass
    # Start of user code -> properties/constructors for Reinette class

    # End of user code
    # Start of user code -> methods for Reinette class

    # End of user code


# Start of user code -> functions/methods for model package

# End of user code
