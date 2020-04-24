import numpy as np
import pandas as pd
stats = pd.read_csv('Imported_data.csv')
stats[:1]

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
	N = input('How many games would you like to simulate: ')

def intro():
	print(100*'=')
	a = 'Welcome to the Hockey Simulator! This Simulator uses the current seasons stats to determine the outcome of a game'
	print(a)
	print(100*'=')

def simNGames(N):
	pass

def simOneGame():
	pass

if __name__ == '__main__': main()

#Testing player object
p1 = Player('Alex Akiu', 23, 'Arizona', 'RW', 101, 0.43, 0.50)
print(p1)