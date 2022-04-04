# create data structure to maintain animal shelter
# implement operations: enqueue, dequeueAny, dequeueDog, dequeueCat

import unittest
from collections import deque


class Animal:
    def __init__(self, counter, type):  # type- Dog or Cat
        self.counter = counter
        self.type = type

# using deque class
class AnimalShelter:
    def __init__(self):
        self.dog_shelter = deque()
        self.cat_shelter = deque()
        self.counter = 0

    def enqueue(self, type): # O(1)
        self.counter += 1
        animal = Animal(self.counter, type)
        if animal.type == "Dog":
            self.dog_shelter.append(animal)
        else:
            self.cat_shelter.append(animal)

    def dequeueAny(self): #O(1)
        if self.dog_shelter[0].counter < self.cat_shelter[0].counter:
            return self.dog_shelter.popleft()
        else:
            return self.cat_shelter.popleft()

    def dequeueDog(self): #O(1)
        if len(self.dog_shelter) == 0:
            raise Exception("Error. No more dogs.")
        return self.dog_shelter.popleft()

    def dequeueCat(self): #O(1)
        if len(self.cat_shelter) == 0:
            raise Exception("Error. No more cats.")
        return self.cat_shelter.popleft()

    def returnShelter(self, type):
        res = []
        if type == "Dog":
            for i in self.dog_shelter:
                res.append(i.counter)
        else:
            for i in self.cat_shelter:
                res.append(i.counter)
        return res

class TestAnimalShelter(unittest.TestCase):
    def test_dequeueDog(self):
        s = AnimalShelter()
        for i in range(3):
            s.enqueue("Dog")
            s.enqueue("Cat")
        s.dequeueDog()
        self.assertEqual(s.returnShelter("Dog"), [3,5])
        self.assertEqual(s.returnShelter("Cat"), [2,4,6])

    def test_dequeueDog_exception(self):
        s = AnimalShelter()
        for i in range(3):
            s.enqueue("Dog")
            s.enqueue("Cat")
        for i in range(3):
            s.dequeueDog()
        with self.assertRaises(Exception):
            s.dequeueDog()
        self.assertEqual(s.returnShelter("Cat"), [2,4,6])

    def test_dequeueCat(self):
        s = AnimalShelter()
        for i in range(3):
            s.enqueue("Dog")
            s.enqueue("Cat")
        s.dequeueCat()
        self.assertEqual(s.returnShelter("Dog"), [1,3,5])
        self.assertEqual(s.returnShelter("Cat"), [4,6])

    def test_dequeueAny(self):
        s = AnimalShelter()
        for i in range(3):
            s.enqueue("Dog")
            s.enqueue("Cat")
        s.dequeueDog()
        s.dequeueAny()
        self.assertEqual(s.returnShelter("Dog"), [3,5])
        self.assertEqual(s.returnShelter("Cat"), [4,6])

