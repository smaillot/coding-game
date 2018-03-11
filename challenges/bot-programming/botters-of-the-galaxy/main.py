import sys
import math
import random
import numpy as np

HEROES = ['DEADPOOL', 'DOCTOR_STRANGE', 'HULK', 'IRONMAN', 'VALKYRIE']

def debug(msg):
    print(msg, file=sys.stderr)

class Game(object):
    def __init__(self):
        self.my_team = int(input())
        self.players = [Player(0), Player(1)]
        self.map = Map()
        self.read_spawns()
        self.objects = []
        self.read_objects()
        self.turn = 0
        
    def __getattr__(self, key):
        
        if key == 'me':
            return self.players[self.my_team]
        elif key == 'ennemy':
            return self.players[1 - self.my_team]
        
    def read_spawns(self):
        self.map.read_spawns(int(input()))        
        
    def read_objects(self):
        for i in range(int(input())):
            self.objects.append(Object(*input().split()))

    def read_entities(self):
        self.players[self.my_team].reset_entities()
        self.players[1 - self.my_team].reset_entities()
        for i in range(int(input())):
            entity = input().split()
            self.players[int(entity[1])].add_entity(*entity)

    def read_turn(self):
        self.players[self.my_team].gold = int(input())
        self.players[1 - self.my_team].gold = int(input())
        heroes_waiting = int(input())
        if heroes_waiting < 0:
            return 0
        else:
            self.turn += 1
            return 1
                
class Player(object):
    def __init__(self, id):
        self.id = id
        self.gold = 0
        self.entities = []
        self.heroes = []
        
    def reset_entities(self):
        self.entities = []
        self.heroes = []
        
    def add_entity(self, *args):
        if args[2] == 'HERO':
            self.heroes.append(Hero(*args))
        else:
            self.entities.append(Entity(*args[:13]))
            
    def get_bounds(self, unit_type):
        if len(self.entities) > 0:
            x_axis = [e.x for e in self.entities if e.type.upper() == unit_type.upper()]
            if len(x_axis) > 0:
                return [np.min(x_axis), np.max(x_axis)]
            else:
                return []
        else:
            return []
        
class Map(object):
    def __init__(self):
        self.bushes = []
        self.spawns = []
        
    def add_spawn(self, *args):
        if args[0] == 'Bush':
            self.bushes.append(Spawn(*args[1:]))
        elif args[1] == 'Spawn':
            self.spawns.append(Spawn(*args[1:]))
        
    def read_spawns(self, n):
        for i in range(n):
            self.add_spawn(*input().split())
        
class Spawn(object):
    def __init__(self, x, y, radius):
        self.x = int(x)
        self.y = int(y)
        self.radius = int(radius)
        
class Object(object):
    def __init__(self, name, cost, damage, health, max_health, mana, max_mana, speed, regen, is_potion):
        self.name = name
        self.cost = int(cost)
        self.damage = int(damage)
        self.health = int(health)
        self.max_health = int(max_health)
        self.mana = int(mana)
        self.max_mana = int(max_mana)
        self.speed = int(speed)
        solf.regen = int(regen)
        self.is_potion = bool(is_potion)

class Entity(object):
    def __init__(self, id, team, entity_type, x, y, attackRange, health, max_health, shield, attack_damage, movement_speed, stun_duration, gold_value):
        self.id = int(id)
        self.team = int(team)
        self.type = entity_type
        self.x = int(x)
        self.y = int(y)
        self.attackRange = int(attackRange)
        self.health = int(health)
        self.maxHealth = int(max_health)
        self.shield = int(shield)
        self.attack_damage = int(attack_damage)
        self.movement_speed = int(movement_speed)
        self.stun_duration = int(stun_duration)
        self.cost = int(gold_value)
        
    def distance(self, entity):
        return np.sqrt(pow(self.x - entity.x, 2) + pow(self.y - entity.y, 2))
        
class Hero(Entity):
    def __init__(self, id, team, entity_type, x, y, attackRange, health, max_health, shield, attack_damage, movement_speed, stun_duration, gold_value, count_down_1, count_down_2, count_down_3, mana, max_mana, mana_regeneration, hero_type, is_visible, items_owned):
        Entity.__init__(self, id, team, entity_type, x, y, attackRange, health, max_health, shield, attack_damage, movement_speed, stun_duration, gold_value)
        self.count_down_1 = int(count_down_1)
        self.count_down_2 = int(count_down_2)
        self.count_down_3 = int(count_down_3)
        self.mana = int(mana)
        self.max_mana = int(max_mana)
        self.mana_regeneration = int(mana_regeneration)
        self.hero_type = hero_type
        self.is_visible = int(is_visible)
        self.items_owned = int(items_owned)

class Printer(object):
    def hero(self, name):
        print(name)
    
    def wait(self):
        print('WAIT')
        
    def move(self, x, y):
        print('MOVE {} {}'.format(x, y))

    def attack(self, unit_id):
        print('ATTACK {}'.format(unit_id))

    def attack_nearest(self, unit_type):
        print('ATTACK_NEAREST {}'.format(unit_type))

    def attack_move(self, x, y, unit_id):
        print('MOVE_ATTACK {} {} {}'.format(x, y, unit_id))

    def buy(self, item_name):
        print('BUY {}'.format(item_name))

    def sell(self, item_name):
        print('SELL {}'.format(item_name))

class Solver(object):
    def choose_hero(self):
        return random.choice(HEROES)

game = Game() # init game object
printer = Printer()
solver = Solver()
# game loop
while True:
    round_type = game.read_turn() # if the turn is frozen, choose a hero
    game.read_entities()
    if round_type == 0:
        printer.hero(solver.choose_hero())
    else: # regular turn
        #if len(game.me.heroes) > 0:
        #    if len(game.ennemy.heroes) > 0:
        #        # printer.attack_move(game.ennemy.heroes[0].x, game.ennemy.heroes[0].y, game.ennemy.heroes[0].id)
        #        printer.attack_nearest('HERO ')
        #    else: 
        #        printer.attack_nearest('UNIT ')
        #else:
        #    printer.wait()
        if len(game.me.heroes) > 0:
            bounds = game.me.get_bounds('UNIT')
            
            can_attack = False
            for e in game.ennemy.entities:
                if e.distance(game.me.heroes[0]) < game.me.heroes[0].attackRange:
                    can_attack = True
                    break
            
            if len(game.me.heroes) > 0 and can_attack:
                printer.attack_nearest('UNIT')
            else:
                if len(bounds) > 0: 
                    printer.move(bounds[1 - game.my_team], game.me.heroes[0].y)
                else:
                    printer.wait()
        else:
            printer.wait()