import re
import numpy as np
import pandas as pd

import os
from sklearn.model_selection import train_test_split

import urllib.request
from urllib.error import HTTPError

import PIL
from PIL import Image


def read_and_clean_data(path):
    df = pd.read_csv(path, encoding="ISO-8859-1", usecols=["imdbId", "Title", "Genre", "Poster"])
    df.set_index(["imdbId"], inplace=True)
    print(f"Shape of the original dataset: {df.shape}")
    df.dropna(inplace=True)
    print(f"Shape after dropping rows with missing values: {df.shape}")
    df.drop_duplicates(subset="Poster", keep=False, inplace=True)
    print(f"Shape after dropping rows with potentially misleading poster link: {df.shape}\n")
    return df

def add_year_variable(df):
    re_year = re.compile("\((\d{4})\)")
    df["year"] = df.Title.map(lambda x: int(re_year.findall(x)[0]) if re_year.findall(x) else None)
    print(f"There are movies between {int(np.min(df.year))} and {int(np.max(df.year))} available in the dataset.\n")
    return df

def create_boolean_genres(df):
    df["Genre"] = df.Genre.map(lambda x: x.split("|"))
    all_genres = set([item for l in df.Genre for item in l])
    print(f"There are {len(all_genres)} genres in the dataset: {all_genres}\n")
    for genre in all_genres:
        new_var = "is_" + re.sub(r'\W+', '', genre.lower())
        df[new_var] = df.Genre.map(lambda x: genre in x)
    df.drop(["Genre"], axis=1, inplace=True)
    return df

def extract_genre_data(df, genre="Action"):
    filter_var = "is_" + re.sub(r'\W+', '', genre.lower())
    df_genre = df.copy().loc[df[filter_var]]
    print(f"{genre} movies in the dataset: {df_genre.shape[0]}\n")
    return df_genre

def select_years(df, min_year=1950, max_year=2000, add_decades=True):
    df_range = df.copy().loc[(df.year >= min_year) & (df.year < max_year)]
    print(f"Movies left between {min_year} and {max_year}: {df_range.shape[0]}")
    if add_decades:
        df_range["decade"] = df_range.year.apply(lambda x: str(int(x))[2] +"0s")
        print(f"Movies per decade in the dataset:\n{df_range.decade.value_counts()}\n")
    return df_range

def sample_same_number_per_decade(df, use_test_sample=False):
    min_number = 40 if use_test_sample else np.min(df.decade.value_counts())
    df_sample = df.groupby("decade").apply(lambda x: x.sample(min_number))
    print(f"Sample includes {min_number} movies per decade")
    return df_sample

def create_train_and_test_dfs(df, prop_test=.2, strat = 'decade'):
    if strat is not None:
        strat = df[strat]
    train, test = train_test_split(df, test_size=prop_test, stratify=strat)
    print(f"Number of movies in training data: {train.shape[0]}")
    print(f"Number of movies in testing data:  {test.shape[0]}\n")
    return {"train": train, "test": test}

def create_folder_structure(image_folder="movie_posters", splits=["train", "test"], classes=None):
    for s in splits:
        for c in classes:
            folder_name = "/".join([image_folder, s, c])
            try:
                os.makedirs(folder_name)
            except FileExistsError:
                print(f"{folder_name} already exists.")
        print("\n")
        
def download_posters(dfs, image_folder="movie_posters"):
    for k, df in dfs.items():
        print(f"Starting with downloading files for {k}...\n")
        already_downloaded = 0
        http_errors = []
        for index, movie in df.iterrows():
            movie_id = str(index[1])
            movie_decade = index[0]
            file_name = movie_id + ".jpg"
            file_path = "/".join([image_folder, k, movie_decade, file_name])
            if os.path.isfile(file_path):
                already_downloaded += 1
            else:
                try:
                    urllib.request.urlretrieve(movie.Poster, file_path)       
                except HTTPError:
                    http_errors.append(movie_id)
        print(f"{len(http_errors)} posters had an HTTPError.")
        print(f"{already_downloaded} posters were downloaded before.\n")
        count = 0
        for root, dirs, files in os.walk("/".join([image_folder, k])):
            if len(dirs) == 0:
                count += len(files)
                print(f"Number of pictures in {root}:\t{len(files)}")
        print(f"\nTotal number of pictures available for {k}: {count}\n")

def delete_black_and_white_posters(image_folder=None):
    print(f"\nChecking for black and white pictures in {image_folder}...")
    count = 0
    for root, dirs, files in os.walk(image_folder):
        if len(files) > 0:
            for f in files:
                file_path = "/".join([root, f])
                if np.asarray(Image.open(file_path)).shape != (268, 182, 3):
                    os.remove(file_path)
                    count += 1
    print(f"Files without RGB and therefore deleted: {count}")    
    
    
### TO DOWNLOAD ALL ####
def create_all_folders(image_folder="movie_posters",name = 'all', classes=None):
    for c in classes:
        folder_name = "/".join([image_folder, name, c])
        try:
            os.makedirs(folder_name)
        except FileExistsError:
            print(f"{folder_name} already exists.")
    print("\n")
    
def download_all(df, image_folder="movie_posters", name = 'all'):
    if not os.path.exists("/".join([image_folder, name])):
        os.mkdir("/".join([image_folder, name]))
    print(f"Starting with all downloading files..\n")
    already_downloaded = 0
    http_errors = []
    for index, movie in df.iterrows():
        movie_id = str(index[1])
        movie_decade = index[0]
        file_name = movie_id + ".jpg"
        file_path = "/".join([image_folder, name, movie_decade, file_name])
        if os.path.isfile(file_path):
            already_downloaded += 1
        else:
            try:
                urllib.request.urlretrieve(movie.Poster, file_path)       
            except HTTPError:
                http_errors.append(movie_id)
    print(f"{len(http_errors)} posters had an HTTPError.")
    print(f"{already_downloaded} posters were downloaded before.\n")
    count = 0
    for root, dirs, files in os.walk("/".join([image_folder, name])):
        if len(dirs) == 0:
            count += len(files)
            print(f"Number of pictures in {root}:\t{len(files)}")
    print(f"\nTotal number of pictures available for {k}: {count}\n")