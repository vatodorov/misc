# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:08:01 2017

@author: BRE49823
"""

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

df[['A']] = 0
df.A[df.D < 0] = 5


type(inputData['BrentPrice'])
type(inputData.BrentPrice)
type(inputData[[1]])


brentPriceDf = pd.read_csv('C:/GitRepos/EAA_Analytics/Personal/VT/Forecasts/Brent_DI_data.csv')

brentPriceDf = brentPriceDf[[1, 2, 3, 4]]

brentPriceArr = brentPriceDf.iloc[:,0:].values
trainSize = int(len(brentPriceArr) * 2/3)
train = brentPriceArr[0:trainSize, :]
validate = brentPriceArr[trainSize:len(brentPriceArr), :]


xVarColumns = [1, 2, 3]
yVarColumns = [0]

trainX = train[:,xVarColumns]
validateX = validate[:, xVarColumns]
    
trainY = train[:, yVarColumns]
validateY = validate[:, yVarColumns]

dataframe_length = len(trainY)


# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
validateX =  np.reshape(validateX, (validateX.shape[0], 1, validateX.shape[1]))

    
tt = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
tt2 = np.reshape(trainX, (152, 1, 3))
tt3 = trainX.reshape(152, 1, 3)





x = np.arange(10)
type(x)
x[2]

x.shape = (2,5)
y = x.reshape(5, 2)
d = y.reshape(2,5)



