from Tree import Tree
from Node import Node
import re

class TreeBuilder:
	def __init__(self, data):
		self.data = data
		self.tree = None

	def computeLevel(self, rawNode):
		level = 1
		for c in rawNode:
			if(c == '|'):
				level = level + 1
			elif(c == '+' or c == '\\'):
				break
		# fix some special issue	
		space = re.search(r'\|\s+',rawNode)
		if space:
			space_count = len(space.group(0))
			# print(space_count)
			level = level + (space_count - 3) / 3
		return level

	def build(self):
		with open(self.data) as f:
			mvn_result = f.read()
			nodeList = mvn_result.split('\n')
		parent = Node(nodeList[0])
		
		self.tree = Tree(parent)
		for rawNode in nodeList[1:]:
			level = self.computeLevel(rawNode)
			child = Node(rawNode)

			while(parent.getLevel() >= level):
				parent = parent.getParent()

			parent.addChild(child)
			parent = child
		
		return self.tree


def main():
	dataFile = "dependency.txt"
	tree = TreeBuilder(dataFile).build()
	print(len(tree.toList()))
	# for i in tree.toList():
	# 	print(i.handled_data)


if __name__ == '__main__':
	main()

