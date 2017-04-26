# LazyDS


Tired of thinking about what variables you've created during a long day of data science-ing in a jupyter notebook that you might want to save for later? Who knows when your kernel will give out and you'll need to re-run that dastardly long-running computation. With *LazyDS*, you can now save all the variables in your session and re-load them at a later date with a few short lines of code.

## Quick Start

### Saving

```
from lazyDS import save_session

a = range(10)
b = 'this thing'
c = 42
d = {}
e = lambda x: x+1 # this won't save
save_session('test_session')
```

### Loading

```
from lazyDS import load_session
loaded_vars = load_session('test_session')
for var_name in loaded_vars:
    exec(var_name + " = loaded_vars[var_name]")
print a, b, c, d
```

## Get Coffee!

:coffee: :coffee: :coffee:

