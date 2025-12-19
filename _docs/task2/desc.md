# Task 2: Data Processing

## What you'll learn
What data processing is and why it is important

## What you'll do
Meet your supervisor Liam, a software engineer at Quantium
Perform some data processing to reorganise the data into a format that you can work with

---

## Here is the background information on your task
In this task, you will become familiar with the art of data processing. Data processing is the esoteric practice of squishing data into a useful format. Data points themselves — raw quantities in isolation — are useless but become useful when arranged in thoughtful proximity with other data points. When done skilfully, a carefully organized corpus of data can be interrogated for useful information: answers to difficult questions, surprising insights which were initially hidden, and elusive trends which can quite literally be used to predict the future. There is an immense power buried in the sea of data collected with nonchalant regularity all around the world which can be harnessed if you choose to do so. The first step in the transmutation of data into information is a process affectionately referred to as “data processing”.

By way of illustration, Soul Foods has asked the question, “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?” Seems like a useful thing to know if you’re the one making those sorts of decisions. But all you have at your disposal are a few CSV files with a handful of seemingly random columns. Attempt to answer the question by simply looking at the available data. The answer isn’t very obvious, is it? Your task is to mould that raw material into something useful.

---

## Here is your task
1. Soul Foods has provided you with three CSV files, all of which are in the data folder of the starter repo you cloned in the last task. These CSV files contain transaction data for Soul Foods’s entire morsel line. Each row indicates the quantity of a given type of morsel sold in a given region at a given price on a given day. Take a moment to acquaint yourself with the data contained in each one of these files.
 
2. Next, we’ll go field by field and think about how we can use each one:
    - The first field, “product”, contains many different types of morsels. Soul Foods is only interested in Pink Morsels, so we can remove any row which contains another type of product.
    - Next come “quantity” and “price”. Since we’re interested in the total sales for a given day, these can be combined into a single field, “sales,” by multiplying them together.
    - The date field is useful as is and can remain untouched.
    - It would be nice to filter by region in the final visualisation, so we’ll also leave the region field untouched.
 
3. Your task is to use the above instructions to convert the three CSV files into a single formatted output file. Your output file should contain three fields:
    - Sales
    - Date
    - Region
 
When you are finished, commit and push your changes, then submit a link to your repo below!

