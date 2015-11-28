#!/usr/bin/env python
import numpy as np
from seasonal_stats import PlayerSeasonals

with open ('top10k.txt', 'r') as f:

    players = f.read().splitlines()

    f.close()

playerScores = [PlayerSeasonals(i) for i in players[0:5]]
wins = [player.wins for player in playerScores]
hours = [player.hours for player in playerScores]

array_wins = np.array(wins)
array_hours = np.array(hours)
array_playerScores = np.array(playerScores)
mask = np.not_equal(wins, np.zeros(len(wins)))
array_wins = array_wins[mask]
array_hours = array_hours[mask]
array_playerScores = array_playerScores[mask]


fig = plt.figure()
ax = fig.add_subplot(111)
labels = [player.name for player in array_playerScores]
plt.semilogx(array_hours,array_wins,'o')
plt.axis([0,2000,0,20])
for label, x, y in zip(labels, array_hours, array_wins):
        plt.annotate(
        label, 
        xy = (x, y), xytext = (50*np.random.rand(), 30*np.random.rand()+np.random.randint(5,10)),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
plt.title('Seasonal Hiscore Results of the top {} ranked players'.format(len(playerScores)))
plt.xlabel('Hours spent (log scale)')
plt.ylabel('Number of Hiscores Won')
plt.savefig('Seasonal Hiscores')
plt.show()