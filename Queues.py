class CircularQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty for the dequeue operation')

        front = (self._front + 1) % len(self._data)

        dequeued_element = self._data[self._front]
        self._data[self._front] = None  #THIS IS GARBAGE COLLECTION. Giving the empty slots the value none, to show that the queue is not full
        self._size -=1

        return dequeued_element

    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        tail = (self._front + self._size) % len(self._data) #TO TRACE THE BACK OF THE QUEUE. The result is a positional argument
        self._data[tail] = element
        self._size += 1 #self._size = self._size + 1




    def resize(self,new_capacity):
        pass

class Empty(Exception):
    pass

if __name__ == '__main__':

    obj_queue = CircularQueue()

    insert_elements = [11,22,33,44,55]

    for element in insert_elements:
        obj_queue.enqueue(element)

        print(f"Added Element : {element} ")
        print(f"The new size of the queue : {len(obj_queue)}")

    # print("\n Current Queue Representation : ")
