---
jupyter:
  jupytext:
    formats: ipynb,md,py:percent
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Pandas

## Introduction

`pandas` is the Python Data Analysis package. It allows for data ingestion, transformation and cleaning, and creates objects that can then be passed on to analytic packages like `statsmodels` and `scikit-learn` for modeling and packages like `matplotlib`, `seaborn`, and `plotly` for visualization. 

`pandas` is built on top of numpy, so many numpy functions are commonly used in manipulating `pandas` objects. 

> `pandas` is a pretty extensive package, and we'll only be able to cover some of its features. For more details, there is free online documentation at [pandas.pydata.org](https://pandas.pydata.org). You can also look at the book ["Python for Data Analysis (2nd edition)"](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython-dp-1491957662/dp/1491957662/) by Wes McKinney, the original developer of the pandas package, for more details.

## Starting pandas

As with any Python module, you have to "activate" `pandas` by using `import`. The "standard" alias for `pandas` is `pd`. We will also import `numpy`, since `pandas` uses some `numpy` functions in the workflows. 

```python
import numpy as np
import pandas as pd
```
## Data import and export

Most data sets you will work with are set up in tables, so are rectangular in shape. Think Excel spreadsheets. In `pandas` the structure that will hold this kind of data is a `DataFrame`.  We can read external data into a `DataFrame` using one of many `read_*` functions. We can also write from a `DataFrame` to a variety of formats using `to_*` functions. The most common of these are listed below:

| Format type | Description | reader       | writer     |
| ----------- | ----------- | ------------ | ---------- |
| text        | CSV         | read_csv     | to_csv     |
|             | Excel       | read_excel   | to_excel   |
| text        | JSON        | read_json    | to_json    |
| binary      | Feather     | read_feather | to_feather |
| binary      | SAS         | read_sas     |            |
| SQL         | SQL         | read_sql     | to_sql     |

We'll start by reading in the `mtcars` dataset stored as a CSV file

```python
pd.read_csv('data/mtcars.csv')
```

This just prints out the data, but then it's lost. To use this data, we have to give it a name, so it's stored in Python's memory

```python
mtcars = pd.read_csv('data/mtcars.csv')
```

> One of the big differences between a spreadsheet program and a programming language from the data science perspective is that you have to load data into the programming language. It's not "just there" like Excel. This is a good thing, since it allows the common functionality of the programming language to work across multiple data sets, and also keeps the original data set pristine. Excel users can run into problems and [corrupt their data](https://nature.berkeley.edu/garbelottoat/?p=1488) if they are not careful.

If we wanted to write this data set back out into an Excel file, say, we could do

```python
mtcars.to_excel('data/mtcars.xlsx')
```

> You may get an error if you don't have the `openpyxl` package installed. You can easily install it from the Anaconda prompt using `conda insall openpyxl` and following the prompts. 



## Exploring a data set

We would like to get some idea about this data set. There are a bunch of functions linked to the `DataFrame` object that help us in this. First we will use `head` to see the first 8 rows of this data set

```python
mtcars.head(8)
```
This is our first look into this data. We notice a few things. Each column has a name, and each row has an *index*, starting at 0. 

> If you're interested in the last N rows, there is a corresponding `tail` function

Let's look at the data types of each of the columns

```python
mtcars.dtypes
```

This tells us that some of the variables, like `mpg` and `disp`, are floating point (decimal) numbers, several are integers, and `make` is an "object". The `dtypes` function borrows from `numpy`, where there isn't really a type for character or categorical variables. So most often, when you see "object" in the output of `dtypes`, you think it's a character or categorical variable. 

We can also look at the data structure in a bit more detail.

```python
mtcars.info()
```

This tells us that this is indeed a `DataFrame`, wth 12 columns, each with 32 valid observations. Each row has an index value ranging from 0 to 11. We also get the approximate size of this object in memory.

You can also quickly find the number of rows and columns of a data set by using `shape` which is borrowed from numpy.

```python
mtcars.shape
```

More generally, we can get a summary of each variable using the `describe` function

```python
mtcars.describe()
```



These are usually the first steps in exploring the data.


## Data structures and types

