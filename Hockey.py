import numpy as np
import pandas as pd

#Hockey player class
class Player():
	"""This class defines a movie with the players team, position and some other stats"""
	def __init__(self, name, age, team, pos, GP, CFPer, THRUPer):
		self.name = name
		self.age = age
		self.team = team
		self.pos = pos
		self.GP = GP
		self.CFPer = CFPer
		self.THRUPer = THRUPer

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

	def getTeam(self):
		return self.team

	def getPosition(self):
		return self.pos

	def __str__(self):
		return str(self.getName()) + ' plays for ' + str(self.getTeam())

#main function to run all sub functions
def main():
	intro()
	N = getInputs()
	wins_1, wins_2 = simNGames(N)
	gameSummary(wins_1,wins_2)

def intro():
	print(100*'=')
	a = 'Welcome to the Hockey Simulator! This Simulator uses the current seasons stats to determine the outcome of a game. Teams are preset based on data imported into excel sheet.'
	print(a)
	print(100*'=')

def teams():
	#function to initialize teams
	#probably a good place to do the data import and seperate the players into teams
	team_1 = []
	team_2 = []
	pass

def getInputs():
	N = int(input('How many games would you like to simulate: '))
	return N

def simNGames(N):
	wins_team_1 = 0
	wins_team_2 = 0

	for i in range(N):
		score_1, score_2, win_1, win_2 = simOneGame()

		print('score team 1: ', score_1)
		print('score team 2: ', score_2)

		if win_1:
			wins_team_1 += 1
		elif win_2:
			wins_team_2 += 1

	return wins_team_1, wins_team_2

def simOneGame():
	minutes = 0
	win_1 = False
	win_2 = False
	score_team_1 = 1
	score_team_2 = 0

	#main game clock
	while minutes < 60:

		minutes += 1

	#check if scores are equal and if they are go into overtime
	if score_team_1 == score_team_2:
		print('overtime')
	elif score_team_1 > score_team_2:
		win_1 = True
	elif score_team_2 > score_team_1:
		win_2 = True

	return  score_team_1, score_team_2, win_1, win_2

def gameSummary(stat1, stat2):
	print('Team 1 won {0} games'.format(stat1))
	print('Team 2 won {0} games'.format(stat2))

def faceOff():
	#select a center from each team and have them faceoff
	#use face off win% of each player
	pass

if __name__ == '__main__': main()

#Any test code put down here
#Testing player object
p1 = Player('Alex Akiu', 23, 'Arizona', 'C', 101, 0.43, 0.50)
print(p1)

# stats = pd.read_csv('Imported_data.csv')
# stats[:1]cl