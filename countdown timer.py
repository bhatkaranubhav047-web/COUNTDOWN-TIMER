import time 

seconds = int(input("Enter countdown time in seconds: "))

if seconds <= 0:
    print("Please enter a positive number!")
else:
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        
        print(timer,end="\r", flush=True)
        
        time.sleep(1)
        seconds -= 1
        
print("00:00")
print("Time's up!")            