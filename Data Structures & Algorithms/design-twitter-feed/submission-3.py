from collections import defaultdict, OrderedDict

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # A follows B -> A: {B}
        self.user_tweets = defaultdict(list) # A has tweets 1, 3, 5 -> A: [1, 3, 5]
        self.tweet_user = OrderedDict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.user_tweets[userId].append(tweetId)
        self.tweet_user[tweetId] = userId
        # print(self.tweet_user[tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        # print("get feed", userId )
        # print(f"{self.tweet_user=}")
        # print(f"{self.follows=}")
        for tweet, uid in reversed(self.tweet_user.items()):
            if uid == userId or uid in self.follows[userId]:
                res.append(tweet)
                if len(res) == 10:
                    break
        # print(res)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
