""" Library for methods used in the views or another python files."""

# by Richi Rod AKA @richionline / falken20

import pandas as pd
import lxml


def scrap_web(url):
    """
    For getting data weather of a specific url
    :param url: The url of a specific web
    """
    data = pd.read_html(url)
    df = data[0]
    print('ROD url scrapping: ', data[0])

    # Cleaning the info it doesn't neccesary
    df = df.drop([4], axis=1) # axis is the column name
    df = df.drop([0,1,2,3,4,5])

    # Get seveal rows and cols
    df = df.iloc[0:6, [0, 1]]

    # We can change the name of the columns
    df.columns = ('Parameter', 'Value')

    # Clean and restore the index number because it is kind of
    # annoying but it is not necessary
    df = df.reset_index(drop=True)

    return df