{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Excel Data Analysis

## Exercises

---

### Exercise 1

Import the [Mice Protein Expression](https://www.kaggle.com/datasets/ruslankl/mice-protein-expression?resource=download) in Excel. This dataset contains data about expression levels of 77 proteins measured in the cerebral cortex in mice. The protein names are abbreviated. The abbreviations of protein names are followed by N indicating that they were measured in the nuclear fraction meaning that for the protein name you should remove the `_N`.

> Take a good look to column separators and the decimal separators!

Rename this worksheet `data`.  
Create a new worksheet and name it `analysis`.  
Then perform the following calculations on a new worksheet and display them as a table:  

- Calculate the minimum, maximum, average, median from all the columns (proteins). Display the answers in a table.  

> Although there are different classes of mice in the dataset (there are 38 control mice and 34 trisomic mice (Down syndrome)), you do not need to take care of this (yet).

### Exercise 2

Use filter and sort to answer the following questions:  
1. Which mouse has the highest expression of Tau?  
2. What is the relative expression value in this mouse?  
3. Which mouse has the lowest expression of pAKT?  
4. How many empty cells are in the BAD column?  
5. Which mouse of the Ts65Dn genotype group has the highest Tau expression (se multi-sort or filters)?  
6. Which mouse of the Ts65Dn genotype, and saline treatment group has the highest Tau expression (se multi-sort or filters)?  

### Exercise 3

1. An relative expression level > 0.5 would be considered a high expression level. How many mice do have a high expression level for DYRK1A?  
2. Apply this calculation for all proteins. For which protein do you observe a count of 218?  
3. Glutamate receptor subunits NR1 and NR2A are included in the dataset. How many mice do have higher expression levels for NR1 compared to NR2A?  

### Exercise 4

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

