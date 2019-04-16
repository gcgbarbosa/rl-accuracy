import configparser

from columnConfig import ColumnConfig

class ConfigLoader:
    def __init__(self, configFileAddress):
        # VERIFICAR SE TODOS OS CAMPOS DO CONFIG ESTAO NO LUGAR
        self.config = configparser.ConfigParser()
        self.config.read(configFileAddress)
        # load config

    def getConfig(self):
        return self.config
    
    def getColumnList(self):
        return self.config.sections()

    def getColumnByNumber(self, number):
        number = str(number)
        if number in self.config:
            columnConfig = ColumnConfig(self.config[number])
            return columnConfig
        return None

    def getScoreIndex(self):
        return self.config.get('DEFAULT', 'IndexScore')

    def getYIndex(self):
        return self.config.get('DEFAULT', 'Y')