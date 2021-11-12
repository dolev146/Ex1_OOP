# Ex1_OOP
  bibliography:
  https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...
  https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c
  
# algo description:
  check how much elevator is in the json file.
  make number of list that represent the number of the elevators that in the json file
  id = the place of the elev in the list 
  insert all the calls that in the csv file to list that represent the calls by the over the csv rows.
  insert dict (to each of the list) that contain the time of the finish of the latest call that in the current list.
  if there is only one elevator - put 0 in all the collum that in the csv file.
  if not - iter the list of the calls by compute the start time of the call and the by the dict of the list- insert the call to the shortest 
  by that iter all the calls that in the list
  when finish -insert the assignees of the calls to the csv file 
  at the end return the csv file
  
    # each of the list that represent elevator need to contain one dict that the key will be the time that the elevator
    # finish her task-mean that the last call that in the list was end (need a function that compute that time..)
    # and the val wil be scoop that the elev is in - the range of the src and dest of the last call in the list of calls
  
