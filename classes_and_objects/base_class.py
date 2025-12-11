class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


class MasalaChai(Chai):
    
    """ Duplicancy

    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level
    """
    """ Explicit Code

    def __init__(self, type_, strength, spice_level):
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level
    """
    def __init__(self, type_, strength, spice_level):
        super().__init__(self, type_, strength)
        self.spice_level = spice_level