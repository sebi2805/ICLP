import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;

import java.util.ArrayList;
import java.util.List;

public class Crawler {
	public static void main(String args[]) {
		List<String> urls = List.of(
			"https://google.com",
			"https://jsonplaceholder.typicode.com/posts/1",
			"https://jsonplaceholder.typicode.com/posts/2",
			"https://jsonplaceholder.typicode.com/posts/3"
		);

        List<CompletableFuture<String>> futureTasks = new ArrayList<>();

		for (String url : urls) {
			futureTasks.add(CompletableFuture.supplyAsync(() -> new CrawlerTask(url).call()));
		}

		for (CompletableFuture<String> futureTask : futureTasks) {
			try {
                futureTask.thenAccept(result -> {
                    System.out.println("Page content:\n" + result.getContent());
                });
			}
			catch (Exception ex) {
				ex.printStackTrace();
			}
		}
	}
}

class CrawlerTask {
	private String url;
    private String webContent;
	public CrawlerTask(String url) {
		this.url = url;
	}

	public String call() {
		StringBuilder content = new StringBuilder();

		try {
			System.out.println("Accessing: " + url);
			
			HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
			connection.setRequestMethod("GET");
			connection.setConnectTimeout(5000);
			connection.setReadTimeout(5000);

			int status = connection.getResponseCode();
			if (status == 200) {
				BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
				String line;
				while ((line = reader.readLine()) != null) {
					content.append(line).append("\n");
				}
				reader.close();
			}
			else {
				content.append("Cannot acces this page: ").append(status);
			}

			connection.disconnect();
		}
		catch (Exception ex) {
			ex.printStackTrace();
			webContent = "Error: " + url;
		}

		webContent = content.toString();
	}
    public String getContent(){
        return webContent;
    }
}