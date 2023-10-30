import pandas as pd

class SeriesData:
    def __init__ (self,dateStart,dateEnd,timeSeriesList):
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.timeSeriesList = timeSeriesList

class DataImport:
    def __init__(self,seriesInstance):
        self.seriesInstance = seriesInstance
        self.dataRaw = pd.DataFrame()
        self.dataClean = pd.DataFrame()

    def ImportData(self):


    return
'''
Monthly amounts outstanding of monetary financial institutions' sterling and all foreign currency M3 (UK estimate of EMU aggregate) liabilities to private and public sectors (in sterling millions) not seasonally adjusted 
'''