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
*<sub>Figure 8: 1 duplicate row removed.</sub>*

## Trimming text

Often, data will contain extra whitespace such as spaces. Extra spaces are notoriously difficult to spot, especially those at the end. Those extra spaces may interfere with later analysis. 

![extra spaces](./pics_05_data_cleaning/fig9.png)
*<sub>Figure 9: Only 1 Milk counted as one cell contains Milk with a tailing space.</sub>*

The `TRIM` function will remove trailing whitespace:

![extra spaces](./pics_05_data_cleaning/fig10.png)
*<sub>Figure 10: The TRIM function in action.</sub>*

As a result, the tailing whitespace is now removed and the `COUNTIF` function returns the expected result.

## Find and replace

Find and replace is usefull to clean data. This example shows some HTML tags in cells:

![find replace](./pics_05_data_cleaning/fig11.png)
*<sub>Figure 11: HTML tags in cells.</sub>*

Removing them is easy using find and replace:

![find replace](./pics_05_data_cleaning/fig12.png)
*<sub>Figure 12: Remove HTML tags in cells.</sub>*

The `*` is a wildcard that represents any text. Note that you do not need to exlicitely specify an empty string in the `replace with` field. Excel will take care of this.

![find replace](./pics_05_data_cleaning/fig13.png)
*<sub>Figure 13: HTML tags removed.</sub>*

There are some other handy functions that work on strings that can help you:

| **Function** | **Explanation**                                                                                                                                                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FIND         | FIND and FINDB locate one text string within a second text string, and return the number of the starting position of the first text string from the first character of the second text string.                                 |
| SEARCH       | The SEARCH and SEARCHB functions locate one text string within a second text string, and return the number of the starting position of the first text string from the first character of the second text string.               |
| REPLACE      | REPLACE replaces part of a text string, based on the number of characters you specify, with a different text string.                                                                                                           |
| SUBSTITUTE   | Substitutes new_text for old_text in a text string. Use SUBSTITUTE when you want to replace specific text in a text string; use REPLACE when you want to replace any text that occurs in a specific location in a text string. |
| LEFT         | LEFT returns the first character or characters in a text string, based on the number of characters you specify.                                                                                                                |
| RIGHT        | RIGHT returns the last character or characters in a text string, based on the number of characters you specify.                                                                                                                |
| LEN          | LEN returns the number of characters in a text string.                                                                                                                                                                         |
| MID          | MID returns a specific number of characters from a text string, starting at the position you specify, based on the number of characters you specify.                                                                           |


## Dealing with missing data

https://real-statistics.com/descriptive-statistics/missing-data/


### Exersises and Solutions:


- [Exercises]()
- [Solutions]()

---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

