import pandas as pd
import numpy as np


def task3():

    file_path = 'data/trends_clean.csv'

    try:

        #1Load and explore
        df = pd.read_csv(file_path)
        print(f"Loaded data: {df.shape}")

        print("\nFirst 5 Rows:")
        print(df.head())

        average_score = df["score"].mean()
        print(f"\nAverage Score: {average_score:.0f}")

        average_comments = df["num_comments"].mean()
        print(f"\nAverage Comments: {average_comments:.0f}")

        #2Analysis with Numpy
        numpy_array = df["score"].to_numpy()

        mean_score = np.mean(numpy_array)
        median_score = np.median(numpy_array)
        std_dev_score = np.std(numpy_array)
        max_score = np.max(numpy_array)
        min_score = np.min(numpy_array)

        print(f"Mean score     : {mean_score:.0f} ")
        print(f"Median score   : {median_score:0f}")
        print(f"Std deviation  : {std_dev_score:.0f}")
        print(f"Max score      : {max_score:,}")
        print(f"Min score     :  {min_score:,}")

        max_category = df["category"].value_counts()
        category_name = max_category.idxmax()
        category_count = max_category.max()

        print(f"\nMost stories in:{category_name} ({category_count} stories)")

        max_comments = df["num_comments"].idxmax()
        max_comments_story = df.loc[max_comments]

        print(f'\nMost commented story: "{max_comments_story["title"]}" - {max_comments_story["num_comments"]:,} comments')

        #3Add New Columns

        df["engagement"] = df["num_comments"]/(df["score"] +1)
        df["is_popular"] = df["score"] > average_score

        #4Save the Result
        analyzed_path = "data/trends_analyzed.csv"
        df.to_csv(analyzed_path, index=False)

        print(f"\nSaved to {analyzed_path} ")

    except Exception as e:
        print()


if __name__ == "__main__":
    task3()