pandas has two main data types: `Series` and `DataFrame`. These are analogous to vectors and matrices, in that a `Series` is 1-dimensional while a `DataFrame` is 2-dimensional. 

### pd.Series

The `Series` object holds data from a single input variable, and is required, much like numpy arrays, to be homogeneous in type. You can create `Series` objects from lists or numpy arrays quite easily

```python
s = pd.Series([1,3,5,np.nan, 9, 13])
s
```

```python
s2 = pd.Series(np.arange(1,20))
s2
```
You can access elements of a `Series` much like a `dict`

```python
s2[4]
```

There is no requirement that the index of a `Series` has to be numeric. It can be any kind of scalar object

```python
s3 = pd.Series(np.random.normal(0,1, (5,)), index = ['a','b','c','d','e'])
s3
```

```python
s3['d']
```

You can extract the actual values into a numpy array

```python
s3.to_numpy()
```

### pd.DataFrame

The `DataFrame` object holds a rectangular data set. Each column of a `DataFrame` is a `Series` object. This means that each column of a `DataFrame` must be comprised of data of the same type, but different columns can hold data of different types. This structure is extremely useful in practical data science. The invention of this structure was, in my opinion, transformative in making Python an effective data science tool.

The `DataFrame` can be created by importing data, as we saw in the previous section. It can also be created by a few methods within Python.

First, it can be created from a 2-dimensional `numpy` array.

```python
rng = np.random.RandomState(25)
d1 = pd.DataFrame(rng.normal(0,1, (4,5)))
d1
```

