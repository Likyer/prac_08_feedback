"""
CP1404/CP5632 Practical 8
Taxi class
Name：LIU YUHAO
"""

from prac_08_feedback.taxi import Taxi


def main():
    """Code to test Taxi class."""

    taxi_1 = Taxi("Prius 1", 100)
    taxi_1.drive(40)
    print(taxi_1)
    print(taxi_1.get_fare())

    taxi_1.start_fare()
    taxi_1.drive(100)
    print(taxi_1)
    print(taxi_1.get_fare())


main()