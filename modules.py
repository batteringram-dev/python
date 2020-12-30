
# Modules are really useful in Python. They can import a python file into another python file.
# In this program i am going to import what's there in " useful_tools.py " into the " modules.py " file. There are 2 basic modules in Python. Built-In module and external module.
# The built-in module is already built into python so there's no need to access it as it's already there.
# The external module can be located in the editor in a file called " lib " under " External Libraries " file.
# The command " pip " is really useful in installing 3rd party modules from google.
# " pip " should be installed first in cmd. Then it can be used for installing the packages.
# Once installed, the package will be under " site-packages " under " External Libraries ".

import useful_tools

print(useful_tools.names)
