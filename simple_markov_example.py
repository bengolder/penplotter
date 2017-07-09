from random import uniform

# this is a state transition matrix
choices = {
	'a': {'a': 0, 'b': 0.3, 'c': .7},
	'b': {'a': .4, 'b': 0.2, 'c': .4},
	'c': {'a': .6, 'b': 0.3, 'c': .1},
}




def choose_next_state(current_state):
	probabilities = choices[current_state]
	return weighted_choice(probabilities)


def weighted_choice(probabilities):
	n = uniform(0.0, 1.0)
	for item, weight in probabilities.items():
		if n <= weight:
			return item
		n = n - weight


for j in range(50):
	states = ['c']
	for i in range(20):
		next_state = choose_next_state(states[-1])
		states.append(next_state)
	print(states)

