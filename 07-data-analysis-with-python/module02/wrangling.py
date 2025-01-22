"""Module 02 - Lab: Data Wrangling - Laptop Pricing"""
import asyncio
import locale
import os

import aiohttp
import matplotlib.pyplot as plt
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

    """
    Task 1
    Missing data was last converted from '?' to numpy.NaN. Pandas uses NaN and Null
    values interchangeably. This means, you can just identify the entries having Null
    values. Write a code that identifies which columns have missing data.
    """
    # missing_data = df.isnull()
    # for column in missing_data.columns.values.tolist():
    #     print(missing_data[column].value_counts())
    #     print("")
        
    """"
    Task 2a
    Missing values in attributes that have continuous data are best replaced using
    Mean value. We note that values in "Weight_kg" attribute are continuous in nature,
    and some values are missing. Therefore, write a code to replace the missing values
    of weight with the average value of the attribute.
    """
    # avg_weight = df['weight_kg'].astype('float').mean(axis=0)
    # print(df['weight_kg'][29:50])
    # df['weight_kg'].replace(np.nan, avg_weight, inplace=True)
    # print(df['weight_kg'][29:50])

    """
    Task 2b
    Missing values in attributes that have categorical data are best replaced using the
    most frequent value. We note that values in "screen_size_cm" attribute are
    categorical in nature, and some values are missing. Therefore, write a code to
    replace the missing values of Screen Size with the most frequent value of the attribute.
    """
    # most_common_screen_size = df['screen_size_cm'].value_counts().idxmax()
    # df['screen_size_cm'].replace(np.nan, most_common_screen_size, inplace=True)
    # print(df['screen_size_cm'].isnull().value_counts())

    """
    Task 3 SEE NOTE BELOW
    Both "Weight_kg" and "Screen_Size_cm" are seen to have the data type "Object", while both
    of them should be having a data type of "float". Write a code to fix the data type of
    these two columns.
    
    NOTE: The features are already of type float at this point but we have used object in order
    to demonstrate making the data type change. When using this file as the starting point
    for later modules do not use this code unless instructed to
    """
    # print(df['weight_kg'].dtype)
    # df['weight_kg'] = df['weight_kg'].astype(object)
    # print(df['weight_kg'].dtype)
    # print(df.dtypes)

    """
    Task 4a
    The value of Screen_size usually has a standard unit of inches. Similarly, weight of the
    laptop is needed to be in pounds. Use the below mentioned units of conversion and write
    a code to modify the columns of the dataframe accordingly. Update their names as well.

    1 inch = 2.54 cm
    1 kg   = 2.205 pounds
    """
    # print(df['screen_size_cm'].head())
    # print(df['weight_kg'].head())
    # df.rename(columns={"screen_size_cm": "screen_size_in", "weight_kg": "weight_lb"}, inplace=True)
    # df['screen_size_in'] = df['screen_size_in']/2.54
    # df['weight_lb'] = df['weight_lb']*2.205
    # print(df['screen_size_in'].head())
    # print(df['weight_lb'].head())

    """
    Task 4b
    Often it is required to normalize a continuous data attribute. Write a code to normalize the
    "CPU_frequency" attribute with respect to the maximum value available in the dataset.
    """
    # Using simple feature scaling normalization approach
    # Divide each value by the max value for the future resulting in values between 0 and 1
    # df['cpu_frequency'] = df['cpu_frequency']/df['cpu_frequency'].max()

    """
    Task 5a
    Binning is a process of creating a categorical attribute which splits the values of a
    continuous data into a specified number of groups. In this case, write a code to create
    3 bins for the attribute "Price". These bins would be named "Low", "Medium" and "High".
    The new attribute will be named "Price-binned".
    """
    # bins = np.linspace(min(df['price']), max(df['price']), 4)
    # bin_names = ['low', 'medium', 'high']
    # df['price-binned'] = pd.cut(df['price'], bins, labels=bin_names, include_lowest=True)
    # print(df['price-binned'].tail())

    """
    Task 5b
    Also, plot the bar graph of these bins.
    """
    # plt.bar(bin_names, df["price-binned"].value_counts())
    # plt.xlabel("price")
    # plt.ylabel("count")
    # plt.title("price bins")
    # plt.show()

    """
    Task 6
    Convert the "Screen" attribute of the dataset into 2 indicator variables, "Screen-IPS_panel"
    and "Screen-Full_HD". Then drop the "Screen" attribute from the dataset.
    """
    # print(df['screen'].value_counts())
    # dummys = pd.get_dummies(df['screen'])
    # print(dummys.keys())
    # dummys.rename(columns={"Full HD": "full-hd", "IPS Panel": "ips-panel"}, inplace=True)
    # df = pd.concat([df, dummys], axis=1)
    # print(df.info())


if __name__ == '__main__':
    asyncio.run(main())
