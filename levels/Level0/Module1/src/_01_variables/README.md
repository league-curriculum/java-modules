
# What is a Variable?

- Variables are used to hold values in your Java program
- Before you can put a value into a variable you must declare, or create it. How?
  - First describe the "type" of information it will hold, for example:
    - String or int
  - Next give it a "meaningful" name or identifier, for example:
    - nameOfSchool or numberOfStudents
    
    ```java
    String nameOfSchool;
    Int numberOfStudents;
    ```

- Rules for naming variables
  - Start with a lowercase letter
  - Use camel case
  - Can include numbers and underscores, but not spaces or special characters
  - Should be meaningful, i.e. self-documenting
  - You declare a variable once, but you can use it many times in the code

## Using a Variable

After you have declared a variable, you need to give it a value before it can be useful to your program. The first time you put a value in a variable, is called "variable initialization". See example below:

```java
nameOfSchool = "Queen Mary";
numberOfStudents = 1000;
```

**Note:** The type of information you put into the variable must match the type you gave the variable when you declared it.

You can also initialize a variable in the same line of code that you declared it as follows:

```java
String nameOfSchool = "Queen Mary";
Int numberOfStudents = 1000;
```

If you try to use a variable that has no value, you might get an error like this:

```
Exception in thread "main" java.lang.NullPointerException
```
