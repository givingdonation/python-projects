#!/usr/bin/env python3
##!/usr/bin/env python3
from random import *
verbs = ["motivates", "shows","demostrates","makes", "states"]

verbings = ["motivating", "showing","making", "demostrating"]

nouns = ["actions", "intentions","motivations","choices","claims"]

thisit = ["this", "it"]

cuz = ["because","since"]

matters = ["matters", "is important", "has precident"]

accom = ["accomplishes", "achieves"]

effect = ["effectively","with power","comprehensively","completely","totally"]

succe = ["successful","high achieving"]
for i in range(0,7):
    print(f"{choice(thisit)} {choice(matters)} {choice(cuz)} {choice(thisit)} {choice(verbs)} their {choice(nouns)} {choice(effect)}. What {choice(thisit)} {choice(accom)} is {choice(verbings)} the {choice(nouns)}. {choice(thisit)} is {choice(succe)} {choice(cuz)} they, {choice(effect)}, {choice(verbs)[:-1]} the {choice(nouns)}.")
