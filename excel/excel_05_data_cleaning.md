{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Excel: Data Cleaning


## Introduction

In data science, data is typically organized in a structured format, such as a table or a spreadsheet. This allows for easy manipulation and analysis of the data.

However, a lot of data coming from external sources such as lab equipment and factory equipment will not be directly suitable for data analysis. In that case, data cleaning en reorganization might me required.

Excel lacks behind Python and R in capabilities of data reorganization and cleaning. Nevertheless, Excel has some features that are worth explaining. We will discuss them here.

## Text to column feature

If your csv data import fails, you can manually parse your text to various columns. Take a look at the following example:

![food](./pics_05_data_cleaning/fig1.png)
*<sub>Figure 1: All data in a single column</sub>*

As you can see, all data is loaded in the first column. You can use the `text to columns` functionality that can be found on the data tab in the ribbon.

![food2](./pics_05_data_cleaning/fig2.png)
*<sub>Figure 2: Select the delimiter</sub>*

Here the correct culumn separator is selected to parse the text. The result is as follows:

![food3](./pics_05_data_cleaning/fig3.png)
*<sub>Figure 3: Text separated to columns</sub>*

As you can see from the picture above, the text is now separated in different columns based on the correct column separator.


## Remove duplicates

On the data tab in the ribbon, you will find an option to remove duplicate rows:

![duplicates](./pics_05_data_cleaning/fig4.png)
*<sub>Figure 4: Remove duplicates feature</sub>*

As can be seen from the picture below, row ID 2 is a duplicate.

![duplicates](./pics_05_data_cleaning/fig5.png)
*<sub>Figure 5: Two duplicate rows</sub>*

You can select columns to compare. In the case below, all columns were selected.

![duplicates](./pics_05_data_cleaning/fig6.png)
*<sub>Figure 6: Columns selected to compare</sub>*

Excel reports the removal of 1 duplicate row.

![duplicates](./pics_05_data_cleaning/fig7.png)
*<sub>Figure 7: 1 duplicate value removed.</sub>*

And the result is 1 duplicate row removed.

![duplicates](./pics_05_data_cleaning/fig8.png)
*<sub>Figure 7: 1 duplicate row removed.</sub>*

## Trimming text


## Find and replace

## Dealing with missing data

https://real-statistics.com/descriptive-statistics/missing-data/


### Exersises and Solutions:


- [Exercises]()
- [Solutions]()

---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

