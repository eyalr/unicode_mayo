"""
The MIT License (MIT)

Copyright (c) 2015 Eyal Reuveni

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class UnicodeSafetyWrapper(object):
    """Wrap unicodes strings and will blow up if it encounters bytestrings"""

    __slots__ = ('real_string',)

    def __init__(self, real_string):
        if isinstance(real_string, bytes):
            raise TypeError('Only unicode is supported')
        self.real_string = real_string

    def __unicode__(self):
        return unicode(self.real_string)

    def __str__(self):
        raise TypeError('Attempted to call str() on a unicode string')

    def __repr__(self):
        return '<class UnicodeSafetyWrapper on top of %s>' % (
            repr(self.real_string),
        )

    def __mod__(self, other):
        _fail_on_bytes(other)

        return self.real_string % other

    def format(self, other):
        _fail_on_bytes(other)

        return self.real_string.format(other)

    def __add__(self, other):
        _fail_on_bytes(other)

        return self.real_string + other

    def __radd__(self, other):
        _fail_on_bytes(other)

        return other + self.real_string

    def __iadd__(self, other):
        _fail_on_bytes(other)

        self.real_string = self.real_string + other

    def encode(self, *args):
        return self.real_string.encode(*args)

    def decode(self, *args):
        raise TypeError('Attempted to call decode() on a unicode string')
        return self.real_string.decode(*args)


def _fail_on_bytes(other):
    def _fail_on_bytes_helper(possibly_bytes):
        if isinstance(possibly_bytes, bytes):
            raise TypeError(
                'Attempted string formatting without decoding utf-8'
            )
    if isinstance(other, dict):
        for val in other.itervalues():
            _fail_on_bytes_helper(val)
    elif isinstance(other, (list, tuple)):
        for val in other:
            _fail_on_bytes_helper(val)
    else:
        _fail_on_bytes_helper(other)
