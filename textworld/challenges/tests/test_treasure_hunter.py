# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.
import os

import textworld
from textworld.challenges import treasure_hunter
from textworld.utils import make_temp_directory
from textworld.generator import compile_game


# def test_making_treasure_hunter_games():
#     for level in range(1, 30 + 1):
#         print('level:{}'.format(level))
#         options = textworld.GameOptions()
#         options.seeds = 1234
#
#         settings = {"level": level}
#         game = treasure_hunter.make(settings, options)
#         assert len(game.quests[0].commands) == game.metadata["quest_length"], "Level {}".format(level)
#         assert len(game.world.rooms) == game.metadata["world_size"], "Level {}".format(level)
#

# TODO: zxf treasure_hunter game source
def test_hunter_game_play(level=2):
    print('level:{}'.format(level))
    options = textworld.GameOptions()
    options.seeds = 1234

    settings = {"level": level}
    game = treasure_hunter.make(settings, options)
    options.path = './'
    game_file = compile_game(game, options)
    textworld.play(game_file)

    # with make_temp_directory(prefix="test_render_wrapper") as tmpdir:
    #     options.path = tmpdir
    #     game_file = compile_game(game, options)
    #     print(os.getcwd())

        # textworld.play(game_file)


# zxf
if __name__ == '__main__':
    # test_making_treasure_hunter_games()

    test_hunter_game_play(level=10)