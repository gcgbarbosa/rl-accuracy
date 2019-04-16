from pair import Pair
from record import Record
from attribute import Attribute
#from .Attribute import Attribute
#from .Attribute import Attribute

class RecordReader:
    def __init__(self, config):
        self.config = config
        # load config
        
    def isNaN(self, num):
        return num != num

    def convertDateToStandardFormat(self, value):
        if self.isNaN(value):
            return None
        return value
    
    def convertNameToStandardFormat(self, value):
        if self.isNaN(value):
            return None
        return value
    
    def convertIbgeToStandardFormat(self, value):
        if self.isNaN(value):
            return None
        if type(value) == float:
            return str(int(value))
        return value
    
    def convertCategoricalToStandardFormat(self, value):
        if self.isNaN(value):
            return None
        return value
    
    

    def getValueTupleFromRow(self, row, columnConfig):
        
        attributeTreatment = {
            'date' : self.convertDateToStandardFormat,
            'name' : self.convertNameToStandardFormat,
            'ibge' : self.convertIbgeToStandardFormat,
            'categorical' : self.convertCategoricalToStandardFormat,
        }

        treatmentFunction = attributeTreatment.get(columnConfig.getType())

        valueA = row[columnConfig.getIndexA()]
        valueB = row[columnConfig.getIndexB()]
        
        if columnConfig.getType() == 'date': 
            treatedValueA = treatmentFunction(valueA)#, format)
            treatedValueB = treatmentFunction(valueB)#, format)
        else :
            treatedValueA = treatmentFunction(valueA)
            treatedValueB = treatmentFunction(valueB)

        return(treatedValueA,treatedValueB)

    def fromPandasRowToRecordTuple(self, row):
        config = self.config
        # list of attributes
        tmpAttributeListA = []
        tmpAttributeListB = []
        for column in config.getColumnList():
            columnConfig = config.getColumnByNumber(column)
            
            tmpId = columnConfig.getId()
            tmpType = columnConfig.getType()

            tmpValueTuple = self.getValueTupleFromRow(row, columnConfig)

            tmpAttributeA = Attribute(tmpId, tmpType, tmpValueTuple[0])
            tmpAttributeListA.append(tmpAttributeA)
            
            tmpAttributeB = Attribute(tmpId, tmpType, tmpValueTuple[1])
            tmpAttributeListB.append(tmpAttributeB)
        
        recordA = Record(tmpAttributeListA)
        recordB = Record(tmpAttributeListB)
        return (recordA, recordB)
    
    def getScoreFromRow(self, row, index):
        if row[index]:
            return row[index]
        return None

    def getYFromRow(self, row, index):
        return row[index]



    def fromPandasRowToPair(self, row):
        config = self.config

        recordTuple = self.fromPandasRowToRecordTuple(row)

        recordA = recordTuple[0]
        recordB = recordTuple[1]

        # get score
        score = self.getScoreFromRow(row, config.getScoreIndex())
        y = self.getYFromRow(row, config.getYIndex())

        pair = Pair(recordA, recordB, score, y)
        
        # return Pair
        return pair