import numpy as np
import pandas as pd
import random

stats = pd.read_csv('All_data.csv')

#Hockey player class
class Player():
	"""This class defines a movie with the players team, position and some other stats"""
	def __init__(self, Name, Team, Pos, FO, Thru, CF, Penalties, Minor, GP, PPG):
		self.Name = Name
		self.Team = Team
		self.Pos = Pos
		self.FO = FO
		self.Thru = Thru
		self.CF = CF
		self.Penalties = Penalties
		self.Minor = Minor
		self.GP = GP
		self.PPG = PPG

	def getName(self):
		return self.Name

	def getTeam(self):
		return self.Team

	def getPosition(self):
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
	#Actual Players
	PlayerList = []
	for i in range(len(stats)):
		PlayerList.append(Player(stats.iloc[i]['Player'], stats.iloc[i]['Team'], stats.iloc[i]['Pos'],
								stats.iloc[i]['FO'], stats.iloc[i]['Thru'], stats.iloc[i]['CF'], 
								stats.iloc[i]['Penalties'], stats.iloc[i]['Minor'], stats.iloc[i]['GP'], 
								stats.iloc[i]['PPG']))
	
	team_1 = []
	team_2 = []

	for i in PlayerList:
		if i.getTeam() == PlayerList[0].getTeam():
			team_1.append(i)
		else:
			team_2.append(i)
			
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
	print('Begin new game',controlling_team)
	while minutes < 60:

		lineup = control(controlling_team,team_1,team_2)

		for i in lineup:

			if random.random() < i.getThru(): #Seeing if player scores

				if i.getTeam() == team_1[0].getTeam():
					print('Team 1 score')
					score_team_1 += 1
					controlling_team = faceOff(team_1,team_2)
					break

				elif i.getTeam() == team_2[0].getTeam():
					print('Team 2 score')
					score_team_2 += 1
					controlling_team = faceOff(team_1,team_2)
					break
	
			elif random.random() < i.getCF(): #To see if puck get stolen
				
				if i.getTeam() == team_1[0].getTeam():
					controlling_team = team_2[0].getTeam()
					print('if part Team switched to', controlling_team)
					break
				elif i.getTeam() == team_2[0].getTeam():
					controlling_team = team_1[0].getTeam()
					print('else part team switched to', controlling_team) #issues here****
					break
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
	lineup = ''
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