__author__ = 'Andreas'
import time
class Task:
    def __init__(self,time_estimate,type,customer):
        self.time_estimate = time_estimate
        self.type = type
        self.customer = customer

    def add_to_queue(self,queue):
        queue.add_to_queue(self)

class Queue:
    def __init__(self):
        self.number_of_tasks = 0
        self.task_dict = {}
        self.tasks = []
        self.average_task_time = 0
        self.time_to_estimate = 0
        self.tasks_done = 0
        self.task_start = 0
        self.startTime = time.time()

    def add_to_queue(self,task):
        self.tasks.append(task)

    def estimate_time(self):
        queue_time_estimate = 0
        if self.tasks == []:
            return 0
        else:
            for task in self.tasks:
                queue_time_estimate += task.time_estimate
            return queue_time_estimate

    def list_tasks(self):
        print "Tasks in Queue:"
        i = 0
        for item in self.tasks:
            print "Task " + str(i) + " : " + "{0} for {1}, estimated time: {2} minutes".format(item.type,item.customer,item.time_estimate)
            i += 1

    def activate_task(self,task):
        self.task_start = time.time()
        self.current_task = self.tasks.pop(self.tasks.index(task))

    def finish_task(self):
        task_time = time.time() - self.task_start
        self.tasks_done += 1
        self.average_task_time = (task_time + self.average_task_time) / self.tasks_done
        task_time_to_estimate = self.current_task.time_estimate - task_time
        self.time_to_estimate = (task_time_to_estimate + self.time_to_estimate) / self.tasks_done
        print "Task completed in {t} seconds - {e} compared to time estimate. Current average task time compared to estimate:{tt}".format(task_time,task_time_to_estimate,self.time_to_estimate)
        self.current_task = None
        self.list_tasks()

def create_a_task():
    customer_name = raw_input("Please enter customer name")
    task_type = raw_input("Please enter a task type")
    time_estimate = float(raw_input("Please enter a time estimate"))
    return Task(time_estimate,task_type,customer_name)

def main():
    queue_name = raw_input("Welcome to Queue Manager.  Please input a name for your first queue.")
    queue_name = Queue()
    print "Queue initiated."
    loop(queue_name)

def loop(queue):
    choice = raw_input('''Please choose one of the following options: [L]ist tasks in queue, [C]reate a Task, [B]egin a task, [F]inish current task, [C]urrent Statistics, [Q]uit ''')
    if choice == "C":
        queue.task_dict[queue.number_of_tasks] = create_a_task()
        queue.add_to_queue(queue.task_dict[queue.number_of_tasks])
        queue.number_of_tasks += 1
        print "Task creation complete"
        loop(queue)
    elif choice == "L":
        queue.list_tasks()
        loop(queue)
    elif choice == "B":
        task_number = raw_input("Please chose a task number to begin")
        queue.activate_task(int(queue.task_dict[task_number]))
        loop(queue)
    elif choice == "F":
        queue.finish_task()
        loop(queue)
    elif choice == "C":
        print "Seconds since queue start : " + str(time.time() - queue.startTime)
        print "Average Task Time : " + str(queue.average_task_time)
        print "Average Task Time to Estimate : " + str(queue.time_to_estimate)
        loop(queue)
    elif choice == "Q":
        exit()
    else:
        print "Please chose a valid option"
        loop(queue)


main()