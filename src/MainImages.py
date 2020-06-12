import pygame
import os
from src.ResizeClass import resize
"""
# otwieranie zamka

first_background = resize(pygame.image.load(os.path.join('..\img\Level1', 'otwieranie_zamka.png')))

# cyfry do 1 levelu

zero = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '0a.png')))
one = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '1a.png')))
two = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '2.png')))
three = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '3.png')))
four = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '4.png')))
five = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '5.png')))
six = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '6.png')))
seven = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '7.png')))
eight = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '8.png')))
nine = resize(pygame.image.load(os.path.join('..\img\Level1\Cyfry', '9.png')))

numbers = {0: zero, 1: one, 2: two, 3: three, 4: four,
           5: five, 6: six, 7: seven, 8: eight, 9: nine}

# piny do 1 lvl

pin_0_up = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_1_gora.png')))
pin_1_up = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_2_gora.png')))
pin_2_up = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_3_gora.png')))
pin_3_up = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_4_gora.png')))
pin_4_up = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_5_gora.png')))
pin_5_up = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_6_gora.png')))
pin_6_up = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_7_gora.png')))

pins_up = {0: pin_0_up, 1: pin_1_up, 2: pin_2_up, 3: pin_3_up,
            4: pin_4_up, 5: pin_5_up, 6: pin_6_up}

pin_0_down = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_1_dol.png')))
pin_1_down = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_2_dol.png')))
pin_2_down = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_3_dol.png')))
pin_3_down = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_4_dol.png')))
pin_4_down = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_5_dol.png')))
pin_5_down = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_6_dol.png')))
pin_6_down = resize(pygame.image.load(os.path.join('..\img\Level1\Bolce', 'bolec_7_dol.png')))

pins_down = {0: pin_0_down, 1: pin_1_down, 2: pin_2_down,
             3: pin_3_down, 4: pin_4_down, 5: pin_5_down, 6: pin_6_down}

"""


# Platformowe Levele

platform_background = resize(pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'background.png')))

# Ruchy Postaci

stand_right = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_standR.png'))
walk_right1 = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_walkR1.png'))
walk_right2 = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_walkR2.png'))
stand_left = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_standL.png'))
walk_left1 = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_walkL1.png'))
walk_left2 = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_walkL2.png'))
fail_left = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_fallL.png'))
fail_right = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_fallR.png'))
jump_left = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_jumpL.png'))
jump_right = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'player_jumpR.png'))
images_right = [walk_right1, walk_right2]
images_left = [walk_left1, walk_left2]

# Platformy
platform_left = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'grass_L.png'))
platform_center = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'grass_C.png'))
platform_right = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'grass_R.png'))
single_platform = pygame.image.load(os.path.join('..\..\img\Platforms_Levels', 'grass_single.png'))
platforms = [single_platform, platform_left, platform_center, platform_right]
