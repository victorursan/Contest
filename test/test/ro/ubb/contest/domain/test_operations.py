'''
Created on Oct 21, 2014

@author: victor
'''
from ro.ubb.contest.domain.operations import create_participant, \
  insert_participant_at_position, remove_participant_at_position, \
  remove_participants_in_interval, replace_score_for_participant_at_position, \
  add_participant, find_less_than, sort_by_score, average_of_interval, \
  minimum_of_interval, find_participant, multiples_of_score_in_interval, \
  filter_participants_with_score_multiple_of, \
  filter_participants_with_score_greater_then, extra_point

from ro.ubb.contest.models.Participant import Participant


def create_list():
  lst = []
  add_participant(lst, Participant(name="Mike", id_participant=0, score=60))
  add_participant(lst, Participant(name="John", id_participant=1, score=65))
  add_participant(lst, Participant(name="Steve", id_participant=2, score=70))
  add_participant(lst, Participant(name="Alexis", id_participant=3, score=75))
  add_participant(lst, Participant(name="Michael", id_participant=4, score=80))
  return lst


def test_create_participant():
  participant = create_participant(name="Mike", id_participant=0, score=60)
  assert (participant == (Participant(name="Mike", id_participant=0, score=60)))
  participant = create_participant(name="John", id_participant=1, score=65)
  assert (participant == (Participant(name="John", id_participant=1, score=65)))
  participant = create_participant(name="Steve", id_participant=2, score=70)
  assert (participant == (Participant(name="Steve", id_participant=2, score=70)))


def test_add_participant():
  l = create_list()
  assert (len(l) == 5)


def test_insert_participant_at_position():
  l = create_list()
  insert_participant_at_position(lst=l, participant=Participant(name="Lexi", id_participant=12, score=60), position=2)
  assert (l[2] == (Participant(name="Lexi", id_participant=12, score=60)))
  insert_participant_at_position(lst=l, participant=Participant(name="Olivia", id_participant=13, score=70), position=3)
  assert (l[3] == (Participant(name="Olivia", id_participant=13, score=70)))
  insert_participant_at_position(lst=l, participant=Participant(name="Alexander", id_participant=14, score=80),
                                 position=1)
  assert (l[1] == (Participant(name="Alexander", id_participant=14, score=80)))


def test_remove_participant_at_position():
  l = create_list()
  participant = l[2]
  remove_participant_at_position(lst=l, position=2)
  assert (not find_participant(l, participant))
  participant = l[3]
  remove_participant_at_position(lst=l, position=3)
  assert (not find_participant(l, participant))


def test_remove_participants_in_interval():
  # I could do a better assertion
  l = create_list()
  remove_participants_in_interval(lst=l, first=1, last=2)
  assert (len(l) == 3)
  l = create_list()
  remove_participants_in_interval(lst=l, first=0, last=4)
  assert (len(l) == 0)
  l = create_list()
  remove_participants_in_interval(lst=l, first=2, last=4)
  assert (len(l) == 2)
  l = create_list()
  remove_participants_in_interval(lst=l, first=0, last=3)
  assert (len(l) == 1)


def test_replace_score_for_participant_at_position():
  l = create_list()
  replace_score_for_participant_at_position(lst=l, score=40, position=3)
  assert (l[3].score == 40)
  replace_score_for_participant_at_position(lst=l, score=55, position=0)
  assert (l[0].score == 55)
  replace_score_for_participant_at_position(lst=l, score=45, position=1)
  assert (l[1].score == 45)
  replace_score_for_participant_at_position(lst=l, score=35, position=2)
  assert (l[2].score == 35)


def test_find_less_than():
  l = create_list()
  assert (len(find_less_than(l, 70)) == 2)
  assert (len(find_less_than(l, 80)) == 4)
  assert (len(find_less_than(l, 100)) == 5)


def test_sort_by_score():
  l = create_list()
  assert (sort_by_score(l, reverse=False)[4].id_participant == 4)
  assert (sort_by_score(l, reverse=True)[4].id_participant == 0)


def test_average_of_interval():
  l = create_list()
  assert (average_of_interval(l, 1, 2) == 67.5)
  assert (average_of_interval(l, 1, 3) == 70)
  assert (average_of_interval(l, 2, 4) == 75)


def test_minimum_of_interval():
  l = create_list()
  assert (minimum_of_interval(l, 1, 2) == (Participant(name="John", id_participant=1, score=65)))
  assert (minimum_of_interval(l, 1, 3) == (Participant(name="John", id_participant=1, score=65)))
  assert (minimum_of_interval(l, 2, 4) == (Participant(name="Steve", id_participant=2, score=70)))


def test_multiples_of_score_in_interval():
  l = create_list()
  assert (len(multiples_of_score_in_interval(l, 10, 0, 4)) == 3)
  assert (len(multiples_of_score_in_interval(l, 10, 1, 4)) == 2)
  assert (len(multiples_of_score_in_interval(l, 5, 0, 4)) == 5)


def test_filter_participants_with_score_multiple_of():
  l = create_list()
  filter_participants_with_score_multiple_of(l, 10)
  assert (len(l) == 3)
  l = create_list()
  filter_participants_with_score_multiple_of(l, 5)
  assert (len(l) == 5)
  l = create_list()
  filter_participants_with_score_multiple_of(l, 3)
  assert (len(l) == 2)


def test_filter_participants_with_score_greater_then():
  l = create_list()
  filter_participants_with_score_greater_then(l, 10)
  assert (len(l) == 5)
  l = create_list()
  filter_participants_with_score_greater_then(l, 65)
  assert (len(l) == 3)
  l = create_list()
  filter_participants_with_score_greater_then(l, 75)
  assert (len(l) == 1)


def test_extra_point():
  l = create_list()
  assert (len(extra_point(l)) == 2)


def test_operations():
  test_create_participant()
  test_add_participant()
  test_insert_participant_at_position()
  test_remove_participant_at_position()
  test_remove_participants_in_interval()
  test_replace_score_for_participant_at_position()
  test_find_less_than()
  test_sort_by_score()
  test_average_of_interval()
  test_minimum_of_interval()
  test_multiples_of_score_in_interval()
  test_filter_participants_with_score_multiple_of()
  test_filter_participants_with_score_greater_then()
  test_extra_point()