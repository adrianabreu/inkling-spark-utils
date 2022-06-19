# Inklings-Spark-Utils

"A.k.a. Infra-Nocturnal Kappa." - Hard-Boiled Wonderland (Haruki Murakami)

This project aims to compile small utilities I tend to use on my daily job as well as to explore some alternative solutions for common problems.

# Module

## Arguments

Include a simple argument parser for the most commons args you would use in a etl, that is a range of dates (from-to).


## Dataframe

Here are a collection of functions for ensure dataframe alignment with a certain schema. That's useful when you have wide tables fed through multiple sources, so you can focus on the partial transformation and then led these functions take care of the rest.

1. select_schema_cols

2. complete_dataframe

3. cast_dataframe

## Testing

Here is an oversimplified testing module extracted from [Mr Powers](https://github.com/MrPowers) [Chispa](https://github.com/MrPowers/chispa). These method provide an standard way for comparing dataframe. The original chispa library also provides hints about the exact difference and some options for inequality.