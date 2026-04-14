import requests
import json
import time
import os
from datetime import datetime


STORIES_URL = "https://hacker-news.firebaseio.com/v0/newstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

STORY_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

"""Fetch the top 500 stories from hacker news"""
def fetch_stories():
    try:
        response = requests.get(STORIES_URL,headers = headers)

        if response.status_code == 200:
            story_ids = response.json()
            return story_ids[:500]
        else:
            print(f"Error etching the stories:{response.status_code}");
            return []

    except Exception as e:
        print(f"Error fetching the stories: {e}");
        return []  
    

"""Fetch the details of a story"""
def fetch_story(story_id):
    try:

        response = requests.get(STORY_URL.format(story_id),headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching the story details: {response.status_code}")
            return None

    except Exception as e:
        print(f"Error while fecthing the story details: {e}")
        return None         


"""Catrgorize the story"""
def categorize_story(title):
    if not title:
        return None
    
    title_lower = title.lower()

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
            
    return None

""" Function to save the data in json file"""
def task1():
    story_ids = fetch_stories()
    stories_per_category = []

    story_count = {category: 0 for category in CATEGORIES};

    for category in CATEGORIES:
        print(f"Current category: {category}")
        for story_id in story_ids:

            if story_count[category]  >=25:
                break

            story_details = fetch_story(story_id)

            if not story_details:
                continue

            story_title = story_details.get("title","")

            story_category = categorize_story(story_title)

            if story_category == category:
                story_dict ={"post_id": story_details.get("id"), "title": story_title , "category": story_category, "score": story_details.get("score",0), "num_comments": story_details.get("descendants",0), "author": story_details.get("by", ""), "colledcted_at": datetime.now().isoformat()}
                stories_per_category.append(story_dict)
                story_count[category] +=1

        time.sleep(2)   #sleep for 2 seconds to avoid hitting the API rate limit

    if not os.path.exists("data"): #create a directory named data if it doesn't exists
        os.makedirs("data")
    
    file_name = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json" #create a file inside data directory with name trends_yyyymmdd.json

    with open(file_name,'w') as f: #dump the data in json
        json.dump(stories_per_category,f, indent=3)

    print(f"Collected {len(stories_per_category)} stories.Saved to {file_name}")    





if __name__ == "__main__":
    task1()


