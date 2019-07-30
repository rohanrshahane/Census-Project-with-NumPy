# initialize array A and Identity matrix
import numpy as np
import statistics
path = "C:\\Rohan\\Python\\Data\\file.csv"
data = np.genfromtxt(path, delimiter=",",skip_header=1)

new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

census = np.concatenate((data,new_record),0)

age = census[:,0]
age = age.flatten()

filter = np.asarray([0])

race_0 = census[np.in1d(census[:,2], filter)]

len_0 = len(race_0)

filter1 = np.asarray([1])
race_1 = census[np.in1d(census[:,2], filter1)]

len_1 = len(race_1)


filter2 = np.asarray([2])
race_2 = census[np.in1d(census[:,2], filter2)]

len_2 = len(race_2)


filter3 = np.asarray([3])
race_3 = census[np.in1d(census[:,2], filter3)]

len_3 = len(race_3)


filter4 = np.asarray([4])
race_4 = census[np.in1d(census[:,2], filter4)]

len_4 = len(race_4)


max_age  = np.max(age)
min_age  = np.min(age)
age_mean = round(np.mean(age),2)
age_std = round(statistics.stdev(age), 3)
age_std = age_std - age_std % 0.01

filterAge = census[:,0] > 60

senior_citizens = np.array(census[filterAge], dtype=float)
working_hours_sum = sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = round( working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)

filterH = census[:,1] > 10
high = np.array(census[filterH], dtype=int)
print(len(high ))

filterL = census[:,1] <= 10
low = np.array(census[filterL], dtype=int)

path1 = "C:\\Rohan\\Python\\Data\\file12.txt"
np.savetxt(path1, low,delimiter=",")
print(len(low))

avg_pay_high = round(np.mean(high[:,7]),2)
print(avg_pay_high)
avg_pay_low =  round(np.mean(low[:,7]),2)
print(avg_pay_low)

