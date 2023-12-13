@namespace
class SpriteKind:
    Plants = SpriteKind.create()
    pea = SpriteKind.create()
    shooter = SpriteKind.create()
    wall = SpriteKind.create()
    soon = SpriteKind.create()

def on_on_overlap(sprite4, otherSprite3):
    if controller.A.is_pressed():
        sprites.destroy(otherSprite3, effects.warm_radial, 100)
        info.change_score_by(25)
sprites.on_overlap(SpriteKind.player, SpriteKind.soon, on_on_overlap)

def on_a_pressed():
    global Peashooter, mySprite2, statusbar, Sunflower, mySprite3, SunFlower_HP, Wallnut, mySprite4, WallnutHp
    if game2 == 1:
        if tiles.tile_at_location_equals(tiles.get_tile_location(grid.sprite_col(mySprite), grid.sprite_row(mySprite)),
            assets.tile("""
                myTile5
            """)):
            if info.score() >= 100:
                mySprite.set_image(img("""
                    1 1 1 1 . . . . . . . . 1 1 1 1 
                                        1 e e e f . . . . . . . . . . 1 
                                        1 e e f f f f f f f . . . . . 1 
                                        1 f f f 7 7 7 7 7 f f . f . . 1 
                                        . . f 7 7 7 7 7 7 7 f f 7 f . . 
                                        . . f 7 7 f 7 7 f 7 f 7 f f . . 
                                        . . f 7 7 7 7 7 7 7 f 7 f f . . 
                                        . . f 7 7 7 7 7 7 7 f f 7 f . . 
                                        . . f f 7 7 7 7 7 f f . f . . . 
                                        . . . f f f f f f f . . . . . . 
                                        . . . . f e e e f . . . . . . . 
                                        . . . . . f f f . . . . . . . . 
                                        1 . . . . f 7 f . . . . . . . 1 
                                        1 . . f f f 7 f f f . . . . . 1 
                                        1 . f e f f 7 f f e f . . . . 1 
                                        1 1 1 1 e e f e e f . . 1 1 1 1
                """))
                Peashooter += 1
        if tiles.tile_at_location_equals(tiles.get_tile_location(grid.sprite_col(mySprite), grid.sprite_row(mySprite)),
            sprites.castle.tile_grass1):
            if Peashooter >= 1:
                mySprite2 = sprites.create(img("""
                        f f f f . . . . . . . . . . . . 
                                            f e e e f . . . . . . . . . . . 
                                            f e e f f f f f f f . . . . . . 
                                            . f f f 7 7 7 7 7 f f . f . . . 
                                            . . f 7 7 7 7 7 7 7 f f 7 f . . 
                                            . . f 7 7 f 7 7 f 7 f 7 f f . . 
                                            . . f 7 7 7 7 7 7 7 f 7 f f . . 
                                            . . f 7 7 7 7 7 7 7 f f 7 f . . 
                                            . . f f 7 7 7 7 7 f f . f . . . 
                                            . . . f f f f f f f . . . . . . 
                                            . . . . f e e e f . . . . . . . 
                                            . . . . . f f f . . . . . . . . 
                                            . . . . . f 7 f . . . . . . . . 
                                            . . . f f f 7 f f f . . . . . . 
                                            . . f e f f 7 f f e f . . . . . 
                                            . . . f e e f e e f . . . . . .
                    """),
                    SpriteKind.shooter)
                mySprite2.set_position(mySprite.x, mySprite.y)
                mySprite.set_image(img("""
                    1 1 1 1 . . . . . . . . 1 1 1 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        . . . . . . . . . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . 1 1 1 1 1 1 1 . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 1 1 1 . . . . . . . . 1 1 1 1
                """))
                statusbar = statusbars.create(20, 4, StatusBarKind.health)
                statusbar.max = 4
                statusbar.attach_to_sprite(mySprite2)
                statusbar.set_flag(SpriteFlag.INVISIBLE, True)
                info.change_score_by(-100)
                Peashooter = 0
        if tiles.tile_at_location_equals(tiles.get_tile_location(grid.sprite_col(mySprite), grid.sprite_row(mySprite)),
            assets.tile("""
                myTile7
            """)):
            if info.score() >= 50:
                mySprite.set_image(img("""
                    1 1 1 1 f f . f f f f . 1 1 1 1 
                                        1 . f 5 5 5 f 5 5 5 5 f . . . 1 
                                        1 f 5 5 f f f f f f f f f . . 1 
                                        1 f 5 f f e e e e e f f 5 f . 1 
                                        . f 5 f e e e e e e e f 5 f . . 
                                        . . f f e f e e e f e f 5 f . . 
                                        . f 5 f e e e e e e e f f . . . 
                                        . f 5 f e f e e e f e f 5 f . . 
                                        . f 5 f e e f f f e e f 5 f . . 
                                        . . f 5 f e e e e e f 5 5 f . . 
                                        . . . f f f f f f f f f f . . . 
                                        . . . . . . f f f . . . . . . . 
                                        1 . . . . . f 7 f . . . . . . 1 
                                        1 . . . f f f 7 f f f . . . . 1 
                                        1 . . f e f f 7 f f e f . . . 1 
                                        1 1 1 1 f e e f e e f . 1 1 1 1
                """))
                Sunflower += 1
        if tiles.tile_at_location_equals(tiles.get_tile_location(grid.sprite_col(mySprite), grid.sprite_row(mySprite)),
            sprites.castle.tile_grass1):
            if Sunflower >= 1:
                mySprite3 = sprites.create(img("""
                        . . . f f f . f f f f . . . . . 
                                            . . f 5 5 5 f 5 5 5 5 f . . . . 
                                            . f 5 5 f f f f f f f f f . . . 
                                            . f 5 f f e e e e e f f 5 f . . 
                                            . f 5 f e e e e e e e f 5 f . . 
                                            . . f f e f e e e f e f 5 f . . 
                                            . f 5 f e e e e e e e f f . . . 
                                            . f 5 f e f e e e f e f 5 f . . 
                                            . f 5 f e e f f f e e f 5 f . . 
                                            . . f 5 f e e e e e f 5 5 f . . 
                                            . . . f f f f f f f f f f . . . 
                                            . . . . . . f f f . . . . . . . 
                                            . . . . . . f 7 f . . . . . . . 
                                            . . . . f f f 7 f f f . . . . . 
                                            . . . f e f f 7 f f e f . . . . 
                                            . . . . f e e f e e f . . . . .
                    """),
                    SpriteKind.Plants)
                mySprite3.set_position(mySprite.x, mySprite.y)
                mySprite.set_image(img("""
                    1 1 1 1 . . . . . . . . 1 1 1 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        . . . . . . . . . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . 1 1 1 1 1 1 1 . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 1 1 1 . . . . . . . . 1 1 1 1
                """))
                SunFlower_HP = statusbars.create(20, 4, StatusBarKind.health)
                SunFlower_HP.max = 4
                SunFlower_HP.attach_to_sprite(mySprite3)
                SunFlower_HP.set_flag(SpriteFlag.INVISIBLE, True)
                Sunflower = 0
                info.change_score_by(-50)
        if tiles.tile_at_location_equals(tiles.get_tile_location(grid.sprite_col(mySprite), grid.sprite_row(mySprite)),
            assets.tile("""
                myTile8
            """)):
            if info.score() >= 50:
                mySprite.set_image(img("""
                    1 1 1 1 . . . . . . . . 1 1 1 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . f f f f f . . . . . 1 
                                        . . . . f f 4 4 4 f f . . . . . 
                                        . . . f f 4 4 4 4 4 f f . . . . 
                                        . . . f 4 4 4 4 4 4 4 f . . . . 
                                        . . f f 4 4 f 4 4 f 4 f f . . . 
                                        . . f 4 4 4 4 4 4 4 4 4 f . . . 
                                        . . f 4 4 4 4 4 4 4 4 4 f . . . 
                                        . . f 4 4 f 4 4 4 4 f 4 f . . . 
                                        . . f 4 4 4 f f f f 4 4 f . . . 
                                        1 . f 4 4 4 4 4 4 4 4 4 f . . 1 
                                        1 . f 4 4 4 4 4 4 4 4 4 f . . 1 
                                        1 . f f 4 4 4 4 4 4 4 f f . . 1 
                                        1 1 1 1 f f f f f f f f 1 1 1 1
                """))
                Wallnut += 1
        if tiles.tile_at_location_equals(tiles.get_tile_location(grid.sprite_col(mySprite), grid.sprite_row(mySprite)),
            sprites.castle.tile_grass1):
            if Wallnut >= 1:
                mySprite4 = sprites.create(img("""
                        . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . f f f f f . . . . . . 
                                            . . . . f f 4 4 4 f f . . . . . 
                                            . . . f f 4 4 4 4 4 f f . . . . 
                                            . . . f 4 4 4 4 4 4 4 f . . . . 
                                            . . f f 4 4 f 4 4 f 4 f f . . . 
                                            . . f 4 4 4 4 4 4 4 4 4 f . . . 
                                            . . f 4 4 4 4 4 4 4 4 4 f . . . 
                                            . . f 4 4 f 4 4 4 4 f 4 f . . . 
                                            . . f 4 4 4 f f f f 4 4 f . . . 
                                            . . f 4 4 4 4 4 4 4 4 4 f . . . 
                                            . . f 4 4 4 4 4 4 4 4 4 f . . . 
                                            . . f f 4 4 4 4 4 4 4 f f . . . 
                                            . . . f f f f f f f f f . . . .
                    """),
                    SpriteKind.wall)
                mySprite4.set_position(mySprite.x, mySprite.y)
                mySprite.set_image(img("""
                    1 1 1 1 . . . . . . . . 1 1 1 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        . . . . . . . . . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . 1 1 1 1 1 1 1 . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        . . . . . . . 1 . . . . . . . . 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 . . . . . . . . . . . . . . 1 
                                        1 1 1 1 . . . . . . . . 1 1 1 1
                """))
                WallnutHp = statusbars.create(20, 4, StatusBarKind.health)
                WallnutHp.value = 100
                WallnutHp.attach_to_sprite(mySprite4)
                WallnutHp.set_flag(SpriteFlag.INVISIBLE, True)
                info.change_score_by(-50)
                Wallnut = 0
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite, otherSprite):
    sprite.set_velocity(0, 0)
    statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite).value += -0.05
    if statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite).value == 0:
        sprite.set_velocity(0, -3)
        sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.Plants, on_on_overlap2)

