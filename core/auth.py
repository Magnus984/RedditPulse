import praw
from core.config import settings

id = settings.CLIENT_ID
secret = settings.CLIENT_SECRET

reddit = praw.Reddit(
    client_id=id,
    client_secret=secret,
    user_agent="my_reddit_bot/0.1 by RevolutionaryGood536"
)