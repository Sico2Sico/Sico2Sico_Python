import  time


start_time = time.time()

for a in range(1001):
    for b in range(0,1001-a):
        c = 1000- a -b
        if a**2+b**2 == c**2:
            print("a ==%d,b ===%d, c===%d"%(a,b,c))


end_time = time.time()

print("endTiem === %d"%(end_time-start_time))
