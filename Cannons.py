import pygame

cannons = {
    "Cannon" : {
        "damage" : 5,
        "range" : 400,
        "reload" : 500,
        "bullet_size" : 5,
        "projectile_speed" : 300,
        "cost" : 0,
        "sprites" : {
            "up" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/cannon_up.png"), (75, 75)),
            "down" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/cannon_down.png"), (75, 75)),
            "left" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/cannon_left.png"), (75, 75)),
            "right" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/cannon_right.png"), (75, 75)),
            "bullet_image" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/bullet.png"), (50,50))
        },

    },
    "SniperCannon" : {
        "damage" : 15,
        "range" : 700,
        "reload" : 1400,
        "bullet_size" : 5,
        "projectile_speed" : 350,
        "cost" : 0,
        "sprites" : {
            "up" : pygame.transform.scale(pygame.image.load("assets/Tower/SniperCannon/sniper_cannon_up.png"), (80, 75)),
            "down" : pygame.transform.scale(pygame.image.load("assets/Tower/SniperCannon/sniper_cannon_down.png"), (80, 75)),
            "left" : pygame.transform.scale(pygame.image.load("assets/Tower/SniperCannon/sniper_cannon_left.png"), (80, 75)),
            "right" : pygame.transform.scale(pygame.image.load("assets/Tower/SniperCannon/sniper_cannon_right.png"), (80, 75)),
            "bullet_image" : pygame.transform.scale(pygame.image.load("assets/Tower/Cannon/bullet.png"), (40,40))
        },
    },
    "FireCannon" : {
        "damage" : 0,
        "range" : 100,
        "reload" : 700,
        "projectile_speed" : 100,
        "bullet_size" : 30,
        "cost" : 0,
        "fire_duration" : 3000,
        "fire_dps" : 2,
        "sprites" : {
            "up" :pygame.transform.scale(pygame.image.load("assets/Tower/FireCannon/fire_cannon_up.png"), (100, 100)),
            "down":pygame.transform.scale(pygame.image.load("assets/Tower/FireCannon/fire_cannon_up.png"), (100, 100)),
            "left":pygame.transform.scale(pygame.image.load("assets/Tower/FireCannon/fire_cannon_up.png"), (100, 100)),
            "right":pygame.transform.scale(pygame.image.load("assets/Tower/FireCannon/fire_cannon_up.png"), (100, 100)),
            "bullet_image" : pygame.transform.scale(pygame.image.load("assets/Tower/FireCannon/fire_bullet.png"), (75, 75))
        }
    }
}