'''
Created on Oct 21, 2014

@author: victor
'''
from ro.ubb.contest.models.Participant import Participant


def test_Participant():
  s = Participant("Mike", 12, 70)
  assert(s.name == "Mike")
  assert(s.id_participant == 12)
  assert(s.score == 70)
  assert(s == (Participant("Mike", 12, 70)))
  d = Participant("Steve", 13, 80)
  assert(d.name == "Steve")
  assert(d.id_participant == 13)
  assert(d.score == 80)
  assert(d == (Participant("Steve", 13, 80)))
  e = Participant("Andrew", 14, 85)
  assert(e.name == "Andrew")
  assert(e.id_participant == 14)
  assert(e.score == 85)
  assert(e == (Participant("Andrew", 14, 85)))
