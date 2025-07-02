{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)

---

# Schedule and Outline for Students and Teachers

## Aim of the course

The aim of this introductory course is to equip students with the fundamental concepts of data management and analysis, enabling them to proficiently import, clean, prepare, analyze, and visualize data using both Microsoft Excel and R (with an emphasis on the Tidyverse package). The course will focus on practical application with relatively small datasets (under 10,000 rows), enabling students to effectively compare and contrast the capabilities of Excel and R for various data tasks, without delving into advanced programming concepts.

## Course outline

| Lesson number | Excel/R | Subject                                               |
|---------------|---------|-------------------------------------------------------|
| 1             | Excel   | Intro data types, Setup software Excel, Data import   |
| 2             | Excel   | Data cleaning                                         |
| 3             | Excel   | Data analysis                                         |
| 4             | Excel   | Data analysis                                         |
| 5             | Excel   | Data visualization                                    |
| 6             | Excel   | Data visualization                                    |
| 7             | R       | R Basics                                              |
| 8             | R       | Data import                                           |
| 9             | R       | Data cleaning                                         |
| 10            | R       | Data cleaning                                         |
| 11            | R       | Data analysis                                         |
| 12            | R       | Data analysis                                         |
| 13            | R       | Data visualization                                    |
| 14            | R       | Data visualization                                    |


## Outline per lesson

Before the lessons start:
- Install Excel (if not done yet).
- Install Statistics Analysis pack.
- Install Visual Studio Code and the rainbow plugin.
- Install R.
- Install RStudio.

