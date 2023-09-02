


# Using Debugger for help, find and fix the errors in the following Python code:

semi_trucks = [
    'Peterbilt', 'Kenworth', 'Freightliner', 'Volvo', 'International', 
    'Mack', 'Western Star', 'Sterling', 'Autocar', 'Ford', 'GMC', 'Chevrolet', 
    'White', 'Dodge', 'Hino', 'Isuzu', 'Mitsubishi', 'Nissan', 'Toyota', 'Fuso', 
    'UD', 'Mitsubishi Fuso', 'Peterbilt', 'Kenworth', 'Freightliner', 'Volvo', 
    'International', 'Mack', 'Western Star', 'Sterling', 'Autocar', 'Ford', 
    'GMC', 'Chevrolet', 'White', 'Dodge', 'Hino', 'Isuzu', 'Mitsubishi', 'Nissan', 
    'Toyota', 'Fuso', 'UD', 'Mitsubishi Fuso']


# Now, I wanted to arrange the list in alphabetical order, but I forgot how to do it.
# list.(semi_trucks)
# print(semi_trucks)


# The Debugger has given me the solution to the problem.
list.sort(semi_trucks)
print(semi_trucks)
