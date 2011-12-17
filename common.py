class	Environment:
	"Environment is used during code generation to maintain stack indices"
	def	__init__(self):
		self.mapping	=	{}
		self.index	=	0
		self.names = 0

	def	add(self,	param):
		self.mapping[param] = self.index
		self.index	+= 1

	def	add_at(self,	param, at):
		self.mapping[param] = at

	def	get(self,	param):
		if	not	param	in self.mapping:
			exit('unknown local var: %s ' % (param))
		return self.mapping[param]

	def	count(self):
		return len(self.mapping.keys())
	
	def merge_from(self, env, frm):
		for m in env.mapping:
			self.add_at(m, frm)
			frm -= 1

	def increment(self, amount = 1):
		"clone and increment this environment"
		result = Environment()
		result.index = self.index
		for k in self.mapping:
			result.mapping[k] = self.mapping[k] + amount
		return result

	def clone(self):
		"clone this environment so changes wont affect the master environment"
		result = Environment()
		result.index = self.index
		for k in self.mapping:
			result.mapping[k] = self.mapping[k]
		return result

class Visitor(object):
	"generic visitor implementation"
	debug = False

	def visit(self, node, **data):
		"main method of the visitor"
		method = None
		for cls in node.__class__.__mro__:
			method_name = 'visit_' + cls.__name__
			method = getattr(self, method_name, None)
			if method:
				break
		if not method:
			# the fallback is defined on Visitor and thus will always be present
			method = self.fallback
		return method(node, **data)

	def fallback(self, node, **data):
		"generic fallback visit method that gets called if no concrete implementation is available. Prints trace if debug = True. Directs visitor over the children property if represent."
		if self.debug:
			# if we are in debug mode print that we end up here (handy during development)
			print 'fallback ' + node.__class__.__name__
			print node.toStringTree()
		if hasattr(node, 'children'):
			# call and collect results for all children
			result = []
			for child in node.children:
				ans = self.visit(child, **data)
				result.append(ans)
			return result

class CompositeVisitor(Visitor):
	"specialization of of transformer allowing it to be composed of multiple mutually recursive schemes"
	def __init__(self):
		self.active = None
		self.schemes = {}

	def __setitem__(self, key, scheme):
		self.schemes[key] = scheme

	def __getitem__(self, key):
		return self.schemes[key]

	def select(self, scheme):
		self.active = self.schemes[scheme]

	def visit(self, node, **data):
		'direct a visitor over a composite using the classname to select to concrete method to call (instead of an accept method on each class)'
		method = None
		for cls in node.__class__.__mro__:
			method_name = 'visit_' + cls.__name__
			method = getattr(self.active, method_name, None)
			if method:
				break
		if not method:
			method = self.active.fallback
		return method(node, **data)

	def fallback(self, node, **data):
		'generic method to direct a transformer over the children of the current node if the children property is present. prints node name if debug is set to True'
		if self.debug:
			print 'fallback ' + node.__class__.__name__
			print node.toStringTree()
		if hasattr(node, 'children'):
			for child in node.children:
				self.visit(child, **data)