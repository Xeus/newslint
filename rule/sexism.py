import re

gender_words = [
    re.compile('/boys?'),
    re.compile('bros?'),
    re.compile('broth(a|er)s?'),
    re.compile('chicks?'),
    re.compile('dads?'),
    re.compile('dudes?'),
    re.compile('fathers?'),
    re.compile('females?'),
    re.compile('gentlem[ae]n'),
    re.compile('girls?'),
    re.compile('grandfathers?'),
    re.compile('grandmas?'),
    re.compile('grandmothers?'),
    re.compile('grandpas?'),
    re.compile('grann(?:y|ies)'),
    re.compile('guys?'),
    re.compile('husbands?'),
    re.compile('lad(?:y|ies)'),
    re.compile('m[ae]n'),
    re.compile('m[ou]ms?'),
    re.compile('males?'),
    re.compile('momm(?:y|ies)'),
    re.compile('mommas?'),
    re.compile('mothers?'),
    re.compile('papas?'),
    re.compile('sist(a|er)s?'),
    re.compile('wi(?:fe|ves)'),
    re.compile('wom[ae]n')
]

female_gendered_pronouns = [
    'she',
    'her'
]

male_gendered_pronouns = [
    'he',
    'his',
    'him'
]

beardy_words = [
    re.compile('beard(ed|s|y)?'),
    re.compile('grizzl(ed|y)')
]

sexualized_words = [
    'sexy',
    'hawt',
    'phat'
]

def test_gender(self, spec, result):
    gender_mentions = spec.contains_any_of(gender_words)
    if (len(gender_mentions) > 0):
        result.add_error(
            'Gender is mentioned',
            gender_mentions
        )
        result.add_culture_fail_points(len(gender_mentions) / 2)

def test_pronouns(self, spec, result):
    female_mentions = spec.contains_any_of(female_gendered_pronouns)
    male_mentions = spec.contains_any_of(male_gendered_pronouns)
    all_mentions = female_mentions + male_mentions
    if (len(female_mentions) != len(male_mentions)):
        result.add_warning(
            'Gendered pronouns are used and mismatched: ' + ', '.join(all_mentions),
            all_mentions
        )

def test_facial_hair(self, spec, result):
    beardy_mentions = spec.contains_any_of(beardy_words)
    if (len(beardy_mentions) > 0):
        result.add_error(
            'Facial hair is mentioned',
            beardy_mentions
        )
        result.add_culture_fail_points(len(beardy_mentions))

def test_sexualized_terms(self, spec, result):
    sexualized_mentions = spec.contains_any_of(sexualized_words)
    if (len(sexualized_mentions) > 0):
        result.add_warning(
            'Job uses sexualized terms: ' + ', '.join(sexualized_mentions),
            sexualized_mentions
        )
        result.add_culture_fail_points(len(sexualized_mentions) / 2)

def define_rules(linter):
    # Gender mentions
    linter.add_rule({
        'name': 'Gender Mention',
        'desc': 'Mentioning gender in a job spec not only limits the number of people likely to be interested, but can also have legal implications; it is often discriminatory. Check your use of gender-specific terms.',
        'test': test_gender
    })
    # Gendered pronouns
    linter.add_rule({
        'name': 'Gendered Pronouns',
        'desc': 'Inbalanced use of "him/his/her" or "he/she" could indicate that you\'re discriminating against a certain gender. Revise your use of these words to be sure, or replace them with "them" or "they".',
        'test': test_pronouns
    })
    # Facial hair mentions
    linter.add_rule({
        'name': 'Facial Hair Mention',
        'desc': 'The use of "grizzled" or "bearded" indicates that you\'re only looking for male developers.',
        'test': test_facial_hair
    })
    # Sexualized terms
    linter.add_rule({
        'name': 'Sexualized Terms',
        'desc': 'Terms like "sexy code" are often used if the person writing a spec doesn\'t know what they are talking about or can\'t articulate what good code is. It can also be an indicator of bro culture.',
        'test': test_sexualized_terms
    })
