'''
Created on Oct 21, 2014

@author: victor
'''
from test.ro.ubb.contest.domain.test_operations import test_operations
from test.ro.ubb.contest.models.test_Participant import test_Participant


def test_models():
  test_Participant()


def test_domain():
  test_operations()


if __name__ == '__main__':
  test_models()
  test_domain()