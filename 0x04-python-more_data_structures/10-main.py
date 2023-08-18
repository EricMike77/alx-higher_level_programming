#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'James': 12, 'Mensa': 14, 'Clever': 14, 'Akin': 16, 'Ada': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
