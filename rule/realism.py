import re

visionary_words = [
    re.compile('/blue\s*sk(?:y|ies)'),
    re.compile('/enlighten(?:ed|ing)?'),
    re.compile('/green\s*fields?'),
    re.compile('/incentivi[sz]e'),
    'paradigm',
    re.compile('/producti[sz]e'),
    re.compile('/reach(?:ed|ing) out'),
    re.compile('/synerg(?:y|ize|ise)'),
    re.compile('/visionar(?:y|ies)')
]

def test(self, spec, result):
    visionary_mentions = spec.contains_any_of(visionary_words)
    if (len(visionary_mentions) > 0):
        result.add_warning(
            '"Visionary" terminology is used: ',
            visionary_mentions
        )
        result.add_culture_fail_points(len(visionary_mentions) / 2)
        result.add_realism_fail_points(len(visionary_mentions) / 2)

def define_rules(linter):
    # Visionary terminology
    linter.add_rule({
        'name': 'Visionary Terminology',
        'desc': 'Terms like "blue sky" and "enlightened" often indicate that a non technical person (perhaps a CEO or stakeholder) has been involved in writing the spec. Be down-to-earth, and explain things in plain English.',
        'test': test
    })

