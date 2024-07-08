import pytest
from ninja.testing import TestClient

from spm_backend.api import api

client = TestClient(api)
