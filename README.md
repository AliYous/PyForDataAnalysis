# PyForDataAnalysis
Customer online behavior prediction

Test Data for the API :

Here is a set of attributes that should be predicted as a 'won't purchase' visitor by our model :

{
    "Administrative": 3,
    "Administrative_Duration":  87.833333,
    "Informational": 0,
    "Informational_Duration": 0.0,
    "ProductRelated": 27,
    "ProductRelated_Duration": 798.333333,
    "BounceRates": 0.001,
    "ExitRates": 0.012644,
    "PageValues": 22.916036,
    "SpecialDay": 0.8,
    "OperatingSystems": 2,
    "Browser": 2,
    "Region": 3,
    "TrafficType": 1,
    "Weekend": false
}

Here is a set of attributes that should be predicted as a 'will purchase' visitor by our model :

{
    "Administrative": 3,
    "Administrative_Duration":  87.833333,
    "Informational": 0,
    "Informational_Duration": 0.0,
    "ProductRelated": 9,
    "ProductRelated_Duration": 738.000000,
    "BounceRates": 0.001,
    "ExitRates": 0.002,
    "PageValues": 0.0,
    "SpecialDay": 0.4,
    "OperatingSystems": 2,
    "Browser": 2,
    "Region": 1,
    "TrafficType": 2,
    "Weekend": false
}

To run the api :
 - Run the django server (usually on http://127.0.0.1:8000)
 - use postman, insomnia or any other HTTP request software to call the 'http://127.0.0.1:8000/predict' endpoint.
 - Pass one of the above objects as a request body that will be fed to our model, the API will return a response object
containing a prediction of either 0 (customer won't buy) or 1 (will buy)
 
 
