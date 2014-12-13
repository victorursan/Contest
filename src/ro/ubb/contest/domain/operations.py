'''
Created on Oct 21, 2014

@author: victor
'''
from ro.ubb.contest.models.Participant import Participant


def check_position(lst, position):
  '''Checks if the position is a valid position
  
  Args:
    lst - the list of participants
    position - int - the position of the participant
    
  Raises:
    ValueError - if the position is out of the range of the list
  '''
  if not (position in range(0, len(lst))):
    raise ValueError("Position is out of range")


def participants_description(lst):
  '''Prints the description of all participants
  
  Args: 
    lst - the list of participants
  '''
  [print(p.description()) for p in lst]


def create_participant(name, id_participant, score):
  '''Creates a participant
  
  Args:
    name - string - the name of the participant
    id_participant - int - the id of the participant
    score - int - the score of the partcipant
    
  Return:
    participant - and object of class Participant() 
  '''
  return Participant(name, id_participant, score)


def find_participant(lst, participant):
  '''Find a specific participant in the list
  
  Args:
    lst - list - the list of participants
    participant - Participant() - a specific Participant
    
  Return:
    True if the participant is in the list, false otherwise
  '''
  return any(p == participant for p in lst)


def check_participant(lst, participant):
  '''Checks if the participant is in the list

  Args:
    lst - list - the list of participants
    participant - Participant() - a specific participant
  
  Raises:
    ValueError - if the Participant already exists
  '''
  if find_participant(lst, participant):
    raise ValueError("Participant already exists!")


def get_participants_in_bounds(lst, first, last):
  '''Gets the participants between specific bounds
  
  Args:
    lst - list - the list of participants
    first - int - the lower bound
    last - int - the upper bound
  
  Return:
    list - a list of participants between the specified bounds
    
  Raises:
    - if the lower bound is greater than the upper bound
  '''
  check_position(lst, first)
  check_position(lst, last)
  if not (first < last):
    raise ValueError("From is greater than To")
  return lst[first: last + 1]


def add_participant(lst, participant):
  ''' Adds a participant to the list
  
  Args:
    lst - list - the list of participants
    participant - Participant() - a specific participant
  
  Raises:
    ValueError - if the Participant already exists
  '''
  check_participant(lst, participant)
  lst.append(participant)


def insert_participant_at_position(lst, participant, position):
  ''' Inserts a participant at a specific position in the list
  
  Args:
    lst - list - the list of participants
    participant - Participant() - a specific participant  
    position - int - the position we want to add the participant

  Raises:
    ValueError - if the position is out of range
               - if the Participant already exists
  
  '''
  if not (position in range(0, len(lst))):
    raise ValueError("Position is out of range!")
  if find_participant(lst, participant):
    raise ValueError("Participant already exists!")
  lst.insert(position, participant)


def remove_participant_at_position(lst, position):
  ''' Removes the participant at a specific position
  
  Args:
    lst - list - the list of participants
    participant - Participant() - a specific participant  
  
  Raises:
    ValueError - if the position is out of range
  '''
  if not (position in range(0, len(lst))):
    raise ValueError("Position is out of range!")
  lst.remove(lst[position])


def remove_participants_in_interval(lst, first, last):
  ''' Removes the participants between specific bounds
  
  Args:
    lst - list - the list of participants
    first - int - the lower bound
    last - int - the upper bound
  '''
  get_participants_in_bounds(lst, first, last)
  lst[first: last + 1] = []


def replace_score_for_participant_at_position(lst, score, position):
  ''' Replaces the score of the participant at a specific position
  
  Args:
    lst - list - the list of participants
    score - int - the score with which we want to change
    position - int - the position of the participant we want to replace the score
    
  Raises:
    ValueError - if the position is out of range
  '''
  if not (position in range(0, len(lst))):
    raise ValueError("Position is out of range")
  lst[position].score = score


def find_less_than(lst, score):
  ''' Find the participants with the score less than a score
  Args:
    lst - list - the list of participants
    score - int - the lower bound of scores
    
  Return:
    list - a list that have the score greater than the specified score
    
  Raises:
    ValueError - if there aren't such participants
  
  '''
  l = [p for p in lst if p.score < score]
  if len(l) == 0:
    raise ValueError("No results found")
  return l


def find_greater_than(lst, score):
  '''Finds the participants with the score greater than a specific score
  Args:
    lst - list - the list of participants
    score - int - the greater bound of scores
    
  Return:
    list - a list that have the score smaller than the specified score
    
  Raises:
    ValueError - if there aren't such participants
  '''
  l = [p for p in lst if p.score > score]
  if len(l) == 0:
    raise ValueError("No results found")
  return l


def sort_by_score(lst, reverse=False):
  '''Returns the list sorted
  
  Args:
    lst - list - the list of participants
  func mustHaveThis()
  Return:
    list - a sorted list
  '''
  return sorted(lst, key=lambda x: x.score, reverse=reverse)



def average_of_interval(lst, first, last):
  ''' Retuns the average score of the given interval
  
  Args:
    lst - list - the list of participants
    first - int - the lower bound
    last - int - the upper bound
  
  Return:
    float - the average score of the give interval
  '''
  li = get_participants_in_bounds(lst, first, last)
  l = [p.score for p in li]
  return sum(l) / len(l)


def minimum_of_interval(lst, first, last):
  '''Returns the participant with the lowest score from the interval
  
  Args:
    lst - list - the list of participants
    first - int - the lower bound
    last - int - the upper bound
  
  Return:
    participant - the participant with the lowest score from the interval
  '''
  li = get_participants_in_bounds(lst, first, last)
  return sort_by_score(li)[0]


def multiples_of_score_in_interval(lst, mult, first, last):
  """Returns the participant with the score multiple of a number from the interval

  Args:
    lst - list - the list of participants
    mult - int - the number multiple of
    first - int - the lower bound
    last - int - the upper bound

  Return:
    participant - the participant with the score multiple of a number from the interval
  """
  li = get_participants_in_bounds(lst, first, last)
  l = [x for x in li if x.score % mult == 0]
  return l


def filter_participants_with_score_multiple_of(lst, mult):
  """Filters the participants with the score multiple of a number

  Args:
    lst - list - the list of participants
    mult - int - the number multiple of
  """
  lst[:] = [p for p in lst if p.score % mult == 0]


def filter_participants_with_score_greater_then(lst, score):
  """Filter the participants with the score greater then a specify score

  Args:
    lst - list - the list of participants
    score - int - the lower bound of the scores
  """
  lst[:] = find_greater_than(lst, score)


def participants_undo(lst, matrix):
  """Undo's the last done acction

  Args:
    lst - list - the list of participants
    matrix - a list of lists - holds every past list
  """
  if len(matrix) != 0:
    lst[:] = matrix.pop()

def extra_point(lst):
  """Returns a list of participants with the score less than the average

  Args:
    lst - list - the list of participants

  Return
    l - list of participants with the score less than the average
  """
  avg = average_of_interval(lst, 0, len(lst) - 1)
  l = find_less_than(lst, avg)
  l = sort_by_score(l, reverse=True)
  return l