import pandas as pd
import os

FILE_PATH = ""

"""function to load the data from json file to dataframe"""
def load_data():
    data_path = "data"
    if not os.path.exists(data_path):
        print("Folder does not exist")
        return None
    else:
        files = [f for f in os.listdir(data_path) if f.endswith(".json") and os.path.isfile(os.path.join(data_path,f))]

        if not files:
            print("No json files found in the folder")
            return None
        else:
            file_to_load = max(files)
            path = os.path.join(data_path, file_to_load)

            FILE_PATH = path

            try:
                return pd.read_json(path)
            except Exception as e:
                print(f"Error loading the data: {e}")
                return None    


df = load_data() 

if df is not None:
    print(f"Loaded: {len(df)} from {FILE_PATH}")
    #Dropping duplicates
    df = df.drop_duplicates(subset="post_id")
    print(f"After removing duplicates: {len(df)}")

    #Dropping rows with missing values
    df = df.dropna(subset=["post_id","title","score"])
    print(f"After removing nulls: {len(df)}")

    #Fix data types to int
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].fillna(0).astype(int)

    #Remove stories with score less than 5
    df = df[df["score"] >=5]
    print(f"After removing low scores: {len(df)}")

    #Strip whitespace from title
    df["title"] = df["title"].str.strip()

    #Save the cleaned data to csv file
    cleaned_file = "data/trends_clean.csv"
    df.to_csv(cleaned_file, index=False)

    print("Stories per category:")
    print(df["category"].value_counts())

    print(f"Saved {len(df)} rows to {cleaned_file}")

else:
    print("No data loaded")







       
