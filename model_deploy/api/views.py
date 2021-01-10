#Import necessary libraries
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np

# Create your views here
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)

@api_view(["POST"])
def predict_revenue(request):
    try:
        Administrative = request.data.get('Administrative')
        Administrative_Duration = request.data.get('Administrative_Duration')
        Informational = request.data.get('Informational')
        Informational_Duration = request.data.get('Informational_Duration')
        ProductRelated = request.data.get('ProductRelated')
        ProductRelated_Duration = request.data.get('ProductRelated_Duration')
        BounceRates = request.data.get('BounceRates')
        ExitRates = request.data.get('ExitRates')
        PageValues = request.data.get('PageValues')
        SpecialDay = request.data.get('SpecialDay')
        # Month = request.data.get('Month')
        OperatingSystems = request.data.get('OperatingSystems')
        Browser = request.data.get('Browser')
        Region = request.data.get('Region')
        TrafficType = request.data.get('TrafficType')
        # VisitorType = request.data.get('VisitorType')
        Weekend = request.data.get('Weekend')

        fields = [Administrative, Administrative_Duration, Informational,
        Informational_Duration, ProductRelated, ProductRelated_Duration,
        BounceRates, ExitRates, PageValues, SpecialDay,
        OperatingSystems, Browser, Region, TrafficType,
        Weekend]

        if not None in fields:
            #Datapreprocessing Convert the values to float
            Administrative = float(Administrative)
            Administrative_Duration = float(Administrative_Duration)
            Informational = float(Informational)
            Informational_Duration = float(Informational_Duration)
            ProductRelated = float(ProductRelated)
            ProductRelated_Duration = float(ProductRelated_Duration)
            BounceRates = float(BounceRates)
            ExitRates = float(ExitRates)
            PageValues = float(PageValues)
            SpecialDay = float(SpecialDay)
            # Month = str(Month)
            OperatingSystems = float(OperatingSystems)
            Browser = float(Browser)
            Region = float(Region)
            TrafficType = float(TrafficType)
            # VisitorType = str(VisitorType)
            Weekend = float(Weekend)

            result = [Administrative, Administrative_Duration, Informational,
            Informational_Duration, ProductRelated, ProductRelated_Duration,
            BounceRates, ExitRates, PageValues, SpecialDay,
            OperatingSystems, Browser, Region, TrafficType,
            Weekend]

            #Passing data to model & loading the model from disks
            model_path = 'ml_model/random_forest_model.pkl'
            classifier = pickle.load(open(model_path, 'rb'))
            prediction = classifier.predict([result])[0]
            conf_score =  np.max(classifier.predict_proba([result]))*100
            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : prediction,
                'confidence_score' : conf_score
            }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }
    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(predictions)