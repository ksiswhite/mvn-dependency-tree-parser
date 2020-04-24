import re

class Node:
	def __init__(self, data):
		self.parent = None
		self.level = 0
		self.data = data
		self.handled_data = re.match('^[\\\ \+\-\|]*(\w+.*)',data).group(1)
		self.parent_tree = None
		self.children = []
		# self.vendor, self.product, self.version = self.parse_detail()


	def getData(self):
		return self.data
	def getChildren(self):
		return self.children
	def getLevel(self):
		return self.level
	def getParent(self):
		return self.parent

	def joint_parent_tree(self):
		result = self.handled_data
		_parent = self.parent
		# print(_parent.handled_data)
		while(_parent):
			result += '->' + _parent.handled_data 
			_parent = _parent.parent
		return result
			
	# def parse_detail(self):
	# 	return '1','2','3'
	def build_list_with_child(self):
		result = []
		for child in self.children:
			result.append(child)
			if child.children:
				result += child.build_list_with_child()
		return result
	def addChild(self, node):
		if(self.__class__ == node.__class__):
			node.parent = self
			node.level = self.level + 1
			node.parent_tree = node.joint_parent_tree()
			self.children.append(node)