You will notice that it creates default column names, that are merely the column number, starting from 0. We can actually change the column names (which can be extracted and replaced with the `columns` attribute.

```python
d1.columns
```

```python
d1.columns = pd.Index(['V'+str(i) for i in range(1,6)]) # Index creates the right objects for both column names and row names, which can be extracted and changed with the `index` attribute
d1
```

**Exercise:** Can you explain what I did in the list comprehension above? The key points are understanding `str` and how I constructed the `range`.


You can also extract data from a homogeneous `DataFrame` to a `numpy` array

```python
d1.to_numpy()
```

The other easy way to create a `DataFrame` is from a `dict` object, where each component object is either a list or a numpy array, and is homogeneous in type. One exception is if a component is of size 1; then it is repeated to meet the needs of the `DataFrame`'s dimensions

```python
df = pd.DataFrame({
    'A':3.,
    'B':rng.random_sample(5),
    'C': pd.Timestamp('20200512'),
    'D': np.array([6] * 5),
    'E': pd.Categorical(['yes','no','no','yes','no']),
    'F': 'NIH'})
df
```

```python
df.info()
```

We note that C is a date object, E is a category object, and F is a text/string object. pandas has excellent time series capabilities (having origins in FinTech), and the `TimeStamp` function creates datetime objects which can be queried and manipulated in Python. We'll describe category data in the next section.

You can extract particular columns of a `DataFrame` by name

```python
df['E']
```

```python
df['B']
```

```python

```

### Categorical data

`pandas` provides a `Categorical` function and a `category` object type to Python. This type is analogous to the `factor` data type in R. It is meant to address categorical or discrete variables, where we need to use them in analyses. Categorical variables typically take on a small number of unique values, like gender, blood type, country of origin, race, etc. 

You can create categorical `Series` in a couple of ways:

```python
s = pd.Series(['a','b','c'], dtype='category')
```

```python
df['F'].astype('category')
```

You can also create `DataFrame`'s where each column is categorical

```python
df = pd.DataFrame({'A': list('abcd'), 'B': list('bdca')})
df_cat = df.astype('category')
df_cat.dtypes
```

You can explore categorical data in a variety of ways

```python
df_cat['A'].describe()
```

```python
df['A'].value_counts()
```

One issue with categories is that, if a particular level of a category is not seen before, it can create an error. So you can pre-specify the categories you expect

```python
df_cat['B'] = pd.Categorical(list('aabb'), categories = ['a','b','c','d'])
df_cat['B'].value_counts()
```

### Missing data

Both `numpy` and `pandas` allow for missing values, which are a reality in data science. The missing values are coded as `np.nan`. Let's create some data and force some missing values

```python
df = pd.DataFrame(np.random.randn(5, 3), index = ['a','c','e', 'f','g'], columns = ['one','two','three']) # pre-specify index and column names
df['four'] = 20 # add a column named "four", which will all be 20
df['five'] = df['one'] > 0
df
```

```python
df2 = df.reindex(['a','b','c','d','e','f','g'])
df2
```

The code above is creating new blank rows based on the new index values, some of which are present in the existing data and some of which are missing

```python
df2.isna()
```

```python
df2['one'].notna()
```

Getting complete data

```python
df2.dropna(how='any')
```

Filling missing values

```python
df2.fillna(value = 5)
```

Fill with the column mean

```python
df3 = df2.copy()
df3 = df3.select_dtypes(exclude=[object])   # remove non-numeric columns
df3.fillna(df3.mean())  # df3.mean() computes column-wise means
```

## Data transformation

### Arithmetic operations

If you have a `Series` or `DataFrame` that is all numeric, you can add or multiply single numbers to all the elements together.

```python
A = pd.DataFrame(np.random.randn(4,5))
print(A)
```

```python
print(A + 6)
```

```python
print(A * -10)
```

If you have two compatible (same dimension) numeric `DataFrame`s, you can add, subtract, multiply and divide elementwise

```python
B = pd.DataFrame(np.random.randn(4,5) + 4)
print(A + B)
```

```python
print(A * B)
```

If you have a `Series` with the same number of elements as the number of columns of a `DataFrame`, you can do arithmetic operations, with each element of the `Series` acting upon each column of the `DataFrame`

```python
c = pd.Series([1,2,3,4,5])
print(A + c)
```

```python
print(A * c)
```
### Extracting rows and columns

There are two extractor functions in `pandas`:

+ `loc` extracts by label (index label, column label, slice of labels, etc.
+ `iloc` extracts by index (integers, slice objects, etc.


```python
df2.loc['a',:]
```

```python
df2.loc[:, 'three'] # or df['three']
```

```python
df2.loc['a':'c']
```

> Note, in pandas, this slice selector includes the smallest **and largest** index, unlike in other Python and `numpy` uses, where the largest index is omitted

```python
df2.iloc[0:2, :]
```

To add to the confusion, the normal slicing rules apply when we use indices rather than labels.

```python
df2.iloc[0:2, 1:4]
```

```python
df2.loc['a':'b', 'two':'four']
```

As a convenience, if you just use a slice by numbers in a `DataFrame`, it will slice the rows

```python
df2[:3]
```

In contrast, if you supply a single label, it will extract the column!!

```python
df2['two']
```

#### Boolean selection

```python
df2[df2['one'] > 0]
```

```python
df2[(df2['one'] > 0) & (df2['three'] < 0)]
```

#### `query`

`DataFrame`'s have a `query` method allowing selection using a Python expression

```python
n = 10
df = pd.DataFrame(np.random.rand(n, 3), columns = list('abc'))
df
```

```python
df[(df['a'] < df['b']) & (df['b'] < df['c'])]
```

```python
df.query('(a < b) & (b < c)')
```

### Concatenation of data sets

Let's create some example data sets

```python
df1 = pd.DataFrame({'A': ['a'+str(i) for i in range(4)],
    'B': ['b'+str(i) for i in range(4)],
    'C': ['c'+str(i) for i in range(4)],
    'D': ['d'+str(i) for i in range(4)]})

df2 =  pd.DataFrame({'A': ['a'+str(i) for i in range(4,8)],
    'B': ['b'+str(i) for i in range(4,8)],
    'C': ['c'+str(i) for i in range(4,8)],
    'D': ['d'+str(i) for i in range(4,8)]})
df3 =  pd.DataFrame({'A': ['a'+str(i) for i in range(8,12)],
    'B': ['b'+str(i) for i in range(8,12)],
    'C': ['c'+str(i) for i in range(8,12)],
    'D': ['d'+str(i) for i in range(8,12)]})
```

We can concatenate these `DataFrame` objects by row

```python
row_concatenate = pd.concat([df1, df2, df3])
print(row_concatenate)
```

This stacks the dataframes together. They are literally stacked, as is evidenced by the index values being repeated. 

```python
row_concatenate.iloc[3,:]
```

**Exercise:** What happens if you replace `iloc` with `loc`?


This same exercise can be done by the `append` function

```python
df1.append(df2).append(df3)
```

Suppose we want to append a new row to `df1`. Lets create a new row.

```python
new_row = pd.Series(['n1','n2','n3','n4'])
pd.concat([df1, new_row])
```

That's a lot of missing values. The issue is that the we don't have column names in the `new_row`, and the indices are the same, so pandas tries to append it my making a new column. The solution is to make it a `DataFrame`.

```python
new_row = pd.DataFrame([['n1','n2','n3','n4']], columns = ['A','B','C','D'])
print(new_row)
```

```python
pd.concat([df1, new_row])
```

or

```python
df1.append(new_row)
```

#### Adding columns

```python
pd.concat([df1,df2,df3], axis = 1)
```

The option `axis=1` ensures that concatenation happens by columns. The default value `axis = 0` concatenates by rows.


Let's play a little game. Let's change the column names of `df2` and `df3` so they are not the same as `df1`.

```python
df2.columns = ['E','F','G','H']
df3.columns = ['A','D','F','H']
pd.concat([df1,df2,df3])
```

Now pandas ensures that all column names are represented in the new data frame, but with missing values where the row indices and column indices are mismatched. Some of this can be avoided by only joining on common columns. This is done using the `join` option ir `concat`. The default value is 'outer`, which is what you see. above

```python
pd.concat([df1, df3], join = 'inner')
```

You can do the same thing when joining by rows, using `axis = 1` and `join="inner"` to only join on rows with matching indices. Reminder that the indices are just labels and happen to be the row numbers by default. 


### Merging data sets


For this section we'll use a set of data from a survey, also used by Daniel Chen in "Pandas for Everyone"

```python
person = pd.read_csv('data/survey_person.csv')
site = pd.read_csv('data/survey_site.csv')
survey = pd.read_csv('data/survey_survey.csv')
visited = pd.read_csv('data/survey_visited.csv')
```

```python
print(person)
```

```python
print(site)
```

```python
print(survey)
```

```python
print(visited)
```

There are basically four kinds of joins:

| pandas | R          | SQL         | Description                     |
| ------ | ---------- | ----------- | ------------------------------- |
| left   | left_join  | left outer  | keep all rows on left           |
| right  | right_join | right outer | keep all rows on right          |
| outer  | outer_join | full outer  | keep all rows from both         |
| inner  | inner_join | inner       | keep only rows with common keys |


![](graphs/joins.png)

The terms `left` and `right` refer to which data set you call first and second respectively. 

We start with an left join


```python
s2v_merge = survey.merge(visited, left_on = 'taken',right_on = 'ident', how = 'left')
```

```python
print(s2v_merge)
```

Here, the left dataset is `survey` and the right one is `visited`. Since we're doing a left join, we keed all the rows from `survey` and add columns from `visited`, matching on the common key, called "taken" in one dataset and "ident" in the other. Note that the rows of `visited` are repeated as needed to line up with all the rows with common "taken" values. 

We can now add location information, where the common key is the site code

```python
s2v2loc_merge = s2v_merge.merge(site, how = 'left', left_on = 'site', right_on = 'name')
print(s2v2loc_merge)
```

Lastly, we add the person information to this dataset.

```python
merged = s2v2loc_merge.merge(person, how = 'left', left_on = 'person', right_on = 'ident')
print(merged.head())
```

You can merge based on multiple columns as long as they match up. 

```python
ps = person.merge(survey, left_on = 'ident', right_on = 'person')
vs = visited.merge(survey, left_on = 'ident', right_on = 'taken')
print(ps)
```

```python
print(vs)
```

```python
ps_vs = ps.merge(vs, 
                left_on = ['ident','taken', 'quant','reading'],
                right_on = ['person','ident','quant','reading']) # The keys need to correspond
ps_vs.head()
```

Note that since there are common column names, the merge appends `_x` and `_y` to denote which column came from the left and right, respectively.



### Tidy data principles and reshaping datasets

The tidy data principle is a principle espoused by Dr. Hadley Wickham, one of the foremost R developers. [Tidy data](http://vita.had.co.nz/papers/tidy-data.pdf) is a structure for datasets to make them more easily analyzed on computers. The basic principles are

+ Each row is an observation
+ Each column is a variable
+ Each type of observational unit forms a table

> Tidy data is tidy in one way. Untidy data can be untidy in many ways

Let's look at some examples.

```python
from glob import glob
filenames = sorted(glob('data/table*.csv')) # find files matching pattern. I know there are 6 of them
table1, table2, table3, table4a, table4b, table5 = [pd.read_csv(f) for f in filenames] # Use a list comprehension
```

This code imports data from 5 files matching a pattern. Python allows multiple assignments on the left of the `=`, and as each dataset is imported, it gets assigned in order to the variables on the left. 

The following tables refer to the number of TB cases and population in Afghanistan, Brazil and China in 1999 and 2000

```python
print(table1)
```

```python
print(table2)
```
```python
print(table3)
```

```python
print(table4a) # cases
```

```python
print(table4b) # population
```

```python
print(table5)
```

**Exercise:** Describe why and why not each of these datasets are tidy.


### Melting (unpivoting) data

Melting is the operation of collapsing multiple columns into 2 columns, where one column is formed by the old column names, and the other by the corresponding values. Some columns may be kept fixed and their data are repeated to maintain the interrelationships between the variables.

![gather](graphs/gather.png )

We'll start with loading some data on income and religion in the US from the Pew Research Center.

```python
pew = pd.read_csv('data/pew.csv')
print(pew.head())
```

This dataset is considered in "wide" format. There are several issues with it, including the fact that column headers have data. Those column headers are income groups, that should be a column by tidy principles. Our job is to turn this dataset into "long" format with a column for income group. 

We will use the function `melt` to achieve this. This takes a few parameters:

+ **id_vars** is a list of variables that will remain as is
+ **value_vars** is a list of column nmaes that we will melt (or unpivot). By default, it will melt all columns not mentioned in id_vars
+ **var_name** is a string giving the name of the new column created by the headers (default: `variable`)
+ **value_name** is a string giving the name of the new column created by the values (default: `value`)


```python
pew_long = pew.melt(id_vars = ['religion'], var_name = 'income_group', value_name = 'count')
print(pew_long.head())
```

### Separating columns containing multiple variables

We will use an Ebola dataset to illustrate this principle

```python
ebola = pd.read_csv('data/country_timeseries.csv')
print(ebola.head())
```

Note that for each country we have two columns -- one for cases (number infected) and one for deaths. Ideally we want one column for country, one for cases and one for deaths. 

The first step will be to melt this data sets so that the column headers in question from a column and the corresponding data forms a second column.

```python
ebola_long = ebola.melt(id_vars = ['Date','Day'])
print(ebola_long.head())
```

We now need to split the data in the `variable` column to make two columns. One will contain the country name and the other either Cases or Deaths. We will use some string manipulation functions that we will see later to achieve this.

```python
variable_split = ebola_long['variable'].str.split('_', expand=True) # split on the `_` character
print(variable_split[:5])
```

The `expand=True` option forces the creation of an `DataFrame` rather than a list

```python
type(variable_split)
```

We can now concatenate this to the original data

```python
variable_split.columns = ['status','country']

ebola_parsed = pd.concat([ebola_long, variable_split], axis = 1)

ebola_parsed.drop('variable', axis = 1, inplace=True) # Remove the column named "variable" and replace the old data with the new one in the same location

print(ebola_parsed.head())
```

### Pivot/spread datasets

![spread](graphs/spread.png )

If we wanted to, we could also make two columns based on cases and deaths, so for each country and date you could easily read off the cases and deaths. This is achieved using the `pivot_table` function.

```python
ebola_parsed.pivot_table(index = ['Date','Day', 'country'], columns = 'status', values = 'value')
```

This creates something called `MultiIndex` in the `pandas` `DataFrame`. This is useful in some advanced cases, but here, we just want a normal `DataFrame` back. We can achieve that by using the `reset_index` function.

```python
ebola_parsed.pivot_table(index = ['Date','Day','country'], columns = 'status', values = 'value').reset_index()
```

In the `pivot_table` syntax, `index` refers to the columns we don't want to change, `columns` refers to the column whose values will form the column names of the new columns, and `values` is the name of the column that will form the values in the pivoted dataset. 

Pivoting is a 2-column to many-column operation, with the number of columns formed depending on the number of unique values present in the column of the original data that is entered into the `columns` argument of `pivot_table`


**Exercise:** Load the file `weather.csv` into Python and work on making it a tidy dataset. It requires melting and pivoting. The dataset comprises of the maximun and minimum temperatures recorded each day in 2010. There are lots of missing value. Ultimately we want columns for days of the month, maximum temperature and minimum tempearture along with the location ID, the year and the month.


## Data aggregation and split-apply-combine

We'll use the Gapminder dataset for this section

```python
df = pd.read_csv('data/gapminder.tsv', sep = '\t') # data is tab-separated, so we use `\t` to specify that
```
The paradigm we will be exploring is often called *split-apply-combine* or MapReduce or grouped aggregation. The basic idea is that you split a data set up by some feature, apply a recipe to each piece, compute the result, and then put the results back together into a dataset. This can be described in teh following schematic.


![](graphs/split-apply-combine.png)


`pandas` is set up for this. It features the `groupby` function that allows the "split" part of the operation. We can then apply a function to each part and put it back together. Let's see how.

```python
df.head()
```

```python
f"This dataset has {len(df['country'].unique())} countries in it"
```

One of the variables in this dataset is life expectancy at birth, `lifeExp`. Suppose we want to find the average life expectancy of each country over the period of study.

```python
df.groupby('country')['lifeExp'].mean()
```

So what's going on here? First, we use the `groupby` function, telling `pandas` to split the dataset up by values of the column `country`.

```python
df.groupby('country')
```

`pandas` won't show you the actual data, but will tell you that it is a grouped dataframe object. This means that each element of this object is a `DataFrame` with data from one country.

```python
df.groupby('country').ngroups
```

```python
df.groupby('country').get_group('United Kingdom')
```

```python
type(df.groupby('country').get_group('United Kingdom'))
```

```python
avg_lifeexp_country = df.groupby('country')['lifeExp'].mean()
avg_lifeexp_country['United Kingdom']
```

```python
df.groupby('country').get_group('United Kingdom')['lifeExp'].mean()
```

Let's look at if life expectancy has gone up over time, by continent

```python
df.groupby(['continent','year'])['lifeExp'].mean()
```

```python
avg_lifeexp_continent_yr = df.groupby(['continent','year'])['lifeExp'].mean().reset_index()
avg_lifeexp_continent_yr
```

```python
type(avg_lifeexp_continent_yr)
```

The aggregation function, in this case `mean`, does both the "apply" and "combine" parts of the process.


We can do quick aggregations with `pandas`

```python
df.groupby('continent')['lifeExp'].describe()
```

```python
df.groupby('continent').nth(10)
```

You can also use functions from other modules, or your own functions in this aggregation work.

```python
df.groupby('continent')['lifeExp'].agg(np.mean)
```

```python
def my_mean(values):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    return(sum/n)

df.groupby('continent')['lifeExp'].agg(my_mean)
```

You can do many functions at once

```python
df.groupby('year')['lifeExp'].agg([np.count_nonzero, np.mean, np.std])
```

You can also aggregate on different columns at the same time by passing a `dict` to the `agg` function

```python
df.groupby('year').agg({'lifeExp': np.mean,'pop': np.median,'gdpPercap': np.median})
```

#### Transformation


You can do grouped transformations using this same method. We will compute the z-score for each year, i.e. we will substract the average life expectancy and divide by the standard deviation

```python
def my_zscore(values):
    m = np.mean(values)
    s = np.std(values)
    return((values - m)/s)

```

```python
df.groupby('year')['lifeExp'].transform(my_zscore)
```

```python
df['lifeExp_z'] = df.groupby('year')['lifeExp'].transform(my_zscore)
```

```python
df.groupby('year')['lifeExp_z'].mean()
```

#### Filter


We can split the dataset by values of one variable, and filter out those splits that fail some criterion. The following code only keeps countries with a population of at least 10 million at some point during the study period

```python
 df.groupby('country').filter(lambda d: d['pop'].max() > 10000000)

```
