n = int(raw_input())

standings = {}
totals = {}
for r in xrange(1,n+1): # r standing for round
	name, add = raw_input().split()
	add = int(add)
	if totals.has_key(name):
		standings[totals[name][0]].remove(name)
		if len(standings[totals[name][0]]) == 0:
			del standings[totals[name][0]]
			
		# add round score to total
		totals[name][0] += add
		# append total to list of scores
		totals[name][r] = totals[name][0]
	else:
		# this player just entered so create array sized number of rounds + 1
		totals[name] = [0] * (n + 1)
		# first position will be total, put round total in slot r
		totals[name][0], totals[name][r] = add, add 
	
	if standings.has_key(totals[name][0]):
		standings[totals[name][0]].append(name)
	else:
		standings[totals[name][0]] = [name]

max_score = max(standings)
winner = ''
if len(standings[max(standings)]) == 1:
	winner = standings[max(standings)][0]
else:
	# loop over each person's round scores and see who got to max_score first
	low_pos = n + 1
	for person in standings[max(standings)]:
		iter = 1
		while totals[person][iter] < max_score:
			iter += 1
		if iter < low_pos:
			low_pos, winner = iter, person

print winner
