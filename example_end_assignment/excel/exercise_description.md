{% include head.html %}
![Hanze](../hanze/hanze.png)

---

[Go back to the main page](../index.md)

---


# Example Exercise Excel

## Notes for instructors
Exercise 1: focus on Power Query loading and multiple plot types. Pie chart, Box plot, Pivot Column, XY-scatter.  
Exercise 2: More advanced Power Query (transform data required for cleaning). Focus on functions: MIN, MAX, XLOOKUP, FILTER, UNIQUE, COUNT, COUNTIF, AVERAGEIFS.  
Exercise 3: Power Query loading easy here. Focus on filtering large dataset for plotting, conditional formatting and Pivot Table.  


## General Instructions
You have 3.5 hours to complete this exam. Read all questions carefully before you start.
For each exercise, create a separate Excel file. Name each worksheet tab according to the corresponding sub-question (e.g. a, b, c, etc.). Where applicable, load your data using Power Query.  
Organize your work in three folders named exercise_1, exercise_2 and exercise_3. Each folder contains a data subfolder where you store the original unmodified data file(s), and the Excel file for that exercise is placed directly in the exercise folder itself and named “analysis.xlsx”.  
Keep the original data files in the data subfolder of each exercise folder.
When you are finished, zip the entire folder and upload the single zip file to Brightspace before the deadline.  


Rules
- The use of AI tools (such as ChatGPT, Claude, Copilot, or any other AI assistant) is strictly prohibited.
- You are only permitted to consult the following resources: 
- The [course website](https://bml-research.github.io/data_analysis_bml/)
- The official [Microsoft Excel support website](https://support.microsoft.com/excel)
- No other websites, notes, or resources are allowed.  


## Exercise 1

The Comet Goldfish Lifespan Prediction Dataset provides a structured collection of variables used to estimate the longevity of *Carassius auratus*. 


The fictive dataset includes several measurements:
- Environmental Factors: Habitat type (e.g., lakes, ponds), water pH, and tank specifications.
- Biological Metrics: Average length and weight, gender, and specimen color variations.
- Target Variable: Lifespan (years).
Answer the following questions:  
a.	Download the data at [Predict lifespan of a comet goldfish](https://www.kaggle.com/datasets/stealthtechnologies/predict-lifespan-of-a-comet-goldfish). Use PowerQuery in Excel to load the csv in Excel.  
b.	Filter data to exclude blanks for the column Gender. Also create a new column based on the following: True should be mapped to Male, False to Female.  
c.	Create a Pie chart to show the proportion of the different genders. You may need to use Excel formulas to prepare the data. Provide a logical title.  
Now remove the filters.  
d.	Create a box plot to compare the life span between the habitats. Provide a logical title together with axis titles and units.  
e.	Create a pivotchart that shows the average lifespan for each habitat. Provide a logical title together with axis titles and units.  
f.	Investigate a possible correlation between the pH of the water and the life span. Use a suitable chart type to visualize this. Provide a logical title together with axis titles and units. Start the axis with pH value 5. Is there a correlation?  

## Exercise 2
This time we will analyse some weather data from the KNMI. Browse to [KNMI - Uurgegevens van het weer in Nederland](https://www.knmi.nl/nederland-nu/klimatologie/uurgegevens). Download a dataset from 1951-1960 for the weather station at Eelde.
a.	Load the data using Power Query. Note: you need to use “transform” to tweak the loading of the data. Keep the original text file as it contains  important information about the columns!
b.	Create a new tab and find the lowest temperature and highest temperature (at 1.5 m height) using formulas in degrees Celsius (note: read the column info in the text file)!  
c.	At what dates were these temperatures observed? Use formulas to get the answer.
d.	A tropical temperature is defined as a temperature of 30 °C or higher. How many tropical temperatures are in the dataset (at 1.5 m height)?  
e.	There could be multiple tropical temperatures on the same day. How many tropical days are within the dataset (at 1.5 m height)?  
f.	What was the average temperature in 1951? Use formulas to achieve this.  

## Exercise 3
Use the dataset from [Our World in Data](https://github.com/owid/covid-19-data/tree/master/public/data/vaccinations Download vaccinations.csv).  
This dataset contains daily vaccination figures per country worldwide, with columns such as date, location, total_vaccinations, people_vaccinated, people_fully_vaccinated, daily_vaccinations, etc.  
a.	Load the data using Power Query in Excel.  
b.	Create a chart showing the progression of people_fully_vaccinated_per_hundred (in other words, the percentage) over time for the Netherlands. Filter the data accordingly. Provide a logical title together with axis titles and units.  
c.	Use conditional formatting to colour the cells with a colour scale. The minimum value should be red, the maximum value green and the midpoint should be yellow at number 30.  
d.	Provide a pivot chart with the max people_fully_vaccinated_per_hundred per hundred per country. Note that the numbers above 100 are in the dataset because of various reasons (e.g. boosters counted as full vaccination, some small countries (like Gibraltar or San Marino) vaccinated people who are not residents etc.).  

## The finishing touch

For each of the exercises, write a mini report using the following structure:

- Introduction: short introduction about the subject in a couple of sentences  
- Dataset: link to the original dataset  
- Aim: the aim of your analysis  
- Data import: how did you import the data (screenshot)
- Cleaning: did you clean the dataset? If so, how?  
- Results: show your plots together with a short result description.  
- Conclusion: a brief conclusion (one or two sentences).  

## Solutions

The solution can be found [here](./solutions.zip)

The end...

---