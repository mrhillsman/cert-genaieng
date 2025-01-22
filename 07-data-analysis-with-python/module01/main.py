"""Module 01 - Lab: Importing Data Sets - Used Cars Pricing"""
import asyncio
import locale
import os

import aiohttp
import pandas as pd
import numpy as np

headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
           "body-style","drive-wheels","engine-location","wheel-base","length","width",
           "height","curb-weight","engine-type","num-of-cylinders","engine-size",
           "fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
           "city-mpg","highway-mpg","price"]

FILE_PATH = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
             + 'IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv')

async def download(url, filename):
    """Download from url and write to filename"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                with open(filename, 'w', encoding=locale.getencoding()) as f:
                    f.write(await resp.text())

async def main():
    """The entrypoint for the script"""
    if not os.path.isfile('auto.csv'):
        await download(FILE_PATH, 'auto.csv')
    file_name = 'auto.csv'
    df = pd.read_csv(file_name, header=None)
    # print(df.head())
    # question 1 - check the bottom 10 rows
    # print(df.tail(10))
    # set the headers
    df.columns = headers
    df1 = df.replace('?', np.NaN)
    df = df1.dropna(subset=['price'], axis=0)
    # print(df.head())
    # question 2 - find the names of the columns
    # print(df.columns)
    if not os.path.isfile('automobile.csv'):
        df.to_csv('automobile.csv', index=False)
    # check the data type of data frame "df" by .dtypes
    # print(df.dtypes)
    # get a statistical summary of each column such as count,
    # column mean value, column standard deviation, etc.,
    # print(df.describe())
    # describe all the columns in "df"
    # print(df.describe(include="all"))
    # question 3 - apply the  method to ".describe()" to the columns 'length' and 'compression-ratio'
    print(df[['length', 'compression-ratio']].describe())


if __name__ == '__main__':
    asyncio.run(main())
