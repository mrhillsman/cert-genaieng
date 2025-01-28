"""Lab: Model Evaluation and Refinement - Used Cars Pricing"""
# import asyncio
import locale
# import os
import warnings

import aiohttp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sbn

# from scipy import stats

warnings.filterwarnings('ignore')

HEADERS = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
           "body-style","drive-wheels","engine-location","wheel-base","length","width",
           "height","curb-weight","engine-type","num-of-cylinders","engine-size",
           "fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
           "city-mpg","highway-mpg","price"]

FILE_PATH = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
             + 'IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/module_5_auto.csv')


async def download(url, filename):
   """Download from url and write to filename"""
   async with aiohttp.ClientSession() as session:
       async with session.get(url) as resp:
           if resp.status == 200:
               with open(filename, 'w', encoding=locale.getencoding()) as f:
                   f.write(await resp.text())


#async def main():
#    """The entrypoint for the script"""
#    if not os.path.isfile('module_5_auto.csv'):
#        await download(FILE_PATH, 'module_5_auto.csv')
#    file_name = 'module_5_auto.csv'
#
#    df = pd.read_csv(file_name, header=0)
#    df.columns = HEADERS
#
#    supposed_to_be_float = ['price', 'engine-size', 'highway-mpg', 'horsepower']
#    for column in df:
#        if column in supposed_to_be_float:
#            df[column].replace('?', np.nan, inplace=True)
#            if df[column].dtype == 'object':
#                df[column] = df[column].astype(float)
#
#if __name__ == '__main__':
#    asyncio.run(main())

df = pd.read_csv(FILE_PATH, header=0)
df = df._get_numeric_data()
df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1, inplace=True)

def distributionplot(RedFunction, BlueFunction, RedName, BlueName, Title):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    ax1 = sbn.kdeplot(RedFunction, color="r", label=RedName)
    ax2 = sbn.kdeplot(BlueFunction, color="b", label=BlueName, ax=ax1)

    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')
    plt.show()
    plt.close()


def pollyplot(xtrain, xtest, y_train, y_test, lr,poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    #training data
    #testing data
    # lr:  linear regression object
    #poly_transform:  polynomial transformation object

    xmax=max([xtrain.values.max(), xtest.values.max()])
    xmin=min([xtrain.values.min(), xtest.values.min()])
    x=np.arange(xmin, xmax, 0.1)

    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()


y_data = df['price']
x_data = df.drop('price', axis=1)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.4, random_state=0)

print("test samples: ", x_test.shape[0])
print("train samples: ", x_train.shape[0])

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train[['horsepower']], y_train)
print(lr.score(x_test[['horsepower']], y_test))
print(lr.score(x_train[['horsepower']], y_train))

from sklearn.model_selection import cross_val_score
rcross = cross_val_score(lr, x_data[['horsepower']], y_data, cv=4)
print(rcross)

print("The mean of the folds is: ", rcross.mean(), " and the standard deviation is: ", rcross.std())