def on_countdown_end():
    global wave, P2
    m = 0
    if m != 1:
        wave = 1
    else:
        P2 = 1
info.on_countdown_end(on_countdown_end)

def on_overlap_tile(sprite5, location2):
    game.over(False)
scene.on_overlap_tile(SpriteKind.enemy,
    assets.tile("""
        myTile6
    """),
    on_overlap_tile)

def wave1():
    global mySprite5, ZombieHp
    mySprite5 = sprites.create(img("""
            . . . f f f f f . . . . 
                    . . f e e e e e f f . . 
                    . f e e e e e e e f f . 
                    f e e e e e e e f f f f 
                    f e e 7 e e e f f f f f 
                    f e e 7 7 e e e f f f f 
                    f f e 7 7 7 7 7 f f f f 
                    f f e 7 7 f f 7 e 7 f f 
                    . f f 7 7 7 7 7 7 7 f . 
                    . . f b b 7 7 7 f f f . 
                    . . f 1 2 e e e e f . . 
                    . . f 2 e e e 7 7 f . . 
                    . . f 1 e e e 7 7 e . . 
                    . . f 8 8 8 f e e f . . 
                    . . . f f f f f f . . . 
                    . . . . . f f f . . . .
        """),
        SpriteKind.enemy)
    grid.snap(mySprite5)
    grid.place(mySprite5, tiles.get_tile_location(9, randint(1, 5)))
    mySprite5.vx = -3
    ZombieHp = statusbars.create(20, 4, StatusBarKind.enemy_health)
    ZombieHp.value = 10
    ZombieHp.attach_to_sprite(mySprite5)
    ZombieHp.set_flag(SpriteFlag.INVISIBLE, True)

