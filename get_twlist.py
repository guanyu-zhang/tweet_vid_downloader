import GetOldTweets3 as got
import argparse

parser = argparse.ArgumentParser(description="user_name and max_num")
parser.add_argument("--user", "-u", help="twitter user name", type=str)
parser.add_argument("--num", "-n", help="maximum number of tweets", type=int)
args = parser.parse_args()
tweetCriteria = got.manager.TweetCriteria().setUsername(args.user).setMaxTweets(args.num)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)
num = len(tweet)
f = open("tweet_list.txt","w")
for i in range(num):
    f.write(tweet[i].permalink+"\n")
f.close()
print(str(num) + " tweets have been collected, the results can be found in tweet_list.txt")