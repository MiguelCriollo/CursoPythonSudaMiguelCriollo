import asyncio
#Realizado por:Miguel Criollo y Kevin Avila

from ProyectoGrupal.async_counters import DesconectionCounter, InfiniteCounter
from ProyectoGrupal.conection_errors import DesconnectionError
from ProyectoGrupal.http_builder import SudamericanoClient


class RotatingCounter(InfiniteCounter):
    TO_SEARCH = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def __init__(self):
        super().__init__(values=self.TO_SEARCH)


class SudamericanoExtraction:
    TASKS_PER_INSTANCE = 20

    def __init__(self):
        self.task = None
        self.asyncioHasStopped = None
        self.desconection_counter = DesconectionCounter()
        self.ApiManager = SudamericanoClient(desconnectionCounter=self.desconection_counter)

    def startScript(self):

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        self.task = []
        self.asyncioHasStopped = False
        try:
            loop.run_until_complete(self.batchPetitions(tasks=self.task))
        except KeyboardInterrupt as e:
            self.asyncioHasStopped = True
            try:
                print("Batches Cancelation By user")
            except KeyboardInterrupt as e:
                raise e
            raise e
        except Exception as e:
            print("Exception Ignored?:", e)
            print("Data didnt got saved!!!")
        finally:
            try:
                loop.run_until_complete(self.gather_remaining_task(tasks=self.task))
            except DesconnectionError as e:
                raise e
            except Exception as e:
                print("Exception During")
                raise e

    async def gather_remaining_task(self, tasks):
        unfinished_tasks = [6 for task in tasks if not task.done()]
        print(f"Waiting for {len(unfinished_tasks)} to me completed")
        try:
            await asyncio.gather(*tasks, return_exceptions=False)
            print("Finalized Data")

        except DesconnectionError as e:
            raise e
        except Exception as e:
            print(e)
            raise e

    async def batchPetitions(self, tasks):
        semaphore = asyncio.Semaphore(self.TASKS_PER_INSTANCE)
        Counter = RotatingCounter()
        event = asyncio.Event()

        async def run_task(search_str):
            async with semaphore:
                try:
                    result = await self.person_extract(search_str)
                    if semaphore.locked():
                        return result
                    semaphore.release()
                    if not self.asyncioHasStopped:
                        new_str = await Counter.next_value()
                    else:
                        new_str = None
                    if new_str is not None:
                        task = asyncio.create_task(run_task(new_str))
                        tasks.append(task)
                    else:
                        event.set()
                    return result
                except asyncio.CancelledError:
                    pass
                except DesconnectionError as e:
                    event.set()
                    raise e
                except Exception as e:
                    event.set()
                    raise e

        async def create_several_tasks():
            for x in range(self.TASKS_PER_INSTANCE):
                new_value = await Counter.next_value()
                if new_value is not None:
                    task = asyncio.create_task(run_task(new_value))
                    tasks.append(task)
                    await asyncio.sleep(0.020)
            print("Initial tasks Created")

        await create_several_tasks()
        await event.wait()
        print("Tasks Finished")

    async def person_extract(self, search_str):
        newParams = self.ApiManager.PARAMS.copy()
        newParams['s'] =  search_str
        assets = await self.ApiManager.search_by_str(params=newParams, )
        print("Correctly Process")
        return assets


if __name__ == "__main__":
    try:
        SudamericanoExtraction().startScript()

    except KeyboardInterrupt as e:
        print("Scripts Cancelled by the user")

    except DesconnectionError as e:
        print(e)

    except Exception as e:
        raise e
