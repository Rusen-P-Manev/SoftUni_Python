old_record = float(input()) # въвежда се рекорда който трябва да се подобри
distance_in_meters = float(input()) # разтоянието което трябва да преплува
time_in_seconds_per_meter = float(input()) # времето в секунди, за което плува разстояние от 1 м
delay = (distance_in_meters // 15) * 12.5 # съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди
total_time = distance_in_meters\
             * time_in_seconds_per_meter\
             + delay
if total_time < old_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds_to_record = abs(old_record - total_time)
    print(f"No, he failed! He was {seconds_to_record:.2f} seconds slower.")