# test Doc

## This works

Normal reference

::: TestProj.MainModule.MainClass
    :docstring:



## This fails?

Subclass is imported into `TestProj/MainModule/MainClass.py` and then referenced by `TestProj/MainModule/__init__.py`  
from there we reference it here

::: TestProj.MainModule.SubClass
    :docstring:


## or This fails?

Subclass2 is referenced in `TestProj/MainModule/__init__.py`  
from there we reference it here

::: TestProj.MainModule.SubClass2
    :docstring: