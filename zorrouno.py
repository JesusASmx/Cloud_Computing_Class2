import pandas as pd

class processor:
    @staticmethod
    def embbed(d):
        try:
            d = d.drop(["RowNumber", "CustomerId", "Surname", "Geography", "Gender", "Card Type"], axis=1) #Delete non-numerical variables.
        except:
            print("No column named RowNumber")
        return d