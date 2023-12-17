import pygame
from pygame.locals import *
from pygame import mixer
import backend

player = backend.machine_slot(0)

sort_fruits = {
    "slot0" : "IMG/img2.png",
    "slot1" : "IMG/img1.png",
    "slot2" : "IMG/img9.png",
    "slot3" : "IMG/img10.png",
    "slot4" : "IMG/img1.png",
    "slot5" : "IMG/img8.png",
    "slot6" : "IMG/img3.png",
    "slot7" : "IMG/img1.png",
    "slot8" : "IMG/img6.png",
    "slot9" : "IMG/img2.png",
    "slot10" : "IMG/img1.png",
    "slot11" : "IMG/img5.png",
    "slot12" : "IMG/img7.png",
    "slot13" : "IMG/img1.png",
    "slot14" : "IMG/img4.png",
    "slot15" : "IMG/img2.png",
    "slot16" : "IMG/img1.png",
    "slot17" : "IMG/img3.png",
    "slot18" : "IMG/img2.png",
    "slot19" : "IMG/img1.png",
    "slot20" : "IMG/img5.png",
    "slot21" : "IMG/img4.png",
}

def main(sort_fruits):

    pygame.init()

    # CONFIGURACION DE VENTANA Y TASA DE REFRESCO
    size_screen = (820, 780)
    SCREEN = pygame.display.set_mode(size_screen)
    icon = pygame.image.load('IMG/icon.png')
    pygame.display.set_caption('Fruit slots game')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    FPS = 60

    # FUENTE
    font = pygame.font.Font("FONT/Dotf1.ttf", 40)
    font_for_fruits = pygame.font.Font("FONT/Dotf1.ttf", 50)
    instruction_font = pygame.font.SysFont("arial", 20)

    # COLORES
    WHITE = (255,255,255)
    RED = (255,0,0)
    BLACK = (0,0,0)

    # IMAGEN DE FONDO Y TITULO
    background = pygame.image.load('IMG/background.jpg')
    background = pygame.transform.smoothscale(background, size_screen)
    title = pygame.image.load('IMG/title.png')
    title = pygame.transform.smoothscale(title, (350, 100))


    # SUPERFICIE DE SLOTS
    slots_surface = pygame.Surface((520, 445))  #Creacion de superficie con color negro por defecto
    slots_surface.set_colorkey(BLACK)   #Haciendo invisible el color negro
    x_slot = y_slot = 0               #Coordenadas
    width_slots = 70        #Ancho de los slots
    height_slots = 70       #Alto de los slots
    interspace_slots = 5    #Espacio entre slots
    coordinate_slots = []   #Lista de coordenadas

    # SUPERFICIE DE SELECTOR
    selector_surface = pygame.Surface((520,445))
    selector_surface.set_colorkey(BLACK)
    x_select = y_select = 0
    pygame.draw.rect(selector_surface, RED, (x_select, y_select, width_slots, height_slots))
    selector_surface.set_alpha(130)

    # SUPERFICIE DE CREDITOS    
    credits_surface = SCREEN.subsurface((225, 170, 380, 305))
    credits_surface = credits_surface.convert_alpha()
    credits_surface.fill((0,0,0, 0))
    credits_image = pygame.image.load('IMG/credits.png')
    credits_image = pygame.transform.smoothscale(credits_image, (150, 50))
    prize_image = pygame.image.load('IMG/prize.png')
    prize_image = pygame.transform.smoothscale(prize_image, (120, 50))

    # SUPERFICIE DE BOTONES
    buttonsPanel_surface = pygame.Surface((820, 150))
    buttonsPanel_surface = buttonsPanel_surface.convert_alpha()
    buttonsPanel_surface.fill((0,0,0, 0))
    x_buttons, y_buttons = 155, 107
    width_buttons = 43
    height_buttons = 43
    interspace_buttons = 10
    coordinate_buttons = []
    buttons = []

    # CREACION DE SLOTS (acorde al espacio de la superficie)
    for i in range(0,22):
            coordinate_slots.append((x_slot, y_slot))
            pygame.draw.rect(slots_surface, WHITE, (x_slot, y_slot, width_slots, height_slots))
            if i < 6:
                x_slot += width_slots + interspace_slots
            elif i < 11:
                y_slot += height_slots + interspace_slots
            elif i < 17:
                x_slot = x_slot - width_slots - interspace_slots
            else:
                y_slot = y_slot - height_slots - interspace_slots
    
    # CREACION DE IMAGENES
    x_image = y_image = 10
    for i in range(0,22):
        image = pygame.image.load(sort_fruits[f'slot{i}'])
        image = pygame.transform.smoothscale(image, (width_slots-20,height_slots-20))
        slots_surface.blit(image, (x_image,y_image))
        if i < 6:
                x_image += width_slots + interspace_slots
        elif i < 11:
            y_image += height_slots + interspace_slots
        elif i < 17:
            x_image = x_image - width_slots - interspace_slots
        else:
            y_image = y_image - height_slots - interspace_slots

    # CREACION DE BOTONES
    cashout_button1 = pygame.image.load('IMG/cashout_button1.png')
    play_button1 = pygame.image.load('IMG/play_button1.png')
    cashout_button1 = pygame.transform.smoothscale(cashout_button1, (75,75))
    play_button1 = pygame.transform.smoothscale(play_button1, (75, 75))

    for i in range(0,10):
        coordinate_buttons.append((x_buttons, y_buttons))
        pygame.draw.rect(buttonsPanel_surface, BLACK, (x_buttons, 0, width_buttons, height_buttons+20), 0, 10)
        image_fruit = pygame.image.load(f'IMG/img{10-i}.png')
        image_fruit = pygame.transform.smoothscale(image_fruit, (width_buttons-10, height_buttons-10))
        image_button1 = pygame.image.load('IMG/add_button1.png')
        image_button1 = pygame.transform.smoothscale(image_button1, (width_buttons, height_buttons))
        buttons.append(image_button1)
        buttonsPanel_surface.blit(image_fruit, (x_buttons+5, y_buttons-39))
        buttonsPanel_surface.blit(buttons[i], (x_buttons, y_buttons))
        x_buttons += width_buttons + interspace_buttons
        

    # VARIABLES DE BUCLE
    running = True
    run_selector = False
    buttons_event = False
    active_play = True
    count_selector = 0
    count_round_selector = 0
    prize = 0
    mixer.music.set_volume(0.5)

    while running:
        ### INICIO COLA DE EVENTOS
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                 if event.key == K_SPACE:
                    player.set_credits(1)
                    if player.get_credits() < 999:
                        mixer.music.load('SOUND/insert_credit.wav')
                        mixer.music.play()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                buttons_event = True
            else:
                buttonsPanel_surface.blit(cashout_button1, (40,40))
                buttonsPanel_surface.blit(play_button1, (710, 40))
                x_buttons, y_buttons = 155, 107
                
                for i in range(0,10):
                    pygame.draw.rect(buttonsPanel_surface, BLACK, (x_buttons, 0, width_buttons, height_buttons+20), 0, 10)
                    fruit_font = font_for_fruits.render(str(list(player._tablero.values())[9-i]), 0, RED)
                    buttonsPanel_surface.blit(fruit_font, (x_buttons+3, 10))
                    image_button1 = pygame.image.load('IMG/add_button1.png')
                    image_button1 = pygame.transform.smoothscale(image_button1, (width_buttons, height_buttons))
                    buttonsPanel_surface.blit(buttons[i], (x_buttons, y_buttons))
                    x_buttons += width_buttons + interspace_buttons
        ### FINAL COLA DE EVENTOS  

        ### INICIO EVENTO BOTONES
        if buttons_event:
            if cashout_button1.get_rect(topleft=(40,40+575)).collidepoint(pygame.mouse.get_pos()):  # Ejecución de "cobrar"
                    
                    cashout_button2 = pygame.image.load('IMG/cashout_button2.png')
                    cashout_button2 = pygame.transform.smoothscale(cashout_button2, (75,75))
                    buttonsPanel_surface.blit(cashout_button2, (40,40))
                    player.cobrar()
                    mixer.music.load('SOUND/cashout.wav')
                    mixer.music.play()

            elif play_button1.get_rect(topleft=(710,40+575)).collidepoint(pygame.mouse.get_pos()):  # Ejecución de "jugar"
                    
                    prize = 0
                    play_button2 = pygame.image.load('IMG/play_button2.png')
                    play_button2 = pygame.transform.smoothscale(play_button2, (75,75))
                    buttonsPanel_surface.blit(play_button2, (710,40))
                    if active_play and player.confirm_bet():
                        result, pre_prize = player.roulette()      # Aquí va el resultado de la ruleta (backend)
                        initial_pos = (x_select, y_select)      # Posicion inicial de selector para conteo de vueltas
                        count_selector = coordinate_slots.index(initial_pos)    # Pocion inicial del selector para inicio de ruleta
                        run_selector = True # Activacion algoritmo ruleta
                        active_play = False
                        prize_font = font.render("0", 0, RED)
                        mixer.music.load('SOUND/start_roulette.wav')
                        mixer.music.play(-1)

            else:
                # Este bucle busca una a una la coincidencia de colisión con el clic, según las coordenadas (guardadas) de los botones
                for i in range(0,10):
                    if buttons[i].get_rect(topleft=(coordinate_buttons[i][0],coordinate_buttons[i][1]+575)).collidepoint(pygame.mouse.get_pos()):   # Ejecución de añadir apuesta.
                        image_button2 = pygame.image.load('IMG/add_button2.png')
                        image_button2 = pygame.transform.smoothscale(image_button2, (width_buttons, height_buttons))
                        buttonsPanel_surface.blit(image_button2, (coordinate_buttons[i][0], coordinate_buttons[i][1]))
                        player.set_tablero(coordinate_buttons.index(coordinate_buttons[9-i]))
                        if player.confirm_bet():
                            mixer.music.load('SOUND/bet_button.wav')
                            mixer.music.play()

            buttons_event = False
        ### FIN EVENTO BOTONES

        ### INICIO MOVIMIENTO SELECTOR
        if run_selector:

            if count_selector < 22:
                selector_surface.fill(BLACK)
                pygame.draw.rect(selector_surface, RED, (x_select, y_select, width_slots, height_slots))
                count_selector += 1
                
                if count_selector == 22:
                    count_selector = 0
                    x_select, y_select = coordinate_slots[count_selector]
                else:
                    x_select, y_select = coordinate_slots[count_selector]
            
            if coordinate_slots[count_selector] == initial_pos:
                count_round_selector += 1
            
            if coordinate_slots.index((x_select, y_select)) == result and count_round_selector > 1:
                count_round_selector = 0
                run_selector = False
                active_play = True       
                for key in player._tablero.keys():
                    player._tablero[key] = 0
                prize = pre_prize
                player.set_credits(prize)
                if prize == 0:
                    mixer.music.load('SOUND/lose.wav')
                    mixer.music.play()
                else:
                    mixer.music.load('SOUND/win.wav')
                    mixer.music.play()
            
           
            pygame.time.delay(50)
        ### FIN MOVIMIENTO SELECTOR

        # FONDO
        SCREEN.blit(background, (0,0))
        SCREEN.blit(title, ((background.get_width()/2)-160, 0))

        # SLOTS
        SCREEN.blit(slots_surface, (155, 100))

        # SELECTOR
        SCREEN.blit(selector_surface, (155, 100))

        # CREDITOS
        credits_font = font.render(str(player._credits), 0, RED)
        prize_font = font.render(str(prize), 0, RED)
        credits_bg = pygame.draw.rect(credits_surface, BLACK, (110, 70, 170, 50), 0, 5)
        prize_bg = pygame.draw.rect(credits_surface, BLACK, (110, 200, 170, 50), 0, 5)
        credits_surface.blit(credits_image, (120, 25))
        credits_surface.blit(prize_image, (140, 155))
        credits_surface.blit(credits_font, (110+(credits_bg.width - credits_font.get_width()), 78))
        credits_surface.blit(prize_font, (110+(prize_bg.width - prize_font.get_width()), 208))
        SCREEN.blit(credits_surface, (225, 170))


        # PANEL DE BOTONES
        SCREEN.blit(buttonsPanel_surface, (0, 575))

        # INSTRUCCION
        instruction = instruction_font.render("Para agregar créditos use la tecla 'SPACE'...", 0, WHITE)
        SCREEN.blit(instruction, ((SCREEN.get_width()/2)-(instruction.get_width()/2), 745))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main(sort_fruits)