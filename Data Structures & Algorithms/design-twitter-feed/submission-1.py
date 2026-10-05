class Twitter:
    """
    Design Twitter implementation using:
    - Global timestamp counter to order tweets by recency.
    - Per-user list of tweets stored as (timestamp, tweetId), appended in chronological order.
    - Per-user followee set to maintain follower->followee relationships.
    - getNewsFeed uses a k-way merge via a max-heap to retrieve up to 10 most recent tweets across followees and self.
    
    This yields efficient postTweet (O(1)) and getNewsFeed approximately O(10 log F) where F is number of followees considered.
    """

    # Each logical line below has a descriptive comment above it explaining its purpose.

    # Initialize the Twitter object with empty structures and a timestamp counter.
    def __init__(self):
        # Map from userId to list of (timestamp, tweetId) in chronological order (older -> newer).
        self.tweets: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        # Map from userId to set of followeeIds the user follows.
        self.followees: Dict[int, Set[int]] = defaultdict(set)
        # Global timestamp incremented on every post to establish recency ordering.
        self.timestamp: int = 0

    # Post a new tweet by appending (timestamp, tweetId) to the user's tweet list.
    def postTweet(self, userId: int, tweetId: int) -> None:
        # Increment global timestamp to reflect a new more-recent event.
        self.timestamp += 1
        # Append the (timestamp, tweetId) to the user's list, preserving chronological order.
        self.tweets[userId].append((self.timestamp, tweetId))

    # Retrieve up to 10 most recent tweet IDs from user and their followees using a k-way heap merge.
    def getNewsFeed(self, userId: int) -> List[int]:
        # Result list for storing the gathered tweetIds in most-recent-first order.
        result: List[int] = []
        # Local heap to perform k-way merge; use negative timestamps for max-heap behavior.
        heap: List[Tuple[int, int, int]] = []
        # Build the set of users to consider: all followees plus the user themself.
        users_to_check: Set[int] = set(self.followees.get(userId, set()))
        # Ensure the user's own tweets are considered even if they don't follow themselves.
        users_to_check.add(userId)

        # For each candidate user, if they have tweets, push their most recent tweet onto the heap.
        for uid in users_to_check:
            # Skip users with no tweets.
            user_tweets = self.tweets.get(uid)
            # If the user has any tweets, push the latest one (last in list) with index pointer.
            if user_tweets:
                # Index of the most recent tweet for this user.
                idx = len(user_tweets) - 1
                # Extract timestamp and tweetId for the most recent tweet.
                ts, tid = user_tweets[idx]
                # Push a tuple of (-timestamp, tweetId, encoded uid_and_index) to enforce max-heap by timestamp.
                # We also push uid and idx as separate values (packed into tuple) to allow retrieving the next tweet.
                heapq.heappush(heap, (-ts, tid, uid, idx))

        # Pop up to 10 most recent tweets by repeatedly extracting from heap and pushing the next tweet from that user.
        while heap and len(result) < 10:
            # Pop the current most recent tweet entry.
            neg_ts, tid, uid, idx = heapq.heappop(heap)
            # Append tweetId to result list.
            result.append(tid)
            # If there is an older tweet from the same user, push it onto the heap.
            if idx - 1 >= 0:
                # Get the next-most-recent tweet (older) for this user.
                nts, ntid = self.tweets[uid][idx - 1]
                # Push it onto the heap with negative timestamp for max-heap ordering.
                heapq.heappush(heap, (-nts, ntid, uid, idx - 1))

        # Return the collected tweet IDs in most-recent to least-recent order.
        return result

    # Make followerId follow followeeId (no-op if already following).
    def follow(self, followerId: int, followeeId: int) -> None:
        # Prevent a user from following themselves (no-op) to keep semantics simple.
        if followerId == followeeId:
            # No operation when attempting to follow self.
            return
        # Add followeeId to followerId's followee set.
        self.followees[followerId].add(followeeId)

    # Make followerId unfollow followeeId (no-op if not following or trying to unfollow self).
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Prevent self-unfollow (no-op).
        if followerId == followeeId:
            # No operation for self-unfollow.
            return
        # Remove followeeId from followerId's followee set if present.
        if followeeId in self.followees.get(followerId, set()):
            # Use discard-like behavior to remove followeeId safely.
            self.followees[followerId].remove(followeeId)