"""
Created on Oct 21, 2014

@author: victor
"""


class Participant(object):
  def __init__(self, name, id_participant, score):
    self.__name = name
    self.__id_participant = id_participant
    self.__score = score

  @property
  def name(self):
    return self.__name

  @property
  def id_participant(self):
    return self.__id_participant

  @property
  def score(self):
    return self.__score

  @name.setter
  def name(self, value):
    self.__name = value

  @id_participant.setter
  def id_participant(self, value):
    self.__id_participant = value

  @score.setter
  def score(self, value):
    self.__score = value

  def __eq__(self, other):
    if type(self) is type(other):
      return self.__dict__ == other.__dict__
    return False

  def __ne__(self, other):
    if type(self) is type(other):
      return self.__dict__ != other.__dict__
    return True

  def description(self):
    return "name: " + str(self.name) + "\nid: " + str(self.id_participant) + "\nscore:" + str(self.score) + "\n"

