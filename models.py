from marshmallow import Schema, fields, ValidationError, validates_schema

VALID_CMD_COMMANDS = ('filter', 'unique', 'limit', 'map', 'sort', 'file_name')  # Делаем валидатор


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str()

    @validates_schema  # Создаем декоратор
    def check_all_cmd_valid(self, values: dict[str, str], *args, **kwargs):
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid value')


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    path = fields.Str(required=True)
