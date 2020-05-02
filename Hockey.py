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
		
#main function to run all sub functions
def main():
	"""Where all functions will run to simulate the game"""
	intro()
	N = getInputs()
	team_1, team_2 = teams()
	wins_1, wins_2, no_wins = simNGames(N,team_1,team_2)
	gameSummary(wins_1,wins_2, no_wins)

def intro():
	"""Prints a nice introduction header"""
	print(100*'=')
	a = 'Welcome to the Hockey Simulator! This Simulator uses the current seasons stats to determine the outcome of a game. Teams are preset based on data imported into excel sheet.'
	print(a)
	print(100*'=')

def teams():
	"""Where player objects are created and their stats are imported. Players are then sorted into teams"""
	PlayerList = []
	for i in range(len(stats)):
		PlayerList.append(Player(stats.iloc[i]['Player'], stats.iloc[i]['Team'], stats.iloc[i]['Pos'],
								stats.iloc[i]['FO'], stats.iloc[i]['SP'], stats.iloc[i]['CF'], 
<<<<<<< HEAD
								, stats.iloc[i]['GP']))
=======
								stats.iloc[i]['GP']))
>>>>>>> a55052329f12136864c6648cf8521bd21db6d0c4
	team_1 = []
	team_2 = []

	#sorting teams
	for i in PlayerList:
		if i.getTeam() == PlayerList[0].getTeam():
			team_1.append(i)
		else:
			team_2.append(i)

	#adjusting stats for testing
	team_1_mod, team_2_mod = adjustment(team_1,team_2)

	return team_1_mod, team_2_mod

def getInputs():
	"""Only used for getting number of games if user wants to simulate more"""
	N = int(input('How many games would you like to simulate: '))
	return N

def simNGames(N,team_1,team_2):
	"""Simulates number of inputted games and keeps track of stats of each game"""
	wins_team_1 = 0
	wins_team_2 = 0
	no_winner = 0

	for i in range(N):
		score_1, score_2, winner = simOneGame(team_1,team_2)

		if winner == team_1[0].getTeam():
			wins_team_1 += 1
		elif winner == team_2[0].getTeam():
			wins_team_2 += 1
		else:
			no_winner += 1

	return wins_team_1, wins_team_2, no_winner

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
<<<<<<< HEAD
			# print(i.getTeam())
			# print(i.getSP())
			# print(i.getFO())
=======
<<<<<<< HEAD
			print(i.getTeam())
			print(i.getSP())
			print(i.getFO())
=======
		# 	print(i.getTeam())
		# 	print(i.getThru())
		# 	print(i.getFO())
>>>>>>> a55052329f12136864c6648cf8521bd21db6d0c4
>>>>>>> 7d4f338df37ed32b3a185815635ac9a461edb056

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

<<<<<<< HEAD
def Summary(B_RegWins, B_SPWins, B_FOWins, C_RegWins, C_SPWins, C_FOWins):
=======
def gameSummary(stat1, stat2, stat3):
>>>>>>> a55052329f12136864c6648cf8521bd21db6d0c4
	"""Output results"""
	print('Team 1 won {0} games'.format(stat1))
	print('Team 2 won {0} games'.format(stat2))
	print('No winner games {}'.format(stat3))

	x = np.linspace(0,10,10)

	B_reg = [1]*10 #reg data
	B_SP = [1, 3, 5, 9, 13, 19, 27, 35, 43, 57] #increased SP, will be like [stats1[i]] or something
	B_FO = [1, 2, 6, 12, 14, 18, 24, 29, 33, 39] #increased FO, will be like [stats2[i]] or something

	C_reg = [1]*10 #reg data
	C_SP = [1, 3, 5, 9, 13, 19, 27, 35, 43, 57] #increased SP, will be like [stats1[i]] or something
	C_FO = [1, 2, 6, 12, 14, 18, 24, 29, 33, 39] #increased FO, will be like [stats2[i]] or something

	plt.figure(figsize=(20,20))

	plt.subplot(211)
	plt.grid(True)
	plt.xticks(np.arange(0, 11, 1))
	plt.axhline(0, color='black', lw=1)
	plt.axvline(0, color='black', lw=1)
	plt.plot(x, B_reg, '-Db', label = 'Regular Stats')
	plt.plot(x, B_SP, '-Dr', label = 'Increased SP Stats')
	plt.plot(x, B_FO, '-Dk', label = 'Increased FO Stats')
	plt.xlabel('Number of Increments')
	plt.ylabel('Number of Wins out of 100 Games')
	plt.title('Bruins Data for Increasing SP and FO')
	plt.legend()

	plt.subplot(212)
	plt.grid(True)
	plt.xticks(np.arange(0, 11, 1))
	plt.axhline(0, color='black', lw=1)
	plt.axvline(0, color='black', lw=1)
	plt.plot(x, C_reg, '-Db', label = 'Regular Stats')
	plt.plot(x, C_SP, '-Dr', label = 'Increased SP Stats')
	plt.plot(x, C_FO, '-Dk', label = 'Increased FO Stats')
	plt.xlabel('Number of Increments')
	plt.ylabel('Number of Wins out of 100 Games')
	plt.title('Blackhawks Data for Increasing SP and FO')
	plt.legend()

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

	if winner == '':
		winner = 'No winner'
		return winner

def adjustment(team_1,team_2):
	"""Function to adjust certain teams stats"""
	print('\nCurrent teams loaded in for this simulation')
	print('Team 1 is the {0}\nTeam 2 is the {1}'.format(team_1[0].getTeam(),team_2[0].getTeam()))
	team = input('Which team stats would you like to change (please enter T1 or T2. If no change is wanted type skip): ')

	if team == 'skip':
		pass
	else:
		CF_change = float(input('How much would you like to adjust each players CF% (How much they control the puck): '))
		SP_change = float(input('How much would you like to adjust each players SP% (How often the score): '))
		FO_change = float(input('How much would you like to adjust each players FO% (How often they win face offs): '))

		if team == 'T1':
			for i in team_1:
				i.setCF(i.getCF() + CF_change)
				i.setSP(i.getSP() + SP_change)
				i.setFO(i.getFO() + FO_change)
		elif team == 'T2':
			for i in team_2:
				i.setCF(i.getCF() + CF_change)
				i.setSP(i.getSP() + SP_change)
				i.setFO(i.getFO() + FO_change)

	return team_1,team_2

if __name__ == '__main__': main()