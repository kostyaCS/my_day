"""
This module includes all states in one person's day.
"""
import random
import time


def prime(function):
    """
    Decorator, that launch a generator.
    """
    def wrapper(*args, **kwargs):
        func = function(*args, **kwargs)
        func.send(None)
        return func
    return wrapper


class Me:
    """
    This class represent me as a person.
    """
    def __init__(self, day: str) -> None:
        """
        The constructor for a class.
        """
        self.day = day
        self.sleeping = self.sleep()
        self.working = self.work()
        self.eating = self.eat()
        self.walking_out = self.walk_out()
        self.reading = self.read()
        self.running = self.run()
        self.current_state = self.start()

    def clock(self, hour):
        """
        This method represent a clock.
        """
        self.current_state.send(hour)

    @prime
    def start(self):
        """
        This method represent a start of the day.
        """
        while True:
            hour = yield
            print("Starting my day!")
            if hour == 0:
                self.current_state = self.sleeping

    @prime
    def sleep(self):
        """
        This method represent a state of sleeping.
        """
        while True:
            hour = yield
            print(f"I'm sleeping, it's only {hour} o'clock")
            if hour == 5 and random.randint(1, 3) == 2:
                self.current_state = self.running
            elif hour == 7:
                self.current_state = self.eating

    @prime
    def eat(self):
        """
        This method represent a state of eating.
        """
        dishes = ['potato with chicken', 'pasta with tomato sous',
                  'mushrooms soup', 'burger with beef', 
                  'sandwich with tuna']
        while True:
            hour = yield
            print(f"I'm eating {random.choice(dishes)}, it's {hour} o'clock")
            if hour == 8:
                self.current_state = self.working
            elif hour == 15:
                if self.day != 'Monday':
                    self.current_state = self.walking_out
                else:
                    self.current_state = self.working
            elif hour == 20:
                self.current_state = self.working

    @prime
    def work(self):
        """
        This method represent a state of working.
        """
        while True:
            hour = yield
            print(f"I'm working, it's {hour} o'clock")
            if hour == 14:
                self.current_state = self.eating
            elif hour == 18 and self.day == 'Friday':
                if random.random() > 0.5:
                    self.current_state = self.walking_out
            elif hour == 19:
                self.current_state = self.eating
            elif hour == 23:
                self.current_state = self.read()

    @prime
    def walk_out(self):
        """
        This method represent a state of walking out.
        """
        while True:
            hour = yield
            if self.day == 'Friday' and hour > 17:
                if hour == 22:
                    self.current_state = self.reading
                else:
                    print(f"I'm walking out with some beer, it's {hour} o'clock")
            else:
                print(f"I'm walking out, it's {hour} o'clock")
            if hour == 17:
                self.current_state = self.working

    @prime
    def read(self):
        """
        This method represent reading as a state.
        """
        while True:
            hour = yield
            if random.random() < 0.2:
                print("No reading for today, I'm going to sleep! See you tomorrow!")
                self.current_state = self.sleeping
            else:
                print(f"I'm reading, it's {hour} o'clock.")
            if hour == 24:
                self.current_state = self.sleeping

    @prime
    def run(self):
        """
        This method represent running as a state.
        """
        while True:
            hour = yield
            artists = ['Eminem', 'Linkin Park', 'Nirvana']
            print(f"Time to run a bit! Today we're gona listen to\
 {random.choice(artists)} It's only {hour} o'clock!")
            if hour == 7:
                self.current_state = self.eating


if __name__ == '__main__':
    my_day = Me('Friday')
    for one_hour in range(25):
        #time.sleep(1)
        my_day.clock(one_hour)
