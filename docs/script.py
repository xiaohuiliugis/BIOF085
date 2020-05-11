# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # A Python Primer

# %% [markdown]
# ## Introduction
#
# Python is a popular, general purpose scripting language. The [TIOBE index](https://www.tiobe.com/tiobe-index/) ranks Python as the third most popular programming language after C and Java, while this recent article in IEEE Computer Society says
#
# > "Python can be used for web and desktop applications, GUI-based desktop applications, machine learning, data science, and network servers. The programming language enjoys immense community support and offers several open-source libraries, frameworks, and modules that make application development a cakewalk." ([Belani, 2020](https://www.computer.org/publications/tech-news/trends/programming-languages-you-should-learn-in-2020))
#
# ### Python is a modular language
#
# Python is not a monolithic language but is comprised of a base programming language and numerous modules or libraries that add functionality to the language. Several of these libraries are installed with Python. The Anaconda Python Distribution adds more libraries that are useful for data science. Some libraries we will use include `numpy`, `pandas`, `seaborn`, `statsmodels` and `scikit-learn`. In the course of this workshop we will learn how to use Python libraries in your workflow.
#
# ### Python is a scripting language
#
# Using Python requires typing!! You write *code* in Python that is then interpreted by the Python interpreter to make the computer implement your instructions. Your code is like a recipe that you write for the computer. Python is a *high-level language* in that the code is English-like and human-readable and understandable, which reduces the time needed for a person to create the recipe. It is a language in that it has nouns (*variables* or *objects*), verbs (*functions*) and a structure or grammar that allows the programmer to write recipes for different functionalities. 
#
# ## An example
#
# Let's consider the following piece of Python code:

# %%
# set a splitting point
split_point = 3

# make two empty lists
lower = []; upper = []

# Split numbers from 0 to 9 into two groups, one lower or equal to the split point and one higher than the split point
for i in range(10): # count from 0 to 9
  if (i <= split_point):
    lower.append(i)
  else: 
    upper.append(i)

print("lower:", lower)
print('upper:', upper)


# %% [markdown]
# First note that any line (or part of a line) starting with `#` is a **comment** in Python and is ignored by the interpreter. This makes it possible for us to write substantial text to remind us what each piece of our code does
#
# The first piece of code that the Python interpreter actually reads is 

# %%
split_point = 3

# %% [markdown]
# This takes the number 3 and stores it in the **variable** `split_point`. Variables are just names where some Python object is stored. It really works as an address to some particular part of your computer's memory, telling the Python interpreter to look for the value stored at that particular part of memory. Variable names allow your code to be human-readable since it allows you to write expressive names to remind yourself what you are storing. The rules of variable names are: 
#
# 1. Variable names must start with a letter or underscore
# 2. The rest of the name can have letters, numbers or underscores
# 3. Names are case-sensitive
#
# There are several conventions about variable naming, including the one in [PEP8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names) (PEP = Python Enhancement Proposal) and one proposed by [Google](https://google.github.io/styleguide/pyguide.html#316-naming). PEP8 suggests that all variable names should be lowercase, with words separated by underscores (`_`). Google allows for a bit more flexibility. There is no real rule apart from the three above, so you can make your own naming convention. The main point is that names should be, in some sense, self-evident to you so you don't end up scratching your head when you see it. 
#
# The next piece of code initializes two **lists**, named `lower` and `upper`. 

# %%
lower = []; upper = []

# %% [markdown]
# The semi-colon tells Python that, even though written on the same line, a particular instruction ends at the semi-colon, then another piece of instruction is written. 
#
# Lists are a catch-all data structure that can store different kinds of things, In this case we'll use them to store numbers. 
#
# The next piece of code is a **for-loop** or  a loop structure in Python. 

# %%
for i in range(10): # count from 0 to 9
  if (i <= split_point):
    lower.append(i)
  else: 
    upper.append(i)


