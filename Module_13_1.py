import asyncio

num_of_ball = 5

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(num_of_ball):
        await asyncio.sleep(6/power)
        print(f"Силач {name} поднял шар {i+1}")

    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Oleg", 6))
    task2 = asyncio.create_task(start_strongman("Vit", 4))
    task3 = asyncio.create_task(start_strongman("Serg", 3))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
