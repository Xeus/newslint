import re

legacy_tech = [
    'cobol',
    'cvs',
    re.compile('front\s*page'),
    'rcs',
    'sccs',
    re.compile('source\s*safe'),
    re.compile('vb\s*6'),
    re.compile('visual\s*basic\s*6'),
    'vbscript'
]

environments = [
    re.compile('bb\s*edit'),
    re.compile('dream\s*weaver'),
    'eclipse',
    'emacs',
    re.compile('net\s*beans'),
    re.compile('note\s*pad'),
    re.compile('sublime\s*text'),
    re.compile('text\s*wrangler'),
    re.compile('text\s*mate'),
    re.compile('vim?'),
    re.compile('visual\s*studio')
]

expanded_acronyms = [
    re.compile('cascading[\s\-]?style[\s\-]?sheets'),
    re.compile('hyper[\s\-]?text([\s\-]?mark[\s\-]?up([\s\-]?language)?)?')
]

def test_legacy_tech(self, spec, result):
    legacy_tech_mentions = spec.contains_any_of(legacy_tech)
    if (len(legacy_tech_mentions) > 0):
        result.add_notice(
            'Legacy technologies found: ' + ', '.join(legacy_tech_mentions),
            legacy_tech_mentions
        )
        result.add_tech_fail_points(len(legacy_tech_mentions))
        result.add_realism_fail_points(1)

def test_environment(self, spec, result):
    environment_mentions = spec.contains_any_of(environments)
    if (len(environment_mentions) > 0):
        result.add_notice(
            'Development environment is prescribed: ' +
            ', '.join(environment_mentions),
            environment_mentions
        )
        result.add_tech_fail_points(len(environment_mentions))
        result.add_culture_fail_points(1)

def test_expanded_acronyms(self, spec, result):
    expanded_acronym_usage = spec.contains_any_of(expanded_acronyms)
    if (len(expanded_acronym_usage) > 0):
        result.add_warning(
            'Acronyms are expanded: ' +
            ', '.expanded_acronym_usage,
            expanded_acronym_usage
        )
        result.add_tech_fail_points(len(expanded_acronym_usage) / 2)
        result.add_recruiter_fail_points(len(expanded_acronym_usage))

def test_javascript(self, spec, result):
    javascript_fails = spec.contains(re.compile('(java[\s\-]script|java[\s\-]*scripts)', re.I))
    if (len(javascript_fails) > 0):
        result.add_error(
            'JavaScript is one word, and there\'s no "s" on the end',
            javascript_fails
        )
        result.add_recruiter_fail_points(len(javascript_fails))

def test_ror(self, spec, result):
    rails_fails = spec.contains('ruby on rail')
    if (len(rails_fails) > 0):
        result.add_error(
            'Ruby On Rails is plural; there is more than one rail.',
            rails_fails
        )
        result.add_recruiter_fail_points(len(rails_fails))

def define_rules(linter):
    # Legacy technology
    linter.add_rule({
        'name': 'Legacy Technology',
        'desc': 'Legacy technologies can reduce the number of people interested in a job. Sometimes we can\'t avoid this, but extreme legacy tech can often indicate that a company isn\'t willing to move forwards or invest in career development.',
        'test': test_legacy_tech
    })
    # Prescribed environment
    linter.add_rule({
        'name': 'Prescribed Development Environment',
        'desc': 'Unless you\'re building in a something which requires a certain development environment (e.g. iOS development and XCode), it shouldn\'t matter which tools a developer decides to use to write code; their output will be better if they are working in a familiar environment.',
        'test': test_environment
    })
    # Expanded acronyms
    linter.add_rule({
        'name': 'Expanded Acronyms',
        'desc': 'Tech people know their acronyms; you come across as not very tech-savvy if you expand them. You could be putting people off of the job spec by using these.',
        'test': test_expanded_acronyms
    })
    # JavaScript fails
    linter.add_rule({
        'name': 'JavaScript',
        'desc': 'JavaScript is one word. You write JavaScript, not javascripts or java script.',
        'test': test_javascript
    })
    # Rails fails
    linter.add_rule({
        'name': 'Ruby on Rail',
        'desc': 'Ruby On Rails is plural; there is more than one rail.',
        'test': test_ror
    })
