# -*- coding: utf-8 -*-
#
import sys
import os
module = sys.modules[__name__]
CONFIG = module.CONFIG = {}
TRIPLESTORE_CACHE_URL = os.environ.get('TRIPLESTORE_CACHE_URL')
if TRIPLESTORE_CACHE_URL is None or TRIPLESTORE_CACHE_URL == '':
    TRIPLESTORE_CACHE_URL = CONFIG["TRIPLESTORE_CACHE_URL"] = "http://localhost"
#TRIPLESTORE_CACHE_URL = CONFIG["TRIPLESTORE_CACHE_URL"] = "http://db.loci.cat"
TRIPLESTORE_CACHE_PORT = os.environ.get('TRIPLESTORE_CACHE_PORT')
if TRIPLESTORE_CACHE_PORT is None or TRIPLESTORE_CACHE_PORT == '':
    TRIPLESTORE_CACHE_PORT = CONFIG["TRIPLESTORE_CACHE_PORT"] = "7200"
TRIPLESTORE_CACHE_SPARQL_ENDPOINT = CONFIG["TRIPLESTORE_CACHE_SPARQL_ENDPOINT"] = \
    "{}:{}/repositories/default".format(TRIPLESTORE_CACHE_URL, TRIPLESTORE_CACHE_PORT)

