from paver.easy import *
__path__ = path(__file__).abspath().dirname()


@task
def pep8():
    pep8_options = ''
    dirs = ['hr_problem', 'tests']
    for dir in dirs:
       sh('pep8 %s %s' % (pep8_options, dir), cwd=__path__)
    

@task 
def pylint():
    pylint_options = ''
    modules = ['hr_problem']
    for module in modules:
      sh('pylint %s %s' % (pylint_options, module), cwd=__path__)
    files = ['tests']
    for file in files:
      sh('find %s -iname "*.py" | xargs pylint %s' % (file, pylint_options), cwd=__path__) 


@task
def test():
    nose_options = ''
    sh('nosetests %s' % nose_options, cwd=__path__)


@task
@needs('test')
@needs('pylint')
@needs('pep8')
def build():
    pass
