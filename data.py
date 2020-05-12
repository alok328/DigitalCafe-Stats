import numpy as np
import pandas as pd
import json

class Data:

    def myconverter(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj.__str__()

    def getDay(self, date):
        ls = date.split(',')
        return ls[0]


    def makeData(self):
        data = pd.read_csv('dataMay-11-2020.csv')
        data['Date'] = data['Date'].apply(self.getDay)
        data = data.groupby(['Date', 'Meal'], as_index=False).agg({"Consumers": "sum"})
        data = data.sort_values(["Date", "Meal"], ascending = (True, True))
        data = data.to_json(orient='records')
        final_dictionary = eval(data) 
        with open('mealWiseData.json', 'w') as fp:
            json.dump(final_dictionary, fp, default=self.myconverter)

    def dayWise(self):
        data = pd.read_csv('dataMay-11-2020.csv')
        data = data.drop(columns=['Meal'])
        data['Date'] = data['Date'].apply(self.getDay)
        data = data.groupby('Date', as_index=False).agg({'Consumers': 'sum'})
        data = data.to_json(orient='records')
        final_dictionary = eval(data) 
        with open('dayWiseData.json', 'w') as fp:
            json.dump(final_dictionary, fp, default=self.myconverter)
