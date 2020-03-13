import random

class gamePlayer:
    def __init__(self):
        self.pos = 0
        self.landed = []

    ##Gets position of current player
    def get_pos(self):
        return self.pos

    ##Append position of current player
    def give_pos(self,user_pos):
        self.pos = user_pos

    ##Gets list of landed-on properties of current player
    def get_landed(self):
        return self.landed

    ##Append list of landed-on properties of current player
    def give_landed(self,user_landed):
        self.landed = user_landed


class monopolyGame:
    def __init__(self):
        self.dice1 = 0
        self.dice2 = 0
        self.d_count = 0
        self.rand_num = 0
        self.card = ''
        ##Generates chance cards
        self.chance_cards = ['ad:0','ad:39','ad:30','back:3','ad:24','ad:15','ad:11']
        while len(self.chance_cards) != 16:
            self.chance_cards.append('a')
        ##Generates community chest cards
        self.cchest_cards = ['ad:0','ad:30','ad:1']
        while len(self.cchest_cards) != 16:
            self.cchest_cards.append('a')

    def chance(self,user_pos,user_landed):
        ##Gets random card
        self.rand_num = random.randint(0,len(self.chance_cards)-1)
        self.card = self.chance_cards[self.rand_num]
        ##Checks and updates if user pos needs to change
        if self.card == 'a':
            pass
        elif self.card[:1] == 'ad':
            self.card = self.card.split(':')
            user_pos = int(self.card[1])
            user_landed.append(user_pos)
        elif self.card[:3] == 'back':
            self.card = self.card.split(':')
            user_pos -= self.card[1]
            user_landed.append(user_pos)
        return user_pos,user_landed

    def cchest(self,user_pos,user_landed):
        ##Gets random card
        self.rand_num = random.randint(0,len(self.cchest_cards)-1)
        self.card = self.cchest_cards[self.rand_num]
        ##Checks and updates if user pos needs to change
        if self.card == 'a':
            pass
        elif self.card[:1] == 'ad':
            self.card = self.card.split(':')
            user_pos = int(self.card[1])
            user_landed.append(user_pos)
        return user_pos,user_landed
        
    def go_to_jail(self,user_pos):
        ##Puts user in jail
        user_pos = 10
        return user_pos

    def turn(self,user_pos,user_landed):
        ##Sets double count for current player to 0
        self.d_count = 0
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        ##Changes user position
        user_pos += self.dice1
        user_pos += self.dice2
        ##If user position 'leaves the board' (goes past Mayfair), works out where pos should be
        if user_pos >= 40:
            user_pos = user_pos % 40
        ##Appends pos user lands on to list
        user_landed.append(user_pos)
        ##Checks if user on chance
        if user_pos == 7 or user_pos == 22 or user_pos == 36:
            ##Runs chance
            user_pos,user_landed = self.chance(user_pos,user_landed)
            if user_pos == 30:
                ##Sends to jail if chance card drawn requires it
                user_pos = self.go_to_jail(user_pos)
                user_landed.append(user_pos)
        ##Checks if user on community chest
        elif user_pos == 3 or user_pos == 12 or user_pos == 27:
            user_pos,user_landed = self.cchest(user_pos,user_landed)
            ##Runs community chest
            if user_pos == 30:
                ##Sends to jail if community chest card drawn requires it
                user_pos = self.go_to_jail(user_pos)
                user_landed.append(user_pos)
        while (self.dice1 == self.dice2) and (self.d_count <=2):
            ##Runs again, if double is rolled, until doubles == 3 (if necessary)
            self.d_count += 1
            self.dice1 = random.randint(1,6)
            self.dice2 = random.randint(1,6)
            user_pos += self.dice1
            user_pos += self.dice2
            if user_pos >= 40:
                user_pos = user_pos % 40
            user_landed.append(user_pos)
            if user_pos == 7 or user_pos == 22 or user_pos == 36:
                user_pos,user_landed = self.chance(user_pos,user_landed)
                if user_pos == 30:
                    user_pos = self.go_to_jail(user_pos)
                    user_landed.append(user_pos)
            elif user_pos == 3 or user_pos == 12 or user_pos == 27:
                user_pos,user_landed = self.cchest(user_pos,user_landed)
                if user_pos == 30:
                    user_pos = self.go_to_jail(user_pos)
                    user_landed.append(user_pos)
        if self.d_count == 3:
            ##If doubles is 3, sends to jail
            user_pos = 30
            user_pos = self.go_to_jail(user_pos)
            user_landed.append(user_pos)
        return user_pos,user_landed

