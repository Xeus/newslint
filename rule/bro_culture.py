import re

bro_words = [
    re.compile('bros?'),
    re.compile('brogramm(?:er|ers|ing)'),
    'crank',
    'crush',
    re.compile('dude(?:bro)?s?'),
    re.compile('hard[\s\-]*core'),
    'skillz'
]

def test(self, spec, result):
    bro_mentions = spec.contains_any_of(bro_words)
    amount = ('Lots of' if (len(bro_mentions) > 2) else 'Some')
    if (len(bro_mentions) > 0):
        result.add_warning(
            amount + ' "bro culture" terminology is used',
            bro_mentions
        )
        result.add_culture_fail_points(len(bro_mentions))

def define_rules(linter):
    # Bro terminology
    linter.add_rule({
        'name': 'Bro Terminology',
        'desc': 'Bro culture terminology can really reduce the number of people likely to show interest, both male and female. It discriminates against anyone who doesn\'t fit into a single gender-specific archetype.',
        'test': test
    })
