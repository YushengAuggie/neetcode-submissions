import copy
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # user A follows B -> A: [B]
        self.user_tweets = defaultdict(list) # user A has tweet 1,2 -> A: [1, 2]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append(tweetId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        hq = []
        res = []
        back_up = copy.deepcopy(self.user_tweets)
        
        candidates = set()
        self.follows[userId].add(userId)
        for uid in self.follows[userId]:
            if self.user_tweets[uid]:
                tweet = self.user_tweets[uid].pop()
                heapq.heappush(hq, (-tweet, uid))
                candidates.add(uid)

        while len(res) < 10 and candidates:
            minus_tweet, uid = heapq.heappop(hq)
            res.append(-minus_tweet)
            if not self.user_tweets[uid]:
                candidates.remove(uid)
            else:
                next_tweet = self.user_tweets[uid].pop()
                heapq.heappush(hq, (-next_tweet, uid))

        self.user_tweets = back_up
        self.follows[userId].remove(userId)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
