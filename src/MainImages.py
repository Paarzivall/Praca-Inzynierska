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

path = ""
if os.path.isdir('..\img'):
    path = "..\\"

"""
###########################################################
######################## MENU #############################
###########################################################
"""

menu_background = pygame.image.load(os.path.join(path + 'img\\MenuImg', 'menu_background.png'))
start_button = resize(pygame.image.load(os.path.join(path + 'img\\MenuImg', 'start.png')), 1.5)
end_button = resize(pygame.image.load(os.path.join(path + 'img\\MenuImg', 'end.png')), 1.5)
again_button = resize(pygame.image.load(os.path.join(path + 'img\\MenuImg', 'again.png')), 1.5)
title = pygame.image.load(os.path.join(path + 'img\\MenuImg', 'title.png'))
wiking_icon = pygame.image.load(os.path.join(path + 'img\\MenuImg', 'wiking_icon.png'))

"""
###########################################################
################### Binary Convert ########################
###########################################################
"""

# otwieranie zamka
first_background = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert', 'otwieranie_zamka.png')), 1.5)

helper_binary_convert = pygame.image.load(os.path.join(path + 'img\\BinaryConvert', 'helper_image.png'))

# cyfry do 1 levelu

zero = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '0.png')), 1.5)
one = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '1.png')), 1.5)
two = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '2.png')), 1.5)
three = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '3.png')), 1.5)
four = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '4.png')), 1.5)
five = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '5.png')), 1.5)
six = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '6.png')), 1.5)
seven = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '7.png')), 1.5)
eight = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '8.png')), 1.5)
nine = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Cyfry', '9.png')), 1.5)

numbers = {0: zero, 1: one, 2: two, 3: three, 4: four,
           5: five, 6: six, 7: seven, 8: eight, 9: nine}

# piny do 1 lvl

pin_0_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_1_gora.png')), 1.5)
pin_1_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_2_gora.png')), 1.5)
pin_2_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_3_gora.png')), 1.5)
pin_3_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_4_gora.png')), 1.5)
pin_4_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_5_gora.png')), 1.5)
pin_5_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_6_gora.png')), 1.5)
pin_6_up = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_7_gora.png')), 1.5)

pins_up = {0: pin_0_up, 1: pin_1_up, 2: pin_2_up, 3: pin_3_up,
            4: pin_4_up, 5: pin_5_up, 6: pin_6_up}

pin_0_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_1_dol.png')), 1.5)
pin_1_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_2_dol.png')), 1.5)
pin_2_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_3_dol.png')), 1.5)
pin_3_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_4_dol.png')), 1.5)
pin_4_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_5_dol.png')), 1.5)
pin_5_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_6_dol.png')), 1.5)
pin_6_down = resize(pygame.image.load(os.path.join(path + 'img\\BinaryConvert\\Bolce', 'bolec_7_dol.png')), 1.5)

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

platform_background2 = resize(pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'svartal_background.png')), 1.5)
ancient_forest = resize(pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'ancient_forest.png')), 1.5)

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
platforms_grass = [single_platform, platform_left, platform_center, platform_right]

transport_platform_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'metal_L.png'))
transport_platform_center = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'metal_C.png'))
transport_platform_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'metal_R.png'))
single_transport_platform = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'metal_single.png'))
platforms = [single_transport_platform, transport_platform_left, transport_platform_center, transport_platform_right]

platform_left_stone = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'stone_L.png'))
platform_center_stone = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'stone_C.png'))
platform_right_stone = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'stone_R.png'))
single_platform_stone = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'stone_single.png'))
platforms_stone = [single_platform_stone, platform_left_stone, platform_center_stone, platform_right_stone]


platform_left_wood = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'wood_L.png'))
platform_center_wood = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'wood_C.png'))
platform_right_wood = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'wood_R.png'))
single_platform_wood = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'wood_single.png'))
platforms_wood = [single_platform_wood, platform_left_wood, platform_center_wood, platform_right_wood]

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

bullet_enemy_left = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'kamien_L.png'))
bullet_enemy_right = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'kamien_R.png'))

# Portal pod koniec rundy
portal = resize(pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'finish_portal.png')), 1.5)


# itemy na mapie
icon = resize(pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'pergamin_ikona.png')), 5.0625)
pergamin = pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'pergamin_ikona.png'))
potion_max_life = resize(pygame.image.load(os.path.join(path + 'img\\Platforms_Levels', 'potion_max_life.png')), 3.375)

