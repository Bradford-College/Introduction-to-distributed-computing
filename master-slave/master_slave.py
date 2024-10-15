'''
How the code works:
Master Process:
    The master creates multiple slave processes.
    It assigns a task to each slave (calculate the square of a number).
    The results are stored in shared memory (multiprocessing.Array), which the master collects once all slave processes finish.
    Slave Process:

    Each slave process performs the task (calculating the square of a number) and stores the result in a shared memory location.
    After completing the task, the slave process terminates.
In this example, the master-slave architecture is simulated by having the master distribute tasks to the slaves -
(each calculating the square of a number), and the slaves return the results back to the master.
You can adjust the number of slaves or the complexity of tasks to demonstrate the distribution of work.
'''

import multiprocessing
import time

# Function that acts as the 'slave' worker
def calculate_square(number, result, index):
    print(f"Slave process calculating square of {number}")
    result[index] = number * number
    time.sleep(2)  # Simulate some delay

if __name__ == "__main__":
    numbers = [2, 3, 4, 5]
    
    # Master creates a shared memory array to store results from slaves
    result = multiprocessing.Array('i', 4)
    
    processes = []
    
    # Master creates and assigns tasks to slave processes
    for idx, num in enumerate(numbers):
        process = multiprocessing.Process(target=calculate_square, args=(num, result, idx))
        processes.append(process)
        process.start()

    # Master waits for all slave processes to finish
    for process in processes:
        process.join()
    
    # Master collects the results from the slave processes
    print("Results collected by the master:")
    print(result[:])

