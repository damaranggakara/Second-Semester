# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

# Load dataset from CSV
file_path = 'data.csv'  # Ganti dengan path file CSV Anda
data = pd.read_csv('E:\\raka\\pribadi\\UB\\MATA KULIAH SEMESTER 2\\STRUKTUR DATA\\DATA TUGAS SORT,SEARCH.csv')

# Print the first few rows of the dataframe to understand its structure
print(data.head())

# Function to convert percentage strings to float
def convert_percentage(x):
    try:
        return float(x.strip().strip('%')) / 100 if isinstance(x, str) else x
    except ValueError:
        return None  # Handle cases where conversion fails

# Apply the conversion function to the appropriate columns
columns_to_convert = [
    'Uninsured Rate (2010)',
    'Uninsured Rate (2015)',
    'Uninsured Rate Change (2010-2015)',
    'Health Insurance Coverage Change (2010-2015)',
    'Employer Health Insurance Coverage (2015)',
    'Marketplace Health Insurance Coverage (2016)',
    'Marketplace Tax Credits (2016)',
    'Average Monthly Tax Credit (2016)',
    'Medicaid Enrollment Change (2013-2016)'
]

for col in columns_to_convert:
    data[col] = data[col].apply(convert_percentage)

# Drop rows with missing values (if any conversion failed)
data.dropna(inplace=True)

# Define feature columns and target column
features = [
    'Uninsured Rate (2010)',
    'Uninsured Rate (2015)',
    'Uninsured Rate Change (2010-2015)',
    'Health Insurance Coverage Change (2010-2015)',
    'Employer Health Insurance Coverage (2015)',
    'Marketplace Health Insurance Coverage (2016)',
    'Marketplace Tax Credits (2016)',
    'Average Monthly Tax Credit (2016)',
    'State Medicaid Expansion (2016)',
    'Medicaid Enrollment (2013)',
    'Medicaid Enrollment (2016)',
    'Medicaid Enrollment Change (2013-2016)',
    'Medicare Enrollment (2016)'
]

target = 'State'  # Misalnya kita ingin memprediksi State

# Split data into features (X) and target (y)
X = data[features]
y = data[target]

# Encode the target labels if necessary
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# Check if any samples remain
if len(X) == 0:
    print("No samples remaining after data cleaning. Adjust data cleaning process.")
else:
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize the Decision Tree Classifier
    clf = DecisionTreeClassifier(random_state=42)

    # Fit the model with the training data
    clf.fit(X_train, y_train)

    # Predict the target for the test set
    y_pred = clf.predict(X_test)

    # Calculate and print the accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy * 100:.2f}%')

    # Visualize the Decision Tree
    plt.figure(figsize=(20,10))
    tree.plot_tree(clf, feature_names=features, class_names=le.classes_, filled=True)
    plt.show()
