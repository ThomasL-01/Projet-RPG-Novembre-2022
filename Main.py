from tkinter import *
from persos import *

player_pseudo = None
player_class = None
widget_lst =[]
anim_lst =[] 


#Pour faire 2 actions sur 1 bouton       
def double_fonction(*funcs):
    def double_fonction(*fonct1, **fonct2):
        for f in funcs:
            f(*fonct1, **fonct2)
    return double_fonction

def destroy_widgets():
    for widget in widget_lst:
        widget.destroy()
    widget_lst.clear()

def destroy_anim():
    for anim in anim_lst:
        anim.stop_anim()

#Pour recréer une fenètre basique rapidement
def create_window():
    window = Tk()
    window.title("RPG")
    window.geometry("1440x793")
    window.configure(background='black')
    window.minsize(500,500)
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    return window, width, height

#Menu principal
def main_menu():
    window, width, height = create_window()
    btn_quitter = Button(window, text="QUITTER", bg="white", fg="black", command=window.destroy)
    btn_quitter.place(relx=0.5,rely=1, anchor= S, width=1440)
    
    start_button = Button(window, text = "Démarrer jeu" ,font=('Arial', 30),command = double_fonction(window.destroy, pseudo_menu))
    start_button.place(relx=0.5,rely=0.8, anchor=CENTER)

    text_label = Label(window, bg="black", text= "RPG Adventure", font= ("Helvetica", 50), fg="White")
    text_label.place(relx=0.5,rely=0.45, anchor=CENTER)

    window.mainloop()

#Menu choix pseudo joueur
def pseudo_menu():
    window , width, height= create_window()
    btn_menu = Button(window, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(window.destroy, main_menu))
    btn_menu.pack(side = BOTTOM, fill=X)
   
    text_label = Label(window, bg="black", text= "Comment vous appelez-vous ?", font= ("Helvetica", 30), fg="White")
    text_label.place(relx=0.5,rely=0.3, anchor=CENTER)

    pseudo_entry = Entry(window,bg="black", fg="white", width=30, textvariable="Pseudo", font=("Helbetica", 30), insertbackground="white")
    pseudo_entry.place(relx=0.5,rely=0.5, anchor=CENTER)

    error_message = Label(window, bg="black", text= "", font= ("Helvetica", 30), fg="black")
    error_message.place(relx=0.5,rely=0.8, anchor=CENTER)

    def entry():
        global player_pseudo
        text = pseudo_entry.get()
        if text == "" or len(text)> 15:
            error_message.config(text="Taille de pseudo non valide", fg="red")
        elif  " "in text or "#" in text or "!" in text or "?" in text or "&"in text or "("in text or ")"in text or "."in text or "°"in text or "§"in text or "+"in text or "£"in text or "$" in text or "€"in text or "<"in text or ">"in text:
            error_message.config(fg="red", text="Caractère(s) interdit(s) ( ,!,?,#,&,(,),.,°,§,+,£,$,€,<,>)")
        else:
            error_message.config(fg="black")
            player_pseudo = text
            #On ne détruit pas cette fenetre lorsqu'on passe à la suivante
            window.destroy()
            class_choice_menu()

    submit_button = Button(window, bg="white", text="Continuer",font= ("Helvetica", 30), fg="black" , command=entry)
    submit_button.place(relx=0.5,rely=0.7, anchor=CENTER)

    window.mainloop()

