import pickle

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
lis = ['happy']

val = loaded_model.predict(lis)
print(val)
