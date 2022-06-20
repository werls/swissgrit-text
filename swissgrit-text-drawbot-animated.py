# Ragged Text
# Werllen Castro, 2022
# github.com/werls/ragged-text
# 
# Originally made for Guia Anônima
# 
# Full design process on Behance:
# https://

from drawBot import *
from random import random as random
from random import choice as choice

# excerpt taken from the short story "Guia Anônima",
# by writer Junia Zaidan

TXT = 'os círculos viciados dos iniciados mofados com suas penas em riste suas penas empunhadas resguardando o território onde não é qualquer um que entra ah tá hoje em dia qualquer um escreve sim vocês se incomodam com isso né riem disso guerrilla girls pelas tocas galerias subterrâneas perfurando com broca possante ameaçando bastiões blasé do panteão da erudicice bocetas tocaiadas mascaradas pela raiva e pela pena nossas ondas vúlvicas atomizadas fracassadas uma a uma primeira uma a uma segunda uma a uma terceira uma a uma ninguém solta a mão de ninguém pra cada uma continuar cuidando só de si encenando faticamente o enredo ianque cênico fático lugar de falo faltou classe a classe de todas aquelas mulheres desclassificadas mortas na fronteira de um méxico aviltado todas as mulheres seus casos suas chagas o paradeiro das armas dos crimes que as ceifaram e ceifam todos los dias em todos los cantos de nuestra america latina navalhas punhais emes dezesseis ou apenas a indigência abandonada no deserto de sol e fome e escorpiões voz e vulto a histórias de chicanas meninas pobres esperanzas latinas prenhes de sonho de amor em busca de seus homens suas mulheres seus orgasmos seus pratos de comida seus filhos pendurados nos seus peitos e afagando suas tranças sentados no seu colo deslizando do seu cangote até suas pernas estendidas como em posição de shantala que ficam as mães ao cuidar dos bebês seus filhotes pendendo como bichinhos que dependem da mulher que ela é e essa água que escorre agora no meu corpo é também quente porque é lágrima do choro que carrego sempre em mim eu estou aqui espalho-me derramada sobre este lugar sigo serena respiro pelo diafragma e não ranjo mais os dentes à noite sou simplesmente a escultura da índia na prateleira com os filhotes pendurados ex-cultura de um new mexico que embranqueceu siga serena assentada sobre a terra com seus amores dependurados todos imperfeitos descascados o alvitre de uma esculturinha em fratura sob rasura do tempo'

div = 20
grunge = False

# set width and height of the page
# in this case, the size defined is proportional
# to the format of the book "Guia Anônima": 145 x 210 mm

# width, height = int(145 * 5), int(210 * 5)
width, height = 1080, 1080
source_width, source_height = width / div, height / div
destination_width, destination_height = source_width, source_height

# for typography, you can pass one or more fonts
# if a list of fonts is passed, there will be variation
fonts = ['Halyard Display Semibold']
# fonts = ['Elza Bold']

# basic setup
number_of_slices = 700
font_size = 84
line_height = font_size * 1.03

# distortion variables
position_distortion = 3
angle_distortion = 0

# draw loop
for frame in range(60):
    newPage(width, height)
    frameDuration(1/30)
    # size(width, height)
    # draw white background
    fill(1, 0, 0)
    rect(0, 0, width, height)
    
    n_font = 0
    for i in range(number_of_slices):
        font(fonts[n_font])
        fontSize(font_size)

        x = random() * width
        y = random() * height
    
        path = BezierPath()
        path.moveTo((x, y))
        path.lineTo((x + destination_width, y))
        path.lineTo((x + destination_width, y + destination_height))
        path.lineTo((x, y + destination_height))
        path.lineTo((x, y))
    
        with savedState():
            direction = choice((-1, 1))
            clipPath(path)
        
            # grunge can set a bit of randomness
            # to background fill (white or transparent)
            if grunge:
                if random() > .5:
                    fill(1, 0, 0)
                else:
                    fill(1, 0, 0)
            else:
                fill(1, 0, 0)

            rect(x, y, destination_width, destination_height)
            translate(random() * position_distortion, random() * position_distortion)
            rotate(angle_distortion * random() * direction)
            fill(0)
            lineHeight(line_height)
            textBox(TXT, (0, - font_size, width, height + font_size), align = 'left')
    
        if n_font >= len(fonts) - 1:
            n_font = 0
        else:
            n_font += 1
    
# saveImage('./examples/guia-anonima-animated-1080x1080.mp4')
# saveImage('./examples/guia-anonima-excerpt.png')