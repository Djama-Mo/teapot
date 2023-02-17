import os


class Teapot(object):
    def __init__(self):
        self.__state: bool = False
        self.__volume: float = 0.0
        self.__max_volume: float = float(os.environ.get('MAX_VOLUME'))
        self.__boiling_time: int = int(os.environ.get('BOILING_TIME'))
        self.__boiling_temperature: int = int(os.environ.get('BOILING_TEMPERATURE'))
        self.__current_temperature: int = 0

    def get_data(self) -> dict:
        data = {
            "state": "Off" if not self.__state else "On",
            "volume": self.__volume,
            "water_temperature": self.__current_temperature,
        }
        return data
