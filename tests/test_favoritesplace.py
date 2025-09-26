import pytest
from tests.api_client import FavoritesAPIClient
from tests.models import FavoritePlace
from tests.test_data import TestData


class TestFavoritesAPI:

    @pytest.mark.asyncio
    async def test_create_with_required_params(self):
        async with FavoritesAPIClient() as api:
            assert await api.authenticate()
            test_data = TestData.valid_favorite()
            status, response = await api.create_favorite(test_data)
            assert status == 200
            FavoritePlace(**response)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("color", ["BLUE", "GREEN", "RED", "YELLOW"])
    async def test_create_with_valid_colors(self, color):
        async with FavoritesAPIClient() as api:
            assert await api.authenticate()
            test_data = TestData.valid_favorite(color=color)
            status, response = await api.create_favorite(test_data)
            assert status == 200
            favorite = FavoritePlace(**response)
            assert favorite.color == color

    @pytest.mark.asyncio
    async def test_create_without_authentication(self):
        async with FavoritesAPIClient() as api:
            test_data = TestData.valid_favorite()
            status, response = await api.create_favorite(test_data, use_auth=False)
            assert status == 401

    @pytest.mark.asyncio
    async def test_create_without_required_field(self):
        async with FavoritesAPIClient() as api:
            assert await api.authenticate()
            test_data = TestData.invalid_favorite(missing_field="lon")
            status, response = await api.create_favorite(test_data)
            assert status != 200

    @pytest.mark.asyncio
    async def test_create_with_invalid_color(self):
        async with FavoritesAPIClient() as api:
            assert await api.authenticate()
            test_data = TestData.invalid_favorite(invalid_color="INVALID")
            status, response = await api.create_favorite(test_data)
            assert status != 200

    @pytest.mark.asyncio
    @pytest.mark.parametrize("length,expected_status", [(0, 400), (1000, 400)])
    async def test_title_length_validation(self, length, expected_status):
        async with FavoritesAPIClient() as api:
            assert await api.authenticate()
            title = "A" * length if length > 0 else ""
            test_data = TestData.valid_favorite(title=title)
            status, response = await api.create_favorite(test_data)
            assert status == expected_status