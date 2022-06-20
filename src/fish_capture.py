from pandas import DataFrame, Series
import pandas as pd
import numpy as np

class FishCapture():

    data_types = {
        'Bengali Date' : str,
        'English Date': str,
        'Pona': np.float32,
        'Tilapiya': np.float32,
        'Cyprus': np.float32,
        'Black Carp & Glass Carp': np.float32,
        'Bata': np.float32,
        'Silver Carp': np.float32,
        'Tengra': np.float32,
        'Pile': np.float32,
        'Daily Total': np.float32
    }

    @classmethod
    def format_data(cls, data_frame: DataFrame, sheet: str) -> DataFrame:
        df = pd.read_excel(data_frame, sheet_name=sheet, header=0)
        df = df.fillna(0)
        df.drop(df.tail(1).index, inplace=True)
        return df
        
    def __init__(self, data_file: str):
        xls = pd.ExcelFile(data_file)
        self.data = {
            'baisakh': FishCapture.format_data(xls, 'Baisakh'),
            'jaistha': FishCapture.format_data(xls, 'Jaistha')
        }
    
    def fish_caught(self) -> dict:
        pass

    def fish_caught_month(month: str) -> dict:
        pass

    def fish_caught_date(date: str) -> dict:
        pass

    def fish_caught_type(type: str) -> dict:
        pass

    def fish_caught_type(type: str, month: str) -> dict:
        pass