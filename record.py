class Record:
    # instantiation of the object automatically invokes this function
    def __init__(self, attributes):
        self.attributes = attributes

    def getAttributeById(self, id):
        attributes = self.attributes
        
        for attr in attributes:
            if attr.getId() == id:
                return attr
        
        return None

    def getAllAttributes(self):
        return self.attributes
