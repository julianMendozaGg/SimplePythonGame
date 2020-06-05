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


class leftGoku(left):
    def get_sprites(self):
        return[loadImages.load("gokuSprites/GI1.png"),
               loadImages.load("gokuSprites/GI2.png"),
               loadImages.load("gokuSprites/GI3.png"),
               loadImages.load("gokuSprites/GI4.png"),
               loadImages.load("gokuSprites/GI5.png"),
               loadImages.load("gokuSprites/GI6.png"),
               loadImages.load("gokuSprites/GN.png")]

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


class rightGoku(right):
    def get_sprites(self):
        return[loadImages.load("gokuSprites/GD1.png"),
               loadImages.load("gokuSprites/GD2.png"),
               loadImages.load("gokuSprites/GD3.png"),
               loadImages.load("gokuSprites/GD4.png"),
               loadImages.load("gokuSprites/GD5.png"),
               loadImages.load("gokuSprites/GD6.png"),
               loadImages.load("gokuSprites/GN.png")]

# Producto Abstracto up


class up():
    def get_sprites(self): pass


class upMegaman(up):
    def get_sprites(self):
        return[loadImages.load("megSprites/MD1.png"),
               loadImages.load("megSprites/U1.png"),
               loadImages.load("megSprites/U2.png")]


class upGoku(up):
    def get_sprites(self):
        return []
# Producto Abstracto down


class down():
    def get_sprites(self): pass


class downMegaman():
    def get_sprites(self):
        return[loadImages.load("megSprites/D1.png"),
               loadImages.load("megsprites/MD1.png")]


class downGoku(down):
    def get_sprites(self):
        return []
# Producto Abstracto space


class power():
    def get_sprites(self): pass


class powerMegaman():
    def get_sprites(self):
        return[loadImages.load("megSprites/MD1.png"),
               loadImages.load("megSprites/P1.png"),
               loadImages.load("megsprites/P2.png"),
               loadImages.load("megsprites/P3.png")]


class powerGoku(power):
    def get_sprites(self):
        return[loadImages.load("gokuSprites/GP1.png"),
               loadImages.load("gokuSprites/GP2.png"),
               loadImages.load("gokuSprites/GN.png")]
