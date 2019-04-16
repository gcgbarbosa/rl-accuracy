class Pair:
    def __init__(self, recordA, recordB, score, y):
        self.recordA = recordA
        self.recordB = recordB
        self.score = score
        self.y = y

    def getAtributesAsZip(self):
        attributesA = self.recordA.getAllAttributes()
        recordB = self.recordB

        zipAttributes = []
        for attrA in attributesA:
            tmpId = attrA.getId()
            
            attrB = recordB.getAttributeById(tmpId)

            tmpTuple = (attrA, attrB)
            zipAttributes.append(tmpTuple)

        return zipAttributes

    def getRecordA(self):
        return self.recordA
    
    def getRecordB(self):
        return self.recordB

    def getScore(self):
        return self.score

    def getY(self):
        return self.y
