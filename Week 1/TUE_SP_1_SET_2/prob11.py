def running_sum(superhero_stats):
	sum=0
	for i,v in enumerate(superhero_stats):
		sum+=v
		superhero_stats[i]=sum
	return superhero_stats

superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats))

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats))

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats))