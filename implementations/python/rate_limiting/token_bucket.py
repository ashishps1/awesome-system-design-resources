import time

class TokenBucket:
    def __init__(self, capacity, fill_rate):
        self.capacity = capacity  # Maximum number of tokens the bucket can hold
        self.fill_rate = fill_rate  # Rate at which tokens are added (tokens/second)
        self.tokens = capacity  # Current token count, start with a full bucket
        self.last_time = time.time()  # Last time we checked the token count

    def allow_request(self, tokens=1):
        now = time.time()
        # Calculate how many tokens have been added since the last check
        time_passed = now - self.last_time
        self.tokens = min(self.capacity, self.tokens + time_passed * self.fill_rate)
        self.last_time = now

        # Check if we have enough tokens for this request
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

# Usage example
limiter = TokenBucket(capacity=10, fill_rate=1)  # 10 tokens, refill 1 token per second

for _ in range(15):
    print(limiter.allow_request())  # Will print True for the first 10 requests, then False
    time.sleep(0.1)  # Wait a bit between requests

time.sleep(5)  # Wait for bucket to refill
print(limiter.allow_request())  # True