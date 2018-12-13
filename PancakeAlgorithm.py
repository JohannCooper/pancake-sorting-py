GOALSTACK = [4, 3, 2, 1]
TESTSTACK = [2, 4, 1, 3]
moveOptions = [0, 1, 2]
moveHistory = []

def topFlip(stack, level):
	bottomHalf = stack[0 : level]
	topHalf = stack[level : len(stack)]
	topHalf = topHalf[:: -1]

	stack = bottomHalf + topHalf
	return stack

# def recursiveFlip(stack, lastMove, tabLevel):
# 	validMoves = list(moveOptions)
# 	if lastMove in validMoves:
# 		validMoves.remove(lastMove)

# 	for move in validMoves:
# 		newStack = topFlip(stack, move)
# 		if newStack == GOALSTACK:
# 			print "\t" * tabLevel + str(move) + ": " + str(stack) + " GOALSTACK"
# 		elif newStack == TESTSTACK:
# 			print "\t" * tabLevel + str(move) + ": " + str(stack) + " ORIGINAL"
# 		elif [move, newStack] in moveHistory:
# 			print "\t" * tabLevel + str(move) + ": " + str(stack) + " REPEATS"
# 		else:
# 			moveHistory.append([move, newStack])
# 			print "\t" * tabLevel + str(move) + ": " + str(stack)
# 			recursiveFlip(newStack, move, tabLevel + 1)

# recursiveFlip(TESTSTACK, -1, 0)

def recursiveFlip(stack, lastMove, moveLog):
	validMoves = list(moveOptions)
	if lastMove in validMoves:
		validMoves.remove(lastMove)

	for move in validMoves:
		log = moveLog
		newStack = topFlip(stack, move)
		if newStack == GOALSTACK:
			print log + str(move) + "-" + "GOALSTACK"
		elif newStack == TESTSTACK:
			print log + str(move) + "-" + "ORIGINAL"
		elif [move, newStack] in moveHistory:
			continue
			# print log + "-" + str(move) + "-REPEATS"
		else:
			moveHistory.append([move, newStack])
			log += str(move) + "-"
			recursiveFlip(newStack, move, log)

recursiveFlip(TESTSTACK, -1, "")