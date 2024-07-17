from collections import deque
import time

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity  # Maximum number of requests in the bucket
        self.leak_rate = leak_rate  # Rate at which requests leak (requests/second)
        self.bucket = deque()  # Queue to hold request timestamps
        self.last_leak = time.time()  # Last time we leaked from the bucket

    def allow_request(self):
        now = time.time()
        # Simulate leaking from the bucket
        leak_time = now - self.last_leak
        leaked = int(leak_time * self.leak_rate)
        if leaked > 0:
            # Remove the leaked requests from the bucket
            for _ in range(min(leaked, len(self.bucket))):
                self.bucket.popleft()
            self.last_leak = now

        # Check if there's capacity and add the new request
        if len(self.bucket) < self.capacity:
            self.bucket.append(now)
            return True
        return False

# Usage example
limiter = LeakyBucket(capacity=5, leak_rate=1)  # 5 requests, leak 1 per second

for _ in range(10):
    print(limiter.allow_request())  # Will print True for the first 5 requests, then False
    time.sleep(0.1)  # Wait a bit between requests

time.sleep(1)  # Wait for bucket to leak
print(limiter.allow_request())  # True