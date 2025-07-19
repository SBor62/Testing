import pytest
from main import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{
        'url': 'https://example.com/cat.jpg',
        'id': '123'
    }]

    mocker.patch('requests.get', return_value=mock_response)

    result = get_random_cat_image()
    assert result == 'https://example.com/cat.jpg'


def test_get_random_cat_image_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404

    mocker.patch('requests.get', return_value=mock_response)

    result = get_random_cat_image()
    assert result is None
