from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from builder import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)  # Объявлен блюпринт

FILE_NAME = 'data/apache_logs.txt'  # Константа


@main_bp.route('/perform_query', methods=['POST'])  # Метод ограничен на POST (согласно условий задания)
def perform_query():
    data = request.json  # Принимаем данные в формате json
    try:
        validated_data = BatchRequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None  # первый вызов - result None
    path = validated_data['path']

    for query in validated_data['queries']:  # заходим в query, подставляем значения переменных и в data первым
        # результатом идет None, как только это выполнится то в переменную
        # result просядут данные из запроса
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=path,
            data=result
        )

    return jsonify(result)
