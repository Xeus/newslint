import re

rag_words = [
    'gawker',
    'tmz',
    'slate',
    re.compile('shock(ing|er|ed)')
]


def test(self, spec, result):
    rag_mentions = spec.contains_any_of(rag_words)
    amount = ('Lots of' if (len(rag_mentions) > 2) else 'Some')
    if (len(rag_mentions) > 0):
        result.add_warning(
            amount + ' references to writing rags are used',
            rag_mentions
        )
        result.add_culture_fail_points(len(rag_mentions))  # TODO categorize this into new point category


def define_rules(linter):
    linter.add_rule({
        'name': 'Rag References',
        'desc': 'Rags are newspapers or magazines that deal in paparazzi news, accusation-slinging, poor investigating, and shock-value.',
        'test': test
    })
