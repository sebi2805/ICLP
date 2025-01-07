import concurrent.futures
import urllib.request
import asyncio

# Lista de URL-uri pentru descărcare
URLS = [
    'http://www.foxnews.com/',
    'http://www.cnn.com/',
    'http://www.bbc.co.uk/'
]

# Funcția asincronă pentru descărcarea unui URL
async def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        data = conn.read()
        print(f"'{url}' page is {len(data)} bytes")
        return len(data)

# Funcția principală
async def main():
    # Folosim ThreadPoolExecutor pentru operații care nu sunt native async
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Creăm sarcini asincrone pentru fiecare URL
        future_to_url = {asyncio.create_task(load_url(url, 60)): url for url in URLS}

        # Așteptăm și procesăm rezultatele task-urilor
        for future in future_to_url:
            print(await future)

# Pornim evenimentul principal
asyncio.run(main())
