import re

sensationalism_words = [
    re.compile('tears? apart'),
    'screed',
    'demolish',
    'crush',
    re.compile('brown[- ]?shirt'),
    'hitler',
    'gestapo',
    'snitch',
    'delusion',
    'false flag',
    re.compile('racis[tm]'),
    re.compile('meme[- ]?wrangl(ing|e)'),
    'flagrant',
    re.compile('shock(ing|er)'),
    re.compile('solutionis[mt]')
]


def test(self, spec, result):
    sensationalism_mentions = spec.contains_any_of(sensationalism_words)
    amount = ('Lots of' if (len(sensationalism_mentions) > 2) else 'Some')
    if (len(sensationalism_mentions) > 0):
        result.add_warning(
            amount + ' sensationalist terminology is used',
            sensationalism_mentions
        )
        result.add_culture_fail_points(len(sensationalism_mentions))  # TODO categorize this into new point category


def define_rules(linter):
    linter.add_rule({
        'name': 'Sensationalist Terminology',
        'desc': 'Words that indicate that a blurb engages in sensationalism may betray the rest of the article or essay of objectivity, detachment, or fairness.',
        'test': test
    })
