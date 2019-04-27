# Citi-Bike-Rebalancing-simulation-and-modeling
This project was done during my education at Stevens Institute of Technology with collaboration between me and Pro. Paul T. Grogan. 
The project focuses on applying Discrete Event simulation based on Simpy library(MIT License) to model the Citibike Rebalancing system, specifically at Pershing Square North during rush hours.

The project included input validation process, modeling, simulation, and output validation.

The sources of data set were derived from:
1. Citibike website which provided Bike Trip data. (for input validation)
2. Theopenbus.com which publicly provided historical station status (for output validation).

For input validation, arrival times were used which were derived from Bike Trip data and validated them by using Kolmogorov-Smirnov Testing.

In my modeling, Although Citibike is a nonprofit organization, I assumed that one of Citibike's business objectives is to gain 
as much revenue as possible; therefore, my key performance measure of the model is the revenue(balance). 
Moreover, there are unrevealed information of citibike rebalancing program that I was unable to obtain, so the modeling may not completely reflect the real scenario of the system. And the objective of the project was to show the application of Discrete Event simulation used Simpy.

