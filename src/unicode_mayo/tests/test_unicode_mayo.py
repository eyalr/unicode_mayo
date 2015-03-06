from .. import UnicodeSafetyWrapper, BytestringSafetyWrapper

class TestUnicodeSafetyWrapper(object):
    def test_unicode_okay(self):
        wrapped = UnicodeSafetyWrapper(u'unicode')
        wrapped + u'works'
        wrapped.encode('utf-8')
        unicode(wrapped)
        repr(wrapped)
        ','.join((wrapped, u'5'))
        wrapped += u'5'
        assert(isinstance(wrapped, UnicodeSafetyWrapper))
        assert(isinstance(u'5' + wrapped, UnicodeSafetyWrapper))

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


class TestByteStringSafetyWrapper(object):
    def test_bytes_okay(self):
        wrapped = BytestringSafetyWrapper('utf-8 stuff')
        wrapped + 'works'
        wrapped.decode('utf-8')
        str(wrapped)
        repr(wrapped)
        ','.join((wrapped, '5'))
        wrapped += '5'
        assert(isinstance(wrapped, BytestringSafetyWrapper))
        assert(isinstance('5' + wrapped, BytestringSafetyWrapper))

    def test_bytes_wrong_operations(self):
        wrapped = BytestringSafetyWrapper('utf-8 stuff')
        try:
            wrapped + u'doesn\'t work'
            assert('broken!')
        except TypeError:
            pass

        try:
            wrapped.encode('utf-8')
            assert('broken!')
        except TypeError:
            pass

        try:
            unicode(wrapped)
            assert('broken!')
        except TypeError:
            pass

    def test_bytes_formatting_ok(self):
        wrapped = BytestringSafetyWrapper('utf-8 stuff {}')

        if not wrapped.format('testing') == 'utf-8 stuff testing':
            assert('broken!')

        wrapped = BytestringSafetyWrapper('utf-8 stuff {test}')

        if not wrapped.format(test='testing') == 'utf-8 stuff testing':
            assert('broken!')

    def test_bytes_formatting_bytes_broken(self):
        wrapped = BytestringSafetyWrapper('utf-8 stuff {}')

        try:
            wrapped.format(u'testing')
            assert('broken!')
        except TypeError:
            pass

    def test_bytes_mod_ok(self):
        wrapped = BytestringSafetyWrapper('utf-8 stuff %s')

        if not wrapped % ('testing',) == 'utf-8 stuff testing':
            assert('broken!')

    def test_bytes_formatting_bytes_broken(self):
        wrapped = BytestringSafetyWrapper('utf-8 stuff %s')

        try:
            wrapped % (u'testing',)
            assert('broken!')
        except TypeError:
            pass
