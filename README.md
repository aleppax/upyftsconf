# upyftsconf
micropython Far Too Simple Config File

a simplistic way of storing configuration data for projects written in micropython.

## How it works
copy the file config.py at the root of your project.
Edit it adding as many dictionaries as you wish, those are factory settings but can be modified.
You can also add new dictionaries or settings simply by using the method `add(dictionary_name, key_name, value)`
If the dictionary doesn't exist, it creates it and add the key:value pair.

```micropython
# example
mftsc = {
    'I' : 'exist',
}
```

Do not nest collection items inside dictionaries.
Do not write below this banner:

```micropython
### micropython far too simple config ###
###  do not write below this header   ###
```

## Usage

```micropython
import config
config.add('dict_name','key','value')
myvalue = config.dict_name['key']
```