class mySimulation:
    def __init__(self):
        self.player1 = gamePlayer()
        self.player2 = gamePlayer()
        self.player3 = gamePlayer()
        self.player4 = gamePlayer()
        self.temp_pos = 0
        self.temp_landed = []
        self.total = []
        self.temp_total = []
        self.temp = []
        self.dict = {}
        self.count = 0
        self.game = monopolyGame()

    def round(self):
        ##Gets each player's pos, landed list, then takes turn, then appends back both
        self.temp_pos = self.player1.get_pos()
        self.temp_landed = self.player1.get_landed()
        self.temp_pos,self.temp_landed = self.game.turn(self.temp_pos,self.temp_landed)
        self.player1.give_pos(self.temp_pos)
        self.player1.give_landed(self.temp_landed)
        self.temp_pos = self.player2.get_pos()
        self.temp_landed = self.player2.get_landed()
        self.temp_pos,self.temp_landed = self.game.turn(self.temp_pos,self.temp_landed)
        self.player2.give_pos(self.temp_pos)
        self.player2.give_landed(self.temp_landed)
        self.temp_pos = self.player1.get_pos()
        self.temp_landed = self.player1.get_landed()
        self.temp_pos,self.temp_landed = self.game.turn(self.temp_pos,self.temp_landed)
        self.player3.give_pos(self.temp_pos)
        self.player3.give_landed(self.temp_landed)
        self.temp_pos = self.player4.get_pos()
        self.temp_landed = self.player4.get_landed()
        self.temp_pos,self.temp_landed = self.game.turn(self.temp_pos,self.temp_landed)
        self.player4.give_pos(self.temp_pos)
        self.player4.give_landed(self.temp_landed)

    def collect_totals(self):
        ##Adds every land into a big list
        self.temp_total = self.player1.get_landed()
        for a in range(len(self.temp_total)):
            self.total.append(self.temp_total[a])
        self.temp_total = self.player2.get_landed()
        for a in range(len(self.temp_total)):
            self.total.append(self.temp_total[a])
        self.temp_total = self.player3.get_landed()
        for a in range(len(self.temp_total)):
            self.total.append(self.temp_total[a])
        self.temp_total = self.player4.get_landed()
        for a in range(len(self.temp_total)):
            self.total.append(self.temp_total[a])
        
    def total_sort(self):
        self.total.sort()
##        for b in range(40):
##            for c in range(len(self.total)):
##                for d in range(len(self.total[c])):
##                    if self.total[c][d] == b:
##                        self.temp.append(self.total[c][d])
##        for e in range(40):
##            self.count = 0
##            for f in range(len(self.temp)):
##                if int(self.temp[f]) == e:
##                    self.count += 1
##            self.dict[str(e)] = self.count

    def get_total(self):
        return self.total

def run_sim():
    simulation1 = mySimulation()
    for a in range(50):
        simulation1.round()
    simulation1.collect_totals()
    simulation1.total_sort()
    listy = simulation1.get_total()
    return listy

big_list = []

for b in range(1000):
    listy = run_sim()
    for c in range(len(listy)):
        big_list.append(listy[c])

big_list.sort()

dictionary = {}

file = open('data.txt','w+')

for d in range(40):
    count = 0
    for e in range(len(big_list)):
        if int(big_list[e]) == d:
            count += 1
    dictionary[str(d)] = count
    file.write(str(d) + ';' + str(count) + '\n')
file.close()


print(str(dictionary))
        
##    for c in range(len(dictionary)):
##        temp.append([str(c),str(dictionary[str(c)])])
##    for d in range(40):
##        for e in range(len(temp)):
##            if str(temp[e][0]) == (d):
##                big_dict[str(d)] = int(big_dict[str(d)])
##                big_dict[str(d)] += int(temp[e][1])

##print('final' + str(big_dict))
##    
