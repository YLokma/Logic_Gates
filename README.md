# Logic_Gates

*This is **Youssof Lokma** and **Eyad Mohamed**'s submission for the logic gates project on 24th of April 2022*

## Project Description
This was inspired by **Cambridge's IGCSE Computer Science** Digital Logic chapter, we started on 24th of November 2021. The purpose of the project is to solve complex questions that otherwise we **can't trace manually**, so we used **Python**. the gates it can deal with are: (NOT, AND, OR, NAND, NOR, XOR)


## File Structure
* Main: This is the user's portal to use all files
* Logic_Gates_Main: This is the newer, faster user's portal, recommended for most users it removes all the repetition seen in older versions (it only depends on Functions & All_Outputs)
* Functions: Contains all functions required by other files
    * Statement Validation: this function validates the statement entered by the user and converts it to be useable
    * Numerical Input Validation: this function is used to make sure the input is a number in the accepted range
    * Gates: Uses functional programming in order to call and define each gate since it is going to be used multiple times (NOT, AND, OR, NAND, NOR, XOR)
    * Table_Function: this function generates a truth table based on the number of inputs provided by the user, 3 by default
* All_Outputs: Contains all input and output statements for a cleaner and simpler code
* Logic_Gates_int: This uses the user input as the number of inputs to solve any question involving any number of inputs and gates
    * Type of input used for points: numbers
    * Type of input used for gates: numbers
* Logic_Gates_mix: This combines the best of both worlds, it takes the user's input for the number of inputs and has no limit for the number of gates while being easy to understand
    * Type of input used for points: numbers
    * Type of input used for gates: text
* Logic_Gates_str: This uses the 3 inputs as default to solve all common questions in the curriculum, it is limited by the alphabet and has a maximum of 9 gates.
    * Type of input used for points: text
    * Type of input used for gates: text

# How To Use
**Download & install python from https://www.python.org/downloads/**

---
## General Use Instructions

1. Double click Logic_Gates_Main.py or Main.py
2. Choose your input method
3. Depending on the type you choose, you may need to enter the number of inputs
4. Enter the number of gates in the circuit and let's call the first inputs and the outputs of gates "Points"
5. Enter each small statement individually, each statement can have a maximum of 2 points joined by 1 gate
6. Voila! X is your circuit's output

## Here is an example
If we want to solve this question:
```
X = ((NOT A) AND (B OR C))
```
Here are the input methods, choose the one you prefer
### 1. Input using numbers only:
![image](https://user-images.githubusercontent.com/94978677/168430106-53faf932-b598-4e5c-a8f1-d30bc5cf25cb.png)

**Note: spaces are not an issue as long as you are consistent during each input**

### 2. Input using numbers and text

![image](https://user-images.githubusercontent.com/94978677/168430388-907c6064-1ebf-45a5-821b-07f1b1ccd9f0.png)


**Note: capitalization is not an issue, but spaces are required**

### 3. Input using text only:

![image](https://user-images.githubusercontent.com/94978677/168430308-845d1dc0-a9ae-4545-8111-49f72f2a4ebb.png)

**Note: capitalization is not an issue, but spaces are required**



### Windows
In order to run on windows you can use your favourite text editor or via the command-line via the command using CMD
```
python Logic_Gates_Main.py
```

### Mac OS & Linux
The same applies like windows but the commands change like so (use any terminal you prefer):
```
python3 Logic_Gates_Main.py
```

## Testing
- [ ] Further testing
- [ ] Prettifying the CLI
- [ ] Using arguments and help messages in CLI