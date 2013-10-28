import result_class
import spec_class


class Linter(object):
    rules = []

    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def lint(self, content):
        spec = spec_class.create(content)
        result = result_class.create()
        for rule in self.rules:
            result.set_current_rule(rule)
            rule['test'](self, spec, result)
            result.clear_current_rule()
        return result


def create():
    return Linter()
