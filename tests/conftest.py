from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset mutable in-memory data so tests are isolated."""
    original_state = deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_state)
