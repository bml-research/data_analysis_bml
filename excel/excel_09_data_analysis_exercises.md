{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Excel Data Analysis

## Exercises

---

### Exercise 1

Import the [Mice Protein Expression](https://www.kaggle.com/datasets/ruslankl/mice-protein-expression?resource=download) in Excel. This dataset contains data about expression levels of 77 proteins measured in the cerebral cortex in mice.

> Take a good look to column separators and the decimal separators!

Rename this worksheet `data`.  
Create a new worksheet and name it `analysis`.  
Then perform the following calculations on a new worksheet and display them as a table:  

- Calculate the minimum, maximum, average, median from all the columns (proteins). Display the answers in a table.  

> Although there are different classes of mice in the dataset (there are 38 control mice and 34 trisomic mice (Down syndrome)), you do not need to take care of this (yet).

### Exercise 2

Use filter and sort to answer the following questions:  
1. Which item has the highest Calories from fat?  
2. Which items have the highest Iron (% Daily Value)?  
3. Which Beef & Pork item has the lowest Calories from fat?  
4. Which Coffee & Tea or Smoothies & Shakes item has the highest amount of carbohydrates?  
5. Which item has the highest saturated fat and lowest carbohydrates value (use multi-sort to practice)?  

### Exercise 3

1. More then 600 calories would be considered high energetic. How many items are high energetic?  
2. How many items are between 300 and 600 calories?  
3. How many items are measured in the serving size Fluid Ounce (fl oz cup) (hint: use a wildcard)?  

### Exersise 4

1. Use conditional formatting to indicate high energetic food items (>600 calories). Use red markup for these. Which two categories show the highest number of red cells?  
2. Use conditional formatting to check for duplicate food items. Use red markup for these. Are there any duplicate items?  
3. Use conditional formatting to indicate a % Daily Value > 100% for Vitamin A. Which category are these items mainly found?  
4. Use conditional formatting to indicate a % Daily Value >= 100% for Vitamin C. Use green markup for these. Make sure that you include 100%! How many items do you find that meet this criteria?  


### Exercise 5

Create a new worksheet and name it pivot.  
Create a Pivot table and group the categories.  
Calculate:  
- the Average of Total Fat (% Daily Value)  
- the Average of Saturated Fat (% Daily Value)  
- the Average of Cholesterol (% Daily Value)  

Round the values to 1 decimal.  


---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

