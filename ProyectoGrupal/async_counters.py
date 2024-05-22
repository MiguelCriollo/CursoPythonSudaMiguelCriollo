import asyncio

from ProyectoGrupal.conection_errors import DesconnectionError


class CounterBuilder:
    def __init__(self, values):
        self._values = values
        self._index = 0
        self._lock = asyncio.Lock()


class InfiniteCounter(CounterBuilder):
    def __init__(self, values):
        super().__init__(values)

    async def next_value(self):
        async with self._lock:
            if self._index >= len(self._values):
                self._index = 0
            value = self._values[self._index]
            self._index += 1
            return value


class DesconectionCounter:

    def __init__(self, maxDisconnetions=3, raiseAt=30, notificationEach=10):
        self._max_disconnections = maxDisconnetions
        self._notification_each = notificationEach
        self._raise_at = raiseAt
        self._lock = asyncio.Lock()
        self._disconnections = 0
        self._index = 0

    async def reset_disconnection(self):
        self._index = 0
        self._disconnections = 0

    async def add_disconnection(self):
        async with self._lock:
            if self._index >= self._raise_at:
                self._disconnections += 1
                if self._disconnections >= self._max_disconnections:
                    raise DesconnectionError
                else:
                    print(f"Disconnection Detected: {self._disconnections}/{self._max_disconnections}")
            if self._index % self._notification_each == 0:
                print(f"Client Connection Error {self._index + self._notification_each}/{self._raise_at}")
            self._index += 1
