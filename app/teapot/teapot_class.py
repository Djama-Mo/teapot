from os import environ
from time import sleep

from exceptions.custom_exceptions import (
    IncorrectValueOfVolume, BoiledWater
)


class Teapot(object):
    def __init__(self):
        self.__state: bool = False
        self.__volume: float = 0.0
        self.__max_volume: float = float(environ.get('MAX_VOLUME'))
        self.__boiling_time: int = int(environ.get('BOILING_TIME'))
        self.__boiling_temperature: int = int(environ.get('BOILING_TEMPERATURE'))
        self.__current_temperature: int = 0

    def get_data(self) -> dict:
        data = {
            "state": "Off" if not self.__state else "On",
            "volume": f"{self.__volume}L",
            "water_temperature": self.__current_temperature,
        }
        return data

    def fill_teapot(self, water: float) -> bool:
        if water <= 0.0:
            raise IncorrectValueOfVolume

        current_volume: float = self.__volume + water
        self.__current_temperature = 25

        if current_volume > self.__max_volume:
            self.__volume = self.__max_volume
            return True

        self.__volume = round(current_volume, 1)
        return True

    def check_before_boiling(self):
        if not self.__volume:
            raise IncorrectValueOfVolume

        if self.__current_temperature >= 100:
            raise BoiledWater

    def turn_on(self):
        self.__state = True

        for _ in range(self.__boiling_time):
            sleep(1)
            self.__current_temperature += 7.5
            yield f"{self.__current_temperature}"

            if self.__current_temperature >= 100:
                self.__state = False
                return

        self.__state = False

    def turn_off(self):
        self.__state = False
