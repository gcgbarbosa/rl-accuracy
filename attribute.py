class Attribute:
    def __init__(self, id, type, value):
        self.id = id
        self.type = type

        # for each type
            # validate value
            # if wrong value throw error
        self.value = value
    
    def getId(self):
        return self.id

    def getType(self):
        return self.type
    
    def getValue(self):
        return self.value


    def _validadeDateAttribute(self, value, format):
        return True

    def _validadeNameAttribute(self, value):
        return True

    def _validadeStringAttribute(self, value):
        return True

    def _validadeCategoricalAttribute(self, value):
        return True
    
    def _validadeIbgeAttribute(self, value):
        return True