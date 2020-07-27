#!/usr/bin/env python

import sys

if (len(sys.argv) != 3):
	print("	The game is played by 2 players only")
	sys.exit(1)
else:
	player1 = str(sys.argv[1])
	player2 = str(sys.argv[2])


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def show_board():
	print("	Choose a number between 1-9")
	print("""	.___.___.___.
	| 1 | 2 | 3 |
	|___|___|___|
	| 4 | 5 | 6 |
	|___|___|___|
	| 7 | 8 | 9 |
	|___|___|___|""")

def play_game():
	game_count = 1
	turn = True
	show_board()
	while game_count < 10:
		print("")
		print("	TURN NUMBER " + str(game_count))
		a = 1 if turn else 0
		if a == 1:
			print("	{}'s turn".format(player1))
			choice = input("	>> ")
			if (choice.isdigit() == False):
				if (choice == 'RESET' or choice == 'RESTART'):
					restart()
				else:
					print("	{} choose a number 1-9".format(player1))
					print("	Make your turn again!")
			else:
				if (int(choice) < 1 or int(choice) > 9):
					print("	{} choose a number 1-9".format(player1))
					print("	Make your turn again!")
				else:
					if str(board[int(choice) - 1]) != ' ':
						print("	TAKEN")
						print("	Make your turn again!")
					else:
						turn = False
						choice = int(choice)
						board[choice - 1] = 'O'
						print_board(board)
						check_win(player1, board, 'O')
						game_count = game_count + 1
		else:
			print("	{}'s turn".format(player2))
			choice = input("	>> ")
			if (choice.isdigit() == False):
				if (choice == 'RESET' or choice == 'RESTART'):
					restart()
				else:
					print("	{} choose a number 1-9".format(player2))
					print("	Make your turn again!")
			else:
				if (int(choice) < 1 or int(choice) > 9):
					print("	{} choose a number 1-9".format(player2))
					print("	Make your turn again!")
				else:
					if str(board[int(choice) - 1]) != ' ':
						print("	TAKEN")
						print("	Make your turn again!")
					else:
						turn = True
						choice = int(choice)
						board[choice - 1] = 'X'
						print_board(board)
						check_win(player2, board, 'X')
						game_count = game_count + 1
	print("	DRAW")
	restart()

def print_board(board):
	iterator = 0
	while iterator < 9:
		if iterator < 3:
			print("	.___.___.___.")
			print("	| {0} | {1} | {2} |".format(board[iterator], board[iterator+1], board[iterator+2]))
			print("	|___|___|___|")
			iterator = iterator + 3
		if iterator < 6:
			print("	| {0} | {1} | {2} |".format(board[iterator], board[iterator+1], board[iterator+2]))
			print("	|___|___|___|")
			iterator = iterator + 3
		if iterator < 9:
			print("	| {0} | {1} | {2} |".format(board[iterator], board[iterator+1], board[iterator+2]))
			print("	|___|___|___|")
			iterator = iterator + 3

def check_win(player, board, test):
	for i in range(len(board)):
		if (i == 0):
			if((board[i] == test and board[i+1] == test and board[i+2] == test) or (board[i] == test and board[i+3] == test and board[i+6] == test) or (board[i] == test and board[i+4] == test and board[i+8] == test)):
				print("	PLAYER {} WINS".format(player))
				restart()
		if (i == 1):
			if(board[i] == test and board[i+3] == test and board[i+6] == test):
				print("	PLAYER {} WINS".format(player))
				restart()
		if (i == 2):
			if ((board[i] == test and board[i+2] == test and board[i+4] == test) or (board[i] == test and board[i+3] == test and board[i+6] == test)):
				print("	PLAYER {} WINS".format(player))
				restart()
		if (i == 3):
			if(board[i] == test and board[i+1] == test and board[i+2] == test):
				print("	PLAYER {} WINS".format(player))
				restart()
		if (i == 6):
			if (board[i] == test and board[i+1] == test and board[i+2] == test):
				print("	PLAYER {} WINS".format(player))
				restart()

def restart():
	restart = input("	Do you want to restart the game? Y/N: ")
	if(restart == 'Y' or restart == 'y'):
		board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
		player1 = str(sys.argv[2])
		player2 = str(sys.argv[1])
		play_game()
	else:
		sys.exit(0)

play_game()