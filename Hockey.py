import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

stats = pd.read_csv('All_data.csv')

#Hockey player class
class Player():
	"""This class defines a movie with the players team, position and some other stats"""
	def __init__(self, Name, Team, Pos, FO, SP, CF, GP):
		self.Name = Name
		self.Team = Team
		self.Pos = Pos
		self.FO = FO
		self.SP = SP
		self.CF = CF
		self.GP = GP

	def getName(self):
		return self.Name

	def getTeam(self):
		return self.Team

	def getPosition(self):
		return self.Pos

	def getFO(self):
		return self.FO

	def getSP(self):
		return self.SP

	def getCF(self):
		return self.CF

	def getGP(self):
		return self.GP

	def setFO(self,new_FO):
		self.FO = new_FO

	def setSP(self,new_SP):
		self.SP = new_SP

	def setCF(self,new_CF):
		self.CF =new_CF

	def __str__(self):
		return str(self.getName()) + ' plays for ' + str(self.getTeam())
		
def main():
	"""Where all functions will run to simulate the game"""
	intro()
	team_1, team_2 = teams()
	team, incr = getInputs(team_1,team_2)
	RegWins, SPWins, FOWins, CFWins = iterGames(team_1, team_2, incr, team)
	Summary(RegWins, SPWins, FOWins, CFWins, team, team_1, team_2)

def intro():
	"""Prints a nice introduction header"""
	print(150*'=')
	a = 'This program allows you to see how much of an impact CF, FO and SP percentage have on the impact of a game for 10 iterations.'
	print(a)
	print(150*'=')

def teams():
	"""Where player objects are created and their stats are imported. Players are then sorted into teams"""
	PlayerList = []
	for i in range(len(stats)):
		PlayerList.append(Player(stats.iloc[i]['Player'], stats.iloc[i]['Team'], stats.iloc[i]['Pos'],
								stats.iloc[i]['FO'], stats.iloc[i]['SP'], stats.iloc[i]['CF'],stats.iloc[i]['GP']))
	team_1 = []
	team_2 = []

	#sorting teams
	for i in PlayerList:
		if i.getTeam() == PlayerList[0].getTeam():
			team_1.append(i)
		else:
			team_2.append(i)

	return team_1, team_2

def getInputs(team_1,team_2):
	"""getting user inputs"""
	print('\nCurrent teams loaded in for this simulation')
	print('Team 1 is the {0}\nTeam 2 is the {1}'.format(team_1[0].getTeam(),team_2[0].getTeam()))
	print('CF% (How much they control the puck)')
	print('SP% (How often the score)')
	print('FO% (How often they win face offs)')
	team = input('Which team stats would you like to change (please enter T1 or T2): ')
	incr = float(input('How much would you like to increment these stats by (0.01-0.1): '))

	return team, incr

def iterGames(team_1, team_2, incr, team):
	count = 10
	N = 100
	current_val = 0
	rounds = 0
	RegWins = []
	SPWins = []
	FOWins = []
	CFWins = []

	while rounds < count:
		RegWins.append(simNGames(100,team_1,team_2,team,current_val, 'REG'))
		SPWins.append(simNGames(100,team_1,team_2,team,current_val, 'SP'))
		FOWins.append(simNGames(100,team_1,team_2,team,current_val, 'FO'))
		CFWins.append(simNGames(100,team_1,team_2,team,current_val, 'CF'))

		current_val += incr
		rounds += 1

	return RegWins, SPWins, FOWins, CFWins

def simNGames(N,team_1,team_2, team, current_val, stat):
	"""Simulates number of inputted games and keeps track of stats of each game"""
	wins_team_1 = 0
	wins_team_2 = 0

	team_1, team_2 = statChange(team_1,team_2,current_val,team,stat)

	for i in range(N):
		score_1, score_2, winner = simOneGame(team_1,team_2)

		if winner == team_1[0].getTeam():
			wins_team_1 += 1
		elif winner == team_2[0].getTeam():
			wins_team_2 += 1

	if team == 'T1':
		return wins_team_1
	elif team =='T2':
		return wins_team_2

