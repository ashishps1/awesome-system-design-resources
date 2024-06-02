import hashlib

class IPHash():
    def __init__(self, servers):
        self.servers = servers

    def get_next_server(self, client_ip):
        hash_value = hashlib.md5(client_ip.encode()).hexdigest()
        index = int(hash_value, 16) % len(self.servers)
        return self.servers[index]

# Example usage
servers = ["Server1", "Server2", "Server3"]
load_balancer = IPHash(servers)

client_ips = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4"]
for ip in client_ips:
    server = load_balancer.get_next_server(ip)
    print(f"Client {ip} -> {server}")