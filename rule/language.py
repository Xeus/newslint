import re

swears = [
    'bloody',
    'bugger',
    'cunt',
    re.compile('fuck(?:er|ing)?'),
    re.compile('piss(?:ing)?'),
    'shit'
]

def test(self, spec, result):
    swear_mentions = spec.contains_any_of(swears)
    if (len(swear_mentions) > 0):
        result.add_warning(
            'Swearing in a job spec isn\'t very professional: ',
            swear_mentions
        )
        result.add_recruiter_fail_points(len(swear_mentions))

def define_rules(linter):
    # Profanity
    linter.add_rule({
        'name': 'Profanity',
        'desc': 'While swearing in the workplace can be OK, you shouldn\'t be using profanity in a job spec; it\'s unprofessional.',
        'test': test
    })
