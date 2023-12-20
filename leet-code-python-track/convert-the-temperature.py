class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        list = []
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        list.insert(0,kelvin)
        list.insert(1,fahrenheit)
        return list