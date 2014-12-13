'''Created on Oct 21, 2014@author: victor'''from ro.ubb.contest.domain.operations import create_participant, add_participant, \  insert_participant_at_position, remove_participant_at_position, \  remove_participants_in_interval, replace_score_for_participant_at_position, \  participants_description, find_less_than, sort_by_score, find_greater_than, \  minimum_of_interval, multiples_of_score_in_interval, average_of_interval, \  filter_participants_with_score_greater_then, \  filter_participants_with_score_multiple_of, participants_undo, extra_pointfrom test.ro.ubb.contest.domain.test_operations import create_listdef print_options():  print("1 - Print all participants \n\2 - Add participant \n\3 - Insert participant at position \n\4 - Remove participant \n\5 - Remove participants in interval \n\6 - Replace score for participant at position \n\7 - Find participants with the score less than... \n\8 - Sort participants by score \n\9 - Find participants with the score greater than...sorted \n\10- The average of participants between... \n\11- The participant with the lowest score of participants between... \n\12- The participants with the score multiple of k of participants between... \n\13- Filter participants with the score multiple of k\n\14- Filter participants with score greater than ...\n\15- Undo \n\16- Extra point \n\x - Exit")def print_participants(l):  if len(l) == 0:    print("There are no participants")  else:    participants_description(l)def ui_get_valid_int(prmt):  value = 0  try:    value = int(input(prmt))  except ValueError:    print("Invalid input")  return valuedef ui_create_participant():  name = ""  try:    name = input("name: ")  except ValueError:    print("Invalid input.")  id_participant = ui_get_valid_int("id_participant: ")  score = ui_get_valid_int("score: ")  return create_participant(name=name, id_participant=id_participant, score=score)def ui_add_participant(l):  participant = ui_create_participant()  try:    add_participant(l, participant)  except ValueError as ve:    print(ve)def ui_insert_participant_at_position(l):  position = ui_get_valid_int("position: ")  participant = ui_create_participant()  try:    insert_participant_at_position(l, participant, position)  except ValueError as ve:    print(ve)def ui_remove_participant_at_position(l):  position = ui_get_valid_int("position: ")  try:    remove_participant_at_position(l, position)  except ValueError as ve:    print(ve)def ui_remove_participants_in_interval(l):  first = ui_get_valid_int("from: ")  last = ui_get_valid_int("to: ")  try:    remove_participants_in_interval(l, first, last)  except ValueError as ve:    print(ve)def ui_replace_score_for_participant_at_position(l):  score = ui_get_valid_int("score: ")  position = ui_get_valid_int("position: ")  try:    replace_score_for_participant_at_position(l, score, position)  except ValueError as ve:    print(ve)def ui_find_less_than(l):  lst = []  score = ui_get_valid_int("score: ")  try:    lst = find_less_than(l, score)  except ValueError as ve:    print(ve)  participants_description(lst)def ui_sort_by_score(l):  lst = []  try:    lst = sort_by_score(l, reverse=False)  except ValueError as ve:    print(ve)  participants_description(lst)def ui_greater_than_and_sorted(l):  score = ui_get_valid_int("score: ")  lst = []  try:    lst = find_greater_than(l, score)    lst = sort_by_score(lst, reverse=False)  except ValueError as ve:    print(ve)  participants_description(lst)def ui_average_of_interval(l):  first = ui_get_valid_int("from: ")  last = ui_get_valid_int("to: ")  result = 0  try:    result = average_of_interval(l, first, last)  except ValueError as ve:    print(ve)  print(result)def ui_minimum_of_interval(l):  first = ui_get_valid_int("from: ")  last = ui_get_valid_int("to: ")  participant = 0  try:    participant = minimum_of_interval(l, first, last)  except ValueError as ve:    print(ve)  print(participant.description())def ui_multiples_of_score_in_interval(l):  first = ui_get_valid_int("from: ")  last = ui_get_valid_int("to: ")  mult = ui_get_valid_int("multiple: ")  lst = []  try:    lst = multiples_of_score_in_interval(l, mult, first, last)  except ValueError as ve:    print(ve)  print_participants(lst)def ui_filter_participants_with_score_multiple_of(l):  score = ui_get_valid_int("score: ")  try:    filter_participants_with_score_multiple_of(l, score)  except ValueError as ve:    print(ve)  print_participants(l)def ui_filter_participants_with_score_greater_then(l):  score = ui_get_valid_int("score: ")  try:    filter_participants_with_score_greater_then(l, score)  except ValueError as ve:    print(ve)  print_participants(l)def ui_undo(l, matrix):  participants_undo(l, matrix)def ui_extra_point(l):  print_participants(extra_point(l))def run():  l = create_list()  matrix = [list(l)]  options = {1: print_participants, 2: ui_add_participant, 3: ui_insert_participant_at_position,             4: ui_remove_participant_at_position, 5: ui_remove_participants_in_interval,             6: ui_replace_score_for_participant_at_position, 7: ui_find_less_than,             8: ui_sort_by_score, 9: ui_greater_than_and_sorted, 10: ui_average_of_interval,             11: ui_minimum_of_interval, 12: ui_multiples_of_score_in_interval,             13: ui_filter_participants_with_score_multiple_of,             14: ui_filter_participants_with_score_greater_then, 16: ui_extra_point}  while True:    print_options()    opt = input("option: ")    print("\n")    if opt == "x":      break    try:      opt = int(opt)      if opt == 15:        ui_undo(l, matrix)      else:        if opt in (2, 3, 4, 5, 6, 13, 14):          test_list = [x for x in l]          matrix.append(list(test_list))        options[opt](l)    except ValueError:      print("Invalid option")    except KeyError:      print("The chosen option is not yet implemented")    print("\n")  