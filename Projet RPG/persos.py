from Informations import *
from random import randint, choice

need_dir_menu = False
potion_heal = 50
dialogue_box_text = ""

#creation classe personnage parent 
class Personnage:
    def __init__(self,classe):
        self.classe = classe
        self.current_anim = "idle"

#creation classe player
class Player(Personnage):
    def __init__(self, classe,name):
        super().__init__(classe)
        self.max_health = classes[classe]["PV"]
        self.pv = self.max_health 
        self.attack_damages = classes[classe]["damages"]
        self.speed = classes[classe]["speed"]  #vitesse d'attaque
        self.current_speed = 0 #Vitesse actuelle
        self.dodge = classes[classe]["dodge"] #proba d'esquive
        self.crit = classes[classe]["crit"]    #proba de coup critique
        self.name = name
        self.pot_nb = 1

        if self.classe == "skeleton": #si classe = skeleton alors on lui donne des réanimations
            self.reanimations = 5

    #test si le joueur est en vie
    def is_alive(self):
        if self.pv <=0:
            is_alive = False
        else:
            is_alive = True
        return is_alive

    def attack(self,persob): #attaque du player
        global dialogue_box_text
        #L'ennemi ne peut pas esquiver un crit
        crit = randint(0,100)
        is_enemy_dodging = randint(0,100)
        if crit <= self.crit:#si dans les probas de critique
            persob.pv -= self.attack_damages *2 #crit = 2x attack dammages
            dialogue_box_text = f"Vous infligez un coup critique à l'ennemi -{self.attack_damages *2} PV pour l'adversaire! \n il a {persob.pv} PV et vous en avez {self.pv}"
            
        else:
            if is_enemy_dodging <= persob.dodge:
                #L'ennemi esquive l'attaque
                dialogue_box_text = "L'adversaire à esquivé votre attaque"

            else:
                #on met des dégats à l'adversaire
                persob.pv -= self.attack_damages
                dialogue_box_text = f"Vous attaquez l'ennemi -{self.attack_damages} PV pour l'adversaire! \n il a {persob.pv} PV et vous en avez {self.pv}"
        if persob.pv <=0:#dans le cas ou on vainc l'ennemi
            dialogue_box_text = "Vous avez vaincu l'ennemi"
        return dialogue_box_text

    #si on a besoin de revive le player (avec des stats qui baissent)
    def revive(self):
        if self.reanimations > 0:
            self.max_health -= 0.1 * self.max_health
            self.pv = self.max_health
            self.attack_damages -= 0.1 * self.attack_damages
            self.speed -= 0.1 * self.speed
            self.dodge -= 0.1 * self.dodge
            self.crit -= 0.1 * self.crit
        else:
            pass

    #pour heal le player
    def heal(self):
        self.pot_nb -=1
        if self.pv +potion_heal > self.max_health:
            self.pv += self.max_health - self.pv
        else:
            self.pv += potion_heal

#classe bot 
class Bot(Personnage):
    def __init__(self, classe):
        super().__init__(classe)
        self.max_health = classes[classe]["PV"]
        self.pv = self.max_health 
        self.attack_damages = classes[classe]["damages"]
        self.speed = classes[classe]["speed"]  #vitesse d'attaque
        self.current_speed = 0 #Vitesse actuelle
        self.dodge = classes[classe]["dodge"] #proba d'esquive
        self.crit = classes[classe]["crit"]    #proba de coup critique

    #idem
    def is_alive(self):
        if self.pv <=0:
            is_alive = False
        else:
            is_alive = True
        return is_alive

    #idem
    def attack(self,persob): #attaque du bot
        global dialogue_box_text
        #L'ennemi ne peut pas esquiver un crit
        crit = randint(0,100)
        is_enemy_dodging = randint(0,100)
        if crit <= self.crit:#si dans les probas de critique
            persob.pv -= self.attack_damages *2 #crit = 2x attack dammages
            dialogue_box_text = f"L'ennemi vous inflige un coup critique -{self.attack_damages *2} PV! \n il a {self.pv} PV et vous en avez {persob.pv}"
        else:
            if is_enemy_dodging > persob.dodge:
                #L'ennemi esquive l'attaque, mettre un texte dans la boite de dialogue
                dialogue_box_text = "Vous esquivez l'attaque adverse !"

            else:
                persob.pv -= self.attack_damages
                dialogue_box_text = f"L'ennemi vous attaque -{self.attack_damages} PV! \n il a {self.pv} PV et vous en avez {persob.pv}"
        return dialogue_box_text



def choose_direction(direction1): #calcule la proba de pouvoir aller dans certains biomes (ruines = plus rare)
    direction = None
    while direction != "ruines" or direction != "mountain" or direction != "forest":
        direction = randint(1,100)
        if 1<=direction<=15 and direction1 != "ruines":
            direction = "ruines" 
            return direction 
        elif 16<=direction<=50 and direction1 != "mountain":
            direction = "mountain"
            return direction 
        elif 51<=direction<=100 and direction1!= "forest":
            direction = "forest"
            return direction 
    
def create_mob(biome): #creer un mob en fonction de sa proba de spawn dans le biome en question
    """agressive: True = agressif, False = passif"""
    classe_mob = randint(1,100)

    if biome == "mountain":
        if 1<=classe_mob <= 65:
            classe_mob = "rat"
        elif 66 <= classe_mob <= 80:
            classe_mob = "goblin"
        elif 81 <= classe_mob <= 100:
            classe_mob = "fire_spirit"
    elif biome == "forest":
        if 1<=classe_mob <= 10:
            classe_mob = "rat"
        elif 11 <= classe_mob <= 80:
            classe_mob = "goblin"
        elif 81 <= classe_mob <= 100:
            classe_mob = "fire_spirit"
    else:
        if 81<=classe_mob <= 92:
            classe_mob = "rat"
        elif 93 <= classe_mob <= 100:
            classe_mob = "goblin"
        elif 1 <= classe_mob <= 80:
            classe_mob = "fire_spirit"

    return Bot(classe_mob)

#classe gif animé
class AnimatedGif():
    def __init__(self,x, y, max_frame, path:str, label, root, zoom = 1, speed = 100, repeat = 1):
        self.x = x
        self.y = y
        self.max_frame = max_frame
        self.path = path
        self.label = label
        self.root = root
        self.zoom = zoom
        self.speed = speed
        self.repeat = repeat
        self.frames = [PhotoImage(file=path,format = 'gif -index %i' %(i)).zoom(zoom) for i in range(max_frame)]
        self.updating = True

    #permet l'update du gif au nb max de frame du gif
    def update(self, ind):
        if self.updating and self.path !=None:
            if ind+1 <= self.max_frame: #si indice + petit que max frame alors update la frame
                frame = self.frames[ind]
                ind += 1
            else:
                frame = self.frames[ind-1] #(cas ou l'anim n'est pas infinie) comme l'anim va 1 trop loin on fige l'anim à la derniere frame
            if ind == self.max_frame and self.repeat == -1: #si infini alors l'index de frame revient à 0 pour restart l'anim
                ind = 0
            self.label.configure(image=frame)
            self.root.after(self.speed, self.update, ind)
            self.label.place(relx=self.x,rely=self.y)


    def stop_anim(self): # arrète l'animation (normalement) 
        self.updating = False
        self.label.config(image = "")

