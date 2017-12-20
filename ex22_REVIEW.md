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

If however, you want to do math with the user entered data, you will need to pass the `input()` within an `int()` like `x=int(input())` which gets the number as a string from `input()` then converts it to an integer using `int()`

**Ex12: Prompting People**

**Ex13: Parameters, Unpacking, Variables**

**Ex14: Prompting And Passing**

**Ex15: Reading Files**

**Ex16: Reading And Writing Files**

**Ex17: More Files**

**Ex18: Names, Variables, Code, Functions**

**Ex19: Functions And Variables**

**Ex20: Functions And Files**

**Ex21: Functions Can Return Something**
