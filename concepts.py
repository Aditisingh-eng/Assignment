# For loop: It is used to iterate over a sequence (like a list, tuple, or string) or perform an action a specific number of times.
for i in range(5):
    print("For loop iteration:", i)

# While loop: It repeatedly executes a block of code as long as the given condition is true.
j = 0
while j < 5:
    print("While loop iteration:", j)
    j += 1

# Continue statement: When encountered within a loop, it immediately stops the current iteration and jumps to the next iteration.
for k in range(5):
    if k == 2:
        continue
    print("Continue example:", k)

# If-else statement: It allows you to execute different code blocks based on the condition provided. If the condition is true, the code inside the if block is executed; otherwise, the code inside the else block is executed.
num = 10
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Switch statement:: It allows you to perform different actions based on the value of a variable, but Python doesn't have a direct switch statement, however, it can be implemented using a dictionary)
def switch_example(day):
    switch_dict = {
        "Monday": "It's Monday!",
        "Tuesday": "It's Tuesday!",
    }
    print(switch_dict.get(day, "It's some other day."))

switch_example("Monday")

# Here's Switch Implementation in JavaScript

# function switchExample(day) {
#   switch (day) {
#     case "Monday":
#       console.log("It's Monday!");
#       break;
#     case "Tuesday":
#       console.log("It's Tuesday!");
#       break;
#     case "Wednesday":
#       console.log("It's Wednesday!");
#       break;
#     case "Thursday":
#       console.log("It's Thursday!");
#       break;
#     case "Friday":
#       console.log("It's Friday!");
#       break;
#     case "Saturday":
#       console.log("It's Saturday!");
#       break;
#     case "Sunday":
#       console.log("It's Sunday!");
#       break;
#     default:
#       console.log("It's some other day.");
#       break;
#   }
# }

# // Usage
# switchExample("Monday");   // Output: It's Monday!
# switchExample("Friday");   // Output: It's Friday!
# switchExample("Unknown");  // Output: It's some other day.


# -----------------------------------------------------------------------------------
# RECURSION 
# -----------------------------------------------------------------------------------

# Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller instances of the same problem. Here's an example of a recursive function to calculate the factorial of a non-negative integer:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Testing the factorial function
print("Factorial of 5 is:", factorial(5))  
print("Factorial of 0 is:", factorial(0))
print("Factorial of 1 is:", factorial(1))

# Outputs
# Factorial of 5 is: 120
# Factorial of 0 is: 1
# Factorial of 1 is: 1

# In the above example, the factorial function is defined recursively. When n is either 0 or 1, the base case is reached, and the function returns 1. Otherwise, the function calculates n * factorial(n - 1) by making a recursive call to factorial with the argument n - 1.
# To compute the factorial of 5, the function goes through the following steps:
# factorial(5) = 5 * factorial(4)
#              = 5 * (4 * factorial(3))
#              = 5 * (4 * (3 * factorial(2)))
#              = 5 * (4 * (3 * (2 * factorial(1))))
#              = 5 * (4 * (3 * (2 * 1)))
#              = 5 * (4 * (3 * 2))
#              = 5 * (4 * 6)
#              = 5 * 24
#              = 120




# -----------------------------------------------------------------------------------
# BINARY SEARCH TREE 
# -----------------------------------------------------------------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if not current_node.left:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if not current_node.right:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if not current_node or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

# Usage
bst = BinarySearchTree()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(25)
bst.insert(5)

# Searching for a value
result_node = bst.search(20)
if result_node:
    print("Found:", result_node.value)
else:
    print("Not Found")


# The TreeNode class represents each node in the tree, containing a value, and left and right child pointers. The BinarySearchTree class represents the entire tree and includes methods to insert elements and search for a specific value.
# The insert method inserts a new value into the tree while maintaining the BST property (left child < parent < right child). The _insert_recursive helper method is used to perform the insertion in a recursive manner.
# The search method searches for a given value in the tree and returns the corresponding node if found. The _search_recursive helper method is used for the recursive search.
# In the usage example, we insert some values into the BST and then search for the value 20. If the value is found, we print "Found" along with the value; otherwise, we print "Not Found."


# -----------------------------------------------------------------------------
# CLOSURE
# -----------------------------------------------------------------------------

# In Python, a closure is a function object that remembers values in the enclosing scope, even if they are not present in memory. Closures are created when a nested function references a value from its containing (enclosing) function. Here's a simple demonstration of a closure in Python:
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Create a closure
closure_example = outer_function(10)

# Use the closure to perform addition
result = closure_example(5)
print("Result:", result)  # Output: Result: 15

# In this example, we have an outer_function that takes a parameter x and returns an inner function called inner_function. The inner_function has access to the x parameter from its enclosing scope (the outer_function). This makes inner_function a closure.

# When we call outer_function(10), it returns inner_function, but with x set to 10. The returned function becomes the closure, and we store it in the variable closure_example.

# We can then use the closure to perform addition by calling closure_example(5). The closure remembers the value x as 10, so when we call closure_example(5), it adds 5 to the remembered value 10 and returns 15.

# The closure allows inner_function to access and "remember" the value of x even after outer_function has finished executing. This behavior is what makes closures a powerful feature in Python and other functional programming languages.

