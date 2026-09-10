import requests


def is_url_reachable(url):
    """Verifica se a URL informada está ativa e respondendo com status 200."""
    if not url:
        return False
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False