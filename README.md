# Ex1
Chapter 1 - ID’s: 212727283, 315907113
In this problem we have a building, elevators and a call. Our call is destined to a certain floor. Our problem is to allocate the fastest elevator. This elevator will reach the caller in the least amount of time and will take him to the provided destination using a provided cmd algorithm. 
      
  For this problem we searched the web and found useful sources to 
  help us with the problem.
  
First source:
  fitst source is about a hard drive that resembles the elevator algorithm:	
    https://www.youtube.com/watch?v=JXqVvmBOyyQ	

Second source:
    Elevator Low Level System Design | Object Oriented Design | Elevator Algorithm
    https://www.youtube.com/watch?v=14Cc8IDWtFM

Third source:
A comprehensive look about the science behind elevators and the elevators algorithm
https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/




The Offline Algorithm:
This algorithm is using the csv and jason files. This files include building paramaters, elevators parameters and information about a certain call. Using this information we can build classes that read the files. With those classes we can access the paramaters of each object. The algorithm will use the formula for calculating the time it takes for an elevator to reach floor a to floor b. The formula is as follows: CloseTime + StartTime + df/speed + StopTime + OpenTime (df == |floor_a-floor_b). With this formula in hand we will calculate the time it takes for the elevator to reach the destination of last call to the source of the new call + time it takes from source of new call to the final destination. We then add the overall time it takes for the elevator and we do this dynamically throughout the calls process. We create a list for allocated calls, list of calls designated to elevators, and for elevators. For each call we will calculate the best time, using the formula, for an elevator to reach the caller. We then add the best time to a field we created called time in the Elevator class. Finally we add the elevator with the best time to list for allocated calls.
