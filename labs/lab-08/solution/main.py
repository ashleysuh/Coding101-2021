import pandas as pd
import sklearn.neural_network
from sklearn.linear_model import LogisticRegression
from sklearn import tree
import sklearn.pipeline
import sklearn.metrics
# import plotting libraries



# load files from directory
df_x_train = pd.read_csv("data_sneaker_vs_sandal/x_train.csv")
df_y_train = pd.read_csv("data_sneaker_vs_sandal/y_train.csv")
df_x_test = pd.read_csv("data_sneaker_vs_sandal/x_test.csv")
df_y_test = pd.read_csv("data_sneaker_vs_sandal/y_test.csv")

#convert them to numpy
x_train = df_x_train.to_numpy()
y_train = df_y_train.to_numpy()
x_test = df_x_test.to_numpy()
y_test = df_y_test.to_numpy()


#x and y should have the same number of rows for the train and test sets
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

print("files loaded")

#Logistic Classifier


logistic = LogisticRegression(verbose=1,n_jobs=1, max_iter=200)

# setup a pipeline to preprocess the input data using a sklearn scaler or call the sklearn scaler on the input data directly
logistic = sklearn.pipeline.Pipeline([
        ('rescale', sklearn.preprocessing.MinMaxScaler()),
        ('log', logistic)])

#fit and predict
logistic.fit(x_train, y_train.flatten())

y_hat_test = logistic.predict_proba(x_test)

#calculate loss (lower is better) and save results
test_results_logistic = sklearn.metrics.log_loss(y_test, y_hat_test)

# print(y_hat_test.shape) # (2002, 2)
# print(y_test.shape) # (2002, 1)

print("Logistic Regression Results:", test_results_logistic)



#Decision Tree Classifier
dtree = tree.DecisionTreeClassifier(criterion="entropy")

# setup a pipeline to preprocess the input data using a sklearn scaler or call the sklearn scaler on the input data directly
dtree = sklearn.pipeline.Pipeline([
        ('rescale', sklearn.preprocessing.MinMaxScaler()),
        ('tree', dtree)])

#fit and predict
dtree.fit(x_train, y_train.flatten())

y_hat_test = dtree.predict_proba(x_test)

#calculate loss (lower is better) and save results
test_results_dtree = sklearn.metrics.log_loss(y_test, y_hat_test)

print("Decision Tree Classifier Results:", test_results_dtree)

# MLP Classifier

mlp = sklearn.neural_network.MLPClassifier(activation='relu', alpha=0.17152165622510307, batch_size='auto',
              beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08,
              hidden_layer_sizes=11, learning_rate='constant',
              learning_rate_init=0.001, max_iter=200,
              momentum=0.9, n_iter_no_change=10, nesterovs_momentum=True,
              power_t=0.5, random_state=202, shuffle=True, solver='adam',
              tol=0.0001, validation_fraction=0.1, verbose=True)

# setup a pipeline to preprocess the input data using a sklearn scaler or call the sklearn scaler on the input data directly
mlp = sklearn.pipeline.Pipeline([
        ('rescale', sklearn.preprocessing.MinMaxScaler()),
        ('mlp', mlp)])

#fit and predict
mlp.fit(x_train, y_train.flatten())

y_hat_test = mlp.predict_proba(x_test)

#calculate loss (lower is better) and save results
test_results_mlp = sklearn.metrics.log_loss(y_test, y_hat_test)

print("MLP Results:", test_results_mlp)

#print summary results of all 3 classifiers
print("Logistic Regression Results:", test_results_logistic)
print("Decision Tree Classifier Results:", test_results_dtree)
print("MLP Results:", test_results_mlp)