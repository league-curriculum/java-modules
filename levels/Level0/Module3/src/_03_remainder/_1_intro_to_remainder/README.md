

# Introduction to Remainder

The remainder operator is represented as the percent sign %. This just means the remainder after division. You may also hear this be called modulo.
A common use for remainder is to test if a number is odd or even.
To do this test, you divide the number by 2.
If the remainder is zero, the number is even, but if the remainder is one, the number is odd. In code this would look like this:
```
int number = new Random().nextInt(100);
 if (number % 2 == 0) {
     System.out.println("number is even");
 }
 else {
     System.out.println("number is odd");
 }
```
Another use for remainder could be to track every 20 times a loop is executed, as follows:
```
for (int i=1; i<=1000; i++) {
    // do some code
    if (i % 20 == 0){
        System.out.println("20 more repeats completed");
    }
}
```

## Eclipse Recipes

FizzBuzz

## Processing Recipes

Bullseye
Bumble Bee