"""
###########################################################
###################### Cutsceny ###########################
###########################################################
"""

cutscena_1 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#1.png')), 1.5)
cutscena_2 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#2.png')), 1.5)
cutscena_3 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#3.png')), 1.5)
cutscena_4 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#4.png')), 1.5)
cutscena_5 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#5.png')), 1.5)
cutscena_6 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#6.png')), 1.5)
cutscena_7 = resize(pygame.image.load(os.path.join(path + 'img\\Cutsceny', 'cutscena#7.png')), 1.5)


"""
###########################################################
#################### Bubble Sort ##########################
###########################################################
"""

#background
bubble_background = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'mechanizm_szkic.png')), 1.5)

helper_bubble_sort = pygame.image.load(os.path.join(path + 'img\\bubble', 'helper_bubble_sort.png'))

switch_button = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'switch_off.png')), 1.5)
switch_button_light = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'switch_on.png')), 1.5)
next_button = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'button_R.png')), 1.5)

# cyfry
image_0 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '0.png')), 1.5)
image_1 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '1.png')), 1.5)
image_2 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '2.png')), 1.5)
image_3 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '3.png')), 1.5)
image_4 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '4.png')), 1.5)
image_5 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '5.png')), 1.5)
image_6 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '6.png')), 1.5)
image_7 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '7.png')), 1.5)
image_8 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '8.png')), 1.5)
image_9 = resize(pygame.image.load(os.path.join(path + 'img\\bubble', '9.png')), 1.5)

numbers_image = {0: image_0, 1: image_1, 2: image_2, 3: image_3, 4: image_4,
                 5: image_5, 6: image_6, 7: image_7, 8: image_8, 9: image_9}

lock = resize(pygame.image.load(os.path.join(path + 'img\\bubble', 'kolatka.png')))

"""
###########################################################
###################### PlayFair ###########################
###########################################################
"""

helper_playfair = pygame.image.load(os.path.join(path + 'img\\PlayFair', 'playfair_helper.png'))

playfair_background = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'backgroundPlayFair.png')), 1.5)

#litery
literaA = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaA.png')), 1.5)
literaB = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaB.png')), 1.5)
literaC = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaC.png')), 1.5)
literaD = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaD.png')), 1.5)
literaE = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaE.png')), 1.5)
literaF = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaF.png')), 1.5)
literaG = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaG.png')), 1.5)
literaH = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaH.png')), 1.5)
literaI = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaI.png')), 1.5)
literaK = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaK.png')), 1.5)
literaL = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaL.png')), 1.5)
literaM = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaM.png')), 1.5)
literaN = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaN.png')), 1.5)
literaO = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaO.png')), 1.5)
literaP = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaP.png')), 1.5)
literaQ = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaQ.png')), 1.5)
literaR = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaR.png')), 1.5)
literaS = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaS.png')), 1.5)
literaT = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaT.png')), 1.5)
literaU = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaU.png')), 1.5)
literaV = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaV.png')), 1.5)
literaW = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaW.png')), 1.5)
literaX = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaX.png')), 1.5)
literaY = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaY.png')), 1.5)
literaZ = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'literaZ.png')), 1.5)

letters = {'A': literaA, 'B': literaB, 'C': literaC, 'D': literaD, 'E': literaE, 'F': literaF,
           'G': literaG, 'H': literaH, 'I': literaI, 'K': literaK, 'L': literaL, 'M': literaM,
           'N': literaN, 'O': literaO, 'P': literaP, 'Q': literaQ, 'R': literaR, 'S': literaS,
           'T': literaT, 'U': literaU, 'V': literaV, 'W': literaW, 'X': literaX, 'Y': literaY, 'Z': literaZ}

try_open_button = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'drzewo.png')), 5.0625)

table = resize(pygame.image.load(os.path.join(path + 'img\\PlayFair', 'table.png')), 3.375)


"""
###########################################################
###################### Binary Tree ########################
###########################################################
"""
binary_background = pygame.image.load(os.path.join(path + 'img\\BinarySearch', 'background.jpg'))
platform_binary = pygame.image.load(os.path.join(path + 'img\\BinarySearch', 'platform.png'))
helper_binary_tree = pygame.image.load(os.path.join(path + 'img\\BinarySearch', 'binary_helper.png'))