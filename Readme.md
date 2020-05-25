# Objective

Explore how to structure the folders of a large Python project

----

# Example projects

https://github.com/scikit-learn

---------------

# Example articles

- https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#example-directory-structure
- [Basic example of init.py](https://pythontips.com/2013/07/28/what-is-__init__-py/)
- [Advanced example of how to create a init.py and export stuff](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)

----

# How is sklearn structured?
root
- [sklearn]
    - [svm]
        - _init__.py
        - _classes.py
        - [tests1]

    - [tests2]

## Where are the SVM classes defined?
In the file _classes.py

## How does tests1 folder reference the LinearSVC class?
    
The *tests1* folder has the following imports
```
from sklearn.svm import LinearSVC
from sklearn.svm import LinearSVR    
```

## How does init.py export the class LinearSVC

```
from ._classes import SVC, NuSVC, SVR, NuSVR, OneClassSVM, LinearSVC, \
        LinearSVR
from ._bounds import l1_min_c

__all__ = ['LinearSVC',
           'LinearSVR',
           'NuSVC',
           'NuSVR',
           'OneClassSVM',
           'SVC',
           'SVR',
           'l1_min_c']

```

## How does _all_ work   ?
Linked to, but not explicitly mentioned here, is exactly when __all__ is used. It is a list of strings defining what symbols in a module will be exported when from <module> import * is used on the module


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


# What did I do to get Modules working in Visual Studio?
## This was the project structure
root
- MyMathLib.csproj
    - Point.py
    - __init__.py
- Tests.csproj

## What did I add to init.py

```
from .Point import Point

__all__ =[ "Point"]

```

## Setting the path so that modules are discoverable
The most challenging part comes here!
The Tests.csproj was configured as follows
```
<SearchPath>..\</SearchPath>
```