#Menu choix classe joueur
def class_choice_menu():
    #On crée une nouvelle fenetre (pour avoir les images inon ça marche pas)la précédente existe tjrs
    window , width, height= create_window()

    btn_retour = Button(window, text="RETOUR", bg="white", fg="black", command=double_fonction(window.destroy, pseudo_menu)) #On détruit cette fenetre (comme la précédente n'apas été détruite on revient en arrière)
    btn_retour.pack(side = BOTTOM, fill=X)

    text_label =  Label(window, bg="black", text= "Choix de la classe du joueur\nClique sur les personnages pour plus d'informations !", font= ("Helvetica", 30), fg="White")
    text_label.pack(pady=(50,0))#met un ecart en haut de 20 et en bas de 0

    ninja_text = Label(window, bg="black", text= "Classe Ninja", font= ("Helvetica", 30), fg="red")
    skeleton_text = Label(window, bg="black", text= "Classe Squelette", font= ("Helvetica", 30), fg="red")
    warrior_text = Label(window, bg="black", text= "Classe Guerrier", font= ("Helvetica", 30), fg="red")

    def set_player_class(classe, window):
        global player_class
        player_class= classe
        window.destroy()
        game_menu()
        return player_class

    ninja_text.place(relx=0.25, rely=0.35, anchor=E)
    skeleton_text.place(relx=0.5, rely=0.35, anchor=CENTER)
    warrior_text.place(relx=0.75, rely=0.35, anchor=W)

    ninja_button = Button(window, text = "Choisir" ,font=('Arial', 30),command = lambda:set_player_class("ninja", window))
    skeleton_button = Button(window, text = "Choisir" ,font=('Arial', 30),command = lambda:set_player_class("skeleton", window))
    warrior_button = Button(window, text = "Choisir" ,font=('Arial', 30),command = lambda:set_player_class("warrior", window))

    ninja_button.place(relx=0.225, rely=0.75, anchor=E)
    skeleton_button.place(relx=0.5, rely=0.75, anchor=CENTER)
    warrior_button.place(relx=0.8, rely=0.75, anchor=W)

    def info_class(classe):
        info_w = Toplevel(master=window)
        info_w.title(f"Info classe {classe}")
        info_w.geometry("500x200")
        info_w.config(bg='black')

        text_info = Label(info_w, text= infos_classes[classe], bg='black',fg='white',font=('Arial', 20))
        text_info.pack(fill='both', expand = YES)

        info_w.mainloop()

    ninja_frame = Frame(window, bg='black')
    ninja_frame.place(relx=0.25, rely=0.53, anchor=E)
    ninja_image = PhotoImage(file=r"ninja.png", master=window).zoom(9)
    ninja_class_button = Button(ninja_frame, bg='black', image=ninja_image, command=lambda:info_class('ninja'), bd=0, highlightthickness=0)
    ninja_class_button.pack()

    skeleton_frame = Frame(window, bg='black')
    skeleton_frame.place(relx=0.5, rely=0.53, anchor=CENTER)
    skeleton_image = PhotoImage(file=r"Skeleton.png", master=window).zoom(6)
    skeleton_class_button = Button(skeleton_frame, bg='black', image=skeleton_image, command=lambda:info_class('skeleton'), bd=0, highlightthickness=0)
    skeleton_class_button.pack()

    warrior_frame = Frame(window, bg='black')
    warrior_frame.place(relx=0.8, rely=0.53, anchor=W)
    warrior_image = PhotoImage(file=r"warrior.png", master=window).zoom(6)
    warrior_class_button = Button(warrior_frame, bg='black', image=warrior_image, command=lambda:info_class('warrior'), bd=0, highlightthickness=0)
    warrior_class_button.pack()   

    window.mainloop()

def create_dialogue_box(root, width, height):
    dialogue_box = Label(root, highlightthickness=2, bd= 2,font=("Helvetica", 25) ,width = int(width/20), height=int(height/126), relief=SOLID)
    dialogue_box.place(relx=0.15, rely=0.63)
    return dialogue_box

