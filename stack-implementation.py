from collections import deque
class MyStack(object):

    def __init__(self):
        self.queue = deque()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        q = self.queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    
    def pop(self):
        return self.queue.popleft()

    
    def top(self):
        return self.queue[0]


    def empty(self):
        return len(self.queue) == 0