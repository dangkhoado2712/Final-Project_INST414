# Final-Project_INST414
## I.	Topic:
For the final project topic, because COVID-19 is not a topic that people are concerned a lot about in this period, I want to analyze the COVID-19 vaccine distribution in the USA from 2021 to 2022 to see the trend of the vaccination distribution and the real situation of the vaccination based on the vaccination rate in the U.S. 
## II.	Dataset:

*	Link for the dataset: https://ourworldindata.org/us-states-vaccinations.
*	The U.S population: https://www.kaggle.com/datasets/alexandrepetit881234/us-population-by-state?resource=download&select=us_pop_by_state.csv 
* The dataset is from kaggle.com which represents the vaccine for COVID-19 that is available in the USA. Also, the dataset also provides state-by-state data on COVID-19 vaccinations in the U.S. The dataset has 16 columns and 42981 rows.
* The dataset is updated daily, so it is up-to-date and the data is recent. The source of data is reliable and transparent.

## III.	Questions:

These are some questions that the result of the data analysis will attempt to answer to have insight into the vaccination campaign in the United States, so we can see the people’s concern about the COVID-19 pandemic.
*	How many people are fully vaccinated per the vaccination distributed?
*	How is the different vaccination distribution between states?
*	Which state has the highest and lowest vaccination rate?
*	How will people attempt to get the vaccine in the future?
*	What is the vaccination attempt different between 2021 and 2022?

## IV.	Data Analysis Process:

*	Clean the dataset
*	Analyze data using tools such as python and R
*	Visualization of the dataset using tools such as Python, Power BI
*	Prediction future trends of vaccination using Python and Power BI

## Problem and Solutions:
* The data is updated by time so I cannot delete the NaN value for the whole dataset because the data will be lost. Therefore, I created the data frames and delete the NaN for each column and when it needs for analysis.
* It is hard to detect the outlier and error in the dataset because the data is not continuous. I use the statistic summarize to understand more about the data and detect the error.
* For some data, using Power BI is not suitable for showing data. Using the multiple tools such as Python, Tableau and Power BI will help create the data better. 

## Accomplishment:

* Import and extraction the data from data source.
* Using Python to clean the data and create the data frame for specific intended analyze. Also, export the new data frame as CSV file namely cleaned_states and cleaned_US for future analyze.
* Using Power BI to create data visualization for the vaccination distribution between the states and using the filter to choose the states which have the high population. Also, compare the Maryland vaccination distribution situation with another states.
* Using Python to do the regression analysis for the data of Maryland. 
* Setup the regression analysis to see the effect of the total vaccinations, daily vaccination and total distributed on the people fully vaccinated in MD.Plot and analyze the result based on the regression analysis result.
* Using Power Bi to make prediction on the dataset of people fully vaccination, daily vaccination.

## Result:
* All most of the states are doing the vaccination protocol very. The percentage of people finish the protocol is over 50% and keep continuing to rising in the future.
California has the highest total vaccination and Wyoming has the lowest total vaccination. 
* As the result of the regression analysis, the amount of people fully vaccination is affected by the total vaccination and total distribution. It is not affected by daily vaccination rate.
* The total of people fully vaccination still increase in the future based on the forecast tools. The chart also show people get more vaccine in the cold weather months and the rate is slow down in the warm weather months.
* The booster vaccination is decreasing as 50% now, so people stop taking the booster. It can be the reason is the booster is for elders or people do not have too much concern about COVID-19
