import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# Load the dataset
data = sm.datasets.get_rdataset("dietox", "geepack").data
data['initial_weight'] = data.groupby('Pig')['Weight'].transform('first')

mixed_model = smf.mixedlm(
    "Weight ~ Time + initial_weight + C(Evit)", 
    data, 
    groups=data["Pig"],
    re_formula="~Time"    
    ).fit()

print(mixed_model.summary())

random_effects = mixed_model.random_effects
plt.figure(figsize=(10, 6))
plt.bar(range(len(random_effects)), [re[0] for re in random_effects.values()])
plt.axhline(0, color='red', linestyle='--')
plt.xticks(range(len(random_effects)), random_effects.keys(), rotation=90)
plt.xlabel('Pig')
plt.ylabel('Random Effect for Intercept')
plt.title('Random Effects for Intercept by Pig')
plt.show()