from Factories import*


# Nuestro constructor
class Builder():
    def get_sprites(self): pass
    def set_sprites(self): pass


# Nuestro constructor concreto
class MegamanBuilder():
    def __init__(self):
        self.factory = MegamanSpritesFactory()

    def get_sprites(self):
        return [self.factory.moveLeft(),
                self.factory.moveRight(),
                self.factory.moveUp(),
                self.factory.moveDown(),
                self.factory.power()]


class GokuBuilder():
    def __init__(self):
        self.factory = GokuSpritesFactory()

    def get_sprites(self):
        return [self.factory.moveLeft(),
                self.factory.moveRight(),
                self.factory.moveUp(),
                self.factory.moveDown(),
                self.factory.power()]
