# duckdoor
Raspberry pi zero W controlled TB6612FNG  motor controller using lead screw / threaded rod based door opener and closer with limit switches to control stopping

This repo contains scripts that I reference in my youtube video https://www.youtube.com/watch?v=B-sUuR_nrbo 

Essentially the scrips set up an interface with a TB6612FNG and define some functions to induce my motor to move clockwise or counterclockwise. 
Additionally the movement is stopped at full open or close by limit switches.  

In this updated version of the scripts I run full speed for about 12 seconds, then drop to about half speed for the remaining distance.   This was an attempt to "come in softer" when approaching the limit switches. 

The wiring of the interface to the TB6612FNG can be learned by reading the GPIO setup pins, they are labeled in comments. 
