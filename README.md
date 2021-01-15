# overbond

I have made two csv files for sample inputs. I made this choice because data could be large and therefore it is easier to store data in csv format. 'Book1.csv' and 'Book2.csv' are the two csv files that I import in my code. Both the challenges have an additional output showing how the csv file looks like. For now, to make the calculations in the two challenges, the company just has to provide the appropriate csv file. The program can be changed in the future to directly accept input from the user. 

I chose python because I have not used Ruby before and they have a lot of similarities.
Ruby and Python are high-level scripting languages; their programs don't need to be compiled. Both languages are dynamically typed. They also support object-oriented programming (OOP) out of the box.

I kept the approach to the challenges really simple. For the first challenge, I looked for the government contract closest to a given coporate contract and calculated the yield spread. For the second challenge, I sorted all the government contracts according to their term years and then I looked for the range of government contracts (on the basis of term years) in which a given corporate contract lies. The reason for sort was to make it easier to find the range of government contract.

### Tests

I wrote 4 tests in total for the four different functions I made. Two tests simply check if the print statement prints properly and confirm that it matches the expected output. The other two tests are for helper functions.

### Instructions

To check the functionality of first challenge -
* Open command line
* Go to the directory where the files are cloned
* Run the command "python challenge1.py" for the first challenge and the command "python challenge2.py" for the second challenge
* To run the tests on these two challenges, Run the command "python -m unittest unit_tests.py".
