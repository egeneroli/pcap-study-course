class QueueError(IndexError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.__lst: list = []

    def put(self, elem):
        self.__lst.append(elem)

    def get(self):
        e = self.__lst[0]
        del self.__lst[0]
        return e


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")