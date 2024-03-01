
 # Array List
 Variables are used to hold a single value. For example:
 int age = 12; 
String name = “Sarah”;
 However, what if a program needed a list of names? We don't want to declare multiple variables with meaningless names like name1, name2, name3, etc.
Arrays allow us to store multiple values of the same type. E.g.
 String[] names = {"Sarah", "Joe","Ali", "Jose"};
String[] moreNames = new String[4];
 Unfortunately, we need to know exactly how many elements we are going to get before we can declare the array, which limits their use in our programs.


  This is where ArrayList comes in handy. 

ArrayLists grow and shrink according to how many elements are currently stored in them, i.e. they are "dynamic". In addition, you can add a mixture of object types in a single ArrayList.
 ArrayList namesList = new ArrayList();
    namesList.add("Sarah");
	namesList.add(10);
	namesList.add(3.14);
 However, if you want to limit an ArrayList to a specific type of object, you can declare its type when you create it:
 ArrayList&lt;String&gt; namesList = new ArrayList();
namesList.add("Sarah");
 Things to find out before you finish this module:
 How to create and inititialize an ArrayList
How to add and remove items from an ArrayList
How to loop through all the elements of an ArrayList (advantages and disadvantages of different types of loop)
Advantages and disadvantages of ArrayLists
 <div style="float: left; width: 50%;">
  ## Sample Program
  ArrayListDemo
 </div>
 <div style="float: left; width: 50%;">
  ## Student Recipes
  IntroToArrayList
        GuestBook
 </div>

