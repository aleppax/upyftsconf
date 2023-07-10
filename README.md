![micropython Far Too Simple Config File!](/upyftsc.jpg "uPyftsConf")

# uPyftsConf
micropython Far Too Simple Config File

a simplicistic way of storing configuration data for projects written in micropython. (single file, 92 lines of code)

## How it works
copy the file config.py inside a "libs" folder, import it.

If you prefer you can edit the file by adding as many dictionaries as you wish before the lines with code, those are factory settings but can be modified afterwards.

You can also add new dictionaries or settings simply by using the method `set(dictionary_name, key_name, value)`
If the dictionary doesn't exist, it creates it and adds the key:value pair.

The function `set` writes the new settings both in memory and to the configuration file (config.py), then reloads the module itself.

```micropython
# example
from libs import config
config.set('upyftsconf','I','exist')
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
from libs import config
config.set('dict_name','key','value')
myvalue = config.dict_name['key']
# or
myvalue = config.dict_name.get('key')
```
