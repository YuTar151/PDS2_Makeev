from sklearn.ensemble import StackingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = load_breast_cancer()

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12)

estimators = [('lgr', LogisticRegression()), ('sgc', DecisionTreeClassifier())]
model_cls = StackingClassifier(estimators=estimators, final_estimator=SVC())

model_cls.fit(X_train, y_train)

print(model_cls.score(X_test, y_test))