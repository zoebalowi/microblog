"""
Test routes for routes for authorizing users, app/main/routes
"""
# pylint: disable=redefined-outer-name,unused-argument

def test_version_default_value(client):
    """
    Test default version.
    """
    client.application.config['VERSION'] = 'unknown'

    response = client.get('/version')

    assert response.status_code == 200
    assert b'unknown' in response.data


def test_version_known_value(client):
    """
    Test configured version.
    """
    client.application.config['VERSION'] = '1.2.3'

    response = client.get('/version')

    assert response.status_code == 200
    assert b'1.2.3' in response.data
