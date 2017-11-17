import os
import sys
import json
import time
sys.path.insert(0, "./app")

import configparser
from EmailSender import EmailSender
from NmapExpert import NmapExpert


def ConfigSectionMap(section, Config):
    """
    get a specific section and return a dict
    :param section: specific section
    :param Config:
    :return: dict
    """
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                logging.info("skip: %s" % option)
        except:
            logging.info("exception on %s!" % option)
            dict1[option] = None
    return dict1


def get_general_conf(name):
    """
    get the general conf
    :return:
    """
    Config = configparser.ConfigParser()
    Config.read("./conf/config.conf")
    myprior = {}
    for sec in Config.sections():
        if sec == name:
            myprior = ConfigSectionMap(sec, Config)
    return myprior

if __name__ == '__main__':
    nmapex = NmapExpert()
    hash_hosts = []
    macs = {}
    with open('./spec/mac-hash.json', 'r') as f:
        macs = json.loads(f.read())

    notin = lambda arr1, arr2: [elem for elem in arr1 if elem not in arr2]
    itsin = lambda arr1, arr2: [elem for elem in arr1 if elem in arr2]
    parse = lambda arr: [elem["host"] + \
        "    " + \
        elem["vendor"] +\
        "   " +\
        elem["mac"] for elem in arr]

    fl = True
    while fl:

        aux = nmapex.get_hash_hosts()
        ups = notin(aux, hash_hosts)
        downs = notin(hash_hosts, aux)

        hash_hosts = aux

        for ma in macs.keys():
            for ha in hash_hosts:
                if macs[ma] == ha["mac"]:
                    print ma + "    " + ha["host"]+"    up"

        print "UPS"
        for elem in parse(ups):
            print elem

        print "DOWNS"
        for elem in parse(downs):
            print elem

        time.sleep(20)
