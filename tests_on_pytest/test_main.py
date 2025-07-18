import pytest
from main import count_vowels


def test_only_russian_vowels():
    assert count_vowels("аеёиоуыэюя") == 10  # Все возможные гласные
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10  # Проверка заглавных
    assert count_vowels("ёжик") == 2         # ё, и


def test_no_russian_vowels():
    assert count_vowels("прст") == 0        # Нет гласных
    assert count_vowels("123!@#") == 0      # Цифры и символы
    assert count_vowels("КЛНМ") == 0        # Заглавные согласные


def test_mixed_text():
    assert count_vowels("Привет, мир!") == 3  # и, е, и
    assert count_vowels("ООО 'Рога и Копыта'") == 9  # О,О,О,о,а,и,о
    assert count_vowels("Съешь ещё этих мягких французских булок") == 12


def test_empty_string():
    assert count_vowels("") == 0
