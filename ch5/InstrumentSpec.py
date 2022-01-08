from enum import Enum
class Type(Enum):
	"""
	This class is created to get rid of and ditch this annoying string comparssion.
	"""
	COUSTIC = "ACOUSTIC"
	ELECTRIC = "ELECTRIC"

	def to_string(self):
		return ACOUSTIC.Title() , ELECTRIC.Title()

	
class InstrumentType(Enum):
    GUITAR = "GUITAR"
    MANDOLIN = "MANDOLIN"
    BANJO = "BANJO"    
    DOBROS = "DOBROS"
    FIDDLES = "FIDDLES"

class Style(Enum):
    STYLE1 = "BOLLYWOOD"
    STYLE2 = "HOLLYWOOD"

class Builder(Enum):
    FENDER = "FENDER"
    MARTIN = "MARTIN"
    GIBSON = "GIBSON"

    def to_string(self):
    	return FENDER.Title, GIBSON.Title(), MARTIN.Title()

   
class Wood(Enum):
	CEDAR = "CEDAR"
	MAPLE = "MAPLE"
	COCOBOLO = "COCOBOLO"
	ALDER = "ALDER"

	def to_string(self):
		return CEDAR.Title() , ALDER.Title() , COCOBOLO.Title(), MAPLE.Title() 


class InstrumentSpec:
	"""
	We nolonger need to add or car about all that kind of properiests, since we thought that
	If we have a set of properties that vary across objs, we can strore all these properities 
	usen=ing collectios like map.
	"""
	"""
	def __init__(self,builder,type_of, model,backwood, topwood):
		self.type_of, self.builder, self.model,self.backwood, self.topwood = type_of, builder, model,backwood, topwood

	def getBuilder(self):
		return self.builder

	def getModel(self):
		return self.model
	
	def getType(self):
		return self.type_of

	def getBackwood(self):
		return self.backwood
	
	def getTopwood(self):
		return self.backwood
	"""
	def __init__(self, spec):
		self.spec = spec

	def getProperties(self):
		return self.spec

	def getProperty(self, prob):
		return self.spec[prob]

	def match(self, InsSpec):
		ans = []
		for key in self.spec: #to loop over the keys of the getting insSpac that we need to search for
			if key in InsSpec:
				if InsSpec[key] == self.spec[key]:
					return True
		return False
	