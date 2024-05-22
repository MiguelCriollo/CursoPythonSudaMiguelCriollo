import asyncio
import json
import sys
from typing import Dict

import aiohttp

from ProyectoGrupal.async_counters import DesconectionCounter



class AiohttpRequestBuilder:
    def __init__(self, url=None, params=None, headers=None):
        self.__url = url
        self.__params = params
        self.__headers = headers

    @property
    def url(self):
        return self.__url

    @property
    def params(self):
        return self.__params

    @property
    def headers(self):
        return self.__headers



class SudamericanoClient(AiohttpRequestBuilder):
    URL = 'https://sudamericano.edu.ec/'
    PARAMS: dict[str, str] = {
        's': 'test'
    }
    GET_OPTIONS = {
        'ssl': False,
        'headers': [('Connection', 'close')],
        'allow_redirects': False,
    }

    def __init__(self, desconnectionCounter: DesconectionCounter, timeout=5, ):
        super().__init__(url=self.URL, params=self.PARAMS, )  # Call base class constructor
        self.__DesconectionCounter = desconnectionCounter
        self.__session_timeout = aiohttp.ClientTimeout(timeout)

    async def __basic_get_petition(self, session: aiohttp.ClientSession, params: dict = None):
        async with session.get(url=self.url,
                               params=params,
                               timeout=self.__session_timeout,
                               **self.GET_OPTIONS) as response:

            if response.status == 200:
                return None
            elif response.status == 403:
                print("\nBloqued errors on Identification: ")
                print("The Conection has been bloqued, waiting...")
                sys.exit(message="Program Terminated Due Conexion Ban")
            elif response.status == 429:
                print("To many requests, trying again")
                await asyncio.sleep(30)
            else:
                print("Conection Error Ocurred :  Server status:", response.status)
                await asyncio.sleep(0)
        await self.__DesconectionCounter.reset_disconnection()

    async def search_by_str(self, params=PARAMS):
        while True:
            try:
                async with aiohttp.ClientSession(timeout=self.__session_timeout) as session:
                    try:
                        data = await self.__basic_get_petition(session=session, params=params)
                        return data
                    except asyncio.exceptions.CancelledError as e:
                        raise e
                    finally:
                        session.cookie_jar.clear()
            except asyncio.TimeoutError as e:
                print("Timeout")
            except aiohttp.client_exceptions.ClientHttpProxyError as e:
                print("Proxy Error: ", e)
                await asyncio.sleep(1)
            except aiohttp.client_exceptions.ClientConnectorError as e:
                try:
                    await self.__DesconectionCounter.add_disconnection()
                except Exception as ex:
                    raise ex
                await asyncio.sleep(1)
            except asyncio.exceptions.CancelledError as e:
                raise e
            except RuntimeError as e:
                print("aa")
            except Exception as e:
                print("Another Error: ", e)
                raise e
