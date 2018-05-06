from django.http import JsonResponse, HttpResponse

from mongo_connector.connector import Connector


class Handler(object):
    @staticmethod
    def get_events(document):
        document = Connector.find_document('events_collection', document)

        if document is None:
            return JsonResponse({}, status=204)

        del document['_id']

        return JsonResponse(document)
