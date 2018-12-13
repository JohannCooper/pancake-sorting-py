from math import factorial

def topFlip(stack, level):
	bottomHalf = stack[0 : level]
	topHalf = stack[level : len(stack)]
	topHalf = topHalf[:: -1]

	stack = bottomHalf + topHalf
	return stack

def pancakeNumber(PANCAKES):
	PERMUTATIONS = factorial(PANCAKES)
	HIERARCHY = []
	
	HIERARCHY.append([genIntitalStack(PANCAKES)])
	PERMUTATIONS -= 1

	while PERMUTATIONS > 0:
		
		foo = len(HIERARCHY)
		HIERARCHY.append([])
		for j in xrange(0, len(HIERARCHY[foo - 1])):
			for k in xrange(0, PANCAKES):
				testStack = topFlip(HIERARCHY[foo - 1][j], k)
				if (testStack not in HIERARCHY[foo]) and (testStack not in HIERARCHY[foo - 1]) and (testStack not in HIERARCHY[foo - 2]):
					HIERARCHY[foo].append(testStack)
					PERMUTATIONS -= 1

	for entry in HIERARCHY[len(HIERARCHY) - 1]:
		print entry

def createMaxStack(stack, maxLevel):
	if maxLevel == 0:
		print topFlip(stack, 0)
	else:
		testStack = stack
		for i in xrange(0, maxLevel + 1):
			testStack = topFlip(testStack, i)
		createMaxStack(testStack, maxLevel - 1)

def genIntitalStack(PANCAKES):
	stack = []
	for i in xrange(PANCAKES, 0, -1):
		stack.append(i)
	return stack

def reverseMaxStack(stack, maxLevel):
	if maxLevel == len(stack) - 1:
		print stack
	else:
		testStack = stack
		for i in xrange(maxLevel, -1, -1):
			testStack = topFlip(testStack, i)
		reverseMaxStack(testStack, maxLevel + 1)

# pancakeNumber(11)
reverseMaxStack([4, 3, 2, 1], 0)
# createMaxStack(genIntitalStack(4), len(genIntitalStack(4)) - 2)