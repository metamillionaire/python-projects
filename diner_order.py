menu = ['soup of the day','open face sandwich','salad','slice of pie']
for lunch_specials in menu:
	question = input('Would you like to hear our specials?:   ')
	if question == 'Yes' or 'Y':
		print('Here are our specials for the day')
		print(menu)
		order = input('What would you like to order?:   ')
		if order == 'soup of the day':
			print(' So you want the soup of the day')
			print('Coming right up')
		elif order == 'open face sandwich':
			      print('So you want the open face sandwich? Turkey or Roast Beef?')
			      sandwich_type = input('Which one? Turkey or Roast Beef?:   ')
			      if sandwich_type == 'turkey':
				      print('hot open face turkey sandwich')
			      elif sandwich_type == 'roast beef':
				      print('Here is your hot open face roast beef sandwich')
		elif order == 'salad':
			      print('So you ordered the salad, what type of dressing?:   ')
			      BLU = 'blue cheese'
			      RAN = 'ranch'
			      ITA = 'italian'
			      FRE = 'french'
			      dressing = input('What type of dressing would you like?:  ')
			      if dressing == BLU:
				      print('blue cheese')
			      if dressing == RAN:
				      print('ranch')
			      if dressing == ITA:
				      print('italian')
			      if dressing == FRE:
				      print('french')
		elif order == 'slice of pie':
			      print('What type of pie would you like?: We have apple, blueberry and lemon meringue.')
			      pie = input('What type of pie:   ')
			      if pie == 'apple':
				      print('Here is your apple pie')
			      if pie == 'blueberry':
				      print('Here is your blueberry pie')
			      if pie == 'lemon meringue':
				      print('Here is your lemon meringue pie')
		elif question == 'No' or 'N':
			print("Here's the check for your water")
