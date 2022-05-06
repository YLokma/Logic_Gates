# Logic_Gates
*This is **Youssof Lokma** and **Eyad Mohamed**'s submission for the logic gates project on 24th of April 2022*

> Keda El Mfrood 4a8al dlwa2ty - Eyad Mohamed
>
> Garab keda - Youssof Lokma

## Project Description
This was inspired by **Cambridge's IGCSE Computer Science** Digital Logic chapter, we started on 24th of November 2021. The purpose of the project is to solve complex questions that otherwise we **can't trace manually**, so we used **Python**. the gates it can deal with are: (NOT, AND, OR, NAND, NOR, XOR)


## File Structure
* Table_Function: This contains a function that generates a truth table based on the number of inputs provided by the user, 3 by default
* Gates: Uses functional programming in order to call and define each gate since it is going to be used multiple times (NOT, AND, OR, NAND, NOR, XOR)
* Logic_Gates_int: This uses the user input as the number of inputs to solve any question involving any number of inputs and gates
    * Type of input used: Numbers only
* Logic_Gates_Str: This uses the 3 inputs as default to solve all common questions in the curriculum, it is limited by the alphabet and has a maximum of 9 gates. 
    * Type of input used: Normal text
## How To Use
**Python Version Requirement: 3.6+**

---
### General Use Instructions & Examples
If we want to solve this question:
```
X = ((NOT A) AND (B OR C))
```
* Using Logic_Gates_str:

![image](https://user-images.githubusercontent.com/94978677/165080197-d46b68fe-940e-4d6b-b4fe-febea23ec82b.png)

**Note: capitalization is not an issue**
* Using Logic_Gates_int:

![image](https://user-images.githubusercontent.com/94978677/165080636-fc92f7cc-d239-4e22-bad6-814fcfd6afeb.png)

**Note: spaces are not an issue as long as you are consistent during each input (small statement)**

### Windows
In order to run on windows you can use your favourite text editor or via the command-line via the command using CMD
```
python Logic_Gates_str.py
```
If number of inputs needed is other than 3:
```
python Logic_Gates_int.py
```
### Mac OS & Linux
The same applies like windows but the commands change like so (use any terminal you prefer):
```
python3 Logic_Gates_str.py
python3 Logic_Gates_int.py
```

## Testing
- [ ] Further testing
- [ ] Prettifying the CLI
- [ ] Using arguments and help messages in CLI
