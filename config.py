mftsc = {
    'I' : 'exist',
}

### micropython far too simple config ###
###  do not write below this header   ###
###  do not store collection items    ### 
###  usage (add or overwrite config): ###
### >>>import config                  ###
### >>>config.add('mftsc','I','exist')###
###  usage (access config):           ###
### >>>config.mftsc['I']              ###
### 'exist'                           ###
#########################################
import gc
import sys

conf_file = "" # leave empty if you use this file to store data

def add(dictname, key, value):
    newrow = _key_value_dict(key,value)
    me = _open_file_to_lines()
    dict_start = -1
    dict_end = -1
    new_dict = False
    linx = -1
    for rowx, linr in enumerate(me):
        if '### micropython far too simple config ###' in linr:
            new_dict = True
            break
        if linr[:4] == '    ':
            linr = '    ' + ' '.join(linr.split()) + '\n'
        else:
            linr = ' '.join(linr.split()) + '\n'
        if linr[:len(dictname)+4] == dictname + ' = {':
            dict_start = rowx
        if dict_start != -1:
            if "    '" + str(key) in linr:
                linx = rowx
                break
            if linr == '}\n':
                dict_end = rowx
                break
    result = 0
    if new_dict:
        #print('adding new dictionary')
        newfilerows = _new_dict(dictname,key,value) + me
        result = _write_lines_to_file(newfilerows)    
    elif linx != -1:
        #print('replacing row')
        me[linx] = newrow
        result = _write_lines_to_file(me)
    elif dict_end:
        #print('adding new row')
        me.insert(dict_end,newrow)
        result = _write_lines_to_file(me)
    if result:
        return _reload()
    else:
        return sys.modules[__name__]

def _reload():
    mod_name = __name__
    del sys.modules[mod_name]
    gc.collect()
    return __import__(mod_name)

def _new_dict(dictname,key,value):
    return [dictname + ' = {\n',
    _key_value_dict(key,value),
    '}\n']

def _key_value_dict(key,value):
    return "    '" + str(key) + "' : '" + str(value) + "',\n"
    
def _write_lines_to_file(lines):
    global conf_file
    if conf_file == "": conf_file = __file__
    try:
        with open(conf_file, 'w') as f:
            for l in lines:
                f.write(l)
            return 1
    except:
        print("Could not write file: ", __file__)
        return 0

def _open_file_to_lines():
    global conf_file
    conf_lines = []
    if conf_file == "": conf_file = __file__
    try:
        with open(conf_file, 'r') as f:
            conf_lines = f.readlines()
    except:
        print("Could not read file: ", __file__)
    return conf_lines
