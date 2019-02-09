# Citi-Bike-Rebalancing-simulation-and-modeling
This project was done during my education at Stevens Institute of Technology with collaboration between me and Pro. Paul T. Grogan. 
The project is about applying Discrete Event simulation used Simpy library(MIT License) to model the Citibike Rebalancing system, specifically 
at Pershing Square North during rush hours.

The project included input validation process, modeling and simulation, and output validation.

The sources of data set were from:
1. Citibike website which provided Bike Trip data. (for input validation)
2. Theopenbus.com which publicly provided historical station status (for output validation).

For input validation, I used arrival times derived from Bike Trip data and validated them by using Kolmogorov-Smirnov Testing.

In my modeling, Although Citibike may be a nonprofit organization, I assumed that Citibike business objective is to gain 
as much revenue as possible; therefore, my key performance measure of the model is the revenue(balance). 
Also, there are unrevealed information of citibike rebalancing that I was unable to obtain, so the modeling may not completely reflect
the real scenario of the system. And the objective of the project was to show the application of discrete-event simulation used Simpy library.

