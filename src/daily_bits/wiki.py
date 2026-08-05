import os
from dotenv import load_dotenv

import wikipediaapi

load_dotenv()
wiki_user_agent = os.getenv("WIKI_USER_AGENT")

wiki = wikipediaapi.AsyncWikipedia(user_agent=wiki_user_agent, language="en")

async def get_random_article():
    pages = await wiki.random(limit=1)
    page = next(iter(pages.values()))
    text = await page.text
    return page.title, text