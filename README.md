# Basic Data Exploration with pandas on Bikeshare Data
_An exploration of bikeshare data using the pandas library._

# Project Overview

This project aims to utilize the pandas library and basic statistical methods to analyze bikeshare data from three major U.S. cities: Chicago, Washington, and New York City. The analysis includes insights such as the most popular days and common stations.

### Running the Program

To execute the program, simply enter 'python bikeshare.py' in your terminal. This example uses Anaconda's command prompt on a Windows 10 machine.

### Program Details

The program takes user inputs for the city (e.g., Chicago), the desired month for data viewing (e.g., January, with an 'all' option), and the preferred day for data viewing (e.g., Monday, also with an 'all' option).

Upon receiving user input, the program provides an option to view the raw data (initially, 5 rows). Based on user preferences, the program displays the following details:

* Most popular month
* Most popular day
* Most popular hour
* Most popular starting station
* Most popular ending station
* Most common combination of starting and ending stations
* Total trip duration
* Average trip duration
* User types by count
* User types by gender (if available)
* Oldest user (if available)
* Youngest user (if available)
* Most common birth year among users (if available)

At the end, the user can choose to restart the program or exit.

# Requirements

* Language: Python 3.6 or higher
* Libraries: pandas, numpy, time

# Project Data

* chicago.csv - This dataset, located in the data folder, contains bikeshare information for the city of Chicago, provided by Udacity.

* new_york_city.csv - This dataset contains bikeshare information for the city of New York, provided by Udacity.

* washington.csv - This dataset contains bikeshare information for the city of Washington, provided by Udacity. Note: It does not include 'Gender' or 'Birth Year' data.

# Built with

* [Python 3.11.2](https://www.python.org/) - The programming language used.
* [numpy](http://www.numpy.org/) - A library used for this project.
* [pandas](https://pandas.pydata.org/) - Another library used for this project.
* [time](https://docs.python.org/2/library/time.html) - A library utilized for this project.

# Author

 * [Coojanie Heendeniya](https://github.com/CooHeendeniya) - The sole author of this program. Acknowledgements are provided in the 'Acknowledgements' section.
  
# Acknowledgements

* [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) - The pandas documentation was highly beneficial in understanding the implementation of pandas methods in this project.
* [Udacity](https://udacity.com) - The Data Analyst Nanodegree program and instructors at Udacity were instrumental during the pursuit of this project.
* [Tutorialspoint](https://www.tutorialspoint.com/python_data_science/index.htm) - The tutorialspoint data science documentation was highly beneficial in understanding the implementation of pandas methods in this project.