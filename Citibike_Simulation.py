# -*- coding: utf-8 -*-
"""

@Author: Sukit Kajonpradapkul
For Citibike rebancing simulation

"""

import simpy
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

order_threshold = 2.0
order_up_to = 5.0 
delivery_delay = 20 # in minutes
SIM_RUN = 1000  #number of simulation runs
initial_bikes = 15
operation_cost = 2 # USD per bike for operation
oil_gas = 3 # USD per 1 refillment
service_fee = 3 # USD per bike per ride
PENALTY = 3 # USD for cost of loss of business oportunity
loss_profit = 0.1 # USD per bike per minute for loss of business opportunity

def arrival(env, _lambda ,requirement):
    global num_bikes, revenue, penalty, Loss_profit
    interarrival = np.random.exponential(1./_lambda)
    yield env.timeout(interarrival)
    Loss_profit += loss_profit * num_bikes * interarrival
#    print 'Arrival @ t={}, require# {}'.format(env.now, requirement)
    if requirement == 'Rent a bike':
        if num_bikes > 0:
            num_bikes -= 1
            revenue += service_fee
        else:
            penalty += PENALTY
            
    else:
        num_bikes += 1
    
    
#    print ('current num of bikes = {}'.format(num_bikes))


def rebalancing(env, quantity):
    global num_bikes, num_ordered, revenue , cost, Loss_profit
    
    num_ordered = quantity
    cost += (num_ordered * operation_cost) + oil_gas 
    
    yield env.timeout(delivery_delay)
    num_bikes += num_ordered
#    print (" Fill bikes up to ={}".format(num_bikes))
    num_ordered = 0
    
         

def citibike_run(env, _lambda ,requirement, order_up_to, order_threshold):
    global num_bikes, quantity, num_ordered, revenue , cost, penalty, Loss_profit
    num_ordered = 0.0
    quantity = 0.0
    while True:
        
        yield env.process(arrival(env, _lambda ,requirement))
        get_bikes.append(num_bikes)
        if num_bikes <= order_threshold and num_ordered == 0:
           quantity = order_up_to - num_bikes
           env.process(rebalancing(env, quantity))
            
def observe(env):

    while True:

        obs_time.append(env.now)
        obs_bikes.append(num_bikes)
        obs_balance.append(revenue - cost - penalty - Loss_profit)
        yield env.timeout(0.2)
            

       
avg_bikes = []
avg_balance = []
get_balance = []

for i in range(SIM_RUN):
    np.random.seed(i)
    num_bikes = initial_bikes
    revenue = 0
    cost = 0
    penalty = 0
    Loss_profit = 0
    obs_time = []
    obs_bikes = []
    obs_balance = []
    get_bikes = []
                
    env = simpy.Environment()        
    env.process(citibike_run(env, 1.572 ,'Rent a bike', order_up_to, order_threshold))
    env.process(citibike_run(env, 1.183 ,'Return a bike', order_up_to, order_threshold))
    env.process(observe(env))
    env.run(until=180.0) # during 5pm to 8am
    avg_bikes.append(np.mean(get_bikes))
    avg_balance.append(revenue - cost - penalty - Loss_profit)

      



  
if SIM_RUN > 1:    
    print ("The average number of available bikes during the interval = ", np.mean(avg_bikes))
    plt.figure()
    plt.scatter(range(len(avg_bikes)), avg_bikes, c='b', alpha=0.4)    
    plt.xlabel('Simulation runs')
    plt.ylabel('Bike Level')
    plt.title('Average Bike levels at each runs (Threshold= {:.0f}, order-up-to= {:.0f})'.format(order_threshold, order_up_to))
    plt.savefig('Average bike level.png')
    
    plt.figure()
    plt.hist( avg_bikes, color='g')
    plt.xlabel('X Bin')
    plt.ylabel('Count')
    plt.title(' Histogram (average number of bike)(Threshold= {:.0f}, order-up-to= {:.0f})'.format(order_threshold, order_up_to))
    plt.legend(loc='best')
    plt.savefig('Histogram Average bike level.png')



if SIM_RUN <= 1:
        
    plt.figure()
    plt.step(obs_time, obs_bikes, where='post' , color = 'g')
    plt.xlabel('Time (Minutes)')
    plt.ylabel('Bike Level')
    plt.title(' Simulation (Initial bikes = {:.0f}, Threshold = {:.0f}, order-up-to = {:.0f})'.format(initial_bikes, order_threshold, order_up_to))
    plt.savefig('Bikes level (Tshold = {:.0f}, orderut = {:.0f}).png'.format(order_threshold, order_up_to))
    plt.show()
    
    plt.figure()
    plt.step(obs_time, obs_balance, where='post', color = 'r')
    plt.xlabel('Time (Minutes)')
    plt.ylabel('Balance ($)')
    plt.title('Balance (Threshold = {:.0f}, order-up-to = {:.0f})'.format(order_threshold, order_up_to))
    plt.savefig('balance level (Tshold = {:.0f}, orderut = {:.0f}).png'.format(order_threshold, order_up_to))
    plt.show()    

confidence_level = 0.05
z_crit = stats.norm.ppf(1-confidence_level/2)

print ('200 simulation runs  = {:.3f} +/- {:.3f} (95% CI)'.format(np.mean(avg_balance), z_crit*stats.sem(avg_balance)))