import loadImages
# Esta es nustra clase productos donde cada prducto concreto nos retorna una lista de sprites del personaje

# Producto Abstracto left


class left():
    def get_sprites(self): pass


class leftMegaman(left):
    def get_sprites(self):
        return[loadImages.load("megSprites/MI1.png"),
               loadImages.load("megSprites/MI2.png"),
               loadImages.load("megSprites/MI3.png"),
               loadImages.load("megSprites/MI4.png"),
               loadImages.load("megSprites/MI5.png"),
               loadImages.load("megSprites/MI6.png"),
               loadImages.load("megSprites/MI7.png")]

# Producto Abstracto right


class right():
    def get_sprites(self): pass


class rightMegaman(right):
    def get_sprites(self):
        return [loadImages.load("megSprites/MD1.png"),
                loadImages.load("megSprites/MD2.png"),
                loadImages.load("megSprites/MD3.png"),
                loadImages.load("megSprites/MD4.png"),
                loadImages.load("megSprites/MD5.png"),
                loadImages.load("megSprites/MD6.png"),
                loadImages.load("megSprites/MD7.png")]
