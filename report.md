# Report for assignment 3, Group 1

Assignment 3 is about code coverage and complexity.

Contributions from the members of Group 1 are:

- David Kaméus
    -
- Alexander Binett
    -
- Filippa Leuckfeld
    -
- Håvard Alstadheim
    -
- Carin Bystam
    -

## Project

Name: matplotlib

Source repo URL: https://github.com/matplotlib/matplotlib

Forked repo URL: https://github.com/filippaleuckfeld/matplotlib

matplotlib is a python library for creating plots and graphs easily.

## Onboarding experience

### Did it build and run as documented?

We had different experiences building the project and running the tests. The onboarding process was good for non mac users. For mac users we experienced some problems, for example that we had spaces in the file path to the project which was not documented as a problem. There were also some issues with downloading packages with the m1 processor.

## Complexity

1. What are your results for ten complex functions?


   * Did all methods (tools vs. manual count) get the same result?

        * Answer: No, the methods did not get the same result, lizard always had a higher complexty score than the manual calculation. The reason for this might be that lizard counts more decisions than we do by hand.

    * Are the results clear?

        * Answer: Yes, we get coherent results for the manual count. The ten most complex function can be seen below, from least to most complex. The manual counting was done on the lowest five.

            |Function | Manual count | Lizard |
            |---------|--------------|--------|
            |bar@_axes.py|M=31|34|
            |boxplot@_axes.py|M=32|35|
            |_to_rgba_no_colorcycle@colors.py|M=24|36|
            |hexbin@_axes.py|M=34|37|
            |_spectral_helper@mlab.py|M=37|39|
            |eventplot@_axes.py|-|39|
            |_make_image@image.py|-|40|
            |errorbar@_axes.py|-|48|
            |\_\_init\_\_@legend.py|-|59|
            |hist@_axes.py|-|77|

2. Are the functions just complex, or also long?

    * Answer: Most of the functions are very long.

3. What is the purpose of the functions?

    * Answer:

        |Function | Purpose |
        |---------|---------|
        |bar@_axes.py|Make a bar plot.|
        |boxplot@_axes.py|Draw a box and whisker plot.|
        |_to_rgba_no_colorcycle@colors.py|Convert parameter to an RGBA color, with no support for color-cycle syntax.|
        |hexbin@_axes.py|Make a 2D hexagonal binning plot of points x, y.|
        |_spectral_helper@mlab.py|Private helper implementing the common parts between the psd, csd, spectrogram and complex, magnitude, angle, and phase spectrums.|
4. Are exceptions taken into account in the given measurements?

    * Answer: Yes we have taken exceptions into account.

5. Is the documentation clear w.r.t. all the possible outcomes?

    * Answer: It differs between the functions examined. Private helper functions are not thoroughly documented.

## Refactoring

### `_spectral_helper` in mlab.py

- Plan for refactoring:
    - `_spectral_helper` can be refactored such that the `result` and `freqs` return variables are determined in a separate function.
    This would require passing the `mode`, `pad_to`, `detrend_func`, `window`, `numfreqs`, `same_data`, `NFFT`, `scaling_factor` and `scale_by_freq` variables into the new function.

- Estimated impact of refactoring (lower CC, but other drawbacks?).
    - Doing this would move 12 decisions out of `_spectral_helper`, reducing the cyclomatic
    complexity substantially. However, since the `_spectral_helper` function is used quite
    frequently by other functions, another function call for each one might affect performance
    negatively.




### `boxplot` in _axes.py

- Two ideas for refactoring:

    1. The last two big if clauses (combined 26 rows) set values in the `bxpstats` dict based on the `usermedians` and `conf_intervals` parameters. These could be broken out into one or two separate functions.
    2. The `if sym is not None:` if clause contains several other branching points. Its purpose is to set the flierprops dict. This dict could be returned from a different function instead.

- Estimated impact
    - The main benefit of implementing these refactors would be lowering the CC count by a total of 16, and also reducing the number of lines of code in the function. One drawback of implementing either of these changes could be a slight performance loss due to passing (potentially somewhat large) dicts or other values to and from the added functions, but this can be mitigated by passing references instead of copies.

### `hexbin` in _axes.py

