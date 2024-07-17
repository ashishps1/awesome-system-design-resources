import time

class SlidingWindowCounter:
    def __init__(self, window_size, max_requests):
        self.window_size = window_size  # Size of the sliding window in seconds
        self.max_requests = max_requests  # Maximum number of requests per window
        self.current_window = time.time() // window_size
        self.request_count = 0
        self.previous_count = 0

    def allow_request(self):
        now = time.time()
        window = now // self.window_size

        # If we've moved to a new window, update the counts
        if window != self.current_window:
            self.previous_count = self.request_count
            self.request_count = 0
            self.current_window = window

        # Calculate the weighted request count
        window_elapsed = (now % self.window_size) / self.window_size
        threshold = self.previous_count * (1 - window_elapsed) + self.request_count

        # Check if we're within the limit
        if threshold < self.max_requests:
            self.request_count += 1
            return True
        return False

# Usage example
limiter = SlidingWindowCounter(window_size=60, max_requests=5)  # 5 requests per minute

for _ in range(10):
    print(limiter.allow_request())  # Will print True for the first 5 requests, then gradually become False
    time.sleep(0.1)  # Wait a bit between requests

time.sleep(30)  # Wait for half the window to pass
print(limiter.allow_request())  # Might be True or False depending on the exact timing