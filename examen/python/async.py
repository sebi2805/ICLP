
### SECVENTIAL
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


### Paralel import asyncio
import time

# O funcție asincronă care așteaptă un timp specificat și apoi afișează un mesaj
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# Funcția principală
async def main():
    # Creăm două task-uri care rulează în paralel
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Așteptăm finalizarea task-urilor
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

# Pornim event loop-ul și executăm funcția principală
asyncio.run(main())
