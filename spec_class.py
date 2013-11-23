import re
import werkzeug.urls as wz


class Spec(object):

    content = ''

    def __init__(self, content):
        self.content = content

        # make safe, but retain spaces
        self._words = wz.url_fix(content).replace('%20', ' ').split(' ')

        self._body_normalized = ' ' + ' '.join(self._words) + ' '

    def contains(self, phrase):
        return re.findall(prepare_phrase(phrase), self._body_normalized)

    def contains_any_of(self, phrases):
        return filter(
            lambda x: len(x) != 0 or x == '',
            flatten(
                map(
                    lambda x:
                        re.findall(prepare_phrase(x), self._body_normalized),
                        phrases
                )
            )
        )


# via http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)


def create(content):
    return Spec(content)


def prepare_phrase(phrase):
    return phrase if isinstance(phrase, re._pattern_type) else re.compile('\\b' + phrase + '\\b', re.I)  # not guaranteed to work since _ is not public API
