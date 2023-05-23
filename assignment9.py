import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
dataset = sns.load_dataset('titanic')

# Print the desired output
output_columns = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
                  'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
                  'alive', 'alone']

print(dataset[output_columns].head().to_string(index=False))

# Visualize the dataset
sns.boxplot(x='sex', y='age', data=dataset, hue='survived')
plt.show()
