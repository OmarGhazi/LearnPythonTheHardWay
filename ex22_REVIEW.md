**Ex 01: A Good First Program**
- `print()` Display text in console


**Ex 02: Comments And Pound Characters**
 - `#` Used to place comments throughout the code to help explain it further to readers

**Ex 03: Numbers And Math**
 - `+` plus
 - `-` minus
 - `/` slash
 - `*` asterisk
 - `%` percent
 - `<` less-than
 - `>` greater-than
 - `<=` less-than-equal
 - `>=` greater-than-equal
 - Learned about `%` modulo operation that calculates the remainder after division between two numbers

**Ex4: Variables And Names**
 - `_` in variable names is used a lot to put imaginary space between words
 - `floating point` are numbers with decimals
 - `=` assigns the value on the right to a variable on the left
 - `==` tests whether two things have the same value

**Ex5: More Variables And Printing**
 - `print(f...)` format string.
 - `{}` used inside of `print(f...)` to call out variables
 - The `f` before the `"` and the `{}` characters tells Python 3 "Hey, this string needs to be formatted. Put these variables in there"
 - `round()` lets you round floating point number

**Ex6: Strings And Text**
 - `.format()` can be used to format strings as well
 -
   ```
    hilarious = False
    joke_evaluation = "Isn't that joke so funny?! {}"
    print(joke_evaluation.format(hilarious))
    w = "This is the left side of..."
    e = "a string with a right side."
    print(w + e)
   ```

 - This is another way to define variables within a string. In line 2 we are creating a joke_evaluation variable and passing an undefined f string variable  and in line 4 we are printing joke_evaluation but passing the hilarious variable as the f string that goes inside of joke_evaluation

**Ex7: More Printing**

```
print(var1 + var2 + var3, var=' ' )
print(var4 + var5 + var6)
```

prints the variables next to each other with a space before continuing with concatenating the next set of variables. the `end=' '` at the end of each `print` line tells `print` to not end the line with a newline character and go to the next line

**Ex8: Printing, Printing**
 - You can use `formatter = "{} {} {} {}"` as a placeholder and then pass stings, numbers, or boolean using a print command
  -
  ``` print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
```

**Ex9: Printing, Printing, Printing**
 - `\n` creates a new line
 - `"""` lets you type sentences with return characters to form a paragraph

**Ex10: What Was That?**
 - `\` character encodes difficult-to-type characters into a string. These are various escape sequences for different characters that you may want to use in your string

 |Escape|What it does|
 |:----:|------------|
 |`\\`|Backslash (\\)|
 |`\'`|Single-quote (')|
 |`\"`|Double-quote (")|
 |`\a`|ASCII bell (BEL)|
 |`\b`|ASCII backspace (BS)|
 |`\f`|ASCII formfeed (FF)|
 |`\n`|ASCII linefeed (LF)|
 |`\N{name}`|Character named name in the Unicode database (Unicode only)|
 |`\r`|Carriage Return (CR)|
 |`\t`|Horizontal tab (TAB)|
 |`\uxxxx`|Character with 16-bit hex value xxxx|
 |`\Uxxxxxxxx`|Character with 32-bit hex value xxxxxxxx|
 |`\v`|ASCII vertical tab (VT)|
 |`\ooo`|Character with octal value ooo|
 |`\xhh`|Character with hex value hh|

**Ex11: Asking Questions**

`input()` command allows you to gather input from the user and you can assign `input()` to a variable.

If however, you want to do math with the user entered data, you will need to pass the `input()` within an `int()` like `x=int(input())` which gets the number as a string from `input()` then converts it to an integer using `int()`.

**Ex12: Prompting People**

`y=input("Name? ")` promts the user with "Name?" and puts the result into a variable `y`

**Ex13: Parameters, Unpacking, Variables**

Passing variables to a script.

1. You import using `from sys import argv`. This is how you add features to script from Python feature set.

2. The `argv` is "argument variable", a standard name in programming that is found in a lot of other languages

3. `x, y, z = argv` "unpacks" `argv` rather than holding on to the passed arguments. The passed arguments to the script are passed to these variables before ` = argv`

4. `from sys import argv`  is saying import the `sys` module (or library)  

**Ex14: Prompting And Passing**

Using `input()` and `argv` together. Further study drills. Learned about Zork and Adventure games made using python

**Ex15: Reading Files**

`.open()` lets you open a designated Files

`.read()` says do your read command without any parameters

**Ex16: Reading And Writing Files**

`.close()` Closes the file. Like `File -> Save..` in your editor

`.read()` Reads the contents of the file. You can assign the result to a variable

`.readline()` Reads just one line of a text file

`.truncate()` Empties the file

`write('stuff')` Writes "stuff" to the file

`seek(0)` Moves the read/write location to the beginning of the file. **NOTE** the `seek()` function is dealing in *bytes*, not lines. The code `seek(0)` moves the file to the 0 byte of the file, not the first line.

You can also open file in different modes:

1. `'w'` is saying "open this file in 'write' mode,"

2. `'r'` is used for read mode

3. `'a'` is for append

**Ex17: More Files**

`from os.path imprt exists` is a handy way to check the existence of the file and returns True or False.

`len()` is a handy function that gets the length of the string that you pass to it then returns that as a number

**Ex18: Names, Variables, Code, Functions**

`def` is used to create a function

end the line with `:`

*Any lines that belong to the function has to be indented*

Example:

```
def print_one(yourname):
  print("Your name is: {yourname})
```

**Ex19: Functions And Variables**

* You can give a function numbers directly for its parameters
* You can also use variables and pass those variables to the function
* You can also do math that gets passed to the function
* You can also do a combination of the last two bullets

**Ex20: Functions And Files**

Each time you do `.seek(0)` you are moving to the start of the line. Each time you do `.readline()` you are reading a line from the file and moving the read head to the right after the `\n` that ends that line

**Ex21: Functions Can Return Something**

you can use return to return a value, string, or boolean when that function is invoked. For example:

```
def add (a,b):
  print(f"Adding {a} + {b}")
  return a + b
```

is a simple addition function that adds two numbers
