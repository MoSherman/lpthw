"""
    This Game is based on exercise 45 of lpthw
    using lessons learned in all previous exercises 
    but particularly classes and functions.
    This Game is called Home for the Holidays
"""

# Importing exit and radint modules for use later
from sys import exit
from random import randint


class Scene(object):
    
    def enter(self):
        print "This scene is not yet configed. Implement enter()."
        
        exit(1) 

# The games engine, used to play Scenes
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        # takes the Mum scene or returned scene and sets as current 
        current_scene = self.scene_map.opening_scene()
        # sets the Christmas Dinner class and sets it as the last scene
        last_scene = self.scene_map.next_scene('Christmas Dinner')
        
        # loops the game until the Chritmas Dinner scene
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        # allows the last scene to play when loop is no longer true
        current_scene.enter()
        
        

class Hospital(Scene):
    
    pass 
    
    text = """
            Oh no you fell for it! You obviously weren't paying attention
            \nin your assassins boarding school. Your whole family is very 
            \ndisappointed with your poor performance. To top it all off 
            \nthe police got suspicious after a doctor called them about 
            \nyour case. Now the whole family has been arrested on 
            \nsuspicion of multiple murders around the world. You fail 
            \nas an assassin and you've failed your family. And even worse
            \nbecause of all this you are expelled from assassin school.
        
    """           
    
    def enter(self):
        print text
        exit(1)

class ChristmasDinner(Scene):
    
    pass

    text = """
            Wow! You really impressed your family with your skills. 
            \nYou've obviously learned a lot at assassin school.
            \nNow you get to enjoy Christmas Dinner with your family.
            \nHopefully you'll be the one who guess correctly this 
            \nyear as to where Mum has hidden the antidote to the 
            \npoison which was in you lovely holiday feast!       
    """           
    
    def enter(self):
        print text
        exit(1)
    
class Dungeon(Scene):
    
    def enter(self):
        print """
        Well that was a silly trick to fall for as you know your
        \nMum loves poisons and deadly animals most of all.
        \nYou wake up in the families dungeon locked in a cell. 
        \nThere are three baskets in the cell with you and 
        \nknowing your mother you guess that two will have deadly
        \nsnakes in and the third will have a lock picking kit.
        \nNow you just have to choose which basket. So which one?
        \nThe one to the left, the center one, or the one to the right?
        """

        numbers = { 
                    0 : 'left', 
                    1 : 'center', 
                    2 : 'right'
            }
        
        lock_pick = randint(0,2)
        
        choice = numbers.get(raw_input("Which basket will you choose? \n > "))
        
        if choice == lock_pick:
            print "Got lock pick"
            
            exit(1)
        
        elif int(choice):
            except ValueError:
                print "Not an integer! Fix Code!"
        
        else:
            print "Picked a snake"
            
            exit(1)
        
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

    scenes = {
                'Mum' : Mum(), 
                'Dungeon' : Dungeon(), 
                'Hospital' : Hospital(), 
                'Dad' : Dad(),
                'Explosion' : Explosion(), 
                'Brother' : Brother(), 
                'Snake Pit' : SnakePit(), 
                'Christmas Dinner' : ChristmasDinner()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('Dungeon')
a_game = Engine(a_map)
a_game.play()