def on_overlap_tile2(sprite2, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.enemy,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile2)

def on_on_overlap3(sprite8, otherSprite5):
    global kill
    sprites.destroy(sprite8)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite5).value += -1
    if statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite5).value == 0:
        sprites.destroy(otherSprite5)
        kill += 1
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def on_on_overlap4(sprite3, otherSprite2):
    sprite3.set_velocity(0, 0)
    statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite2).value += -0.05
    if statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite2).value == 0:
        sprite3.set_velocity(0, -3)
        sprites.destroy(otherSprite2)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.shooter, on_on_overlap4)

def on_on_overlap5(sprite6, otherSprite4):
    sprite6.set_velocity(0, 0)
    statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite4).value += -0.05
    if statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite4).value == 0:
        sprite6.set_velocity(0, -3)
        sprites.destroy(otherSprite4)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.wall, on_on_overlap5)

projectile: Sprite = None
sun: Sprite = None
ZombieHp: StatusBarSprite = None
mySprite5: Sprite = None
P2 = 0
wave = 0
WallnutHp: StatusBarSprite = None
mySprite4: Sprite = None
SunFlower_HP: StatusBarSprite = None
mySprite3: Sprite = None
statusbar: StatusBarSprite = None
mySprite2: Sprite = None
kill = 0
Wallnut = 0
Sunflower = 0
Peashooter = 0
mySprite: Sprite = None
game2 = 0
player22 = None
scene.set_background_image(img("""
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7776677777777767777777777777777777777777777667777777776777777777777777777777777777766777777777677777777777777777777777777776677777777767777777777777777777777777
        7666777777777667777777777777777777777767766677777777766777777777777777777777776776667777777776677777777777777777777777677666777777777667777777777777777777777767
        7767766777667766777766777777777777777766776776677766776677776677777777777777776677677667776677667777667777777777777777667767766777667766777766777777777777777766
        6666667767766766776766777777777777776676666666776776676677676677777777777777667666666677677667667767667777777777777766766666667767766766776766777777777777776676
        6666677766766666766667777777777777666677666667776676666676666777777777777766667766666777667666667666677777777777776666776666677766766666766667777777777777666677
        6666676666666676666677767777776667776667666667666666667666667776777777666777666766666766666666766666777677777766677766676666676666666676666677767777776667776667
        6666666666666776677666667766677766777666666666666666677667766666776667776677766666666666666667766776666677666777667776666666666666666776677666667766677766777666
        6666666666666766667766677677667766666666666666666666676666776667767766776666666666666666666667666677666776776677666666666666666666666766667766677677667766666666
        66b666666666666666666667667776676666666666b666666666666666666667667776676666666666b666666666666666666667667776676666666666b6666666666666666666676677766766666666
        66b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b67766666666666
        66b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb6766666666666
        66b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb666666666666
        66b66666699dbb666666dd9666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb666666666666
        6bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb666666666666
        6bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb66666666666
        6bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb66666666666
        bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666
        bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666
        bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666
        bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966
        bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996
        bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999
        bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999
        bb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999b
        bb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999b
        bb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999b
        b9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99b
        b9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99b
        b9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bb
        b9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbb
        dd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbb
        9d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb9
        9d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb99
        9d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb999
        9dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd99
        99dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd99
        99ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd9
        9999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d9
        9999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d9
        999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd
        d9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999d
        dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999
        dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
        9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
        ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999
        dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999
        dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
        dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
        dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999
        d99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999d
        d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
        d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
        999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
        999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
        999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9
        9999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd9
        d999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbdddddddd
        ddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbddddddd
        dddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddd
        ddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbddddddd
        ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
        ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
        dddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        ddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbddddd
        dddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddd
        ddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777dddd
        dddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dd
        ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
"""))
pause(2000)
story.print_character_text("Bienvenido a Plantas vs Zombies", "Daniel Reinosa")
pause(2000)
story.show_player_choices("play", "info")
if story.check_last_answer("play"):
    game2 = 1
    scene.set_background_image(img("""
        ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
    """))
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    scene.set_background_color(7)
    scene.camera_follow_sprite(mySprite)
    mySprite = sprites.create(img("""
            1 1 1 1 . . . . . . . . 1 1 1 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 1 . . . . . . . . 
                    . . . . . . . 1 . . . . . . . . 
                    . . . . . . . 1 . . . . . . . . 
                    . . . . 1 1 1 1 1 1 1 . . . . . 
                    . . . . . . . 1 . . . . . . . . 
                    . . . . . . . 1 . . . . . . . . 
                    . . . . . . . 1 . . . . . . . . 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 1 1 1 . . . . . . . . 1 1 1 1
        """),
        SpriteKind.player)
    grid.snap(mySprite)
    grid.move_with_buttons(mySprite)
    grid.place(mySprite, tiles.get_tile_location(0, 0))
    Peashooter = 0
    Sunflower = 0
    Wallnut = 0
    kill = 0
    info.set_score(50)
    info.start_countdown(60)
