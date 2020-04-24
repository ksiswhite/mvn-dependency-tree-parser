######### CLASS TREE  ######### 
import Node
import json

class Tree:
	def __init__(self, root):
		self.root = root

	def parse(self,node):
		result = {}
		if node.children:
			for child in node.children:
				if node.handled_data in result:
					result[node.handled_data].append(self.parse(child))
				else:
					result[node.handled_data] = [self.parse(child)]
		else:
			return {node.handled_data:[]}
		return result

	def toList(self):
		return self.root.build_list_with_child()

	def toJson(self,node):
		return json.dumps(self.parse(node))
######### END OF CLASS #########