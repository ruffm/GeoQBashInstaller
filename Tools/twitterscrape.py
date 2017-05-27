import tweepy

CONSUMER_KEY=' '
CONSUMER_SECRET=' '
ACCESS_TOKEN=' '
ACCESS_TOKEN_SECRET=' '

auth=tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api=tweepy.API(auth) # this works for auth purposes

# https://api.twitter.com/1.1/search/tweets.json?q=sra111%20until%3A2017-4-20&src=typd


search_text="#cats" # set search term here
search_number=100 # set amt to search here
search_result=api.search(search_text, rpp=search_number)

for search in search_result:

    # text=str(search.text)
    id=str(search.id)
    meta=str(search.metadata)
    usr=str(search.user)

    print(search.text)
    print(search.id)
    print(search.metadata)
    print(search.user)

    openFile = open('twitterOutputFile.txt', 'a')
    # openFile.write(text + " " + id + " " + meta + usr + "\n")
    openFile.write(id + " " + meta + usr + "\n" + "\n")
    openFile.close()