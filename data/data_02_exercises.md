{% include head.html %}
![Hanze](../hanze/hanze.png)

---

[Go back to the main page](../index.md)
[Go back to the Data overview page](../data/data_01_index.md)

---


# Data

## Exercises

---

### Exercise 1

Download the [this dataset](https://www.kaggle.com/datasets/anoopjohny/comprehensive-drug-information-dataset).
Open it with a text editor (Notepad or TextEdit on a Mac).  

Describe for the following columns what kind of data it holds. Also describe the scale.  

|Column           |Data type       |Scale            |
|:----------------|:---------------|:----------------|
|Drug Name        |                |                 |
|NDC              |                |                 |
|Price            |                |                 |


### Exercise 2

Have a look at some raw data below:

Protein symbol: HBA1, HBA2, HBB, HBD, HBM  
Length (aa): 142, 142, 147, 147, 141  

Create a data table of the above data.  
Make sure that the observations (or records) and variables (or features) are organized appropriately. Also sort the data based on the protein length (primary) and on protein symbol (secondary).  

### Exercise 3

Heat shock in biology refers to the cellular response to sudden exposure to elevated temperatures. This stress response triggers the production of heat shock proteins (HSPs), which help cells maintain proper protein folding, prevent protein aggregation, and promote cell survival under heat stress conditions. We can apply different temperatures to induce a heat shock for human cells cultured in a laboratory.  

No heat shock is applied if a temperature of 98.6°F is used for 30 minutes.  
A medium heat shock is applied if a temperature of 104.0°F is used for 30 minutes.  
A strong heat shock is applied if a temperature of 107.6°F is used for 30 minutes.  

What is the ratio for "medium" and "strong" compared to no heat shock?  
Calculate the fold induction.  

### Exercise 4

The R library TidyVerse will work best with tidy data.  
Remember that there are three interrelated rules which make a dataset tidy:  
- Each variable must have its own column.  
- Each observation must have its own row.  
- Each value must have its own cell.  

Convert the data table below to a data table that is tidy.  

Cell growth in a 6-well plate over time for various cell types.  

|Cell type      |Day 1  |Day 2  |
|:--------------|------:|------:|
|HEK293         |1.2E04 |2.2E04 |
|A549           |1.1E04 |2.6E04 |
|K562           |0.9E04 |1.9E04 |

Also mention, which of the interrelated rules which make a dataset tidy have not been met.  

### Exercise 5

Another untidy data table. Describe which of the three interrelated rules which make a dataset tidy have not been met and convert the data table to a data table that is tidy.  

|Cell type      |Day 1, Day 2   |
|:--------------|--------------:|
|HEK293         |1.2E04, 2.2E04 |
|A549           |1.1E04, 2.6E04 |
|K562           |0.9E04, 1.9E04 |

### Exercise 6

Here we have a tidy data table. Spread the data set to make it wider and untidy.  

|Cell type      |Day |Medium             |Number of cells |
|:--------------|---:|:------------------|---------------:|
|HEK293         |1   |DMEM               |2.5E04          |
|HEK293         |1   |RPMI               |2.7E04          |
|HEK293         |2   |DMEM               |5.4E04          |
|HEK293         |2   |RPMI               |7.8E04          |
|A549           |1   |DMEM               |1.2E04          |
|A549           |1   |RPMI               |1.4E04          |
|A549           |2   |DMEM               |2.5E04          |
|A549           |2   |RPMI               |5.2E04          |



---

[Go back to the main page](../index.md)
[Go back to the Data overview page](../data/data_01_index.md)

---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

