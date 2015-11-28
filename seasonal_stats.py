#!/usr/bin/env python

import json
import urllib2
import jsonpickle


class PlayerSeasonals(object):

    def __init__(self, name):

        self.name     = name
        self.url      = 'http://services.runescape.com/m=temp-hiscores/getRankings.json?player={}&status=archived'.format(self.name)
        self.hiscores = json.load(urllib2.urlopen(self.url))        
        self.wins     = self.numberWins()
        self.scores   = self.allTimeScores()
        self.hours    = self.scoresToHours()
        self.total    = self.totalHours()
        self.fields   = {1:'title', 2:'rank', 3:'score_raw'}

    def printHiscores(self):
        fields = self.fields
        for obj in self.hiscores:
            print "{} -- Rank: {} Score: {} \n".format(obj[fields[1]], obj[fields[2]], obj[fields[3]]) 
        return
    def numberWins(self):
        wins     = 0
        for obj in self.hiscores:
            rank = obj['rank']
            if rank == 1:
                wins += 1
        return wins

    def allTimeScores(self):

        scores = {'Wilderness PvP Kills': 0,  'Dominion Tower: Endurance Mode' : 0,  'Life Points Healed': 0, 'Red Imp Kills':0, \
        'Solo Zilyana Kills':0, 'Slayer Tower Kills':0, "Fun Weapon Damage to K'ril":0, \
        'Undead Kills' :0, 'Deaths':0, 'Solo Complexity 6 Dungeons':0, 'Clue Scrolls':0, \
        'Herbs Grown':0, 'Stealing Creation Reward Points':0, 'Chronicle Fragments Offered':0}

        for obj in self.hiscores:
            title = obj['title']
            score = obj['score_raw']
            for k in scores:
                if title == k:
                    scores[k] += score
                    
        return scores

    def scoresToHours(self):
        '''Computes time to get cumulative scores.  Rate is defined in points per hour'''
        hours = self.scores.copy()
        total = 0
        rate = {'Wilderness PvP Kills': 300.0,  'Dominion Tower: Endurance Mode' : 0.33,  'Life Points Healed': 2.6e7, 'Red Imp Kills':900.0, \
        'Solo Zilyana Kills':45.0, 'Slayer Tower Kills':1800.0, "Fun Weapon Damage to K'ril":9e5, \
        'Undead Kills' :1800.0, 'Deaths':120.0, 'Solo Complexity 6 Dungeons':30.0, 'Clue Scrolls':12.0, \
        'Herbs Grown':70.0, 'Stealing Creation Reward Points':80.0, 'Chronicle Fragments Offered': 30.0}

        for k in hours:
           hours[k] /= rate[k]

        return hours

    def totalHours(self):
        '''computes total hours spent'''
        total = 0
        for k in self.hours:
            total += self.hours[k]
        return int(total)

    def __str__(self):
        return 'Seasonal Hiscores of {}'.format(self.name)

    def __repr__(self):
        return 'Seasonal Hiscores of {}'.format(self.name)

if __name__ == '__main__':
