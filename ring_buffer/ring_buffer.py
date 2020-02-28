from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == self.capacity:
            # set the self.current to 0 again
            self.current = 0

            # insert into the storage at position current
        self.storage[self.current] = item
        # increment current
        self.current += 1

    def get(self):
        # Note:  This is the only [] allowed
        #list_buffer_contents = []

        # TODO: Your code here
        # return the element in the storage
        # do not return None, use list comprehension
        # return list_buffer_contents

        return [item for item in self.storage if item is not None]

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
