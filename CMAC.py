#CMAC Algorithm for Robot Learning 
#Yash Shah

import numpy as np
import math
import random
import time
import matplotlib.pyplot as plt

# define input range 
# Generating input from 0 to 2*PI
x = 0.0628
data_x=np.arange(0,100)
y = np.arange(0)

#get the actual output for every input point
# Defining the function sin(X) for training 
for i in range (0,100):
    math_function = math.sin((data_x[np.array(i)]) * (x))
    y = np.append(y,math_function)

xy = np.dstack((data_x* x,y))

test_num = np.arange(0)
inp_num = np.arange(0)

#Make a random array of 70  data for training
while (inp_num.size < 70):
    ran_num = random.randint(0,99)
    if ((ran_num in inp_num) == False ):
        inp_num = np.append(inp_num,ran_num)

#Remaining 30 data are used for testing 
while (test_num.size < 30):
    ran_num = random.randint(0,99)
    if((ran_num in inp_num) == False):
        test_num = np.append(test_num,ran_num)

inp_num = np.sort(inp_num)
test_num = np.sort(test_num)

#Defining Weights
w_val = 0.0
w_num = 1
inc_val = 0
w_zero = np.arange(0.0)
w_save = w_zero
err_val = 0.0
q_val = 0
err_arr = np.arange(0)
rms_arr = np.arange(0)
time_arr = np.arange(0)
time_gen_arr = np.arange(0)
rms = 1

# training my CMAC
#loop for different generelization factors
for gen in range(1,30,2):
    start = time.time()
    w = np.random.rand(35)
    pad_val = (gen-1)/2
    w_zero = np.array([0])
    for i in range(pad_val):
        w = np.append(w_zero,w)
        w = np.append(w,w_zero)
        w = np.append(w,w_zero)
    while(rms > 0.01):
        w_z = np.arange(0)
        for j in range(0,70):
            q_val = j/2
            for k in range(gen):
                w_val = w_val + w[np.array(k + q_val)]
            w_y_val = w_val/gen
            y_val = (math.sin(inp_num[np.array(j)] * x))
            if gen==3:
                w_z = np.append(w_z,w_y_val)
            err_val = y_val - w_y_val
            err_arr = np.append( err_arr, err_val)
            corrected_val = err_val/gen
            for k in range(gen):
                w[np.array(k + q_val)] = w[np.array(k + q_val)] + corrected_val
            w_val = 0.0
        rms = np.mean(err_arr**2)
    print gen 
    if gen==3:
        w_save = w_z
        w_weight_save = w
    end = time.time()
    time_arr = np.append(time_arr, (end-start))
    time_gen_arr = np.append(time_gen_arr, gen)
    rms_arr = np.append(rms_arr,rms)
    rms = 1

# testing of trained CMAC 
w_35 = w_save
w_new = w_weight_save[1::2]
new_gen = 3
test_val = 0.0
w_new_arr = np.arange(0)
for j in range(0,30):
    q_val = j/2
    w_avg = w_new[np.array(q_val)] + w_new[np.array(q_val - 1)] + w_new[np.array(q_val + 1)]
    w_avg = w_avg / new_gen
    w_new_arr = np.append(w_new_arr,w_avg)
new_test_data = test_num * x
x_final = data_x* x

#plot different graphs 
plt.plot(x_final,y,'r--') 
plt.grid(True)
plt.show()
plt.plot(new_test_data,w_new_arr,'ro',x_final,y,)
plt.show()
plt.plot(time_gen_arr ,time_arr,'r--')
plt.grid(True)
plt.show()
plt.plot(time_gen_arr,rms_arr,'r--')
plt.grid(True)
plt.show()
plt.plot()
