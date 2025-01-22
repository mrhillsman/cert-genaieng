"""Module 01 - Lab: Importing Data Sets - Laptop Pricing"""
import asyncio
import locale
import os

import aiohttp
import numpy as np
import pandas as pd

HEADERS = ["manufacturer","category","screen","gpu","os","cpu_core",
           "screen_size_inch","cpu_frequency","ram_gb","storage_gb_ssd","weight_kg","price"]

FILE_PATH = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
             + 'IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv')

async def download(url, filename):
    """Download from url and write to filename"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                with open(filename, 'w', encoding=locale.getencoding()) as f:
                    f.write(await resp.text())

async def main():
    """The entrypoint for the script"""
    if not os.path.isfile('laptop.csv'):
        await download(FILE_PATH, 'laptop.csv')
    file_name = 'laptop.csv'

    # Task 1
    # load the dataset to a pandas dataframe named 'df'
    df = pd.read_csv(file_name, header=None)
    print(df.head())

    # Task 2
    # add headers to the dataframe
    df.columns = HEADERS
    print(df.iloc[29])

    # Task 3
    # replace '?' with 'NaN'
    df.replace('?', np.NaN, inplace=True)
    print(df.iloc[29])

    # Task 4
    # print the datatypes of the dataframe columns
    print(df.dtypes)

    # Task 5
    # print the statistical description of the dataset
    # including object types
    print(df.describe(include='all'))

    # Task 6
    # print the summary information of the dataset
    print(df.info())

if __name__ == '__main__':
    asyncio.run(main())