- For refactoring in hexbin, there are two ideas:
    1. The if clause that handles the C parameter is quite large, and contains 15 branches, which is almost 1/4 of all branches in hexbin. As it creates an array `accum` depending on the C parameter, it could be separated into its own function which returns the final `accum` array, and thus reduces the complexity of hexbin.
    2. There is also quite a large for-loop at the end which handles marginals and appends the info into an pre-initalized list `bars`. As it contains 8 branches, it could perhaps also be separated into its own function that returns an array `bars`.

- Estimated impact
    - Implementing these steps would decrease the CC of hexbin by 15. The resulting CC would then be 22 (going by Lizards results). The length of hexbin would reduce by around 60 lines, so while the function would still be long after the refactorings, it is perhaps a bit more manageable than its current length of 188 lines.
    As with boxplot, a drawback could be that it would be some performance loss due to sending potentially large arrays and other required values to the functions.


### `bar` in _axes.py

- For refactoring in bar:
    - There is a part of the function that does conversions on the x and y coordinates. This could instead be done in a separate function since it is just processing the input data for it to be used later.
    - There is a section of code where patches (objects with face and edge color) and errorbars are created. Having that section as a separate function would make sense since they are "building blocks" of the Bar container.

- Estimated impact:
    - Having a separate function for conversions of x and y coordinates would decrease the CC by 4. The solution of creating a function for patches and errorbars would decrease the CC by 12. After these two changes are made, the CC for the function would go from 31 to 15.

### `_to_rgba_no_colorcycle` in colors.py
- Ideas for refactoring:
    - Create helper functions for common operations. For example the format of the hex is checked several times using regular expression, this can be moved to seperate helper functions to make the code more readable.
    - Extract common code blocks to a separate function. There are four hex color formats that are checked in the function. The code that converts each hex color format to an RGBA tuple is very similar. You could extract this code to a separate function to avoid duplication.
    - Reformat the tests. The testing is very unstructured at the moment and could be rewritten in a simpler more readable way.

- Estimated impact:
    Implementing these ideas would reduce the cyclomatic complexity and reduce lines of code. Since there are many checks the code will also become more understandable and readable. One drawback could be a small performance loss since we need to call other functions, but this impact should be so small that we can disregard this.


Carried out refactoring (optional, P+):

git diff ...

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

- How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

    - An attempt was made to use `pytest-cov`, a plugin for pytest that matplotlib already uses. However, there doesn't seem to be a way to make it only do coverage for a single function, it uses files as atomic units. It also defaults to line coverage, not branch coverage, and its documentation and output are not particularly easy to interpret.
Integrating it with the environment was easy, it's already done. But integrating it with this assignment didn't seem possible.

### Your own coverage tool

DIY coverage implementation is modified source code, as can be seen in the [issue/17 branch](https://github.com/filippaleuckfeld/matplotlib/tree/issue/17).

- What kinds of constructs does your tool support, and how accurate is
its output?

    - This works by setting a flag for each branch that is reached in an execution of the function and writing this information to a file.
    The `accumulate_coverage.py` program then checks which flags have been set after all tests have been run.
    The tool supports if/else/while and for constructs, and those that can be rewritten as one of those, as long as the programmer can edit the execution branch to set the flag.
    The accuracy of the coverage tool is therefore dependent on the programmer's implementation of each flag being set. It also can't know if certain branches are unreachable unless the programmer takes this into account.

### Evaluation

1. How detailed is your coverage measurement?
    * It depends on the implementation of flags being set. It will count the number of flags set out of the defined branches, and tell you which flags are not set.

2. What are the limitations of your own tool?
    * It takes a long time to set up, and impacts the performance of the code, since it requires adding instructions that are not necessary to the code's intended purpose.
    * It also can't account for unreachable branches without the programmer telling it not to count those.
    * Since it uses relative paths to store files, tests that run in their own directories will not have their results counted unless they're manually moved to the correct files.

3. Are the results of your tool consistent with existing coverage tools?
    * TODO: use existing coverage tool other than `pytest-cov`

## Coverage improvement

Show the comments that describe the requirements for the coverage.

Report of old coverage: https://github.com/filippaleuckfeld/matplotlib/issues/17#issuecomment-1438609900

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

Current state according to the Essence standard can be seen in [essence.md](./essence.md)

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?
