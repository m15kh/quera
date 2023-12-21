import joblib
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

# Load your dataset
data = pd.read_csv('train.csv')

# Handle NaN values in the 'Text' column
data['Text'].fillna('', inplace=True)

# Split the dataset
X = data['Text']
Y = data['Class']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Apply CountVectorizer
cv = CountVectorizer()
features = cv.fit_transform(x_train)

# Train your SVM model
svm_model = svm.SVC()
svm_model.fit(features, y_train)

# Save the model to a file using joblib
joblib.dump(svm_model, 'svm_model.joblib')

# You can also save the CountVectorizer separately if needed
joblib.dump(cv, 'count_vectorizer.joblib')
