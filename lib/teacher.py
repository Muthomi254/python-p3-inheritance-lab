#!/usr/bin/env python

from user import User
import random

class Teacher(User):
   def __init__(self, first_name, last_name):
        # Call the constructor of the parent class with first_name and last_name
        super().__init__(first_name, last_name)
        # Initialize a list of predefined knowledge
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

   def teach(self):
       # Return a random piece of knowledge
       return random.choice(self.knowledge)
       # Additional functionality can be added here
pass
