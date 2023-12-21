from sklearn.metrics import accuracy_score
import joblib
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Load the SVM model
loaded_svm_model = joblib.load('svm_model.joblib')

# Load the CountVectorizer used during training
cv = joblib.load('count_vectorizer.joblib')

# Load your test data
test_data = pd.read_csv("test.csv")

# Preprocess the 'Text' column in the test data
test_data['Text'].fillna('', inplace=True)  # Handle NaN values
test_data_transformed = cv.transform(test_data['Text'])
predictions = loaded_svm_model.predict(test_data_transformed)

predictions = loaded_svm_model.predict(test_data_transformed)

# Create a DataFrame with the predictions
df = pd.DataFrame({'Predictions': predictions})

# Save the DataFrame to a CSV file named 'submission.csv'
df.to_csv('submission.csv', index=False)

print("Predictions saved to submission.csv")