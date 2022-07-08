import unittest
# stream of integers
# create object that receives new integers
# initialize it, give it the # k
# should have function called average
# return the average of the last k numbers

# 3 functions: constructor, average, receiver
# average - returns the avg of the last k number
# constructor - init(3)
# receive - input is the integer to receive, no output

# edge cases to get the last k average
## if len of the stream is smaller than k, then get the average of all the numbers in the stream
## otherwise, get the average of the last k numbers

# k = 3
# 1,2,3
# 4,2,3
# 4,5,3


# 1,2,3
# 2,3,4
# 3,4,5

# 1,2,3

# in the constructor, have a counter that counts the number of integers that have been received
# when the counter == k, reset the counter so the new number that's received would overwrite the value of the first pos
# average -
# time - O(k)
# space - O(1)

# receive-
# time - O(1)
# space - O(1)

class Stream:
    def __init__(self, k):
        stream = [] # contains all of the integers
        self.k = k

    # return the average of the last k numbers
    ## if len of the stream is smaller than k, then get the average of all the numbers in the stream

    # space - O(1)
    # time - O(k)
    def average(self):
        if len(self.stream) < self.k:
            return sum(self.stream)/len(self.stream)
        else:
            stream_sum = 0
            for i in range(self.k):
                stream_sum += self.stream[-i]
            return stream_sum/self.k

    # space - O(m) where m= the number of integers that are received into the stream
    # time - O(1)
    def receive(self, num):
        self.stream.append(num)

class Stream_2:
    def __init__(self, k):
        if k == 0:
            raise Exception ("k must be greater than 0")
        self.stream = []
        self.k = k
        self.counter = 0

    def average_2(self):
        if len(self.stream) < self.k:
            return sum(self.stream)/len(self.stream)
        else:
            return sum(self.stream)/self.k

    # in the constructor, have a counter that counts the number of integers that have been received
    # when the counter == k, reset the counter so the new number that's received would overwrite the value of the first pos
    def receive_2(self, num):
        self.stream[self.counter] = num
        self.counter += 1
        if self.counter == self.k:
            self.counter = 0


# Test Cases
# 1 - get the average of the last k numbers in the stream
## 0,1,2,3  k=2  avg=2.5
# 2 - get the average of the last k numbers in the stream if len(stream) < k
## 0,1,2,3  k=5  avg=3
# 3 - Instantiate object when k == 0
## k=0  Throw Exception
# 4 - test that new number is received after instantiating object
## instantiate the object where k = 1, recieve(1), avg = 1
# 4 - test that the counter is restarted after counter == k
## instantiate the object where k = 1, recieve(1), receive(2), avg = 2




class Test:
    # get the average of the last k numbers in the stream
    def test_average_2(self):
        s = Stream_2(2)
        #0,1,2 -> average of last 2 (1,2)
        for i in range(3):
            s.receive_2(i)



    # get the average of the last k numbers in the stream if len(stream) < k

