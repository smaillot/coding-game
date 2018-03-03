import sys
import math
import random

HEROES = ['DEADPOOL', 'DOCTOR_STRANGE', 'HULK', 'IRONMAN', 'VALKYRIE']

def debug(msg):
    print(msg, file=sys.stderr)

class Game(object):
    def __init__(self):
        # debug
        debug('read my_team')
        self.my_team = int(input())
        self.players = [Player(0), Player(1)]
        self.map = Map()
        self.read_spawns()
        self.objects = []
        self.read_objects()
        self.turn = 0
        
    def read_spawns(self):
        # debug
        debug('read n_spawns')
        self.map.read_spawns(int(input()))        
        
    def read_objects(self):
        # debug
        debug('read n_objects')
        for i in range(int(input())):
            # debug
            debug('read object line')
            self.objects.append(Object(*input().split()))

    def read_entities(self):
        self.players[self.my_team].reset_entities()
        self.players[1 - self.my_team].reset_entities()
        # debug
        debug('read n_entities')
        for i in range(int(input())):
            # debug
            debug('read entity line')
            entity = input().split()
            self.players[int(entity[1])].add_entity(*entity)

    def read_turn(self):
        # debug
        debug('read my gold')
        self.players[self.my_team].gold = int(input())
        # debug
        debug('read ennemy gold')
        self.players[1 - self.my_team].gold = int(input())
        # debug
        debug('read heroes waiting')
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
        self.id = id
        self.team = team
        self.type = entity_type
        self.x = x
        self.y = y
        self.attackRange = attackRange
        self.health = health
        self.maxHealth = max_health
        self.shield = shield
        self.attack_damage = attack_damage
        self.movement_speed = movement_speed
        self.stun_duration = stun_duration
        self.cost = gold_value
        
class Hero(Entity):
    def __init__(self, id, team, entity_type, x, y, attackRange, health, max_health, shield, attack_damage, movement_speed, stun_duration, gold_value, count_down_1, count_down_2, count_down_3, mana, max_mana, mana_regeneration, hero_type, is_visible, items_owned):
        Entity.__init__(self, id, team, entity_type, x, y, attackRange, health, max_health, shield, attack_damage, movement_speed, stun_duration, gold_value)
        self.count_down_1 = count_down_1
        self.count_down_2 = count_down_2
        self.count_down_3 = count_down_3
        self.mana = mana
        self.max_mana = max_mana
        self.mana_regeneration = mana_regeneration
        self.hero_type = hero_type
        self.is_visible = is_visible
        self.items_owned = items_owned

class Printer(object):
    def hero(self, name):
        print(name)
    
    def wait(self):
        print('WAIT')

    def attack(self, unit_id):
        print('ATTACK {}'.format(unit_id))

    def attack_nearest(self):
        print('ATTACK_NEAREST')

    def attack_move(self, x, y, unit_id):
        print('MOVE_ATTACK {} {} {}')

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
    if round_type < 0:
        printer.hero(solver.choose_hero())
    else: # regular turn
        printer.wait()