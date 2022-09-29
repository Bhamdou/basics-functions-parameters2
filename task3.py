"""Task 3: Default and non default arguments combined
Add a key pages to your previous settings and default_settings dictionaries.

Now, define two functions named get_pages and add_page. They will both have a parameter settings that will default to default_settings.

The function get_pages will simply return the list stored in the key pages of the given settings dictionary.

The function add_page will have an additional positional argument that will be the page as a dictionary. The function will append this argument to the pages key of the given settings dictionary.

Use this test case:

home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))
Your result should look like this:
[{'title': 'Home', 'path': '/'}]
[]
[{'title': 'Home', 'path': '/'}]
[{'title': 'About', 'path': '/about/'}]
"""