Details on installation can be found [here](https://bml-research.github.io/data_analysis_bml/install/data_01_install.html).

### Lessen 01: Intro data types, Setup software Excel, Data import in Excel

- Discuss the various [data types](https://bml-research.github.io/data_analysis_bml/data/data_01_index.html).
- Categorical (nominal, ordinal) and numerical (discrete and continues). Also discuss data scales (ratio, interval and ordinal). Also discuss implications of the data types in calculations and visualizations.
- Discuss the organization of data in 2-dimensional representation. Rows are records and columns variables and features.
- Discuss tidy data. Long format and wider format. 
- Discuss data types in Excel (numeric, text, logical, error) and R (logical, numeric, character)
- Open csv files in Visual Studio Code with the rainbow plugin.
- Discuss region and language settings (use of argument separators Excel and decimal separators).
- Demonstrate Power Query to import csv files. Region settings are important here! 
- Make use of skipping rows, use of headers, renaming columns and find and replace in PowerQuery.
- Notify students about the exercises to practice.
- [Exercise 9 from the R data import section](https://bml-research.github.io/data_analysis_bml/R/R_04_data_import_exercises.html) is also useful for Excel import. 

### Lesson 02: Data Cleaning in Excel

- Demonstrate the text to column feature.
- Demonstrate how to remove duplicates.
- Demonstrate how to trim text.
- Demonstrate how to find and replace text.
- Demonstrate useful string functions such as `FIND`, `SEARCH`, `REPLACE`, `SUBSTITUTE`, `LEFT`, `RIGHT`, `LEN` and `MID`.
- Demonstrate splitting (`TEXTSPLIT`) and concatenating (`CONCAT`) strings.
- Demonstrate how to deal with missing data and the `#N/A` error and the `COUNTBLANK` function.
- Explain difference of implicit and explicit missing data and advantages and disadvantages of both. 
- Demonstrate the `SUM` and `SUMIF` function and how it can be used with explicit missing data. Of course, the same holds for `AVERAGEIF`.

### Lesson 03: Data Analysis in Excel

- Explain the organization of a worksheet (and multiple worksheets).
- Good practice to separate data from analysis. In particular if data sets are large and data sets are progressively growing (more rows added).
- Explain the anatomy of a function (function call, arguments) but also what they return.
- Demonstrate named ranges and how they simplify ranges.
- Discuss array formulas. Even the `SUM` function is an array formula. Some array functions also create output in multiple cells (e.g. `TRANSPOSE`, `UNIQUE`).
- Show how to nest function. For example for if-else clauses. Also demonstrate how nesting functions can create a "MEDIANIF" function that does not exist in Excel (`MEDIAN(IF(ARGS))`).
- Demonstrate some examples from the useful function table. No need to show them all. Pick some with small examples. Good to show the difference between `AVERAGE`, `AVERAGEIF` and `AVERAGEIFS`. Also demonstrate `XLOOKUP`.


### Lesson 04: Data Analysis in Excel

- Demonstrate the filtering and sorting of data including multi-level sort.
- Demonstrate conditional formatting.
- Demonstrate Pivot Tables (can use the example of the website).
- Also demonstrate the limitations. For example: sum and average are possible but median is not possible.
- Demonstrate that the same as a pivot table can be achieved using `UNIQUE` together with `AVERAGEIF`. In line with this, you can also combine `UNIQUE` with a custom "MEDIANIF" `MEDIAN(IF(ARGS))`. 


### Lesson 05: Data Visualization in Excel

- Use the example of the website to demonstrate Excel plotting capabilities.
- Show that graphs are dynamic. First create a column chart for the whole max life span column. Then filter the data as shown at the website. The graph will be adjusted to the selection.
- Demonstrate a clustered column chart.
- Demonstrate that graph types can be easily changed. Clustered column to stacked column and change to relative stacked column by simply changing chart type.
- Demonstrate the PIE chart and how labels can be visualized.
- Demonstrate the radar chart.


### Lesson 06: Data Visualization in Excel

- Demonstrate Box plots and what they mean. Minimum, percentiles, maximum and IQR.
- Demonstrate the difference between line plots and XY-scatter and also demonstrate the x-axis scaling problem using line plots.
- Demonstrate bubble charts.
- Demonstrate Pivot charts. Also the limitations (e.g. no plotting of median values possible).


### Lesson 07: R Basics

- Demonstrate the very basics of R. [See the exercises](https://bml-research.github.io/data_analysis_bml/R/R_02_basics_exercises.html). This can be used during the lesson. See also the [solutions](https://bml-research.github.io/data_analysis_bml/R/R_02_basics_solutions.html).
- Cover the following:
    - variable assignment.
    - build in functions such as `len`, `class`, `sum`, `mean`, `median`, `sd`, `rep`, `seq`, `paste`, `paste0`, `toupper`.
    - build in variables such as `letters` and `LETTERS`.
    - Indexing of vectors.
    - Factor (ordered and unordered).
    - Vectorized operations (e.g. vector + 1).
    - Data frames (creating, indexing, adding column, adding rows, deleting column, deleting rows).
    - Subsetting dataframes (e.g. row with max value for a column).
    - Demonstrate `summary`.
    - Sort data frame.
    - base R plotting (barplot, XY-scatter, boxplot, histogram).

### Lesson 08: Data Import in R

- View csv and tsv using Visual Studio Code with rainbow plugin.
- Explain utf-8, BOM, CRLF (Windows) vs LF (Unix-like).
- Import data using tidyverse (`read_csv`, `read_csv2`, `read_tsv`, `read_delim`).
- Use of arguments: `comment`, `delim`, `na`, `skip`.
- In particular [exercise 9](https://bml-research.github.io/data_analysis_bml/R/R_04_data_import_exercises.html) is useful.
- Write to csv (`write_csv`).
- Import from Excel (`readxl` package).
- Write to Excel (`openxlsx` package).

### Lesson 09: Data Cleaning in R

- Explain difference data frame and tibble.
- Remove rows with missing values (`drop_na`).
- Renaming columns (`rename`).
- Reordering columns (`select`).
- Changing the data type of a column (`mutate`).
- Deal with missing values (from csv and Excel).
- Replace data (subsetting).

### Lesson 10: Data Cleaning in R

- Add row to tibble (`add_row`).
- Replace a whole row tibble (`filter`).
- Replace data in whole column (`mutate`).
- Replace data in entire data frame (`replace`).
- make tidy (`pivot_longer`).
- Untidy (`pivot_wider`).
- Transpose data (`t` from base R, can also be done using `pivot_longer` and `pivot_wider`).
- Separate column in two columns (`separate_wider_delim`).
- Explain the use of the `%>%` operator (from the magrittr package) to chain operations on data frames.

### Lesson 11: Data Analysis in R

- Follow the website and use similar examples.
- It is advised to start with small samples and then continue to the samples of the website.
- Start with loading the csv file in a tibble.
- Than perform analysis like:
    - Selections (rows, columns, items).
    - Filter rows (`filter`).
    - Use operators for filtering rows like: `&`, `|`, `>`, etc.

### Lesson 12: Data Analysis in R

- Arrange rows (`arrange`) for sorting data frames.
- Select columns with select (`select`).
- Summary data using different functions:
    - Simple summary statistics of base R (`summary`).
    - Summarize data using Tidyverse and functions of choice (`summarize`).
    - Summarize data using Tidyverse for multiple columns at once (`summarize_each`).
    - The new way to do this in Tidyverse using `across`.

### Lesson 13: Data Visualization in R

- Demonstrate the use of a base R barplot and a barplot using `ggplot2`.
- Explain the grammar of `ggplot2` (using the layers).
- Use the example from the website. Some preprocessing is required to reduce the size to be plotted.
- Create a bar plot using `ggplot2`.
- Create a grouped bar plot.
- Create a stacked ar plot.
- Create a percent stacked bar plot.
- Switch order of groups (use an unordered factor).

### Lesson 14: Data Visualization in R

- Create a Pie Chart.
- Create a Box Plot.
- Create a grouped Box Plot.
- Create a Line Plot.
- Create a XY-scatter plot.
- Create a Bubble Chart.
- Explain the [Portfolio Exercise](https://bml-research.github.io/data_analysis_bml/portfolio_example/01_example_portfolio.html).


---

>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.