import numpy as np
import pandas as pd
import random

#Hockey player class
class Player():
	"""This class defines a movie with the players team, position and some other stats"""
	def __init__(self, Player, Team, Pos, FO, Thru, CF, Penalties, Minor, GP, PPG):
		self.Player = Player
		self.Team = Team
		self.Pos = Pos
		self.FO = FO
		self.Thru = Thru
		self.CF = CF
        self.Penalties = Penalties
		self.Minor = Minor
		self.GP = GP
        self.PPG = PPG


	def getPlayer(self):
		return self.Player

	def getTeam(self):
		return self.Team

	def getPosition(self):
<<<<<<< HEAD
		return self.pos

	def getFO(self):
		return self.FO

	def getThru(self):
		return self.Thru

	def getCF(self):
		return self.CF

	def setFO(self,new_FO):
		self.FO = new_FO
=======
		return self.Pos

	def getFO(self):
		return self.FO
    
	def getThru(self):
		return self.Thru
    
	def getCF(self):
		return self.CF

	def getPenalties(self):
		return self.Penalties
    
	def getMinor(self):
		return self.Minor
    
	def getGP(self):
		return self.GP
    
	def getPPG(self):
		return self.PPG
>>>>>>> 915ed6a5b435a16e37a3743bf2624c878941a3b6

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
	p1 = Player('Player 1', 'Arizona', 'C', 0.54, 0.72,0.55,1,1,1,1,1)
	p2 = Player('Player 2', 'Arizona', 'RW', 0.43, 0.62,0.56,1,1,1,1,1)
	p3 = Player('Player 3', 'Arizona', 'LW', 0.44, 0.49,0.49,1,1,1,1,1)
	p4 = Player('Player 4', 'Utah', 'C', 0.49, 0.659,0.51,1,1,1,1,1)
	p5 = Player('Player 5', 'Utah', 'RW', 0.40, 0.33,0.48,1,1,1,1,1)
	p6 = Player('Player 7', 'Utah', 'LW', 0.41, 0.8,0.47,1,1,1,1,1)

	team_1 = [p1,p2,p3]
	team_2 = [p4,p5,p6]
	
	return team_1, team_2

def getInputs():
	"""Only used for getting number of games if user wants to simulate more"""
	N = int(input('How many games would you like to simulate: '))
	return N

def simNGames(N):
	"""Simulates number of inputted games and keeps track of stats of each game"""
	team_1, team_2 = teams()
	wins_team_1 = 0
	wins_team_2 = 0

	for i in range(N):
		score_1, score_2, win_1, win_2 = simOneGame(team_1,team_2)

		if win_1:
			wins_team_1 += 1
		elif win_2:
			wins_team_2 += 1

	return wins_team_1, wins_team_2

def simOneGame(team_1, team_2):
	"""Main function that game is run under, all game logic is here."""
	minutes = 0
	win_1 = win_2 = False
	score_team_1 = score_team_2 = 0
	Track_changes = False

	controlling_team = faceOff(team_1,team_2)
	lineup = control(controlling_team,team_1,team_2)

	while minutes < 60:

		for i in lineup:
			if random.random() < i.getThru():
				pass
			else:
				pass

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

def faceOff(team_1, team_2):
	"""Faceoff condtion"""
	controlling_team = ''
	t1c = random.choice([i for i in team_1 if i.getPosition() == 'C'])
	t2c = random.choice([i for i in team_2 if i.getPosition() == 'C'])
	
	if random.random() < t1c.getFO():
		controlling_team = t1c.getTeam()
	else:
		controlling_team = t2c.getTeam()

	return controlling_team

def control(team_name,team_1,team_2):
	"""Function to keep checking who currently has control and will switch the line ups"""
	if team_name == team_1[0].getTeam():
		lineup = offensiveLineup(team_1)
	elif team_name == team_2[0].getTeam():
		lineup = offensiveLineup(team_2)

	return lineup

def offensiveLineup(team):
	"""randomly creates offensive lineup"""
	SL = []
	SL.append(random.choice([i for i in team if i.getPosition() == 'LW']))
	SL.append(random.choice([i for i in team if i.getPosition() == 'C']))
	SL.append(random.choice([i for i in team if i.getPosition() == 'RW']))
	return SL

def overTime():
	"""If both teams have same score then game goes into overtime"""
	pass

if __name__ == '__main__': main()

#Any test code put down here

# stats = pd.read_csv('Imported_data.csv')
# stats[:1]cl