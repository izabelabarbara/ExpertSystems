print('🤩 Career Advice Game 🤩')
print()
peopleType = input('Do you enjoy working with other people? ')
studyType = input('Do you like studying hard? ')
placeType = input('Would you rather work from home of from the office? ')
helpType = input('Do you like helping people or not really? ')

if studyType == 'no' and placeType == 'home':
  print ('You should be an artist!')
elif studyType == 'no' and placeType == 'home':
  print ('You should be a film star or a model!')
elif peopleType == 'yes' and studyType == 'yes' and placeType == 'office' and helpType ==  'yes':
  print ('You should be a doctor!')
elif peopleType == 'yes' and studyType == 'yes' and placeType == 'office' and helpType == 'no':
  print ('You might enjoy a lawyer\'s carreer! lol')
elif peopleType == 'yes' and studyType == 'yes' and placeType == 'home' and helpType == 'no':
  print ('Cool! You will be an engineer!')
elif placeType == 'home' and helpType == 'yes':
  print ('How do you want to help people when you\'re at home???')
elif peopleType == 'no' and studyType == 'yes' and placeType == 'home' and helpType == 'no':
  print ('Wow! You will be programmer!')
