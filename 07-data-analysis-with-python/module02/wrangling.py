"""Module 01 - Lab: Importing Data Sets - Laptop Pricing"""
import asyncio
import locale
import os

import aiohttp
import numpy as np
import pandas as pd

HEADERS = ["index", "manufacturer","category","screen","gpu","os","cpu_core",
           "screen_size_cm","cpu_frequency","ram_gb","storage_gb_ssd","weight_kg","price"]

FILE_PATH = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'+
             'IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv')

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

    df = pd.read_csv(file_name)
    df.columns = HEADERS

    # update screen_size_cm column rounding values to nearest 2 decimals
    df[['screen_size_cm']] = np.round(df[['screen_size_cm']], 2)
    # print(df.head())
    # Task 1
    # Missing data was last converted from '?' to numpy.NaN. Pandas uses NaN and Null
    # values interchangeably. This means, you can just identify the entries having Null
    # values. Write a code that identifies which columns have missing data.
    missing_data = df.isnull()
    for column in missing_data.columns.values.tolist():
        print(missing_data[column].value_counts())
        print("")
        
    # Task 2.a
    # Missing values in attributes that have continuous data are best replaced using
    # Mean value. We note that values in "Weight_kg" attribute are continuous in nature,
    # and some values are missing. Therefore, write a code to replace the missing values
    # of weight with the average value of the attribute.
    avg_weight = df['weight_kg'].astype('float').mean(axis=0)
    print(df['weight_kg'][29:50])
    df['weight_kg'].replace(np.nan, avg_weight, inplace=True)
    print(df['weight_kg'][29:50])

    # Task 2.b




if __name__ == '__main__':
    asyncio.run(main())
