"""Task 2
Keep the previous code and define now a global variable named default_settings as a dictionary with a key title, then create a function named get_title that takes one argument as a dictionary that defaults to default_settings and returns the content of the key title in the given dictionary.

Use this test case:

print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())
Your result should look like this:
My original title
My original title
A new fancy title
My original title"""



settings = {"title":"dr strange"}

def change_site_title( new_name =""):
    settings["title"] = new_name
    return settings

default_settings = {"title":"dr strange2"}
def get_title(dictionary=default_settings):
    return dictionary["title"]
print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())