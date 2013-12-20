import re

swears = [
    'bloody',
    'bugger',
    'cunt',
    'cock',
    'pussy',
    'dick',
    'douche',
    'bitch',
    'porchmonkey',
    'wetback',
    'beyotch',
    ' hoes',
    re.compile('dick[s|]? '),
    'negro',
    'nigga',
    'nigger',
    'kyke',
    'honkey',
    'zipperhead',
    'gook',
    'jackass',
    'asshole',
    re.compile('fuck(?:er|ing)?'),
    re.compile('piss(?:ing)?'),
    'shit'
]


def test(self, spec, result):
    swear_mentions = spec.contains_any_of(swears)
    if (len(swear_mentions) > 0):
        result.add_warning(
            'Swearing in a news article isn\'t very professional: ',
            swear_mentions
        )
        result.add_professionalism_fail_points(len(swear_mentions))


def define_rules(linter):
    # Profanity
    linter.add_rule({
        'name': 'Profanity',
        'desc': 'Profanity in a news article when not used in an appropriate context or in a quote can seem irrational, poorly edited, or inflammatory.',
        'test': test
    })
