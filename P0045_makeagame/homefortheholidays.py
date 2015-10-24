"""
    This Game is based on exercise 45 of lpthw
    using lessons learned in all previous exercises 
    but particularly classes and functions.
    This Game is called Home for the Holidays
"""

class Scene(object):
    
    def enter(self):
        pass 

class Engine(object):
    
    def __init__(self, scene_map)
        pass 
    
    def play(self):
        pass

class Hospital(Scene):
    
    def enter(self):
        pass

class ChristmasDinner(Scene):
    
    def enter(self):
        pass

class Dungeon(Scene):

    def enter(self):
        pass
        
    def baskets(self):
        pass  
        
class Mum(Scene):

    def enter(self):
        pass
            
    def cookies(self):
        pass

class Explosion(Scene):

    def enter(self):
        pass
    
    def skip(self):
        pass

class Dad(Scene):

    def enter(self):
        pass
    
    def stairs(self):
        pass

class SnakePit(Scene):
    
    def enter(self):
        pass
        
    def antidote(self):
        pass

class Brother(Scene):

    def enter(self):
        pass
    
    def door(self):
        pass

class Map(object):
    
    def __init__(self, start_scene):
        pass
    
    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass

a_map = Map('Mum')
a_game = Engine(a_map)
a_game.play()






