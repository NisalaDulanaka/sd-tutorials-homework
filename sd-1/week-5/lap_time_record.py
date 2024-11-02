
number_of_lap_times=int(input("Enter number of lap times: "))
lap_times=[]
for i in range(number_of_lap_times):
    lap_time = float(input(f"Enter lap time {i+1} of {number_of_lap_times}: "))
    lap_times.append(lap_time)

print(f"Fastest lap time {min(lap_times)}")
print(f"Slowest lap time {max(lap_times)}")
print(f"Average lap time {round(sum(lap_times)/len(lap_times))}")
