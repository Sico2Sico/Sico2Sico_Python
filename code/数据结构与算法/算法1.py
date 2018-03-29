import time

start_time = time.time()

for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a**2+b**2 == c**2 and a+b+c == 1000:
                print("a = %d, b =%d c = %d")%(a,b,c)


end_time = time.time()

print("time ===%d"%(start_time - end_time))

