============
unicode_mayo
============

**unicode_mayo** is the mayo in your unicode sandwich. In your development
environment, use it as a wrapper around unicode and byte strings to see if
they're accidentally coming in to contact with byte strings. This can help
catch unicode encode/decode errors before they happen in production!

**unicode_mayo** includes two classes: ``UnicodeSafetyWrapper`` and
``BytestringSafetyWrapper``. The former is meant to envelope unicode strings,
and warns when they come into contact with byte strings; the latter is meant
for byte strings, and warns when it comes into contact with unicode. Place
these in strategic places (likely in development environments only), like
``gettext()`` or all strings from your database.

Installation
============

Installation via ``pip``::

    pip install unicode_mayo

Usage
=====

Something like::

    >>> import unicode_mayo
    >>> wrapped = unicode_mayo.UnicodeSafetyWrapper(u'safety at last!')
    >>> wrapped.encode('utf-8')
    'safety at last!'
    >>> wrapped + u' woohoo!'
    u'safety at last! woohoo!'
    >>> wrapped + 'evil bytestring'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Users/eyalr/personal_work/unicode_mayo/src/unicode_mayo/__init__.py", line 55, in __add__
        _fail_on_bytes(other)
      File "/Users/eyalr/personal_work/unicode_mayo/src/unicode_mayo/__init__.py", line 90, in _fail_on_bytes
        _fail_on_bytes_helper(other)
      File "/Users/eyalr/personal_work/unicode_mayo/src/unicode_mayo/__init__.py", line 81, in _fail_on_bytes_helper
        'Attempted string formatting without decoding utf-8'
    TypeError: Attempted string formatting without decoding utf-8
