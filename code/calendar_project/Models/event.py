import uuid
import json

from jsonschema import validate

class Event(object):
    json_schema = {
        "type": "object",
        "properties": {
            "week_id": {
                "type": "integer",
                "title": "The Week_id Schema "
            },
            "close_date": {
                "type": "integer",
                "title": "The Close_date Schema "
            },
            "title": {
                "type": "string",
                "title": "The Title Schema "
            },
            "number_hours": {
                "type": "number",
                "title": "The Number_hours Schema "
            },
            "number_days": {
                "type": "integer",
                "title": "The Number_days Schema "
            },
            "min_hours": {
                "type": "number",
                "title": "The Min_hours Schema "
            },
            "description": {
                "type": "string",
                "title": "The Description Schema "
            }
        },
        "required": [
            "week_id",
            "close_date",
            "title",
            "number_hours",
            "number_days",
            "min_hours"
        ]
    }

    # TODO: temperature
    def __init__(self, json_data):
        self.id = str(uuid.uuid4())
        self.week_id = json_data['week_id']
        self.close_date = json_data['close_date']
        self.title = json_data['title']
        self.number_hours = json_data['number_hours']
        self.number_days = json_data['number_days']
        self.min_hours = json_data['min_hours']
        self.description = json_data['description']

    @staticmethod
    def validate_json(json_string):
        data = json.loads(json_string)

