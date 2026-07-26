import pygame

cannons = {
    "Cannon" : {
        "damage" : 5,
        "range" : 150,
        "reload" : 500,
        "cost" : 5,
        "sprites" : {
            "up" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/cannon_up.png"), (75, 75)),
            "down" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/cannon_down.png"), (75, 75)),
            "left" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/cannon_left.png"), (75, 75)),
            "right" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/cannon_right.png"), (75, 75))
        }
    },
    "SniperCannon" : {
        "damage" : 15,
        "range" : 300,
        "reload" : 1000,
        "cost" : 10,
        "sprites" : {
            "up" : pygame.transform.scale(pygame.image.load("assets/Tower/SniperCannon/sniper_cannon_up.png"), (80, 75)),
            "down" : pygame.transform.scale(pygame.image.load("assets/Tower/SniperCannon/sniper_cannon_down.png"), (80, 75)),
            "left" : pygame.transform.scale(pygame.image.load("assets/Tower/SniperCannon/sniper_cannon_left.png"), (80, 75)),
            "right" : pygame.transform.scale(pygame.image.load("assets/Tower/SniperCannon/sniper_cannon_right.png"), (80, 75))
        }
    }
}