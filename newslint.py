import sys
import linter_class
import lintlog
# import rule.bro_culture as bro_culture
# import rule.bubble as bubble
# import rule.expectations as expectations
# import rule.language as language
# import rule.realism as realism
# import rule.sexism as sexism
# import rule.tech as tech
import rule.partisan_slang as partisan_slang
import rule.pundit as pundit
import rule.rag as rag
import rule.sensationalism as sensationalism


def newslint(content):
    linter = linter_class.create()
    inject_rules_into_linter(linter)
    return linter.lint(content)


def inject_rules_into_linter(linter):
    # bro_culture.define_rules(linter)
    # bubble.define_rules(linter)
    # expectations.define_rules(linter)
    # language.define_rules(linter)
    # realism.define_rules(linter)
    # sexism.define_rules(linter)
    # tech.define_rules(linter)

    partisan_slang.define_rules(linter)
    pundit.define_rules(linter)
    rag.define_rules(linter)
    sensationalism.define_rules(linter)


def main():
    result = newslint(sys.argv[1])
    lintlog.report(result, {'verbose': False})

if __name__ == "__main__":
    main()