#Menu de fight
def game_menu():#C'est juste un 1er test
    player = Player(player_class, player_pseudo)
    bg_nb = randint(1,2) #choix entre bg 1 et 2
    game_window , width, height= create_window()


    def  next_event(biome,nb_events):
        if nb_events > 0:
            event = choice(lst_event)
            if event == "passive_mob":
                destroy_widgets()
                passive_fight(biome,nb_events)
            
            elif event == "angry_mob":
                destroy_widgets()
                agressive_fight(biome,nb_events)
                
            else:
                destroy_widgets()
                potion(biome,nb_events)
    
        elif nb_events == 0:
            destroy_widgets()
            direction_menu()
    
    def passive_fight(biome,nb_events):
        nb_events-=1
        bg = PhotoImage(file = f"{biome}{bg_nb}.png")
        
        #Création barre de bouton / actions du combat
        bg_canvas = Canvas(game_window, highlightthickness=0, bd=0, bg="black")
        bg_canvas.pack(expand=YES, fill=BOTH) 
        bg_canvas.create_image(0,0,anchor=NW, image= bg)

        dialogue_box = create_dialogue_box(bg_canvas, width, height)
        def start_attack():
            dialogue_box.config(text="A l'attaque !\nC'est à vous de jouer")
            attack_button.config(command=player_attack)
            heal_button.place(relx = 0.445, rely=0.91)
            heal_button.config(state=ACTIVE)
            do_not_attack_button.destroy()

        def player_attack():
            text = player.attack(bot)
            dialogue_box.config(text=text)
            attack_button.config(state=DISABLED)
            heal_button.config(state=DISABLED)
            player.current_speed = 0

            #play anim
            player.current_anim = "attack"
            player_anim = AnimatedGif(x=0.6,y=0.47,max_frame =infos_anim[player.classe][player.current_anim]["max_frame"],
                label = Label(game_window, bg = "black"), root=game_window, path=f"{player.classe}/{player.current_anim}.gif",
                speed=infos_anim[player.classe][player.current_anim]["speed"],repeat=1, zoom=infos_anim[player.classe][player.current_anim]["zoom"])
            player_anim.update(0)

            def set_anim():
                player.current_anim = "idle"
                idle_anim(0.6,0.47,player,player_anim,-1)

            #a la fin de l'anim, passe l'anim en idle
            game_window.after(infos_anim[player_class][player.current_anim]["max_frame"]*infos_anim[player_class][player.current_anim]["speed"],set_anim)
            check_end_fight()
            game_window.after(1500,update_fight)

        def idle_anim(x,y,perso,object1,repeat):
            perso.current_anim = "idle"
            object1.stop_anim() #arrete l'anim attack
            object = AnimatedGif(x=x,y=y,max_frame =infos_anim[perso.classe][perso.current_anim]["max_frame"],
                label = Label(game_window, bg = "black"), root=game_window, path=f"{perso.classe}/{perso.current_anim}.gif",
                speed=infos_anim[perso.classe][perso.current_anim]["speed"],repeat=repeat, zoom=infos_anim[perso.classe][perso.current_anim]["zoom"])
            object.update(0)    #lance l'anim idle

        def bot_attack():
            text = bot.attack(player)
            dialogue_box.config(text=text)
            bot.current_speed= 0

            #play anim
            bot.current_anim = "attack"
            bot_anim = AnimatedGif(x=0.4,y=0.45,max_frame =infos_anim[bot.classe][bot.current_anim]["max_frame"],
                label = Label(game_window, bg = "black"), root=game_window, path=f"{bot.classe}/{bot.current_anim}.gif",
                speed=infos_anim[bot.classe][bot.current_anim]["speed"],repeat=1, zoom=infos_anim[bot.classe][bot.current_anim]["zoom"])
            bot_anim.update(0)

            def set_anim():
                bot.current_anim = "idle"
                idle_anim(0.4,0.45,bot,bot_anim,-1)

            game_window.after(infos_anim[bot.classe][bot.current_anim]["max_frame"]*infos_anim[bot.classe][bot.current_anim]["speed"],set_anim)
            check_end_fight()
            game_window.after(1500,update_fight)
            
        def check_end_fight():
            if not player.is_alive():
                if player_class == "skeleton":
                    if player.reanimations > 0:
                        player.reanimations-=1
                        player.revive()
                        dialogue_box.config(text = "Vous avez été réssucité ! \n Vos stats ont été diminuées")
                        game_window.after(2000,update_fight)
                else:
                    player_anim.stop_anim()
                    player_anim.label.destroy()
                    player_anim.path = None
                    dialogue_box.config(text="Vous avez perdu !!")

            elif not bot.is_alive():
                bot_anim.stop_anim()
                bot_anim.label.destroy()
                bot_anim.path = None
                continue_button.place(relx=0.76,rely=0.91)
                dialogue_box.config(text="Continuons notre chemin !")

        def update_fight():
            player.current_speed += player.speed
            bot.current_speed+=bot.speed
            if player.current_speed >=100 and player.is_alive() and bot.is_alive():
                attack_button.config(state=ACTIVE)
                heal_button.config(state=ACTIVE)
                dialogue_box.config(text=f"A vous de jouer ! \n Vous avez {player.pv} PV. L'adversaire en a {bot.pv}")

            elif bot.current_speed >=100 and bot.is_alive() and player.is_alive():
                dialogue_box.config(text="L'adversaire attaque !")
                game_window.after(1250,bot_attack)
            elif bot.is_alive() and player.is_alive():
                game_window.after(0,update_fight)
        
        def heal_player():
            player.current_speed=0
            if player.pot_nb == 0:
                dialogue_box.config(text = f"Vous n'avez pas de potion !\n Vous avez {player.pv} PV")
            elif player.pv == player.max_health:
                dialogue_box.config(text = f"Vous n'avez pas besoin de vous soigner ! Votre vie est au max !\n Vous avez {player.pv} PV")
            elif player.pot_nb > 0 and player.pv < player.max_health:
                attack_button.config(state=DISABLED)
                heal_button.config(state=DISABLED)
                player.heal()
                dialogue_box.config(text=f"Vous vous êtes soigné ! Il vous reste {player.pot_nb} potion(s) \n Vous avez {player.pv} PV")
                game_window.after(1500,update_fight)
        
        attack_button = Button(bg_canvas, text="Attaquer", bg="white", font=('Arial', 30),fg="black", command=start_attack, state=ACTIVE)
        attack_button.place(relx = 0.15, rely=0.91)
        widget_lst.append(attack_button)

        dialogue_box.config(text="Un ennemi! Il ne semble pas nous attaquer, que faire ?")

        player_label = Label(game_window, bg = "black")
        player_anim = AnimatedGif(x=0.6,y=0.47,max_frame =infos_anim[player_class][player.current_anim]["max_frame"],
            label = player_label, root=game_window, path=f"{player_class}/{player.current_anim}.gif",
            speed=infos_anim[player_class][player.current_anim]["speed"],repeat=-1, zoom=infos_anim[player_class][player.current_anim]["zoom"])
        player_anim.update(0)
        anim_lst.append(player_anim)

        bot = create_mob(biome)
        mob_label = Label(game_window, bg = "black")
        bot_anim =AnimatedGif(x=0.4,y=0.45,max_frame =infos_anim[bot.classe][bot.current_anim]["max_frame"],
            label = mob_label, root=game_window, path=f"{bot.classe}/{bot.current_anim}.gif",
            speed=infos_anim[bot.classe][bot.current_anim]["speed"],repeat=-1, zoom=infos_anim[bot.classe][bot.current_anim]["zoom"])
        bot_anim.update(0)
        anim_lst.append(bot_anim)

        heal_button =  Button(bg_canvas, text="Se soigner", bg="white", font=('Arial', 30),fg="black", command=heal_player, state=DISABLED)
        widget_lst.append(heal_button)

        do_not_attack_button = Button(bg_canvas, text="Ne pas attaquer", bg="white", font=('Arial', 30),fg="black", command=lambda:next_event(biome,nb_events), state=ACTIVE)
        do_not_attack_button.place(relx = 0.704, rely=0.91)
        widget_lst.append(do_not_attack_button)

        continue_button =  Button(bg_canvas, text="Continuer", bg="white", font=('Arial', 30),fg="black", command=lambda:double_fonction(destroy_anim,next_event(biome,nb_events)))
        widget_lst.append(continue_button)
    
        quit_menu = Button(bg_canvas, text="QUITTER", command= game_window.destroy)
        quit_menu.pack(side = BOTTOM, fill=X)
        widget_lst.append(quit_menu)
        widget_lst.append(dialogue_box)
        widget_lst.append(bg_canvas)
        anim_lst.append(player_anim)
        anim_lst.append(bot_anim)
        game_window.mainloop()

    def agressive_fight(biome,nb_events ):
        nb_events-=1
        bg = PhotoImage(file = f"{biome}{bg_nb}.png")
        
        #Création barre de bouton / actions du combat
        bg_canvas = Canvas(game_window, highlightthickness=0, bd=0, bg="black")
        bg_canvas.pack(expand=YES, fill=BOTH) 
        bg_canvas.create_image(0,0,anchor=NW, image= bg)

        dialogue_box = create_dialogue_box(bg_canvas, width, height)


        def player_attack():
            text = player.attack(bot)
            dialogue_box.config(text=text)
            attack_button.config(state=DISABLED)
            heal_button.config(state=DISABLED)
            player.current_speed = 0

            #play anim
            player.current_anim = "attack"
            player_anim = AnimatedGif(x=0.6,y=0.47,max_frame =infos_anim[player.classe][player.current_anim]["max_frame"],
                label = Label(game_window, bg = "black"), root=game_window, path=f"{player.classe}/{player.current_anim}.gif",
                speed=infos_anim[player.classe][player.current_anim]["speed"],repeat=1, zoom=infos_anim[player.classe][player.current_anim]["zoom"])
            
            player_anim.update(0)

            def set_anim():
                player.current_anim = "idle"
                idle_anim(0.6,0.47,player,player_anim,-1)

            game_window.after(infos_anim[player_class][player.current_anim]["max_frame"]*infos_anim[player_class][player.current_anim]["speed"],set_anim)
            check_end_fight()
            game_window.after(1500,update_fight)

        def idle_anim(x,y,perso,object1,repeat = 1):
            perso.current_anim = "idle"
            object1.stop_anim()
            object = AnimatedGif(x=x,y=y,max_frame =infos_anim[perso.classe][perso.current_anim]["max_frame"],
                label = Label(game_window, bg = "black"), root=game_window, path=f"{perso.classe}/{perso.current_anim}.gif",
                speed=infos_anim[perso.classe][perso.current_anim]["speed"],repeat=repeat, zoom=infos_anim[perso.classe][perso.current_anim]["zoom"])
            object.update(0)

        def bot_attack():
            text = bot.attack(player)
            dialogue_box.config(text=text)
            bot.current_speed= 0

            #play anim
            bot.current_anim = "attack"
            bot_anim = AnimatedGif(x=0.4,y=0.45,max_frame =infos_anim[bot.classe][bot.current_anim]["max_frame"],
                label = Label(game_window, bg = "black"), root=game_window, path=f"{bot.classe}/{bot.current_anim}.gif",
                speed=infos_anim[bot.classe][bot.current_anim]["speed"],repeat=1, zoom=infos_anim[bot.classe][bot.current_anim]["zoom"])
            bot_anim.update(0)

            def set_anim():
                bot.current_anim = "idle"
                idle_anim(0.4,0.45,bot,bot_anim,-1)

            game_window.after(infos_anim[bot.classe][bot.current_anim]["max_frame"]*infos_anim[bot.classe][bot.current_anim]["speed"],set_anim)
            check_end_fight()
            game_window.after(1500,update_fight)

        def check_end_fight():
            if not player.is_alive():
                if player_class == "skeleton" and player.reanimations > 0:
                    player.reanimations-=1
                    player_label = Label(game_window, bg = "black")
                    player_anim =AnimatedGif(x=0.6,y=0.47,max_frame =infos_anim[player_class][player.current_anim]["max_frame"],
                        label = player_label, root=game_window, path=f"{player_class}/{player.current_anim}.gif",
                        speed=infos_anim[player_class][player.current_anim]["speed"],repeat=-1, zoom=infos_anim[player_class][player.current_anim]["zoom"])
                    widget_lst.append(player_label)
                    player_anim.update(0)
                    player.revive()
                    dialogue_box.config(text = "Vous avez été réssucité ! \n Vos stats ont été diminuées")
                    game_window.after(2000,update_fight)
                else:
                    dialogue_box.config(text="Vous avez perdu !!")


            elif not bot.is_alive():
                bot_anim.stop_anim()
                continue_button.place(relx=0.76,rely=0.91)
                dialogue_box.config(text="Continuons notre chemin !")

        def update_fight(first_attack=False):
            player.current_speed += player.speed
            bot.current_speed+=bot.speed
            if player.current_speed >=100 and player.is_alive() and bot.is_alive():
                attack_button.config(state=ACTIVE)
                heal_button.config(state=ACTIVE)
                dialogue_box.config(text=f"A vous de jouer ! \n Vous avez {player.pv} PV. L'adversaire en a {bot.pv}")
                
            elif bot.current_speed >=100 and bot.is_alive() and first_attack and player.is_alive():
                dialogue_box.config(text="Un ennemi! Il nous attaque !")
                game_window.after(1250,bot_attack)
                first_attack == False
            elif bot.current_speed >=100 and bot.is_alive() and not first_attack and player.is_alive():
                dialogue_box.config(text="L'adversaire attaque")
                game_window.after(1250,bot_attack)

            elif first_attack:
                game_window.after(0,update_fight,True)
            elif bot.is_alive() and player.is_alive():
                game_window.after(0,update_fight)
                
        def heal_player():
            player.current_speed=0
            if player.pot_nb == 0:
                dialogue_box.config(text = f"Vous n'avez pas de potion !\n Vous avez {player.pv} PV")
            elif player.pv == player.max_health:
                dialogue_box.config(text = f"Vous n'avez pas besoin de vous soigner ! Votre vie est au max !\n Vous avez {player.pv} PV")
            elif player.pot_nb > 0 and player.pv < player.max_health:
                attack_button.config(state=DISABLED)
                heal_button.config(state=DISABLED)
                player.heal()
                dialogue_box.config(text=f"Vous vous êtes soigné ! Il vous reste {player.pot_nb} potion(s) \n Vous avez {player.pv} PV")
                game_window.after(1500,update_fight)
        
        attack_button = Button(bg_canvas, text="Attaquer", bg="white", font=('Arial', 30),fg="black", command=player_attack, state=DISABLED)
        attack_button.place(relx = 0.15, rely=0.91)
        widget_lst.append(attack_button)

        player_label = Label(game_window, bg = "black")
        player_anim =AnimatedGif(x=0.6,y=0.47,max_frame =infos_anim[player_class][player.current_anim]["max_frame"],
            label = player_label, root=game_window, path=f"{player_class}/{player.current_anim}.gif",
            speed=infos_anim[player_class][player.current_anim]["speed"],repeat=-1, zoom=infos_anim[player_class][player.current_anim]["zoom"])
        widget_lst.append(player_label)
        player_anim.update(0)
        anim_lst.append(player_anim)

        bot = create_mob(biome)
        mob_label = Label(game_window, bg = "black")
        bot_anim = AnimatedGif(x=0.4,y=0.45,max_frame =infos_anim[bot.classe][bot.current_anim]["max_frame"],
            label = mob_label, root=game_window, path=f"{bot.classe}/{bot.current_anim}.gif",
            speed=infos_anim[bot.classe][bot.current_anim]["speed"],repeat=-1, zoom=infos_anim[bot.classe][bot.current_anim]["zoom"])
        bot_anim.update(0)
        anim_lst.append(bot_anim)

        heal_button =  Button(bg_canvas, text="Se soigner", bg="white", font=('Arial', 30),fg="black", command=heal_player, state=DISABLED)
        heal_button.place(relx = 0.445, rely=0.91)
        widget_lst.append(heal_button)

        continue_button =  Button(bg_canvas, text="Continuer", bg="white", font=('Arial', 30),fg="black", command=lambda:double_fonction( destroy_anim, next_event(biome,nb_events)))
        widget_lst.append(continue_button)

        quit_button = Button(bg_canvas, text="QUITTER", command= game_window.destroy)
        quit_button.pack(side = BOTTOM, fill=X)
        widget_lst.append(quit_button)
        widget_lst.append(dialogue_box)
        widget_lst.append(bg_canvas)
        anim_lst.append(player_anim)
        anim_lst.append(bot_anim)

        update_fight(True)
        game_window.mainloop()

    def potion(biome,nb_events ):
        def get_potion():
            player.pot_nb+=1
            get_button.config(state=DISABLED)
            continue_button.config(state=ACTIVE)
            dialogue_box.config(text=f"Nous avons récupéré une potion ! \n Nous en avons {player.pot_nb}")
            potion_label.destroy()

        nb_events-=1
        bg = PhotoImage(file = f"{biome}{bg_nb}.png")
        
        #Création barre de bouton / actions du combat
        bg_canvas = Canvas(game_window, highlightthickness=0, bd=0, bg="black")
        bg_canvas.pack(expand=YES, fill=BOTH) 
        bg_canvas.create_image(0,0,anchor=NW, image= bg)

        dialogue_box = create_dialogue_box(bg_canvas, width, height)
        widget_lst.append(dialogue_box)

        potion_img = PhotoImage(file="potion.png").subsample(2)
        potion_label = Label(game_window, bg = "black", image=potion_img)
        potion_label.place(relx=0.34,rely=0.45)
        widget_lst.append(potion_label)

        dialogue_box.config(text=potion_text)

        get_button = Button(bg_canvas, text="Récupérer", bg="white", font=('Arial', 30),fg="black", command=get_potion, state=ACTIVE)
        get_button.place(relx = 0.15, rely=0.91)
        widget_lst.append(get_button)

        player_label = Label(game_window, bg = "black")

        player_anim = AnimatedGif(x=0.6,y=0.47,max_frame =infos_anim[player_class][player.current_anim]["max_frame"],
            label = player_label, root=game_window, path=f"{player_class}/{player.current_anim}.gif",
            speed=infos_anim[player_class][player.current_anim]["speed"],repeat=-1, zoom=infos_anim[player_class][player.current_anim]["zoom"])
        player_anim.update(0)
        anim_lst.append(player_anim)

        #bot = create_mob(biome)
        continue_button =  Button(bg_canvas, text="Continuer", bg="white", font=('Arial', 30),fg="black", command=lambda:double_fonction(destroy_anim,next_event(biome,nb_events)), state=DISABLED)
        continue_button.place(relx = 0.76, rely=0.91) 
        widget_lst.append(continue_button)


        btn_menu = Button(bg_canvas, text="QUITTER", command= game_window.destroy)
        btn_menu.pack(side = BOTTOM, fill=X)
        widget_lst.append(btn_menu)
        widget_lst.append(bg_canvas)
        anim_lst.append(player_anim)
        game_window.mainloop()

    def direction_menu():

        quit_button = Button(game_window, text="QUITTER", bg="white", fg="black", command=game_window.destroy)
        quit_button.pack(side = BOTTOM, fill=X)

        direction1 = choose_direction(None) #direction gauche
        direction2 = choose_direction(direction1) #direction droite

        if direction1 == "mountain":
            text_dir1 = "la montagne"
        if direction1 == "ruines":
            text_dir1 = "les ruines"
        if direction1 == "forest":
            text_dir1 = "la forêt"
        if direction2 == "mountain":
            text_dir2 = "la montagne"
        if direction2 == "ruines":
            text_dir2 = "les ruines"
        if direction2 == "forest":
            text_dir2 = "la forêt"

        left_dir = Button(game_window, width=20, text=f"Pour aller vers {text_dir1}",font=("Helvetica",20), command=lambda:next_event(direction1, randint(1,5)))
        right_dir = Button(game_window, width=20, text=f"Pour aller vers {text_dir2}",font=("Helvetica", 20), command=lambda: next_event(direction2, randint(1,5)))
        
        dialogue_box = create_dialogue_box(game_window, width, height)
        dialogue_box.config(text=direction_text)
        widget_lst.append(dialogue_box)

        left_dir.place(relx=0.04, rely=0.4)
        widget_lst.append(left_dir)
        right_dir.place(relx=0.8, rely=0.4)
        widget_lst.append(right_dir)

        widget_lst.append(quit_button)

        game_window.mainloop()

    direction_menu()

main_menu()