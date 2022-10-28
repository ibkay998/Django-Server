from django.http import JsonResponse


def index(request):
    response = JsonResponse({
        "slackUsername": "ibkay998",
        "backend":True,
        "age":23,
        "bio":"Hi my name is ibukunoluwa oyeniyi and an aspiring software developer interested both in frontend and backend and I love solving problems"
    })
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return response
    
