{% include head.html %}
![Hanze](../hanze/hanze.png)

---

[Go back to the main page](../index.md)  
[Go back to the Data overview page](../data/data_01_index.md)  

---


# Data

## Exercises Solutions

---

### Exercise 1

|Column           |Data type       |Scale            |
|:----------------|:---------------|:----------------|
|Drug Name        |Nominal         |Nominal          |
|NDC              |Continuous      |Ratio            |
|Price            |Continuous      |Ratio            |


### Exercise 2

|Item             |Protein length (aa)|
|:----------------|------------------:|
|HBB              |147                |
|HBD              |147                |
|HBA1             |142                |
|HBA2             |142                |
|HBM              |141                |


### Exercise 3

Note that Fahrenheit scale has no absolute zero (0 °F, was established as the freezing temperature of a solution of brine made from a mixture of water, ice, and ammonium chloride). As a result, we can not directly calculate a ratio as the Fahrenheit scale is an interval scale. We first need to convert the data to Kelvin.

We can use the formula:  $K = (F − 32) \cdot \frac{5}{9} + 273.15$

So we will get the following data:  

No heat shock: 98.6°F = 310.15 K  
Medium head shock: 104.0°F = 313.15 K  
Strong heat shock: 170°F = 315.15 K  

Ratio medium/no heat shock = 313.15/310.15 = 1.0097  
Ratio strong/no heat shock = 315.15/310.15 = 1.0161  

### Exercise 4

The rule "Each variable must have its own column." has not been met. In the untidy table, there are two columns related to the number of cells. Thus, the column names are not names of variables, but values of a variable. Thus, we need to create a column "Day" in order to solve this.

|Cell type      |Day |Number of cells|
|:--------------|---:|--------------:|
|HEK293         |1   |1.2E4          |
|HEK293         |2   |2.2E4          |
|A549           |1   |1.1E4          |
|A549           |2   |2.6E4          |
|K562           |1   |0.9E4          |
|K562           |2   |1.9E4          |

### Exercise 5

The rule "Each value must have its own cell." has not been met. In the untidy table, there are two values related to the number of cells in one cell of the table. Thus, we need to separate them over two records (rows) in order to solve this. Note that we should not separate these values in two columns as this will create the situation as shown in Exercise 4.  

|Cell type      |Day |Number of cells |
|:--------------|---:|---------------:|
|HEK293         |1   |1.2E04          |
|HEK293         |2   |2.2E04          |
|A549           |1   |1.1E04          |
|A549           |2   |2.6E04          |
|K562           |1   |0.9E04          |
|K562           |2   |1.9E04          |

### Exercise 6

The data table spread out (wider):  

|Cell type      |Day |Number of cells DMEM  |Number of cells RPMI     |
|:--------------|---:|---------------------:|------------------------:|
|HEK293         |1   |2.5E04                |2.7E04                   |
|HEK293         |2   |5.4E04                |7.8E04                   |
|A549           |1   |1.2E04                |1.4E04                   |
|A549           |2   |2.5E04                |5.2E04                   |

---

[Go back to the main page](../index.md)  
[Go back to the Data overview page](../data/data_01_index.md)  

---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>

<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>