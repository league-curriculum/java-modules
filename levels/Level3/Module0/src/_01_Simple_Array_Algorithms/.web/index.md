
 <div id="moduleIndex">
  # JUnit Tests
  When you have written a new program, you need to test if it is working properly. Also, if you need to make changes to an existing program, you need to make sure you haven't broken anything that worked before.
  When you develop new code, you sometimes add print statements to check what is happening, but after you have done that, you need to go back and remove the print statements and you might break something in the process. So how can you test a program without changing its code?
  JUnit provides us with a framework to test code "from the outside".
  For example, The code below runs the static method add() on the Algorithms class. This test is not part of the Algorithms class, but an external testing class, and checks that when given the numbers 3 and 1, the add method returns the number 4.
  @Test
	public void testAdd() {
     assertEquals(4, Algorithms.add(3,1));
	}
  If a programmer later changes other parts of the Algorithms class for any reason, they can re-run this test to see if the add() method still works correctly.
  You can use a variety of assertions that allow the program to test for different conditions. In the above example, the code is testing for the equals condition.  Ask your teacher, or search the Internet for a complete overview of the JUnit class and its capabilities.
 </div>

