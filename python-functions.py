# Create a Simple Greeting Function
def greet_user():
    print('Welcome to Python programming!')

greet_user()

# Function with Parameters
def display_full_name(first_name, last_name):
    print(f'Hello {first_name} {last_name}, nice to meet you!')

display_full_name("Data", "Epic")

# Funtion that Returns a Value
def add_number(a, b):
    return a + b

sum = add_number(10, 5)
print(f'The sum is: {sum}')

# Function That Uses a Global Variable
school_name = 'Data Epic Mentorship'

def print_school():
    print(f'Learning python at the {school_name} program')

    group = 'Beginner'
    print(f'Learning python at the {school_name} program as a {group}')

print_school()
