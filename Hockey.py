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
	simNGames(N)

def intro():
	print(100*'=')
	a = 'Welcome to the Hockey Simulator! This Simulator uses the current seasons stats to determine the outcome of a game'
	print(a)
	print(100*'=')

def getInputs():
	N = int(input('How many games would you like to simulate: '))
	return N

def simNGames(N):
	for i in range(N):
		simOneGame()

def simOneGame():
	#main game clock
	for i in range(60):
		pass

	#check if scores are equal if not go into overtime


def teams():
	#function to initialize teams
	#probably a good place to do the data import and seperate the players into teams
	team_1 = []
	team_2 = []
	pass

def faceOff():
	#select a center from each team and have them faceoff
	#use face off win% of each player
	pass

if __name__ == '__main__': main()


#Any test code put down here
#Testing player object
p1 = Player('Alex Akiu', 23, 'Arizona', 'RW', 101, 0.43, 0.50)
print(p1)

# stats = pd.read_csv('Imported_data.csv')
# stats[:1]cl