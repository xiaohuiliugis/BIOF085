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

# %% [markdown]
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
# Every time a code block starts, the previous line ends in a colon (:). The code block ends when the indentation ends. We'll go into these elements in a bit. 
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
# #### Some general rules on Python syntax
#
# 1. Comments are marked by `#`
# 2. A statement is terminated by the end of a line, or by a `;`. 
# 3. Indentation specifies blocks of code within particular structures. Whitespace at the beginning of lines matters. Typically you want to have 2 or 4 spaces to specify indentation, not a tab (\t) character. This can be set up in your IDE
# 4. Whitespace within lines does not matter, so you can use spaces liberally to make your code more readable
# 5. Parentheses (`()`) are for grouping pieces of code or for calling functions.
#
# There are several conventions about code styling including the one in [PEP8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names) (PEP = Python Enhancement Proposal) and one proposed by [Google](https://google.github.io/styleguide/pyguide.html#316-naming). We will typically be using lower case names, with words separated by underscores, in this workshop, basically following PEP8. Other conventions are of course allowed as long as they are within the basic rules stated above. 
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
# Floating point numbers can be entered either as decimals or in scientific notation

# %%
x = 0.0005
y = 5e-4
print(x == y)

# %% [markdown]
# You can also store integers in a variable. Integers are of course numbers, but can be stored more efficiently on your computer. They are stored as an *integer* type, called `int`

# %%
b = 23
type(b)

# %% [markdown]
# These are the two primary numerical data types in Python. There are some others that we don't use as often, called `long` (for *long integers*) and `complex` (for *complex numbers*)
#
# #### Operations on numbers
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

# %% [markdown]
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
# #### Operations
#
# Strings also have some "arithmetic" associated with it, which involves, essentially, concatenation and repetition. Let's start by considering two character variables that we've initialized. 

# %%
a = 'a'
b = 'b'

# %% [markdown]
# Then we get the following operations and results
#
# | Operation | Result  |
# | --------- | ------- |
# | a + b     | 'ab'    |
# | a * 5     | 'aaaaa' |
#
# We can also see if a particular character or character string is part of an exemplar string

# %%
last_name = 'Dasgupta'
'gup' in last_name

# %% [markdown]
# There are several *functions* that apply to strings, that we will look at throughout the workshop, and especially when we look at string manipulation.
#
# ### Truthiness
#
# Truthiness means evaluating the truth of a statement. This typically results in a Boolean object, which can take values `True` and `False`, but Python has several equivalent representations. The following values are considered the same as False:
#
# > `None`, `False`, zero (`0`, `0L`, `0.0`), any empty sequence (`[]`, `''`, `()`), and a few others
#
# All other values are considered True. Usually we'll denote truth by `True` and the number `1`. 
#
# #### Operations
#
# We will typically test for the truth of some comparisons. For example, if we have two numbers stored in `x` and `y`, then we can perform the following comparisons
#
# | Operation | Result                            |
# | --------- | --------------------------------- |
# | x < y     | x is strictly less than y         |
# | x <= y    | x is less than or equal to y      |
# | x == y    | x equals y (note, it's 2 = signs) |
# | x != y    | x is not equal to y               |
# | x > y     | x is strictly greater than y      |
# | x >= y    | x is greater or equal to y        |
#
# We can chain these comparisons using Boolean operations
#
# | Operation | Result                                   |
# | --------- | ---------------------------------------- |
# | x \| y    | Either x is true or y is true or both    |
# | x & y     | Both x and y are true                    |
# | not x     | if x is true, then false, and vice versa |
#
# For example, if we have a number stored in `x`, and want to find out if it is between 3 and 7, we could write

# %%
(x >= 3) & (x <= 7)
# %% [markdown]
#

# %% [markdown]
# #### A note about variables and types
#
# Some computer languages like C, C++ and Java require you to specify the type of data that will be held in a particular variable. For example, 
#
# ```c
# int x = 4;
# float y = 3.25;
# ```
#
# If you try later in the program to assign something of a different type to that variable, you will raise an error. For example, if I did, later in the program, `x = 3.95;`, that would be an error in C. 
#
# Python is **dynamically typed**, in that the same variable name can be assigned to different data types in different parts of the program, and the variable will simply be "overwritten". (This is not quite correct. What actually happens is that the variable name now "points" to a different part of the computer's memory where the new data is then stored in appropriate format). So the following is completely fine in Python:

