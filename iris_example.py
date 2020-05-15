# Imports
from sacred import Experiment
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sacred.observers import FileStorageObserver
import joblib
import os

# Create an experiment
ex = Experiment()

# Create an observer to watch the experiment
ex.observers.append(FileStorageObserver('my_runs'))


# Define hyperparameters
# By including them in this function, they can be altered
# using command line arguments
@ex.config
def my_config():
    MODEL_DIR = './tmp'
    MODEL_NAME = 'gs_result.pkl'
    MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)
    parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 10]}


@ex.automain
def my_main(MODEL_DIR, MODEL_NAME, MODEL_PATH, parameters):
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)

    # Load in the iris dataset
    iris = datasets.load_iris()

    # Ceate an SVM classifier
    svr = svm.SVC()

    # Create a grid search
    clf = GridSearchCV(svr, parameters, verbose=1)

    # Run the grid search
    clf.fit(iris.data, iris.target)

    # Save the grid search object
    joblib.dump(clf, MODEL_PATH)

    # Add the saved grid search object as an artifact
    ex.add_artifact(MODEL_PATH)

    # Return the results to be logged
    return clf.cv_results_
