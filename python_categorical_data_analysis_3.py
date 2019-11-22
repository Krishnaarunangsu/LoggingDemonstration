from scipy.stats import chi2_contingency
from scipy.stats import chi2
# contingency table
table = [	[10, 20, 30],
			[6,  9,  17]]
print(table)
stat, p, dof, expected = chi2_contingency(table)
print(f'Stat:{stat}')
print(f'p-value:{p}')
print('dof=%d' % dof)
print(f'Expected:{expected}')
# interpret test-statistic
prob = 0.95
critical = chi2.ppf(prob, dof)
print(f'Critical:{critical}')
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
if abs(stat) >= critical:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')
# interpret p-value
alpha = 1.0 - prob
print('significance=%.3f, p=%.3f' % (alpha, p))
print(f'Alpha:{alpha}')
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')


# https://machinelearningmastery.com/chi-squared-test-for-machine-learning/
