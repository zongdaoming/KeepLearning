#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: Naive Dorming
# @time: 2021/03/29 20:30:11
pokemon = ['pikachu', 'charmander', 'squirtle', 'bulbasaur']
types = ['electric', 'fire', 'water', 'grass'] # not used
levels = [16, 11, 9, 12]
fainted = [True, False, False, False]

# 也需要形参的传递
def next_pokemon(pokemon, levels, fainted):
    best_level = -1;
    best_pokemon =pokemon[0];
    for cur_pokeman, level, has_fainted in zip(pokemon, levels,fainted):
        if not has_fainted and level > best_level:
            best_level = level
            best_pokemon = cur_pokeman
    return best_pokemon

print(next_pokemon(pokemon,levels,fainted))

