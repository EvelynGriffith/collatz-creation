# Collatz Chains

## Evelyn Griffith

## Program Input and Output

### What is the output from running the following command?

`poetry run collatzcreator --minimum 1 --maximum 10 --display`

```🕵  Let's investigate the behavior of the Collatz sequence!

  The first input to try will be 1
  The last input to try will be 10

The inputs to the Collatz function:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

✨ What is the length of the Collatz chain before the function produces the value of 1?

📏 The length of the resulting Collatz chain:

[1, 2, 8, 3, 6, 9, 17, 4, 20, 7]

✨ What is the summary information about the length of the Collatz chain?

  The minimum length of a Collatz chain is: 1
  The maximum length of a Collatz chain is: 20
  The mean of the length of a Collatz chain is: 7.70
  The median of the length of a Collatz chain is: 6.50
  The standard deviation of the length of a Collatz chain is: 5.97

🤷 Can you find a pattern between the input number and the length of the Collatz chain?

📦 Check the file called 'graphs/collatz.pdf' to see a graph that visualizes the results!
```

### What is the output from running the following command?

`poetry run collatzcreator --minimum 1 --maximum 100 --display`

```🕵  Let's investigate the behavior of the Collatz sequence!

  The first input to try will be 1
  The last input to try will be 100

The inputs to the Collatz function:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,   
75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

✨ What is the length of the Collatz chain before the function produces the value of 1?

📏 The length of the resulting Collatz chain:

[1, 2, 8, 3, 6, 9, 17, 4, 20, 7, 15, 10, 10, 18, 18, 5, 13, 21, 21, 8, 8, 16, 16, 11, 24, 11, 112, 19, 19, 19, 107, 6, 27, 14, 14, 22, 22, 22, 35,
9, 110, 9, 30, 17, 17, 17, 105, 12, 25, 25, 25, 12, 12, 113, 113, 20, 33, 20, 33, 20, 20, 108, 108, 7, 28, 28, 28, 15, 15, 15, 103, 23, 116, 23,  
15, 23, 23, 36, 36, 10, 23, 111, 111, 10, 10, 31, 31, 18, 31, 18, 93, 18, 18, 106, 106, 13, 119, 26, 26, 26]

✨ What is the summary information about the length of the Collatz chain?

  The minimum length of a Collatz chain is: 1
  The maximum length of a Collatz chain is: 119
  The mean of the length of a Collatz chain is: 32.42
  The median of the length of a Collatz chain is: 20.00
  The standard deviation of the length of a Collatz chain is: 34.29

🤷 Can you find a pattern between the input number and the length of the Collatz chain?

📦 Check the file called 'graphs/collatz.pdf' to see a graph that visualizes the results!
```

## Source Code

### Describe in detail how the following source code works

#### Explain the source code statement `if number % 2 == 0:`

This piece of code is using the operator called the modular operator. What this operator is going to do, is it is going to take the remainder. This means that in this line, if the variable called `number` has a remainder of 0 when divided by two, it will follow on with the conditional logic. This particular phrase in python is usally used to check whether or not a number is even.

## Explain `number = number // 2`

This line in the code is going to take a variable called `number` and it will take the number and it will do the integer division of number divided by 2. This is also called "floor division" and it will also take the float value that can sometimes be found and round up or down to the appropriate value. This is very useful when working with floating point values that need to be changed into integers. It can allow the floating point value to be changed into and integer without the use of the use of a `round()`.

## Explain the meaning and purpose of the following two lines of source code

```numbers_internal = copy.deepcopy(numbers)
numbers_internal.sort()
```

This code is going to create a deepcopy of a list called numbers within a variable called `copy`. The `numbers_internal` varibale is going to hold this new list which has been copied to within a copy called `copy`. The `numbers_internal` variable in the next line when using `.sort()` is going to then take the numbers_internal variable and sort the internal data based on what's inside of it. This is really interesting because it is going to basically take the `numbers` variable
data and it will then copy and deepcopy that into the `numbers_internal` variable and then the `numbers_internal` variable will be sorted through the `.sort()` function. This is cool because we aren't really changing the values or data within the numbers variable we are just reformatting and copying it so that it is manipulated into the forma that we need it to be seen in. These kinds of loopholes in python are really interesting to me.

## Use one paragraph to explain the meaning of the following test case

```python
def test_collatz_input_three():
    """Ensure that input of the number 3 produces the sequence suggested by Stavely on page 92."""
    number = 3
    # create a generator function of all of the outputs
    collatz_output_generator = collatz.Collatz(number)
    # materialize a list from the generator function, which
    # will support multiple assertions on the list
    collatz_output_list = list(collatz_output_generator)
    # ensure that there are eight values in the list
    assert len(list(collatz_output_list)) == 8
    # confirm that the contents of the list are correct
    assert list(collatz_output_list) == [3, 10, 5, 16, 8, 4, 2, 1]
```

This is a test case for the function called `compute_collatz_chain`. It is going to first initialize the variable `number` to a value of 3. Then it is going to create a new variable called `collatz_output_generator` and run the collatz.Collatz() function over the variable number. Then the function will create a new variable called `collatz_output_list` which will create a new list of values that contains the values from the collatz_output_generator variable. This function will then move into assertions. It's saying that if the len of the list called `collatz_output_list` is 8, then the code is partially working. If the list called the `collatz_output_list` is equal to `[3, 10, 5, 16, 8, 4, 2, 1]`, then the function code is working completely correctly.

## Professional Development

### What was the greatest technical challenge that you faced and how did you overcome it?

I think the greatest technical challenge that I am facing over this lab is just understanding what the collatz function is and what it's uses are. I think this is something that I am going to have to continue looking into and working on throughout the semester either through further readings, or discussions with my peers and teachers.

### How did this assignment leverage Python source code from previous assignments?

This lab used a lot of code from previous assignmnts, specifically the code in the summarize.py file. I recognized a lot of funcitons that we used in previous assignments regarding finding the mean, meadian, mode, and standard deviations.

### What is one topic in the scope of this course that you would like to learn more about? Why?

I would really like the learn more about sets and how they work/how they can be used. I feel like the previous lab was the hardest one for me, and I would like the learn more about it so that I can become more comfortable with those concepts and coding practices.

## At your own option, do you have any other insights to share about this assignment?

I thought this lab was really interesting and I felt like I learned a lot about the Collatz functions even though I still feel a little bit murky on the subject. I liked that we were able to run a lot of different numbers and see the interesting changes in the minimum, maximum, mean, median, and standard deviations of the length. I thought this lab was cool! 