import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class LeastResponseTime {
    private List<String> servers;
    private List<Double> responseTimes;

    public LeastResponseTime(List<String> servers) {
        this.servers = servers;
        this.responseTimes = new ArrayList<>(servers.size());
        for (int i = 0; i < servers.size(); i++)
            responseTimes.add(0.0);
    }

    public String getNextServer() {
        double minResponseTime = responseTimes.get(0);
        int minIndex = 0;
        for (int i = 1; i < responseTimes.size(); i++) {
            if (responseTimes.get(i) < minResponseTime) {
                minResponseTime = responseTimes.get(i);
                minIndex = i;
            }
        }
        return servers.get(minIndex);
    }

    public void updateResponseTime(String server, double responseTime) {
        int index = servers.indexOf(server);
        responseTimes.set(index, responseTime);
    }

    public static double simulateResponseTime(String server) {
        // Simulating response time with random delay
        Random random = new Random();
        double delay = 0.1 + (1.0 - 0.1) * random.nextDouble();
        try {
            Thread.sleep((long) (delay * 1000));
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return delay;
    }

    public static void main(String[] args) {
        List<String> servers = List.of("Server1", "Server2", "Server3");
        LeastResponseTime leastResponseTimeLB = new LeastResponseTime(servers);

        for (int i = 0; i < 6; i++) {
            String server = leastResponseTimeLB.getNextServer();
            System.out.println("Request " + (i + 1) + " -> " + server);
            double responseTime = simulateResponseTime(server);
            leastResponseTimeLB.updateResponseTime(server, responseTime);
            System.out.println("Response Time: " + String.format("%.2f", responseTime) + "s");
        }

    }
}