# %%
x = 4                   # An int
x = 3.5                 # A float
x = "That's my mother"  # A str
x = True                # A bool
# %% [markdown]
#

# %% [markdown]
# ## Data structures in Python
#
# Python has several in-built data structures. We'll describe the three most used ones: 
#
# 1. Lists (`[]`)
# 2. Tuples (`()`)
# 3. Dictionaries or dicts (`{}`)
#
# Lists are baskets that can contain different kinds of things. They  are ordered, so that there is a first element, and a second element, and a last element, in order. However, the *kinds* of things in a single list doesn't have to be the same type. 
#
# Tuples are basically like lists, except that they are *immutable*, i.e., once they are created, individual values can't be changed. They are also ordered, so there is a first element, a second element and so on. 
#
# Dictionaries are **unordered** key-value pairs, which  are very fast for looking up things. They work almost like hash tables.  Dictionaries will be very useful to us as we progress towards the PyData stack. Elements need to be referred to by *key*, not by position.
#
# ### Lists

# %%
test_list = ['apple', 3, True, 'Harvey', 48205]
test_list

# %% [markdown]
# There are various operations we can do on lists. First, we can determine the length (or size) of the list

# %%
len(test_list)

# %% [markdown]
# The list is a catch-all, but we're usually interested in extracting elements from the list. This can be done by *position*, since lists are *ordered*. We can extract the 1^st^ element of the list using

# %%
test_list[0]

# %% [markdown]
# > Wait!! The index is 0? 
# >
# > Yup. Python is based deep underneath on the C language, where counting starts at 0. So the first element has index 0, second has index 1, and so on. So you need to be careful if you're used to counting from 1, or, if you're used to R, which does start counting at 1. 
#
# We can also extract a set of consecutive elements from a list, which is often convenient. The typical form is to write the index as `a:b`. The (somewhat confusing) rule is that `a:b` means that you start at index `a`, but continue until **before index `b`**. So the notation `2:5` means include elements with index 2, 3, and 4. 

# %%
test_list[2:5]

# %% [markdown]
# If you want to start at the beginning or go to the end, there is a shortcut notation. The same rule holds, though. `:3` does **not** include the element at index 3, but `2:` **does** include the element at index 2. 

# %%
test_list[:3]

# %%
test_list[2:]

# %% [markdown]
# The important thing here is if you provide an index `a:b`, then `a` is include but `b` __is not__.
#
# You can also count **backwards** from the end. The last element in a Python list has index `-1`. So

# %%
test_list[-1]

# %% [markdown]
# You can also use negative indices to denote sequences within the list, with the same indexing rule applying. Note that you count from the last element (-1) and go backwards. 

# %%
test_list[:-1]

# %%
test_list[-3:]

# %%
test_list[-3:-1]

# %% [markdown]
# You can also make a list of lists, or nested lists

# %%
test_nested_list = [[1,'a',2,'b'],[3,'c',4,'d']]
test_nested_list

# %% [markdown]
# This will come in useful when we talk about arrays and data frames.
#
# You can also check if something is in the list, i.e. is a member.

# %%
'Harvey' in test_list

# %% [markdown]
# ### Tuples

# %% [markdown]
# Tuples are like lists, except that once you create them, you can't change them. This is why tuples are great if you want to store fixed parameters or entities within your Python code, since they can't be over-written even by mistake. You can extract elements of a tuple, but you can't over-write them. This is called *immutable*. 

# %%
test_tuple = ('apple', 3, True, 'Harvey', 48205)

# %%
test_tuple[:3]

# %%
test_list[0] = 'pear'
test_list

# %% [markdown]
# See what happens in the next bit of code

# %%
test_tuple[0] = 'pear'
test_tuple

# %% [markdown]
# ### Dictionaries
#
# Dictionaries, or `dict`, are collections of key-value pairs. Each element is referred to by *key*, not by *index*. In a dictionary, the keys can be strings, numbers or tuples, but the values can be any Python object. So you could have a dictionary where one value is a string, another is a number and a third is a DataFrame (essentially a data set, using the pandas library). A simple example might be an entry in a list of contacts

