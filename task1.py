"""Task 1
Define a global variable named settings as a dictionary with a key title that contains a string of your choice, then create a function named change_site_title that takes one argument of type String and assigns it to the key title in the global variable settings.

Use this test case:

print(settings)
change_site_title("A new fancy title")
print(settings)
Your result should look like this:
{'title': 'My original title'}
{'title': 'A new fancy title'}"""

from turtle import title

settings = {'title': 'my_choice'}
def change_site_title(*args):
    settings['title'] = args
    return settings
print(settings)
change_site_title("A new fancy title")
print(settings)