from copy import deepcopy
maze = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
			[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
			[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
			[0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
			[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
			[0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
			[0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
			[0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
			[0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
			[1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

end = (12, 19)
start = (14, 0)
#Deepcopy creates a temporary copy to be edited
path = deepcopy(maze)

moves = []
steps = 0
#The end of the maze has not been found so it is false
found = False

#Here we initialize our function move with currentX and currentY as discriminators
def move(currentX, currentY):
	#Set steps, maze, path, found to global vars so we can change them inside the function. 
	#If we don't do this then we'd get an "UnboundLocalError"
	global steps, maze, path, found
	#Check whether the end of the maze has been reached
	if found == True:
		return False
	#Try/except block: Ensures the program does not try and access a position outside the bounds of path
	#This stops the possibility of an index error. It works by:
	#Checking the value at the current coordinates. If the value is "+" (indicating it's been visited already) 
	#Or if either of the values are negative (indicating it's moved outside the bounds of the maze.)
	#If either happens then it stops the current path and backtracks. 
	try:
		if (path[currentY][currentX] == '+' or currentY*currentX < 0):
			return False
	except IndexError:
	    return False
	#Marks the current position on the path
	markMaze(currentX, currentY)
	#Steps is incremented by 1 to track the number of steps taken. 
	steps = steps + 1
	#Check if the current position is a wall (1 represents a wall and 0 represents a passable area)
	#Returns false if it is equal to one and backtracks
	if maze[currentY][currentX] == 1:
		return False
	#Checks if our current coordinates are equal to the end coordinates
	elif (currentX, currentY) == end:
		found = True
		return True
	elif (move(currentX-1, currentY)):
		moves.append('left')
		return True
	elif (move(currentX, currentY-1)):
		moves.append('up')
		return True
	elif (move(currentX+1, currentY)):
		moves.append('right')
		return True
	elif (move(currentX, currentY+1)):
		moves.append('down')
		return True

def markMaze(currentX, currentY):
	print ('X:', currentX, ' Y:', currentY)
	if (currentX, currentY) == start:
		path[currentY][currentX] = 'S'
	elif (currentX, currentY) == end:
		path[currentY][currentX] = 'E'
	else:
		path[currentY][currentX] = '+'
	for x in path:
		print ('\n',x)

def main():
    move(start[0], start[1])
    print ('')
    print ('moves: ', list(reversed(moves)))
    print('steps: ', steps)

if __name__ == '__main__':
	main()