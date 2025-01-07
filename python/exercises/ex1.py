# 1. Asyncio: Cronometrare concurentă
# Scrie un program care utilizează asyncio pentru a simula un cronometru cu mai multe sarcini:

# Creează trei funcții asincrone care, după un timp de așteptare (1s, 2s, 3s), afișează un mesaj.
# Utilizează asyncio.gather sau asyncio.create_task pentru a rula toate funcțiile în paralel și cronometrează execuția lor.

import asyncio
import time

async def task(time):
    await asyncio.sleep(time / 1000)
    print(time)
    

async def main():
    tasks = [asyncio.create_task(task(index *1000)) for index in range(1, 4)]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()

    print(f"Toate sarcinile au fost completate în {end_time - start_time:.2f} secunde.")