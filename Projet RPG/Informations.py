from tkinter import *
#Dictionnaire des dialogues et informations pour le bon fonctionnement du jeu

infos_classes={'ninja':'Dégats: 20, Vie: 700, Vitesse: 25, Esquive: 30%,\n Chance de critiques: 50%',
            'warrior': 'Dégats: 20, Vie: 1200, \nVitesse: 20, esquive: "0%,\n Chance de critiques: 20% ',
            'skeleton':'(A plusieurs vies avec des\nstats qui diminuent a chaque mort):\n Dégats: 35, Vie: 180, Vitesse: 15,\n Esquive: 15%, \nChance de critiques: 75%, Réanimations: 5 ',}

classes = {'ninja': {'damages':20, 'PV':700, 'speed': 25, 'dodge':30, 'crit':50},
        'warrior': {'damages':20, 'PV':1200, 'speed': 20, 'dodge':20, 'crit':20},
        'skeleton': {'damages':35, 'PV':180, 'speed': 15, 'dodge':15, 'crit':75},
        "goblin":{'damages':10, 'PV':50, 'speed': 25, 'dodge':30, 'crit':50},
        "fire_spirit":{'damages':20, 'PV':30, 'speed': 50, 'dodge':30, 'crit':50},
        "rat":{'damages':20, 'PV':40, 'speed': 30, 'dodge':30, 'crit':50}
        }

infos_anim={"skeleton":{"attack":{"max_frame":18,"speed":100,"zoom":3},
                        "idle":{"max_frame":11,"speed":100,"zoom":3},
                        "hit":{"max_frame":8,"speed":100,"zoom":3}},

            "ninja":{"attack":{"max_frame":4,"speed":200,"zoom":3},
                        "idle":{"max_frame":4,"speed":200,"zoom":3}},

            "warrior":{"attack":{"max_frame":12,"speed":100,"zoom":2},
                        "idle":{"max_frame":6,"speed":150,"zoom":2}},

            "goblin":{"attack":{"max_frame":7,"speed":125,"zoom":2},
                        "idle":{"max_frame":4,"speed":200,"zoom":2}},

            "rat":{"attack":{"max_frame":15,"speed":100,"zoom":3},
                        "idle":{"max_frame":4,"speed":200,"zoom":3}},

            "fire_spirit":{"attack":{"max_frame":9,"speed":100,"zoom":3},
                        "idle":{"max_frame":6,"speed":200,"zoom":3}}}

lst_event = ["angry_mob", "passive_mob", "potion"]

bot_classes=["goblin", "fire_spirit", "rat"] 

biomes = ["ruines", "forest", "mountain"]

passive_mob_text = "Oh un ennemi !/n Mais il ne semble pas nous attaquer, que faire ?"

agressive_mob_text = "Oh un ennemi !/n Il nous attaque, nous devons nous défendre !"

potion_text = "Une potion ! Elle pourra surement nous être utile un jour !"

direction_text = "On arrive à un croisement. On va à gauche où à droite ?"