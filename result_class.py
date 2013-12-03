import math
from sets import Set


class Result(object):
    errors = list()
    warnings = list()
    notices = list()
    fail_points = dict({
        'culture': 0,
        'realism': 0,
        'recruiter': 0,
        'tech': 0
    })

    def __init__(self):
        self.mentions = []
        self.errors = []
        self.warnings = []
        self.notices = []
        self.fail_points = dict({
            'culture': 0,
            'realism': 0,
            'recruiter': 0,
            'tech': 0
        })

    def set_current_rule(self, rule):
        self.current_rule = rule

    def clear_current_rule(self):
        del self.current_rule

    def _add_mentions(self, mentions):
        self.mentions += mentions

    def _add_message(self, type_cat, msg, evidence):
        new_msg = {
            'message': msg,
            'detail': self.current_rule['desc'] if self.current_rule != None else '',
            'evidence': ', '.join(Set(evidence)) if evidence != None else []
        }

        if type_cat == 'errors':
            self.errors.append(new_msg)
        elif type_cat == 'notices':
            self.notices.append(new_msg)
        elif type_cat == 'warnings':
            self.warnings.append(new_msg)

    def add_mentions(self, mentions):
        self._add_mentions(mentions)

    def add_error(self, msg, evidence):
        self._add_message('errors', msg, evidence)

    def add_warning(self, msg, evidence):
        self._add_message('warnings', msg, evidence)

    def add_notice(self, msg, evidence):
        self._add_message('notices', msg, evidence)

    def _add_fail_points(self, type_cat, amount):
        self.fail_points[type_cat] += math.ceil(1 if amount is None else amount)

    def add_culture_fail_points(self, amount):
        self.fail_points['culture'] += math.ceil(1 if amount is None else amount)

    def add_realism_fail_points(self, amount):
        self.fail_points['realism'] += math.ceil(1 if amount is None else amount)

    def add_recruiter_fail_points(self, amount):
        self.fail_points['recruiter'] += math.ceil(1 if amount is None else amount)

    def add_tech_fail_points(self, amount):
        self.fail_points['tech'] += math.ceil(1 if amount is None else amount)

    def has_messages(self):
        return (
            len(self.errors) > 0 or
            len(self.warnings) > 0 or
            len(self.notices) > 0
        )

    def has_fail_points(self):
        return (
            self.fail_points['culture'] > 0 or
            self.fail_points['realism'] > 0 or
            self.fail_points['recruiter'] > 0 or
            self.fail_points['tech'] > 0
        )

    def is_clean(self):
        return (
            not self.has_messages() and
            not self.has_fail_points()
        )


def create():
    return Result()
