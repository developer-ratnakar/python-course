import threading
import time

def take_order():
    for i in range(1, 4):
        print(f"Taking Order of #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing Chai for #{i}")
        time.sleep(2)

order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

#start Threading

order_thread.start()
brew_thread.start()

# wait for both to finish

order_thread.join()
brew_thread.join()

print(f"All orders taken & chai brewed")
