{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Excel Data Cleaning

## Solutions

---

### Exercise 1

Use the text to column feature. Seperator is the pipe symbol `|`.
Then, create a data table with the first row as headers.

![solution](./files_07_data_cleaning_solutions/exercise01/fig1.png)

The solution can be found [here](./files_07_data_cleaning_solutions/exercise01/calories.xlsx).



### Exercise 2

Use the following steps to clean the data:
- First load the data as previously mentioned using the `text-to-column` feature.
- Remove the header row.
- Split the last two columns using the `text-to-column` feature with a space as deliminator.
- Remove the columns containing the units.
- Split the columns that contains the `g` from grams using the `text-to-column` feature with a `g` as deliminator.
- Add the column headers again.
- Format as data table

See example below:

![example](./files_07_data_cleaning_solutions/exercise02/fig1.png)

The solution can be found [here](./files_07_data_cleaning_solutions/exercise02/calories.xlsx)

>Note that alternative approaches are possible.
>For example `=LEFT(C1,LEN(C1)-1)` will strip the g from the numbers.
>Use whatever gets the job done!


---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

