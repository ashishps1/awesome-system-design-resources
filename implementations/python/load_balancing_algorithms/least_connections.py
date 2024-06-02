import random

class LeastConnections:
    def __init__(self, servers):
        self.servers = {server: 0 for server in servers}

    def get_next_server(self):
        # Find the minimum number of connections
        min_connections = min(self.servers.values())
        # Get all servers with the minimum number of connections
        least_loaded_servers = [server for server, connections in self.servers.items() if connections == min_connections]
        # Select a random server from the least loaded servers
        selected_server = random.choice(least_loaded_servers)
        self.servers[selected_server] += 1
        return selected_server

    def release_connection(self, server):
        if self.servers[server] > 0:
            self.servers[server] -= 1

# Example usage
servers = ["Server1", "Server2", "Server3"]
load_balancer = LeastConnections(servers)

for i in range(6):
    server = load_balancer.get_next_server()
    print(f"Request {i + 1} -> {server}")
    load_balancer.release_connection(server)