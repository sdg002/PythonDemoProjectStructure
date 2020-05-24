# Objective

Explore how to structure the folders of a large Python project

----

# Example projects

https://github.com/scikit-learn

---------------

# Example articles

- https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#example-directory-structure
- https://pythontips.com/2013/07/28/what-is-__init__-py/

----

# How is sklearn structured?
root
- [sklearn]
    - [svm]
        - _init__.py
        - _classes.py
        - [tests1]

    - [tests2]

    The tests1 folder has the following imports
    ```
    from sklearn.svm import LinearSVC
    from sklearn.svm import LinearSVR    
    ```
    

# Lessons from the article
- Files name __init__.py are used to mark directories on disk as Python package directories
- If you have the following structure:
```
mydir/spam/__init__.py
midir/spam/module.py
```

and **mydir** is on your path, you can import the code in module.py as

```
import spam.module
```

or
```
from spam import module
```
