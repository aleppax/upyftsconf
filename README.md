![micropython Far Too Simple Config File!](/upyftsc.jpg "uPyftsConf")

# uPyftsConf
micropython Far Too Simple Config File

a simplicistic way of storing configuration data for projects written in micropython. (single file, 92 lines of code)

## How it works
copy the file config.py where you like inside your project, import it.

If you want edit it adding as many dictionaries as you wish, those are factory settings but can be modified afterwards.

You can also add new dictionaries or settings simply by using the method `add(dictionary_name, key_name, value)`
If the dictionary doesn't exist, it creates it and adds the key:value pair.

The function `add` returns the updated config module, therefore you have to assign it to itself: `config = config.add('dict_name','key','value')` , the garbage collector should take care of the rest.

```micropython
# example
config = config.add('upyftsconf','I','exist')
```
the file config.py writes these lines inside itself:

```micropython
upyftsconf = {
    'I' : 'exist',
}
```

Do not nest collection items inside dictionaries.
Do not write below this banner:
(and do not delete it)

```micropython
#########################################
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
