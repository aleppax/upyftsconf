![micropython Far Too Simple Config File!](/upyftsconf.jpg "uPyftsConf")

# uPyftsConf
micropython Far Too Simple Config File

a simplicistic way of storing configuration data for projects written in micropython.

## How it works
copy the file config.py at the root of your project.
Edit it adding as many dictionaries as you wish, those are factory settings but can be modified afterwards.
You can also add new dictionaries or settings simply by using the method `add(dictionary_name, key_name, value)`
If the dictionary doesn't exist, it creates it and adds the key:value pair.
The function `add` returns the config module updated, you have to assign it to itself: `config = config.add('dict_name','key','value')` , the garbage collector should take care of the rest.

```micropython
# example
mftsc = {
    'I' : 'exist',
}
```

Do not nest collection items inside dictionaries.
Do not write below this banner:
(and do not delete the line `### micropython far too simple config ###`)

```micropython
### micropython far too simple config ###
###  do not write below this header   ###
```

## Usage

```micropython
import config
config = config.add('dict_name','key','value')
myvalue = config.dict_name['key']
# or
myvalue = config.dict_name.get('key')
```
