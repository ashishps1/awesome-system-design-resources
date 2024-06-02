import time
import random

class LeastResponseTime:
    def __init__(self, servers):
        self.servers = servers
        self.response_times = [0] * len(servers)

    def get_next_server(self):
        min_response_time = min(self.response_times)
        min_index = self.response_times.index(min_response_time)
        return self.servers[min_index]

    def update_response_time(self, server, response_time):
        index = self.servers.index(server)
        self.response_times[index] = response_time

# Simulated server response time function
def simulate_response_time():
    # Simulating response time with random delay
    delay = random.uniform(0.1, 1.0)
    time.sleep(delay)
    return delay

# Example usage
servers = ["Server1", "Server2", "Server3"]
load_balancer = LeastResponseTime(servers)

for i in range(6):
    server = load_balancer.get_next_server()
    print(f"Request {i + 1} -> {server}")
    response_time = simulate_response_time()
    load_balancer.update_response_time(server, response_time)
    print(f"Response Time: {response_time:.2f}s")