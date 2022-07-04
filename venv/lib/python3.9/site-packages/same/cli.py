#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author acrazing - joking.young@gmail.com
# @version 1.0.0
# @since 2017-05-23 00:27:02
#
# cli.py
#
import json
import os
from sys import argv, stderr, stdout

from same.Api import Module
from same.Client import Client, version


def same_help(fns, config, params):
    """
    :type fns: list[str]
    :type config: dict
    :type params: dict
    :return: 
    """
    print("""same python client
version: %s

Usage:
    %s [MODULE] API [OPTIONS...] [PARAMETERS...]
    
    - MODULE        is the client module name, for example, the `user`, `sense`, etc
    - API           is the api to call, or the property to display, if MODULE is not set,
                    will be the client owned method or property, else will be the module
                    method.
    - OPTIONS       is the client init options must with format `--[name]=[value]`
    - PARAMETERS    is the parameters pass to the API to call, it could be a `[value]` or
                    `[name]=[value]`. Both OPTIONS and PARAMETERS `value` could be a str
                    or start with `'` and end with `'` will be parsed by json.
""" % (version, argv[0]))
    config['flush'] = False
    config['log_file'] = os.devnull
    client = Client(**config)
    props = []
    methods = []
    modules = []
    dicts = {}
    for name in dir(client):
        if name.startswith('_'):
            continue
        value = getattr(client, name)
        dicts[name] = value
        if callable(value):
            methods.append(name)
        elif isinstance(value, Module):
            modules.append(name)
        else:
            props.append(name)
    index = """available MODULE:
    - %s

available API:
    - %s""" % ('\n    - '.join(modules), '\n    - '.join(props + methods))
    if len(fns) == 0:
        print(index)
    elif len(fns) == 1:
        if fns[0] in modules:
            print('module `%s` available API:\n    - %s'
                  % (fns[0], '\n    - '.join([name for name in dir(dicts[fns[0]]) if
                                              not name.startswith('_') and callable(getattr(dicts[fns[0]], name))])))
        elif fns[0] in props:
            print('API `%s` is a property' % fns[0])
        elif fns[0] in methods:
            print('API `%s`:\n%s' % (fns[0], getattr(dicts[fns[0]], '__doc__')))
        else:
            print(index)
    elif fns[0] not in modules or not hasattr(dicts[fns[0]], fns[1]):
        print(index)
    else:
        print('API `%s.%s`:\n%s' % (fns[0], fns[1], getattr(getattr(dicts[fns[0]], fns[1]), '__doc__')))


def same():
    args = argv[1:]
    """:type args: list[str]"""
    config = {}
    data = {}
    fns = []
    """:type fns: list[str]"""
    should_help = False
    for arg in args:
        if arg == '-h' or arg == '--help':
            should_help = True
        elif arg.startswith('--'):
            arg = arg[2:].split('=', 1)
            name = arg[0]
            value = arg[1]
            if value.startswith("'"):
                config[name] = json.loads(value[1:-1])
            else:
                config[name] = value
        elif arg.find('=') == -1:
            fns.append(arg)
        else:
            arg = arg.split('=', 1)
            name = arg[0]
            value = arg[1]
            if value.startswith("'"):
                data[name] = json.loads(value[1:-1])
            else:
                data[name] = value

    if should_help:
        same_help(fns, config, data)
        return
    stderr.write('initializing client with <%s>\n' % config)
    client = Client(**config)
    chains = []
    while len(fns) > 0:
        prop = fns.pop(0)
        client = getattr(client, prop)
        chains.append(prop)
        if callable(client):
            break
    stderr.write('calling same api <%s> with <%s, %s>\n' % ('.'.join(chains), fns, data))
    output = client(*fns, **data) if callable(client) else client
    json.dump(obj=output, fp=stdout, indent=2, default=lambda x: x.__repr__())
    stderr.write('\n')


if __name__ == '__main__':
    same()
