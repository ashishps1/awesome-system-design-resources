import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LeastConnections {
    private Map<String, Integer> serverConnections;

    public LeastConnections(List<String> servers) {
        serverConnections = new HashMap<>();
        for (String server : servers) {
            serverConnections.put(server, 0);
        }
    }

    public String getNextServer() {
        String server = serverConnections.entrySet().stream()
                .min(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .orElse(null);
        if (server != null) {
            serverConnections.computeIfPresent(server, (k, v) -> v + 1);
        }
        return server;
    }

    public void releaseConnection(String server) {
        serverConnections.computeIfPresent(server, (k, v) -> v > 0 ? v - 1 : 0);
    }

    public static void main(String[] args) {
        List<String> servers = List.of("Server1", "Server2", "Server3");
        LeastConnections leastConnectionsLB = new LeastConnections(servers);
        List<String> assignedServers = new ArrayList<>();

        for (int i = 0; i < 6; i++) {
            String server = leastConnectionsLB.getNextServer();
            assignedServers.add(server);
            System.out.println(server);
        }

        for (String server : assignedServers) {
            leastConnectionsLB.releaseConnection(server);
        }
    }
}
