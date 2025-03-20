{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Excel Data Visualization

## Exercises

---

### Exercise 1

Load the [Following dataset](./files_12_data_visualization_exercises/exercise01/exercise01.csv).

It shows RNA expression data with and without a stimulus.

Create a column chart for the `MAP kinase Expression values without a stimulus with expression levels higher than 0.5.

Create the column chart on a new worksheet.
Annotate the axis and add a proper title.

Sort the expression values from low to high (the graph should contain bars with increasing height).

### Exercise 2

From the previous data set, use again the gene expression within the MAP Kinase gene family.
Create a clustered column chart representing the expression values without stimulus and the expression values with stimulus. Make sure to add proper axis titles, a title and a legend. The gene names should be sorted.

### Exercise 3

Use the same data as from exercise 2 to create a stacked column chart. Filter the data that contain the MAP Kinase gene family.
Create a stacked column chart representing the Expression Values with and without stimulus. Make sure to add proper axis titles, a title and a legend. The gene names should be sorted.

### Exercise 4

Use the same data as from exercise 3 to create a relative stacked column chart. Filter the data that contain the MAP Kinase gene family. Create a relative stacked column chart representing the Expression Values with and without stimulus. Make sure to add proper axis titles, a title and a legend. The gene names should be sorted.

### Exercise 5

Use the same data as from exercise 3 to create a pie chart.
Create a pie chart representing the total Expression Value without stimulus per Category. Make sure to add proper axis titles, a title and a legend.

Which category shows the smallest fraction of expression value - stimulus?

### Exercise 6

For this exercise you will use the same data.
Create a box plot for Expression value - stimulus plotted against the Categories.  

Which category shows the lowest median value?

### Exercise 7

For this exercise you will use the same data.
Create a box plot for Expression value - stimulus and + stimulus plotted against the Categories.  

Which category shows the lowest IQR value?

### Exercise 8

In [this dataset](./files_12_data_visualization_exercises/exercise08/ChickWeight.csv) you can find Chick Weight data. It shows the weight (in grams) on day 42 for various chickens that were fed with various diets during 42 days.

Create a radar chart for the various diets on day 42.  
Calculate the average weight per diet.

Two Chickens on a certain diet clearly gained the most weight.  
Wich two chickens on which diet generated the highest weight gains?  

### Exercise 9

Have look at the data [here](./files_12_data_visualization_exercises/exercise09/data.csv)
It contains data about Potassium and Sodium concentrations (in mmol/L) as well as bodyweight (in kg) for various persons.  

Create a bubble chart with the Na concentration as a function of the K concentration.  
The bubble size should be based on the bodyweight.  

As you can see, there is a correlation between the sodium and potassium concentration but there is one person who can be considered an outlier. What is the name of this person?   

### Exercise 10

In [this dataset](./files_12_data_visualization_exercises/exercise10/data.csv), you will find data on the velocity of an enzymatic reaction were obtained by Treloar (1974). The number of counts per minute of radioactive product from the reaction was measured as a function of substrate concentration in parts per million (ppm) and from these counts the initial rate (or velocity) of the reaction was calculated (counts/min/min). The experiment was conducted once with the enzyme treated with Puromycin, and once with the enzyme untreated.

Create a XY-scatter plot with the velocity plotted against the substrate concentration. 

Create a XY-scatter for the experiment without puromycin and an additional XY scatter plot for both (with and without puromycin) conditions.

Does puromycin act as an inhibitor or an activator for this enzyme?

### Exercise 11

For this exercise, we will use the dataset from exercise 7 again. This time, to create a pivot table and plot.

Download the [data set about](https://www.kaggle.com/datasets/kkhandekar/calories-in-food-items-per-100-grams) food calories per 100 g. 

The data set contains units in the cells.  
First clean the dataset.  
Create a pivot plot for the **mean** `Energy per 100 g in KJ` plotted against the `Food Categories`.  

Which two Food Categories show the highest mean energy per weight?
 

---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

