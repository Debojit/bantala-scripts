from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from fish_capture import FishCapture

#Globals
seed_file = r'C:\Users\sinha\OneDrive\Documents\Bantala\Operations\Seed_Stock.xlsx'
capture_file = r'C:\Users\sinha\OneDrive\Documents\Bantala\Operations\Fish_Capture.xlsx'

if __name__ == '__main__':

    fish_captured = FishCapture(capture_file)
    print(fish_captured.data['jaistha'])