# %%
contact = {
  "first_name": "Abhijit",
  "last_name": 'Dasgupta',
  "Age": 48,
  "address": "124 Main St",
  "Employed" : True
}

# %% [markdown]
# If you try to get the first name out using an index, you run into an error:

# %%
contact[0]

# %% [markdown]
# You need to extract it by key

# %%
contact['first_name']

# %% [markdown]
# A dictionary is mutable, so you can change the value of any particular element

# %%
contact['address'] = '123 Main St'
contact['Employed'] = False
contact

# %% [markdown]
# You can see all  the keys and values in a dictionary using extractor functions

# %%
contact.keys()

# %%
contact.values()

# %% [markdown]
# It turns out that dictionaries are really fast in terms of retrieving information, without having to count where an element it. So it is quite useful
#
# We'll see that dictionaries are also one way to easily create pandas DataFrame objects on the fly. 
#
# ## Operational structures in Python
#
# ### Loops and list comprehensions
#
# Loops are a basic construct in computer programming. The basic idea is that you have a recipe that you want to repeatedly run on different entities that you have created. The crude option would be to copy and paste your code several times, changing whatever inputs change across the entities. This is not only error-prone, but inefficient given that loops are a standard element of all programming languages.
#
#  You can create a list of these entities, and, using a loop, run your recipe on each entity automatically. For example, you have a data about votes in the presidential election from all 50 states, and you want to figure out what the percent voting for each major party is. So you could write this recipe in pseudocode as 
#
# ```pseudocode
# Start with a list of datasets, one for each state
# for each state
#     compute and store fraction of votes that are Republican
#     compute and store fraction of votes that are Democratic
# ```
#
# This is just English, but it can be translated easily into actual code. We'll attempt that at the end of this section.
#
# The basic idea of a list is that there is a list of things you want to iterate over. You create a dummy variable as stand-in for each element of that list. Then you create a for-loop. This works like a conveyor belt and basket, so to speak. You line up elements of the list on the conveyor belt, and as you run the loop, one element of the list is "scooped up" and processed. Once that processing is done, the next element is "scooped up", and so forth. The dummy variable is essentially the basket (so the same basket (variable name) is re-used over and over until the conveyor belt (list) is empty). 
#
# In the examples below, we are showing a common use of for loops where we are enumerating the elements of a list as 0, 1, 2, ... using `range(len(test_list))`. So the dummy variable `i` takes values 0, 1, 2, ... until the length of the list is reached. For each value of `i`, this for loop prints the i^th^ element of `test_list`. 

# %%
for i in range(len(test_list)):
    print(test_list[i])

# %% [markdown]
# Sometimes using the index number is easier to understand. However, we don't need to do this. We can just send the list itself into the for-loop (`u`) now is the dummy variable containing the actual element of `test_list`. We'll get the same answer. 

# %%
for u in test_list:
    print(u)

# %% [markdown]
# > The general structure for a `for` loop is:
#
# >```python
# >for (element) in (list):
# >    	do some stuff
# >    	do more stuff
# >```

# %% [markdown]
# <img src='graphs/for_loop.png' height=500 width=500/>

# %% [markdown]
# As a more practical example, let's try and sum a set of numbers using a for-loop (we'll see much better ways of doing this later)
#

# %%
test_list2 = [1,2,3,4,5,6,7,8,9,10]
mysum = 0
for u in test_list2:
    mysum = mysum + u
print(mysum)


# %% [markdown]
# > There are two things to note here. 
# >
# > 1. The code `mysum = mysum + u` is perfectly valid, once you realize that this isn't really math but an assignment or pointer to a location in memory. This code says that you find the current value stored in `mysum`, add the value of `u` to it, and then store it back into the storage that `mysum` points to
# > 2. Indentation matters! Indent the last line and see what happens when you run this code
#

# %% [markdown]
# #### List comprehensions
#
# List comprehensions are quick ways of generating a list from another list by using some recipe. For example, if we wanted to create a list of the squares of all the numbers in `test_list2`, we could write

# %%
squares = [u ** 2 for u in test_list2]
squares

# %% [markdown]
# Similarly, if we wanted to find out what the types of each element of `test_tuple` is, we could use 

# %%
[type(u) for u in test_tuple]

# %% [markdown]
# **Exercise:** Can you use a list comprehension to find out the types of each element of the `contact` dict?
#
#
#
#
#
