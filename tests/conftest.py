from src.models import Product
import pytest

@pytest.fixture
def product_type():
    return Product("Smartphone", "Cool_Smartphone", 100, 14)
