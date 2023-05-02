
# FileSync Script
	1	define the paths of source, replica, sync interval and log file paths then assign them to arguments.
	2	set up logging config with log file and console output
	3	create the replica of the source folder that is provided (if not exist)
	4	a function to sync the replica and source folder
	5	First loop looks into the source folder,
	6	Seconde loop looks into the replica folder
	7	a while loop working with given interval

## Setup
To execute this script, you need to define 4 arguments, these are the arguments by order
first arg : path of the folder that you want to create of the replica
secong arg : path of replica folder
third arg : path of log file
fourth arg : time interval (in seconds)

## Execution
```
python Assessment.py path/to/source path/to/replica path/to/logFile time_interval
```
