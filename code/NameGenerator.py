#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


class NameGenerator:
    """A Humanoid Name Generator.

    It can generate names for male or female humanoids.
    It may be expanded to generate names according to race/origin.
    """
    def MaleNameGenerator(self):
        race = randint(0, 1)  # race index, can be given as variable later
        lines = 0
        name = ''
        file = ''
        if race == 0:
            with open("NameFiles/MSpNames", "r") as file:
                for i, l in enumerate(file):
                    pass
                lines = i+1
            file = open("NameFiles/MSpNames", "r")
        else:
            with open("NameFiles/MEngNames", "r") as file:
                for i, l in enumerate(file):
                    pass
                lines = i + 1
            file = open("NameFiles/MEngNames", "r")

        index = randint(0, lines)
        name = file.readlines()[index]
        file.close()
        return name

    def FemaleNameGenerator(self):
        race = randint(0, 1)  # race index, can be given as variable later
        lines = 0
        name = ''
        file = ''
        if race == 0:
            with open("NameFiles/FSpNames", "r") as file:
                for i, l in enumerate(file):
                    pass
                lines = i + 1
            file = open("NameFiles/FSpNames", "r")
        else:
            with open("NameFiles/FEngNames", "r") as file:
                for i, l in enumerate(file):
                    pass
                lines = i + 1
            file = open("NameFiles/FEngNames", "r")

        index = randint(0, lines)
        name = file.readlines()[index]
        file.close()
        return name
