class ColumnConfig:
    def __init__(self, columnInfo):
        self.columnInfo = columnInfo

    def getType(self):
        return self.columnInfo.get('type')

    def getId(self):
        return self.columnInfo.get('id')

    def getIndexA(self):
        return self.columnInfo.get('indexa')

    def getIndexB(self):
        return self.columnInfo.get('indexb')

    def getFeaturesList(self):
        # store variable for working
        features = self.columnInfo.get('features')
        # caso nao exista nenhuma feature a ser calculada para esta coluna
        if not features:
            return []
        # split each feature
        features =  features.split(',')
        # strip to remove whitespaces
        features = [feature.strip() for feature in features]
        return features