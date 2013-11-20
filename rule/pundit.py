import re

pundit_words = [
    'krauthammer',
    re.compile('(thomas|tom) friedman'),
    'ayn rand',
    'gold standard',
    'rand paul',
    'ron paul',
    'bachmann',
    'gingrich',
    'slate',
    'msnbc',
    'foxnews',
    'ann coulter',
    'david brooks',
    'ezra klein',
    'dana perino',
    'evgeny morozov',
    'karl rove',
    'maureen dowd'
]


def test(self, spec, result):
    pundit_mentions = spec.contains_any_of(pundit_words)
    amount = ('Lots of' if (len(pundit_mentions) > 2) else 'Some')
    if (len(pundit_mentions) > 0):
        result.add_warning(
            amount + ' references to punditry are used',
            pundit_mentions
        )
        result.add_culture_fail_points(len(pundit_mentions))  # TODO categorize this into new point category


def define_rules(linter):
    linter.add_rule({
        'name': 'Punditry References',
        'desc': 'References to pundits, who give more lip service to politics and rumor than to subject matter expertise and objectivity, can undermine the veracity of a story.',
        'test': test
    })
