import numpy as np
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def train_svms(name, kingdoms):
    linear_svm = SVC(gamma=1/kingdoms[name][0].shape[0],
                kernel="linear", probability=True, random_state=0)
    linear_svm.fit(kingdoms[name][0], kingdoms[name][1])
    return linear_svm

def train_rfs(name, kingdoms):
    hierarchical_rf = RandomForestClassifier(n_estimators=10, n_jobs=-1)
    hierarchical_rf.fit(kingdoms[name][0], kingdoms[name][1])
    return hierarchical_rf