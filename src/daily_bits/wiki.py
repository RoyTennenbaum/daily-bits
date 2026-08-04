import os

from dotenv import load_dotenv
import wikipediaapi

load_dotenv()
wiki_user_agent = os.getenv("WIKI_USER_AGENT")

wiki = wikipediaapi.AsyncWikipedia(user_agent=wiki_user_agent, language="en")
