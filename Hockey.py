import numpy as np
import pandas as pd

#Hockey player class
class Player():
	"""This class defines a movie with the players team, position and some other stats"""
	def __init__(self, name, team, pos, FO, Thru, CF, Minor, Major, PIMG, GP, PPTOI):
		self.name = name
		self.team = team
		self.pos = pos
		self.FO = FO
		self.Thru = Thru
		self.CF = CF
		self.Minor = Minor
		self.Major = Major
        self.PIMG = PIMG
		self.GP = GP
        self.PPTOI = PPTOI

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

	def getTeam(self):
		return self.team

	def getPosition(self):
		return self.pos

	def getFOWPer(self):
		return self.FOWPer

	def __str__(self):
		return str(self.getName()) + ' plays for ' + str(self.getTeam())

#main function to run all sub functions
def main():
	"""Where all functions will run to simulate the game"""
	intro()
	N = getInputs()
	wins_1, wins_2 = simNGames(N)
	gameSummary(wins_1,wins_2)

def intro():
	"""Prints a nice introduction header"""
	print(100*'=')
	a = 'Welcome to the Hockey Simulator! This Simulator uses the current seasons stats to determine the outcome of a game. Teams are preset based on data imported into excel sheet.'
	print(a)
	print(100*'=')

def teams():
	"""Where player objects are created and their stats are imported. Players are then sorted into teams"""
	#Test Players
	p1 = Player('Player 1', 23, 'Arizona', 'C', 101, 0.43, 0.52)
	p2 = Player('Player 2', 23, 'Arizona', 'RW', 101, 0.43, 0.49)
	p3 = Player('Player 3', 23, 'Arizona', 'LW', 101, 0.43, 0.34)
	p4 = Player('Player 4', 23, 'Utah', 'C', 101, 0.43, 0.503)
	p5 = Player('Player 5', 23, 'Utah', 'RW', 101, 0.43, 0.42)
	p6 = Player('Player 7', 23, 'Utah', 'LW', 101, 0.43, 0.45)

	team_1 = [p1,p2,p3]
	team_2 = [p4,p5,p6]
	
	return team_1, team_2

def getInputs():
	"""Only used for getting number of games if user wants to simulate more"""
	N = int(input('How many games would you like to simulate: '))
	track events
	return N

def simNGames(N):
	"""Simulates number of inputted games and keeps track of stats of each game"""
	team_1, team_2 = teams()
	wins_team_1 = 0
	wins_team_2 = 0

	for i in range(N):
		score_1, score_2, win_1, win_2 = simOneGame(team_1,team_2)

		print('score team 1: ', score_1)
		print('score team 2: ', score_2)

		if win_1:
			wins_team_1 += 1
		elif win_2:
			wins_team_2 += 1

	return wins_team_1, wins_team_2

def simOneGame(team_1, team_2):
	"""Main function that game is run under, all game logic is here."""
	minutes = 0
	win_1 = False
	win_2 = False
	score_team_1 = 0
	score_team_2 = 0
	Track_changes = False

	#main game clock
	while minutes < 60:

		minutes += 1

	#check if scores are equal and if they are go into overtime
	if score_team_1 == score_team_2:
		overTime()
	elif score_team_1 > score_team_2:
		win_1 = True
	elif score_team_2 > score_team_1:
		win_2 = True

	return  score_team_1, score_team_2, win_1, win_2

def gameSummary(stat1, stat2):
	"""Output results"""
	print('Team 1 won {0} games'.format(stat1))
	print('Team 2 won {0} games'.format(stat2))

def faceOff():
	#select a center from each team and have them faceoff
	#use face off win% of each player
	pass

def overTime():
	pass

if __name__ == '__main__': main()

#Any test code put down here

# stats = pd.read_csv('Imported_data.csv')
# stats[:1]cl