import threading
import time
# The philosopher thread
def philosopher(left, right):    
    while True:
      if not left.locked():
        left.acquire()
        if not right.locked():
          right.acquire()
          print(f'Philosopher at \
          {threading.currentThread()} is eating.')
          time.sleep(1)
          right.release()
          left.release()
          break
        else:
          left.release()

# def philosopher(left, right):
#     if id(left) < id(right):
#       first, second = left, right
#     else:
#       first, second = right, left

#     while True:
#       with first:
#         with second:
#             print(f'Philosopher at \
#             {threading.currentThread()} is eating.')
#             time.sleep(1)
#             break

if __name__=="__main__":
  # The chopsticks
  N_FORKS = 5
  forks = [threading.Lock() for n in range(N_FORKS)]
  # Create all of the philosophers
  phils = [ \
    threading.Thread(target=philosopher,args=(forks[n], forks \
      [(n + 1) % N_FORKS])) for n in range(N_FORKS)]
  # Run all of the philosophers
  for p in phils:
      p.start()