# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import glob
import os
import sys
import numpy as np
import random
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import xlwt 
from xlwt import Workbook 
import xlsxwriter 
from openpyxl import load_workbook
# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Activation, Flatten
# from Keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
# from keras.optimizers import SGD, RMSprop, adam
# from keras.utils.np_utils import to_categorical
# from keras.callbacks import Callback
# from keras import backend as K
# K.backend()
# import tensorflow as tf
# import matplotlib.pyplot as plt


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__== '__main__':
    path = ROOT_DIR+'\\'
    folderName = []
    folderAddress = []
    all_files = []
    excelFileName = []
    # Get folder name
    for i in range(4):
        folderla = i +1
        folder = str(folderla)
        folderName.append("data_Q"+str(folder) +"_2019")
        folderAddress.append(path+"data_Q"+str(folder) +"_2019"+"\\")
    print(folderAddress)
        
    #Get all the files from folders
    #all_files contains four list with total 365 files indicated for 365 days for the year of 2019
    for i in folderAddress:
        all_files.append(glob.glob(i+ "/*.csv"))
    print(len(all_files[0]),len(all_files[1]),len(all_files[2]),len(all_files[3]))
    
    #Prepare for panda to handle the data visulization.
    for i in range(4):
        allFilesName = i
        for fileName in all_files[allFilesName]:
            print("current running for the session" + str(fileName))    
            df = pd.read_csv(fileName)
            #### Create new file at location at ROOT_DIR
            for i in range(len(df)):
                if df.iloc[:,2][i] not in excelFileName:
                    excelFileName.append( df.iloc[:,2][i])
                    # print(len(excelFileName)) ##### total has 39 files
                workbook_Address= ROOT_DIR+"\\"+str(df.iloc[:,2][i])+'.xlsx'
            #if exist add rows otherwise create new one              
                if os.path.isfile(ROOT_DIR +"\\" +str(df.iloc[:,2][i])+'.csv'):
                    x = pd.DataFrame(df.iloc[i]).T.to_csv(index=False, header=False)
                    x = x.replace('\n', '')
                    file = open(ROOT_DIR +"\\" +str(df.iloc[:,2][i])+'.csv','a+')
                    file.writelines(x)
                    file.flush()
                    file.close()
                    # print("old book", str(df.iloc[:,2][i]))                    
                    # writer = pd.ExcelWriter(ROOT_DIR+"\\"+str(df.iloc[:,2][i])+'.xlsx')
                    # reader = pd.read_excel(workbook_Address)
                    # print(len(reader))
                    # # df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)
                    # pd.DataFrame(df.iloc[i]).T.to_excel(writer,header=False,startrow= len(reader)+1,index=False) # append a new row to the excel
                    # writer.close()
                else:
                    x = pd.DataFrame(df.iloc[i]).T.to_csv(index=False)
                    x = x.replace('\n', '')
                    file = open(ROOT_DIR +"\\" +str(df.iloc[:,2][i])+'.csv','a+')
                    file.writelines(x)
                    file.flush()
                    # # workbook = xlsxwriter.Workbook(ROOT_DIR+"\\"+str(df.iloc[:,2][i])+'.xlsx')
                    # # worksheet= workbook.add_worksheet()
                    # # # df.iloc[i].to_excel(workbook)
                    # # workbook.close()
                    
                    # writer = pd.ExcelWriter(ROOT_DIR+"\\"+str(df.iloc[:,2][i])+'.xlsx')+
                    # # df.iloc[i].to_excel(writer,header=False,startrow= 0)
                    # pd.DataFrame(df.iloc[i]).T.to_excel(writer,header=False,startrow= 0)
                    # writer.close()
                    