def statChange(team_1,team_2, incr, team,stat):
	if team == 'T1':
		if stat == 'REG':
			pass
		elif stat == 'SP':
			for i in team_1:
				i.setSP(i.getSP() + incr)
		elif stat == 'FO':
			for i in team_1:
				i.setFO(i.getFO() + incr)
		elif stat == 'CF':
			for i in team_1:
				i.setCF(i.getCF() + incr)
	elif team == 'T2':
		if stat == 'REG':
			pass
		elif stat == 'SP':
			for i in team_2:
				i.setSP(i.getSP() + incr)
		elif stat == 'FO':
			for i in team_2:
				i.setFO(i.getFO() + incr)
		elif stat == 'CF':
			for i in team_2:
				i.setCF(i.getCF() + incr)

	return team_1, team_2

def simOneGame(team_1, team_2):
	"""Main function that game is run under, all game logic is here."""
	minutes = 0
	winner = ''
	score_team_1 = score_team_2 = 0
	Track_changes = False

	controlling_team = faceOff(team_1,team_2)

	while minutes < 60:

		lineup = control(controlling_team,team_1,team_2)

		for i in lineup:
			# print(i.getTeam())
			# print(i.getSP())
			# print(i.getFO())

			if random.random() < i.getSP(): #Seeing if player scores
				#print('someone scored', minutes)
				if i.getTeam() == team_1[0].getTeam():
					#print('player scored', i.getTeam())
					score_team_1 += 1
					controlling_team = faceOff(team_1,team_2)
					#print('team 1 scored', minutes)
					#print('')
					break

				elif i.getTeam() == team_2[0].getTeam():
					#print('player scored', i.getTeam())
					score_team_2 += 1
					controlling_team = faceOff(team_1,team_2)
					#print('team 2 scored', minutes)
					#print('')
					break
	
			elif random.random() < i.getCF(): #To see if puck get stolen
				#print('someone missed', minutes)
				if i.getTeam() == team_1[0].getTeam():
					#print('had it stolen', i.getTeam())
					controlling_team = team_2[0].getTeam()
					break

				elif i.getTeam() == team_2[0].getTeam():
					#print('had it stolen', i.getTeam())
					controlling_team = team_1[0].getTeam()
					break

		minutes += 1

	#check if scores are equal and if they are go into overtime
	if score_team_1 == score_team_2:
		winner = overTime(team_1,team_2)
	elif score_team_1 > score_team_2:
		winner = team_1[0].getTeam()
	elif score_team_2 > score_team_1:
		winner = team_2[0].getTeam()

	return  score_team_1, score_team_2, winner

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

def overTime(team_1,team_2):
	"""If both teams have same score then game goes into overtime, basically same as normal game """
	minutes = 0
	winner = ''

	controlling_team = faceOff(team_1,team_2)

	while minutes < 5:

		lineup = control(controlling_team,team_1,team_2)

		for i in lineup:

			if random.random() < i.getSP(): #Seeing if player scores
				if i.getTeam() == team_1[0].getTeam():
					winner = i.getTeam()
					return winner

				elif i.getTeam() == team_2[0].getTeam():
					winner = i.getTeam()
					return winner
	
			elif random.random() < i.getCF(): #To see if puck get stolen
				# print('someone missed', minutes)
				if i.getTeam() == team_1[0].getTeam():
					controlling_team = team_2[0].getTeam()
					break

				elif i.getTeam() == team_2[0].getTeam():
					controlling_team = team_1[0].getTeam()
					break

		minutes += 1

def Summary(RegWins, SPWins, FOWins, CFWins,team,team_1,team_2):
	"""Output results"""
	team_stat = []

	if team == 'T1':
		team_stat = team_1
	elif team == 'T2':
		team_stat = team_2

	x = np.linspace(0,10,10)

	plt.figure(figsize=(20,20))
	plt.grid(True)
	plt.xticks(np.arange(0, 11, 1))
	plt.axhline(0, color='black', lw=1)
	plt.axvline(0, color='black', lw=1)
	plt.plot(x, RegWins, '-Db', label = 'Regular Stats')
	plt.plot(x, SPWins, '-Dr', label = 'Increased SP Stats')
	plt.plot(x, FOWins, '-Dk', label = 'Increased FO Stats')
	plt.plot(x, CFWins, '-Dg', label = 'Increased CF Stats')
	plt.xlabel('Number of Increments')
	plt.ylabel('Number of Wins out of 100 Games')
	plt.title('{0} Data for Increasing SP and FO'.format(team_stat[0].getTeam()))
	plt.legend()
	plt.show()

if __name__ == '__main__': main()