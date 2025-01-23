"""Module 03 - Plotting"""
import asyncio
import locale
import os

import aiohttp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sbn

from scipy import stats

HEADERS = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
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
    if not os.path.isfile('automobile.csv'):
        await download(FILE_PATH, 'automobile.csv')
    file_name = 'automobile.csv'

    df = pd.read_csv(file_name)
    df.columns = HEADERS

    supposed_to_be_float = ['price', 'engine-size', 'highway-mpg', 'horsepower']
    for column in df:
        if column in supposed_to_be_float:
            df[column].replace('?', np.nan, inplace=True)
            if df[column].dtype == 'object':
                df[column] = df[column].astype(float)

    # sbn.regplot(x="engine-size", y="price", data=df)
    # plt.ylim(0,)
    # plt.savefig('correlation-positive-linear.png')
    # plt.show()
    #
    # sbn.regplot(x="highway-mpg", y="price", data=df)
    # plt.ylim(0,)
    # plt.savefig('correlation-negative-linear.png')
    # plt.show()
    #
    # sbn.regplot(x="peak-rpm", y="price", data=df)
    # plt.ylim(0, )
    # plt.savefig('correlation-weak-linear.png')
    # plt.show()

    avg_price = df['price'].mean(axis=0)
    df['price'].replace(np.nan, avg_price, inplace=True)
    avg_horsepower = df['horsepower'].mean(axis=0)
    df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

    coef, pvalue = stats.pearsonr(df['horsepower'], df['price'])
    print(f"Pearson correlation: {coef:.4f}, P-value: {pvalue:.4f}")

if __name__ == '__main__':
    asyncio.run(main())
