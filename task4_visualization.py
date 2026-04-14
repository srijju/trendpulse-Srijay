import os
import pandas as pd
import matplotlib.pyplot as plt

#task1 
df = pd.read_csv("data/trends_analyzed.csv")
os.makedirs("outputs", exist_ok=True)

#1. Bar Chart: Stories per Category
df_category_top_10 = df.sort_values("score",ascending=False).head(10)
df_category_top_10['title_Shortened'] = df["title"].apply(lambda x: x if len(x) <= 50 else x[:47] + " ..")

plt.figure(figsize=(12,6))

#plotting horizontal bar graph CHART 1
plt.barh(df_category_top_10["title_Shortened"], df_category_top_10["score"], color='skyblue')
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png",dpi =300)
#plt.xticks(rotation=270,ha='right')
plt.show()

#plotting bar graph chart2
count_by_category = df["category"].value_counts()
plt.figure(figsize=(12,6))

plt.bar(count_by_category.index, count_by_category.values,color = plt.cm.tab10.colors[:len(count_by_category)])
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Number of Stories per Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png",dpi =300)
plt.show()

#score vs commentsscatter plot
plt.figure(figsize=(10,6))

popular_stories = df[df["is_popular"] == True]
unpopular_stories = df[df["is_popular"] == False]


plt.scatter(popular_stories["score"], popular_stories["num_comments"], color='green', label="Popular Stories", alpha=0.6)
plt.scatter(unpopular_stories["score"], unpopular_stories["num_comments"], color='red', label="Unpopular Stories", alpha=0.6)
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png", dpi=300)
plt.show()

#subplots
fig, axes = plt.subplots(1,3,figsize=(18,6))
axes[0].barh(df_category_top_10["title_Shortened"], df_category_top_10["score"], color='skyblue')
#axes[0].set_title("Top 10 Stories by Score")
axes[0].set_xlabel("Score")
axes[0].invert_yaxis()

axes[1].bar(count_by_category.index, count_by_category.values,color = plt.cm.tab10.colors[:len(count_by_category)])
axes[1].set_xlabel("Category")
axes[1].tick_params(axis='x', rotation=45)

axes[2].scatter(popular_stories["score"], popular_stories["num_comments"], color='green', label="Popular Stories", alpha=0.6)
axes[2].scatter(unpopular_stories["score"], unpopular_stories["num_comments"], color='red', label="Unpopular Stories", alpha=0.6)
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of Comments")
axes[2].legend()

plt.suptitle("Hacker News Trends Analysis", fontsize=16)
plt.tight_layout()
plt.savefig("outputs/dashboard.png", dpi=300)
plt.show()








