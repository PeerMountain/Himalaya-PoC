from teamcity.django import TeamcityDjangoRunner
from django_behave.runner import DjangoBehaveTestSuiteRunner

class CompositeTestRunner(
  DjangoBehaveTestSuiteRunner,
  TeamcityDjangoRunner
):
  pass