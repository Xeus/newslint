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
    'stooge',
    re.compile('game[- ]?chang(?:e|ing)'),
    re.compile('cutting[- ]?edge'),
    re.compile('bleeding[- ]?edge'),
    re.compile('marxis[tm]'),
    re.compile('cron(?:y|ie)'),
    re.compile('fema[ ]?trailer'),
    re.compile('chem[ ]?trails'),
    'snark',
    'delusion',
    'false flag',
    re.compile('racis[tm]'),
    re.compile('meme[- ]?wrangl(?:ing|e)'),
    'flagrant',
    'cult',
    'the establishment',
    'police state',
    re.compile('solutionis[mt]'),
    re.compile('shock(?:ing|er|ed)')
]


def test(self, spec, result):
    sensationalism_mentions = spec.contains_any_of(sensationalism_words)
    amount = ('Lots of' if (len(sensationalism_mentions) > 2) else 'Some')
    if (len(sensationalism_mentions) > 0):
        result.add_error(
            amount + ' sensationalist terminology is used',
            sensationalism_mentions
        )
        result.add_credibility_fail_points(len(sensationalism_mentions))


def define_rules(linter):
    linter.add_rule({
        'name': 'Sensationalist Terminology',
        'desc': 'Words that indicate that a blurb engages in sensationalism may betray the rest of the article or essay of objectivity, detachment, or fairness.',
        'test': test
    })
