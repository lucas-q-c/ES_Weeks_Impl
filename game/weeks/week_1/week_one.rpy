label semana_1:
    $ renpy.say('', semana)
    $ d = 1
    while d < 4:
        $ dia = 'semana1_dia' + str(d)
        call expression dia
        $ d = d + 1
    return