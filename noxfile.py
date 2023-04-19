import nox

@nox.session
def lint_pep8(session):
    session.install("pep8")
    session.run("pep8", "exentions/plugins/")
#this needs test, pylint usually needs init but passing a path usually works
def lint_pylint(session):
    session.install("pylint")
    session.run("pylint", "extensions/plugins/")

def lint_mypy(session):
    session.install("mypy")
    session.run("mypy", "extensions/plugins/")
#force output to stdout, no write to file
def lint_isort(session):
    session.install("isort")
    session.run("isort", "extensions/plugins/", "--stdout")
