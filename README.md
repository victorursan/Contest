P2. Contest
At a programming contest, after evaluating the existing solutions, the evaluation committee has recorded into a list the scores obtained by the participants (at position i into the list is the score of the i-th participant). Knowing that the participants had to solve 10 problems, each problem evaluated with maximum 10 points, write a program in order to help the committee to repeatedly execute the following functionalities (each functionality is exemplified):

I1:
	1. Add into the list the result of a new participant.
 	F1:	 a.add 198 – adds the score 98 for the last participant
 		-check_participant
 		-find_participant
 		-create_participant
 		-add_participant
 		-ui:ui_add_participant
 		-menu: run()
 	F2:	 b.insert 74 at 5 – insert score 74 at position 5 in the list; positions are numbered from 0.
	2. Modify the scores from the list.
 	F3:	 a.remove 1 – removes the score of the participant at position 1.
 	F4:	 b.remove from 1 to 3 – removes the scores of participants at positions 1,2, and 3.
 	F5:	 c.replace 4 with 55 – replaces the score of the participant at position 4 with the score 55.
  
I2: 
	3. Write the participants whose score has different properties.
  	F6:	 a.less than 40 – writes the participants having the score less than 40.
  	F7:	 b.sorted – writes the participants sorted in a certain order, considering their scores
  	F8:	 c.Sorted and greater than 90 - writes the participants having the score greater than 40. 

I3:
	4. Obtain different characteristics of participants.
  	F9:	 a.avg from 1 to 5 – writes the average of the scores for the participants between position 1 and 5 in the list.
  	F10: b.min from 1 to 5 - writes the lowest score of the participants between position 1 and 5 in the list.
  	F11: c.mul 10 from 1 to 5 – writes the scores multiple of 10 of the participants between position 1 and 5 in the list.
  
I3:  
	5. Filter scores.
  	F12: a.filter mul 10 – retains only the participants that have the score multiple of 10 (which have completely completed several/all problems).
  	F13: b.filter greater than 70 –retains only the participants having scores greater than 70.

I4:
	6. Undo the last operation.
  	F14: a.undo – the last operation that has modified the list of scores is cancelled.
  	