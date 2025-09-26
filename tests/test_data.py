class TestData:
    BASE_COORDINATES = {"lat": 55.028254, "lon": 82.918501}

    @staticmethod
    def valid_favorite(title: str = "example", color: str = None):
        data = {"title": title, **TestData.BASE_COORDINATES}
        if color:
            data["color"] = color
        return data

    @staticmethod
    def invalid_favorite(missing_field: str = None, invalid_color: str = None):
        data = {"title": "Тест", **TestData.BASE_COORDINATES}
        if missing_field and missing_field in data:
            del data[missing_field]
        if invalid_color:
            data["color"] = invalid_color
        return data