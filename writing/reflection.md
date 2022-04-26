# Collatz Chains

TODO: Make sure that you delete all of the TODO markers and rephrase all
of the prompts inside of this file. When you are finished working on
this technical writing it should contain polished content without any
mistakes in Markdown syntax, spelling, or grammar.

## Add Your Name Here

## Program Input and Output

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run collatzcreator --minimum 1 --maximum 10 --display`

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run collatzcreator --minimum 1 --maximum 100 --display`

TODO: Although it is not absolutely required, try to run your program
with the largest input value specified in the project description on the
Project Euler web site. If you can get your program to produce the
correct output, then include the output of the program in that
configuration in an additional fenced code block.

## Source Code

### Describe in detail how the following source code works

#### Explain the source code statement `if number % 2 == 0:`

TODO: Use one paragraph to explain the aforementioned source code statement

## Explain `number = number // 2`

TODO: Use one paragraph to explain the aforementioned source code statement

## Explain the meaning and purpose of the following two lines of source code

```
numbers_internal = copy.deepcopy(numbers)
numbers_internal.sort()
```

TODO: Use one paragraph to explain the aforementioned source code segment

## Use one paragraph to explain the meaning of the following test case

```
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

TODO: Use one paragraph to explain the aforementioned source code segment

## Professional Development

### What was the greatest technical challenge that you faced and how did you overcome it?

TODO: Provide a one paragraph response to this question

### How did this assignment leverage Python source code from previous assignments?

TODO: Provide a one paragraph response to this question

### What is one topic in the scope of this course that you would like to learn more about? Why?

TODO: Provide a one paragraph response to this question

## At your own option, do you have any other insights to share about this assignment?

TODO: Provide a one paragraph response to this question
