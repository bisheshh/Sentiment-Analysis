from django.http import HttpResponse
from django.shortcuts import render
import pickle

# load the model from disk
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
lis = []
dic = {}


def home(request):
    return render(request, 'home.html')


def result(request):
    text = request.GET["text"]
    lis.append(text)
    predicted_value = loaded_model.predict(lis)
    print(predicted_value[0])

    if predicted_value[-1] == 1:
        display = 'Positive'
    elif predicted_value[-1] == 0:
        display = 'Negative'

    print(predicted_value)

    return render(request, 'result.html', {'display': display})
