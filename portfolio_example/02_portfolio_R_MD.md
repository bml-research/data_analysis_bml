{% include head.html %}
![Hanze](../hanze/hanze.png)

---

[Go back to the main page](../index.md)

---

# Portfolio R for Medical Diagnostics students 

## The Portfolio Assignment

As the R part is only 1 EC for Medical Diagnostics students, the R part is considerably shorter. It consists only of the Base R part and an Excel import of lab data. Tidyverse will be omitted.

Thus it consists of the following parts:
- [R Basics](../R/R_02_basics.html)  
- [R Basics Exercises](../R/R_02_basics_exercises.html)  
- [R Basics Solutions](../R/R_02_basics_solutions.html)  
- [R Basics Extra Exercises](../R/R_02_basics_add_exercises.html)  
- [R Basics Extra Solutions](../R/R_02_basics_add_solutions.html)  

And for loading data from an Excel file:
- [R data import](../R/R_03_data_import.html)

>For the import, just focus on the part about `readxl`.

## Your Workflow: Step-by-Step

Follow these steps to complete your portfolio effectively:

- Take a lab notebook from a previous theme/module that contains a (linear) calibration curve (or calibration line). Note: it must be your own lab notebook!.
- Ensure that you share this lab notebook with your instructor (collaborate).
- Export you lab notebook as pdf file.
- Include your pdf file in your portfolio.
- Transfer the data from the lab notebook into an Excel file (xlsx file).
- Load this data into R as a data frame using the readxl function.
- Calculate the minimum, median, and maximum of your data points. Do this for both X and Y.
- Plot your calibration curve using base R.
- Add a linear model to your plot.
- Ensure your plot has a good title and proper axis labels including quantities and units.
- Put everything in a neat RMarkdown document. 
- Create a proper YAML front matter at the top of an R Markdown (.Rmd) file. See below for an example.
- Knit your RMarkdown file to HTML.
- Create a zip file of your R portfolio including the Excel file with the data, the pdf file of your lab notebook, the RMarkdown file of your analysis and the knitted HTML document.
- Upload this zip file to Brightspace.


Good luck! 🍀


---

[Go back to the main page](../index.md)  
<a href="#top">⬆️ Back to Top</a>  

---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

