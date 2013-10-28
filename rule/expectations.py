import re

competitive_phrases = [
    'compete',
    'competition',
    re.compile('competitive(?!\ssalary|\spay)'),
    'cutting edge',
    'fail',
    re.compile('fore\s*front'),
    re.compile('super\s*stars?'),
    'the best',
    'top',
    'win'
]

expectation_phrases = [
    'hit the ground running',
    'juggle',
    re.compile('tight deadlines?')
]

def test_competitiveness(self, spec, result):
    competition_mentions = spec.contains_any_of(competitive_phrases)
    if (len(competition_mentions) > 0):
        result.add_notice(
            'The job sounds competitive and performance-based',
            competition_mentions
        )
        result.add_realism_fail_points(len(competition_mentions) / 2)
        result.add_recruiter_fail_points(len(competition_mentions) / 2)

def test_expectations(self, spec, result):
    expectation_mentions = spec.contains_any_of(expectation_phrases)
    if (len(expectation_mentions) > 0):
        result.add_notice(
            'The job sounds like it\'s expecting too much from a new starter',
            expectation_mentions
        )
        result.add_realism_fail_points(len(expectation_mentions))

def define_rules(linter):
    # Competitive environment
    linter.add_rule({
        'name': 'Competitive Environment',
        'desc': 'Competition can be healthy, but for a lot of people a heavily competitive environment can be a strain. You could also potentially be excluding people who have more important outside-of-work commitments, such as a family.',
        'test': test_competitiveness
    })
    # Unrealistic expectations
    linter.add_rule({
        'name': 'New Starter Expectations',
        'desc': 'Terms like "hit the ground running" and others can indicate that the person writing a job spec is unaware of the time and effort involved in preparing a new starter for work.',
        'test': test_expectations
    })

