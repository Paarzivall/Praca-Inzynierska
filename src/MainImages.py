import pygame
import os
from src.ResizeClass import resize

SIZESCREEN = WIDTH, HEIGHT = 1266, 840
SPEED_X = 1
SPEED_Y = 7
SPEED_PLATFORM_X = 6
SPEED_PLATFORM_Y = 0.5
SPEED_BACKGROUND_X = 0.3
SPEED_BACKGROUND_Y = 0
BLOCKS_WIDTH = 70
MAX_BACKGROUND_X = 500
"""
SPEED_PLATFORM_X = 0
SPEED_PLATFORM_Y = 0
SPEED_BACKGROUND_X = 0
SPEED_BACKGROUND_Y = 0
BLOCKS_WIDTH = 70
MAX_BACKGROUND_X = 500"""

path = ""
if os.path.isdir('..\img'):
    path = "..\\"

"""
###########################################################
######################## MENU #############################
###########################################################
"""

menu_background = pygame.image.load(os.path.join(path + 'img\\MenuImg', 'menu_background.png'))
start_button = resize(pygame.image.load(os.path.join(path + 'img\\MenuImg', 'start.png')))
end_button = resize(pygame.image.load(os.path.join(path + 'img\\MenuImg', 'end.png')))
again_button = resize(pygame.image.load(os.path.join(path + 'img\\MenuImg', 'again.png')))
title = pygame.image.load(os.path.join(path + 'img\\MenuImg', 'title.png'))
wiking_icon = pygame.image.load(os.path.join(path + 'img\\MenuImg', 'wiking_icon.png'))

"""
###########################################################
################### Binary Convert ########################
###########################################################
"""

# otwieranie zamka
first_background = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert', 'otwieranie_zamka.png')))

helper_binary_convert = pygame.image.load(os.path.join(path + 'img\\BinaryConvert', 'helper_image.png'))

# cyfry do 1 levelu

zero = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '0.png')))
one = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '1.png')))
two = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '2.png')))
three = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '3.png')))
four = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '4.png')))
five = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '5.png')))
six = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '6.png')))
seven = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '7.png')))
eight = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '8.png')))
nine = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '9.png')))

numbers = {0: zero, 1: one, 2: two, 3: three, 4: four,
           5: five, 6: six, 7: seven, 8: eight, 9: nine}

# piny do 1 lvl

pin_0_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_1_gora.png')))
pin_1_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_2_gora.png')))
pin_2_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_3_gora.png')))
pin_3_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_4_gora.png')))
pin_4_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_5_gora.png')))
pin_5_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_6_gora.png')))
pin_6_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_7_gora.png')))

pins_up = {0: pin_0_up, 1: pin_1_up, 2: pin_2_up, 3: pin_3_up,
            4: pin_4_up, 5: pin_5_up, 6: pin_6_up}

pin_0_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_1_dol.png')))
pin_1_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_2_dol.png')))
pin_2_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_3_dol.png')))
pin_3_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_4_dol.png')))
pin_4_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_5_dol.png')))
pin_5_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_6_dol.png')))
pin_6_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_7_dol.png')))

pins_down = {0: pin_0_down, 1: pin_1_down, 2: pin_2_down,
             3: pin_3_down, 4: pin_4_down, 5: pin_5_down, 6: pin_6_down}

"""
###########################################################
################### Platform Level ########################
###########################################################
"""
helper_platform_1 = pygame.image.load(os.path.join(path + 'img\\Platforms_levels', 'helper_image_1.png'))
helper_platform_2 = pygame.image.load(os.path.join(path + 'img\\Platforms_levels', 'helper_image_1.png'))
helper_platform_none = pygame.image.load(os.path.join(path + 'img\\Platforms_levels', 'helper_image_none.png'))

platform_background2 = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'new_img.jpg'))

# Ruchy Postaci

stand_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_standR.png'))
walk_right1 = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_walkR1.png'))
walk_right2 = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_walkR2.png'))
stand_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_standL.png'))
walk_left1 = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_walkL1.png'))
walk_left2 = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_walkL2.png'))
fail_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_fallL.png'))
fail_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_fallR.png'))
jump_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_jumpL.png'))
jump_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'player_jumpR.png'))
images_right = [walk_right1, walk_right2]
images_left = [walk_left1, walk_left2]

heart = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'heart.png'))

# Platformy
platform_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'grass_L.png'))
platform_center = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'grass_C.png'))
platform_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'grass_R.png'))
single_platform = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'grass_single.png'))
platforms = [single_platform, platform_left, platform_center, platform_right]

transport_platform_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'metal_L.png'))
transport_platform_center = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'metal_C.png'))
transport_platform_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'metal_R.png'))
single_transport_platform = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'metal_single.png'))
platforms = [single_transport_platform, transport_platform_left, transport_platform_center, transport_platform_right]

