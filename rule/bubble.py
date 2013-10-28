import re

bubble_job_titles = [
    re.compile('gurus?'),
    re.compile('hero(:?es)'),
    re.compile('ninjas?'),
    re.compile('rock\s*stars?'),
    re.compile('super\s*stars?')
]

temptations = [
    re.compile('ales?'),
    re.compile('beers?'),
    re.compile('brewskis?'),
    'coffee',
    'foosball',
    re.compile('keg(?:erator)?s?'),
    re.compile('lagers?'),
    re.compile('nerf\s*guns?'),
    re.compile('ping\s*pong?'),
    re.compile('pints?'),
    re.compile('pizzas?'),
    re.compile('play\s*stations?'),
    re.compile('pool\s*table|pool'),
    re.compile('rock\s*walls?'),
    'table football',
    re.compile('table\s*tennis'),
    re.compile('wiis?'),
    re.compile('xbox(?:es|s)?'),
    re.compile('massages?')
]

def test_titles(self, spec, result):
    bubble_job_mentions = spec.contains_any_of(bubble_job_titles)
    if (len(bubble_job_mentions) > 0):
        result.add_warning(
            'Tech people are not ninjas, rock stars, gurus or superstars',
            bubble_job_mentions
        )
        result.add_culture_fail_points(len(bubble_job_mentions) / 2)
        result.add_realism_fail_points(1)

def test_temptations(self, spec, result):
    temptation_mentions = spec.contains_any_of(temptations)
    if (len(temptation_mentions) > 0):
        result.add_warning(
            'Attempt to attract candidates with hollow benefits: ' +
            ', '.join(temptation_mentions),
            temptation_mentions
        )
        result.add_culture_fail_points(1)
        result.add_recruiter_fail_points(len(temptation_mentions) / 2)

def define_rules(linter):
    # Job title fails
    linter.add_rule({
        'name': 'Job "Titles"',
        'desc': 'Referring to tech people as Ninjas or similar devalues the work that they do and shows a lack of respect and professionalism. It\'s also rather cliched and can be an immediate turn-off to many people.',
        'test': test_titles
    })
    # Temptations
    linter.add_rule({
        'name': 'Hollow Benefits',
        'desc': 'Benefits such as "beer fridge" and "pool table" are not bad in themselves, but their appearance in a job spec often disguises the fact that there are few real benefits to working for a company. Be wary of these.',
        'test': test_temptations
    })

