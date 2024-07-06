import pytest
from ninja.testing import TestClient

from spm_backend.api import api


@pytest.fixture
def client() -> TestClient:
    """
    Test client fixture
    """

    return TestClient(api)
