from typing import List

import requests
from urllib.parse import quote_plus
from core.data.config import settings_api
from core.data.models import FilterCriteria, Mark
from dataclasses import asdict


class CarAPI:
    BASE_URL = settings_api.api.api_url
    CODE = settings_api.api.api_code

    def __init__(self, user_id=None):
        self.user_id = user_id

    def _execute_query(self, sql: str):
        sql = quote_plus(sql)
        url = f"{self.BASE_URL}?json&code={self.CODE}&sql={sql}"
        if self.user_id:
            url += f"&user_id={self.user_id}"

        response = requests.get(url)
        print(url)
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                print("Ошибка формата JSON:", response.text)
        else:
            print("Ошибка запроса:", response.status_code, response.text)
            return None

    def get_all_marks(self) -> List[Mark]:
        sql = "SELECT DISTINCT marka_id, marka_name FROM main"
        result = self._execute_query(sql)
        print(result)
        if result:
            return [Mark(**item) for item in result]
        return []

    def get_cars(self, criteria: FilterCriteria):
        sql = "SELECT * FROM main WHERE 1=1"
        criteria_dict = asdict(criteria)

        for key, value in criteria_dict.items():
            if value is not None:
                if key.endswith('_from'):
                    column = key.replace('_from', '')
                    sql += f" AND {column} >= {value}"
                elif key.endswith('_to'):
                    column = key.replace('_to', '')
                    sql += f" AND {column} <= {value}"
                else:
                    sql += f" AND {key}='{value}'"

        return self._execute_query(sql)

    def get_table_columns(self):
        sql = "SELECT marka_id, marka_name FROM main"
        return self._execute_query(sql)



if __name__ == "__main__":
    api = CarAPI()

    # Получение всех марок
    # marks = api.get_all_marks()
    # if marks:
    #     marka_names = [mark['MARKA_NAME'] for mark in marks]
    #     # print(marka_names)

    marks2 = api.get_table_columns()
    print(marks2)

    # Фильтрация по критериям
    # criteria = FilterCriteria(marka_name="Toyota")
    # cars = api.get_cars(criteria)
    # for car in cars:
    #     print(car)
