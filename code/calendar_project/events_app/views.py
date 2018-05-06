from django.http import HttpResponse, JsonResponse
from mongo_connector.connector import Connector
from handler.handler import Handler

# TODO hacer qets y post con vistas basadas en modelos
# (https://stackoverflow.com/questions/19096227/how-to-discriminate-based-on-http-method-in-django-urlpatterns)
# Create your views here.


def hola_mundo(request):
    if request.method == 'GET':
        return Handler.get_events({"id": 3})

    elif request.method == 'POST':

        Connector.add_document("events_collection", {"id": 2, "text": "bassura en el cubo de la basura"})
        return HttpResponse("hola_mundo")

    else:
        return HttpResponse(status=404)

