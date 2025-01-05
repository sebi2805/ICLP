import concurrent.futures
import urllib.request

# Lista de URL-uri pentru descărcare
URLS = [
    'http://www.foxnews.com/',
    'http://www.cnn.com/',
    'http://www.bbc.co.uk/',
]

# Funcția pentru descărcarea unei pagini
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()  # Returnează conținutul paginii

# Funcția principală
if __name__ == '__main__':
    # Creează un ThreadPoolExecutor cu 5 fire
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Trimite fiecare URL spre descărcare, păstrând un mapping între "future" și URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        # Procesează rezultatele pe măsură ce fiecare sarcină este completată
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]  # Obține URL-ul asociat
            try:
                data = future.result()  # Obține conținutul paginii
                print(f'{url}: {len(data)} bytes downloaded')
            except Exception as exc:
                print(f'{url} generated an exception: {exc}')