# Przeciwnicy
enemy_stand_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'zombie_standL.png'))
enemy_stand_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'zombie_standL.png'))
enemy_walk_right1 = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'zombie_walkR1.png'))
enemy_walk_right2 = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'zombie_walkR2.png'))
enemy_walk_left1 = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'zombie_walkL1.png'))
enemy_walk_left2 = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'zombie_walkL2.png'))
enemy_dead_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'zombie_deadL.png'))
enemy_dead_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'zombie_deadL.png'))

enemy_images_right = [enemy_walk_right1, enemy_walk_right2]
enemy_images_left = [enemy_walk_left1, enemy_walk_left2]

# Pociski
bullet_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'strzala_L.png'))
bullet_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'strzala_R.png'))

# gun = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'shotgun.png'))

# Portal pod koniec rundy
portal = resize(pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'finish_portal.png')))

# Sufit
ceiling_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'wall_top_L.png'))
ceiling_center = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'wall_top.png'))
ceiling_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'wall_top_R.png'))

# itemy na mapie
icon = resize(resize(resize(resize(pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'pergamin_ikona.png'))))))
pergamin = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'pergamin_ikona.png'))
cenzura = resize(resize(resize(resize(resize(resize(resize(pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'cenzura.png')))))))))
potion_max_life = resize(resize(resize(pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'potion_max_life.png')))))

"""
###########################################################
###################### Cutsceny ###########################
###########################################################
"""

cutscena_1 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#1.png')))
cutscena_2 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#2.png')))
cutscena_3 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#3.png')))
cutscena_4 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#4.png')))
cutscena_5 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#5.png')))
cutscena_6 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#6.png')))
cutscena_7 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#7.png')))


"""
###########################################################
#################### Bubble Sort ##########################
###########################################################
"""

#background
bubble_background = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'mechanizm_szkic.png')))

helper_bubble_sort = pygame.image.load(os.path.join(path + 'img\\bubble', 'helper_bubble_sort.png'))

switch_button = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'switch_off.png')))
switch_button_light = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'switch_on.png')))
next_button = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'button_R.png')))

# cyfry
image_0 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '0.png')))
image_1 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '1.png')))
image_2 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '2.png')))
image_3 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '3.png')))
image_4 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '4.png')))
image_5 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '5.png')))
image_6 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '6.png')))
image_7 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '7.png')))
image_8 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '8.png')))
image_9 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '9.png')))

numbers_image = {0: image_0, 1: image_1, 2: image_2, 3: image_3, 4: image_4,
                 5: image_5, 6: image_6, 7: image_7, 8: image_8, 9: image_9}

lock = resize(resize(resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'kolatka.png')))))

"""
###########################################################
###################### PlayFair ###########################
###########################################################
"""

helper_playfair = pygame.image.load(os.path.join(path + 'img\\PlayFair', 'playfair_helper.png'))

playfair_background = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'backgroundPlayFair.png')))

#litery
literaA = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaA.png')))
literaB = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaB.png')))
literaC = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaC.png')))
literaD = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaD.png')))
literaE = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaE.png')))
literaF = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaF.png')))
literaG = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaG.png')))
literaH = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaH.png')))
literaI = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaI.png')))
literaK = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaK.png')))
literaL = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaL.png')))
literaM = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaM.png')))
literaN = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaN.png')))
literaO = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaO.png')))
literaP = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaP.png')))
literaQ = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaQ.png')))
literaR = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaR.png')))
literaS = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaS.png')))
literaT = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaT.png')))
literaU = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaU.png')))
literaV = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaV.png')))
literaW = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaW.png')))
literaX = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaX.png')))
literaY = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaY.png')))
literaZ = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaZ.png')))

letters = {'A': literaA, 'B': literaB, 'C': literaC, 'D': literaD, 'E': literaE, 'F': literaF,
           'G': literaG, 'H': literaH, 'I': literaI, 'K': literaK, 'L': literaL, 'M': literaM,
           'N': literaN, 'O': literaO, 'P': literaP, 'Q': literaQ, 'R': literaR, 'S': literaS,
           'T': literaT, 'U': literaU, 'V': literaV, 'W': literaW, 'X': literaX, 'Y': literaY, 'Z': literaZ}

try_open_button = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'button_O_light.png')))

table = resize(resize(resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'table.png')))))


"""
###########################################################
###################### Binary Tree ########################
###########################################################
"""
binary_background = pygame.image.load(os.path.join(path + 'img\\BinarySearch', 'background.jpg'))
platform_binary = pygame.image.load(os.path.join(path + 'img\\BinarySearch', 'platform.png'))
helper_binary_tree = pygame.image.load(os.path.join(path + 'img\\BinarySearch', 'binary_helper.png'))