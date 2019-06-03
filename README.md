# Record linkage accuracy assessment using machine learning (rl-acc)

## How to run

rl-acc is a supervised method to learn and assess the accuracy of record linkage.
It requires a labeled dataset in order to work.
The dataset must have at least three columns: 
the label (y) 
and two coluns with information from the two liked datasets.

### Config file

The first step before running rl-acc is to edit the config file acording to your data.
Assuming you have three columns (y, name_a, and name_b [assuming a and b were the two liked datasets])
you would have the following config file:

```
[DEFAULT]
DBA = a
DBB = b
IndexScore = 
Y = y

[0]
Id = name
Type = name
IndexA = name_a
IndexB = name_b
Features = jaro
```

In the config above,
`Y` means the name of the column in the data containing the label,
`IndexA` and `IndexB` the name of the column containing the variable to be used to extract the features.
`Features` defines the features extracted for this column, which can also be a list, separated by comma (ie, `jaro,hamming`).
Each entry of `Features` must be defined in `featuresExtractor.py` inside `extractFeatures` function.

### Running

Once the config file is configured properly,
you can use the `main.ipnb` notebook to run rl-acc.
The notebook is self expanatory.
If you have any questions, please contact me at gcgbarbosa@gmail.com
