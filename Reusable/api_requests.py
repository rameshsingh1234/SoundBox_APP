import requests


def make_request(url, method, headers=None, payload=None):
    headers = headers or {}
    payload = payload or {}

    if method.upper() == 'GET':
        response = requests.get(url, headers=headers)
    elif method.upper() == 'POST':
        response = requests.post(url, headers=headers, json=payload)
    elif method.upper() == 'PUT':
        response = requests.put(url, headers=headers, json=payload)
    elif method.upper() == 'PATCH':
        response = requests.patch(url, headers=headers, json=payload)
    elif method.upper() == 'DELETE':
        response = requests.delete(url, headers=headers)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")

    return response
