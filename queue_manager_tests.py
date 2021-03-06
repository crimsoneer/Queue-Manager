__author__ = 'Andreas'
import unittest
import time
from queue_manager import Task, Queue


class QueueManagerTests(unittest.TestCase):

    # setup testcase
    def setUp(self):
        self.passport = Task(20, "passport", "Bob")
        self.new_queue = Queue()
        self.passport1 = Task(30, "passport", "Bob 2")
        self.passport2 = Task(20, "passport", "Bob 3")
        self.passport3 = Task(20, "passport", "Bob 4")

    def test_create_task(self):
        self.assertTrue(isinstance(self.passport, Task))  # could this test be more elaborate?
        # TODO -->
        # For example
        # self.assertEquals(passport.time, 20)
        # self.assertEquals(passport.task_type, "passport")

    def test_create_queue(self):
        new_queue = Queue()
        self.assertTrue(isinstance(new_queue.startTime, float))

    def test_add_to_queue(self):
        self.new_queue.add_to_queue(self.passport)
        self.assertTrue(self.passport in self.new_queue.tasks)

    def test_check_time_pass(self):
        new_queue = Queue()
        time.sleep(0.5)
        self.assertTrue(new_queue.startTime < time.time())

    def test_estimate_queue_time(self):
        self.new_queue.add_to_queue(self.passport1)
        self.new_queue.add_to_queue(self.passport2)
        self.new_queue.add_to_queue(self.passport3)
        self.assertEqual(self.new_queue.estimate_time(), 70)

    def test_list_tasks(self):
        self.new_queue.add_to_queue(self.passport1)
        self.new_queue.add_to_queue(self.passport2)
        self.new_queue.add_to_queue(self.passport3)
        self.new_queue.list_tasks()

    def test_activate_task(self):
        self.new_queue.add_to_queue(self.passport1)
        self.new_queue.add_to_queue(self.passport2)
        self.new_queue.add_to_queue(self.passport3)
        self.new_queue.activate_task(self.passport1)
        self.assertEqual(self.new_queue.current_task, self.passport1)


if __name__ == '__main__':
    unittest.main()
