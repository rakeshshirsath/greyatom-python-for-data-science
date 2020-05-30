# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print(np.shape(data))
census = np.concatenate((data,new_record))
print(np.shape(census))

#Age analysis
age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print("Maximun age is ",max_age)
print("Minimum age is ",min_age)
print("Average age is %.2f"%age_mean)
print("Std Deviation is %.2f"%age_std)

race_0 = np.array([r for r in census if r[2]==0])
race_1 = np.array([r for r in census if r[2]==1])
race_2 = np.array([r for r in census if r[2]==2])
race_3 = np.array([r for r in census if r[2]==3])
race_4 = np.array([r for r in census if r[2]==4])

len_0 = race_0.size
len_1 = race_1.size
len_2 = race_2.size
len_3 = race_3.size
len_4 = race_4.size

min_race = min(len_0,len_1,len_2,len_3,len_4)
if min_race == len_0:
    minority_race = 0
elif min_race == len_1:
    minority_race = 1
elif min_race == len_2:
    minority_race = 2
elif min_race == len_3:
    minority_race = 3
elif min_race == len_4:
    minority_race = 4

print(minority_race)

senior_citizens = census[census[:,0] > 60]
working_hours_sum = np.sum(senior_citizens,axis=0)[6] 
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)

high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high,axis=0)[7] 
avg_pay_low = np.mean(low,axis=0)[7] 
print(avg_pay_high,avg_pay_low)


