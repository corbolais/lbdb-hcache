# lbdb-hcache

This a little brother database module and supporting tools for using
the addresses stored in mutt's header cache as an address book.

The motivation for doing this is that to push emails through
lbdb-fetchaddr you need to pull the whole email from the server. This
is fine if you are using offlineimap or a local Maildir, but if you
are using imap normally, it will mean pulling a lot of data. Since
mutt already pulls this data to build the index view, and caches it,
you can extract the information from there.

## Requirements

 - python2.7
 - pytc, Python bindings for tokyo cabinet

## Installing and using

To install:

   $ sudo python setup.py install

To use, first you need to build the database.

   $ lbdb-hcache-extract-addresses

As long as the mutt header cache is in the default place, this will be
all you need. If you have to specify another location, use the
--hcache option.

To use the lbdb, you need to tell it where it can find the lbdb-hcache
module and tell it to use the lbdb-hcache method. The path to the
lbdb-hcache should be

    {sys.prefix}/share/lbdb-hcache/lbdb_modules.

Most likely this will be

    /usr/local/share/lbdb-hcache/lbdb_modules.

Add this to $MODULES_PATH in ~/.lbdbrc and tell it to use the
lbdb-hcache method.

    MODULES_PATH="$MODULES_PATH /usr/local/share/lbdb-hcache/lbdb_modules"
    METHODS="m_hcache"
    SORT_OUTPUT=no

It is advisable to disable sorting on the output, so that the most
commonly seen addresses are shown at the top.

If the database is in a location different to the default, this can
be specified with HCACHE_ADDRESS_DB in ~/.lbdbrc.