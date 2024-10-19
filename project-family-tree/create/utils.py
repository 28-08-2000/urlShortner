from .models import individual

def create_trees(username):
	# we can try here to create a tree
	roots = individual.objects.filter(user=username).filter(father=None).filter(mother=None)

	# create multiple trees
	trees = []
	trees.append(roots)

	# while there at least one has children go downward
	idx = 0
	ok = True
	while ok:
		level = []
		ok = False

		for node in trees[idx]:
			childs = children(node, username)
			for child in childs:
				ok = True
				level.append(child)

		if len(level) != 0:
			trees.append(list(set(level)))
		idx += 1

	# for lst in trees:
	# 	print(lst[0])

	return trees

def children(node, username):
	if node.gender == 'M':
		return individual.objects.filter(user=username).filter(father=node)
	else:
		return individual.objects.filter(user=username).filter(mother=node)