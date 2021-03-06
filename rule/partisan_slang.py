import re

partisan_words = [
    re.compile('obama[ -]?care'),
    'libtard',
    'nobama',
    'death panel',
    'leftist',
    'communist',
    'malkin',
    'coulter',
    'sharpton',
    'sarah palin',
    'pinhead',
    'limbaugh',
    'o\'reilly',
    'krauthammer',
    'bachmann',
    'ron paul',
    'rand paul',
    'john bolton',
    'alex jones',
    'martin bashir',
    'perino',
    'karl rove',
    'stasi',
    re.compile('police[ -]?state'),
    re.compile('hipp(?:ies|y)'),
    re.compile('fly-?over state'),
    'wingnut'
]


def test(self, spec, result):
    partisan_mentions = spec.contains_any_of(partisan_words)
    amount = ('Lots of' if (len(partisan_mentions) > 2) else 'Some')
    if (len(partisan_mentions) > 0):
        result.add_error(
            amount + ' partisan terminology is used',
            partisan_mentions
        )
        result.add_nonpartisanship_fail_points(len(partisan_mentions))  # TODO categorize this into new point category


def define_rules(linter):
    linter.add_rule({
        'name': 'Partisan Terminology',
        'desc': 'Terminology, jargon, and slang used by political parties betrays one\'s true feelings about a subject.',
        'test': test
    })
