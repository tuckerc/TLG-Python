#!/usr/bin/env python3


## re-create file object to explore new method
with open("vlanconfig.cfg", "r") as configfile:
    ## Iterate thrhough configfile
    for config in configfile:
        if len(config) != 0:
            print(config.strip())


