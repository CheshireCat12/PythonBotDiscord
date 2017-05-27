class Command:
	def __init__(self):
		self.commandes = {}

	def __call__(self, fn):
		self.commandes[fn.__name__] = fn
		return fn

	def do(self, name):
		self.commandes[name]()