if story.check_last_answer("info"):
    story.print_character_text("El juego consitste de 3 elementos, soles para puntos,lanzadores para atacar y muros para defender.",
        "Daniel Reinosa")

def on_update_interval():
    global sun
    for value in sprites.all_of_kind(SpriteKind.Plants):
        animation.run_image_animation(value,
            [img("""
                    . . . f f f . f f f f . . . . . 
                                . . f 1 1 1 f 1 1 1 1 f . . . . 
                                . f 1 1 f f f f f f f f f . . . 
                                . f 1 f f d d d d d f f 1 f . . 
                                . f 1 f d d d d d d d f 1 f . . 
                                . . f f d f d d d f d f 1 f . . 
                                . f 1 f d d d d d d d f f . . . 
                                . f 1 f d f d d d f d f 1 f . . 
                                . f 1 f d d f f f d d f 1 f . . 
                                . . f 1 f d d d d d f 1 1 f . . 
                                . . . f f f f f f f f f f . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . f 7 f . . . . . . . 
                                . . . . f f f 7 f f f . . . . . 
                                . . . f e f f 7 f f e f . . . . 
                                . . . . f e e f e e f . . . . .
                """),
                img("""
                    . . . f f f . f f f f . . . . . 
                                . . f 5 5 5 f 5 5 5 5 f . . . . 
                                . f 5 5 f f f f f f f f f . . . 
                                . f 5 f f e e e e e f f 5 f . . 
                                . f 5 f e e e e e e e f 5 f . . 
                                . . f f e f e e e f e f 5 f . . 
                                . f 5 f e e e e e e e f f . . . 
                                . f 5 f e f e e e f e f 5 f . . 
                                . f 5 f e e f f f e e f 5 f . . 
                                . . f 5 f e e e e e f 5 5 f . . 
                                . . . f f f f f f f f f f . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . f 7 f . . . . . . . 
                                . . . . f f f 7 f f f . . . . . 
                                . . . f e f f 7 f f e f . . . . 
                                . . . . f e e f e e f . . . . .
                """)],
            700,
            False)
        sun = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 5 . 5 . 5 . . . . . . 
                            . . . 5 . 5 5 5 5 5 5 . 5 . . . 
                            . . . . 5 5 5 5 5 5 5 5 . . . . 
                            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                            . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                            . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                            . . . . 5 5 5 5 5 5 5 5 . . . . 
                            . . . 5 . 5 5 5 5 5 5 . 5 . . . 
                            . . . . . 5 . 5 . 5 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            value,
            0,
            0)
        sun.set_kind(SpriteKind.soon)
