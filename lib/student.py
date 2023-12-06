#!/usr/bin/env python

from user import User



class Student(User):
    def __init__(self, first_name, last_name):
        # Call the constructor of the parent class with first_name and last_name
        super().__init__(first_name, last_name)
        # Initialize an empty list to store knowledge
        self.knowledge = []

    def learn(self, string):
        # Add the provided string to the knowledge list
        self.knowledge.append(string)
        # Additional functionality can be added here
        pass
