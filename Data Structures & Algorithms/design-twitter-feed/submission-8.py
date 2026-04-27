import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # user A follows B -> A: [B]
        self.user_tweets = defaultdict(list) # user A has tweet 1,2 -> A: [1, 2]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append(tweetId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Time: O(nlogn) # n is the number of user userId follows
        Space: O(n)
        """
        hq = []
        res = []
        
        candidates = self.follows[userId] | {userId}
        
        for uid in candidates:
            if self.user_tweets[uid]:
                idx = len(self.user_tweets[uid]) - 1
                tweet = self.user_tweets[uid][idx]
                heapq.heappush(hq, (-tweet, uid, idx - 1))

        while len(res) < 10 and hq:
            minus_tweet, uid, next_idx = heapq.heappop(hq)
            res.append(-minus_tweet)
            if next_idx >= max(len(self.user_tweets[uid]) - 10, 0):
                next_tweet = self.user_tweets[uid][next_idx]
                heapq.heappush(hq, (-next_tweet, uid, next_idx - 1))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