# %% [markdown]
# It basically works like this:
#
# 1. State with the numbers 0-9 (this is achieved in `range(10)`)
# 2. Loop through each number, naming it `i` each time 
#     1. Computer programs allow you to over-write a variable with a new value
# 3. If the number currently stored in `i` is less than or equal to the value of `split_point`, i.e., 3 then add it to the list `lower`. Otherwise add it to the list `upper`
#
# Note the indentation in the code. **This is not by accident**. Python understands the extent of a particular block of code within a for-loop (or within a `if` statement) using the indentations. In this segment there are 3 code blocks:
#
# 1. The for-loop as a whole (1st indentation)
# 2. The `if` statement testing if the number is less than or equal to the split point, telling Python what to do if the test is true
# 3. The `else` statement stating what to do if the test in the `if` statement is false
#
# Every time a code block starts, the previous line ends in a colon (:). The code block ends when the indentation ends. 
#
# The last bit of code prints out the results

# %%
print("lower:", lower)
print('upper:', upper)

# %% [markdown]
# The `print` statement adds some text, and then prints out a representation of the object stored in the variable being printed. In this example, this is a list, and is printed as
#
# ```
# lower: [0, 1, 2, 3]
# upper: [4, 5, 6, 7, 8, 9]
# ```
#
# We will expand on these concepts in the next few sections. 
#
# ## Data types in Python
#
# We start with objects in Python. Objects can be of different types, including numbers (integers and floats), strings, arrays (vectors and matrices) and others. Any object can be assigned to a name, so that we can refer to the object in our code. We'll start with the basic types of objects.
#
# ### Numeric variables
#
# The following is a line of Python code, where we assign the value 1.2 to the variable `a`. 
#
# > The act of assigning a name is done using the `=` sign. This is not equality in the mathematical sense, and has some non-mathematical behavior, as we'll see

# %%
a = 1.2

# %% [markdown]
# This is an example of a *floating-point number* or a decimal number, which in Python is called a `float`. We can verify this in Python itself.

# %%
type(a)

# %% [markdown]
# You can also store integers in a variable. Integers are of course numbers, but can be stored more efficiently on your computer. They are stored as an *integer* type, called `int`

# %%
b = 23
type(b)

# %% [markdown]
# These are the two primary numerical data types in Python. There are some others that we don't use as often, called `long` (for *long integers*) and `complex` (for *complex numbers*)
#
# ### Strings
#
# Strings are how text is represented within Python. It is always represented as a quoted object using either single (`''`) or double (`""`) quotes, as long as the types of quotes are matched. For example:

# %%
first_name = "Abhijit"
last_name = 'Dasgupta'

# %% [markdown]
# The data type that these are stored in is `str`.

# %%
type(first_name)
# %% [markdown]
# ### Truthiness
#
# Truthiness means evaluating the truth of a statement. This typically results in a Boolean object, like `True` and `False`, but Python has several equivalent representations. The following values are considered the same as False:
#
# > `None`, `False`, zero (`0`, `0L`, `0.0`), any empty sequence (`[]`, `''`, `()`), and a few others
#
# All other values are considered True. Usually we'll denote truth by `True` and the number `1`. 
#
# ### Operating on elemental data types
#
# There is an arithmetic and logic available to operate on elemental data types. For example, we do have addition, subtraction , multiplication and division available. For example, for numbers, we can do the following:
#
# | Operation | Result                             |
# | --------- | ---------------------------------- |
# | x + y     | The sum of x and y                 |
# | x - y     | The difference of x and y          |
# | x * y     | The product of x and y             |
# | x / y     | The quotient of x and y            |
# | - x       | The negative of x                  |
# | abs(x)    | The absolute value of x            |
# | x ** y    | x raised to the power y            |
# | int(x)    | Convert a number to integer        |
# | float(x)  | Convert a number to floating point |
#
# Let's see some examples:

# %%
x = 5
y = 2
# %%
x + y
# %%
x - y
# %%
x * y
# %%
x / y
# %%
x ** y
# %% [markdown]
#