game.on_update_interval(15000, on_update_interval)

def on_update_interval2():
    global projectile
    for value2 in sprites.all_of_kind(SpriteKind.shooter):
        projectile = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . f f f . . . . . . . 
                            . . . . . f 7 7 7 f . . . . . . 
                            . . . . . f 7 7 7 f . . . . . . 
                            . . . . . f 7 7 7 f . . . . . . 
                            . . . . . . f f f . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.projectile)
        projectile.set_position(value2.x, value2.x)
        projectile.set_velocity(50, 0)
        projectile.lifespan = 2000
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    global sun
    sun = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 5 . 5 . 5 . . . . . . 
                    . . . 5 . 5 5 5 5 5 5 . 5 . . . 
                    . . . . 5 5 5 5 5 5 5 5 . . . . 
                    . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                    . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                    . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                    . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                    . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                    . . . . 5 5 5 5 5 5 5 5 . . . . 
                    . . . 5 . 5 5 5 5 5 5 . 5 . . . 
                    . . . . . 5 . 5 . 5 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.soon)
    grid.place(sun, tiles.get_tile_location(randint(3, 10), 0))
    sun.set_velocity(0, 3)
game.on_update_interval(20000, on_update_interval3)

def on_update_interval4():
    if wave == 1:
        wave1()
    if kill == 20:
        game.game_over(True)
game.on_update_interval(10000, on_update_interval4)
