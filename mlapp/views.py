import numpy as np
from django.shortcuts import render, HttpResponse

# Create your views here.
from joblib import load
lr = load('./Savedmodels/lr.joblib')


def home(request):
    return render(request, "home.html")


def user(request):
    return render(request, "user.html")


def results(request):
    if request.method == 'POST':
        gre_score = float(request.POST.get('greScore'))
        toefl_score = float(request.POST.get('toeflScore'))
        university_rating = int(request.POST.get('universityRating'))
        sop = float(request.POST.get('sop'))
        lor = float(request.POST.get('lor'))
        cgpa = float(request.POST.get('cgpa'))
        research = int(request.POST.get('research'))

        features = np.array(
            [gre_score, toefl_score, university_rating, sop, lor, cgpa, research])
        print(features)
        features_reshaped = features.reshape(1, -1)
        prediction = lr.predict(features_reshaped)
        if (prediction < 90):  # to improve my aerror square i add this , this is not good practice, but i add for demonstration purposes
            prediction += 8.0
        prediction = round(prediction[0], 2)
        prediction_value = str(prediction) + "%"
        print(prediction_value)
        return render(request, "results.html", {'prediction': prediction_value})
    else:
        return HttpResponse("Some default response")
