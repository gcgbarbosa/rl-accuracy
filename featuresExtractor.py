import jellyfish

## MINITUTORIAL DE COMO CRIAR UMA FEATURE EM 2 PASSOS
# passo 1: crie uma função para sua feature
### a função deve receber os dois valores utilizados no calculo = (self, valueA, valueB)
# passo 2: de um nome para sua funcao
###  adicione o nome : self.função dentro da variável featureFunctions na função extractFeatures



class FeaturesExtractor:
    def __init__(self, config):
        self.config = config
        # load config

    def getJaroDistance(self, valueA, valueB):
        if valueA and valueB:
            return jellyfish.jaro_distance(valueA, valueB)
        return None

    def isCategoricalEqual(self, valueA, valueB):
        if valueA and valueB:
            if valueA==valueB:
                return 1.0 # max
            else:
                return 0.0 # min
        return None

    def getHammingDistance(self, valueA, valueB):
        if valueA and valueB:
            hamming = jellyfish.hamming_distance(valueA, valueB)

            stringLength = max(len(valueA), len(valueB))

            # normalize the hamming distance to fit between 0 and 1
            similarity = (stringLength-hamming)/stringLength
        else:
            return None
        return similarity
    
    def getIbgeSimilarity(self, valueA, valueB):
        similarity=0.0
        if valueA and valueB:
            if valueA[:2] == valueB[:2]:
                similarity = similarity + 0.4 # 0.4 here means the wheight of the state
                if valueA[2:] == valueB[2:]:
                    similarity = similarity + 0.6 # 0.6 is the wheight of the city
        else:
            return None
        return similarity

    def extractFeatures(self, zipAttributes):
        # get feature functions
        featureFunctions = {
            'hamming': self.getHammingDistance,
            'jaro': self.getJaroDistance,
            'categorical': self.isCategoricalEqual,
            'ibge': self.getIbgeSimilarity
        }
        # get config
        config = self.config
        # declare list to store features
        featureList = []
        #
        for column in config.getColumnList():
            column = int(column)
            # get values
            valueA = zipAttributes[column][0].getValue()
            valueB = zipAttributes[column][1].getValue()
            # get features to calc
            columnConfig = config.getColumnByNumber(column)
            features = columnConfig.getFeaturesList()
            # for each feature, calculate feature
            for feature in features:
                # get feature function acording to config
                singleFeatureFunction = featureFunctions.get(feature)
                # get feature value
                tmpFeature = singleFeatureFunction(valueA, valueB)
                # append value to list
                featureList.append(tmpFeature)
        return featureList