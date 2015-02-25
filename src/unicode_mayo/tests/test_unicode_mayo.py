from .. import UnicodeSafetyWrapper

class TestUnicodeSafetyWrapper(object):
    def test_unicode_okay(self):
        wrapped = UnicodeSafetyWrapper(u'unicode')
        wrapped + u'works'
        wrapped.encode('utf-8')
        unicode(wrapped)
        repr(wrapped)

    def test_unicode_wrong_operations(self):
        wrapped = UnicodeSafetyWrapper(u'unicode')
        try:
            wrapped + 'doesn\'t work'
            assert('broken!')
        except TypeError:
            pass

        try:
            wrapped.decode('utf-8')
            assert('broken!')
        except TypeError:
            pass

        try:
            str(wrapped)
            assert('broken!')
        except TypeError:
            pass

    def test_unicode_formatting_ok(self):
        wrapped = UnicodeSafetyWrapper(u'unicode {}')

        if not wrapped.format(u'testing') == u'wrapped testing':
            assert('broken!')

        wrapped = UnicodeSafetyWrapper(u'unicode {test}')

        if not wrapped.format(test=u'testing') == u'wrapped testing':
            assert('broken!')

    def test_unicode_formatting_bytes_broken(self):
        wrapped = UnicodeSafetyWrapper(u'unicode {}')

        try:
            wrapped.format('testing')
            assert('broken!')
        except TypeError:
            pass

    def test_unicode_mod_ok(self):
        wrapped = UnicodeSafetyWrapper(u'unicode %s')

        if not wrapped % (u'testing',) == u'wrapped testing':
            assert('broken!')

    def test_unicode_formatting_bytes_broken(self):
        wrapped = UnicodeSafetyWrapper(u'unicode %s')

        try:
            wrapped % ('testing',)
            assert('broken!')
        except TypeError:
            pass
