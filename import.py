import os
import json
import requests


class InvalidGeometry(Exception):
    pass


def import_location(locations):
    print('Importing locations (%d) ...' % len(locations))
    response = session.post(
        'http://{api_server_host}/stores/replace'.format(
            api_server_host=api_server_host),
        params={'private_key': private_key},
        json={'stores': locations})

    print('Import time:', response.elapsed.total_seconds())
    if response.status_code >= 400:
        print('Import Failed')
        print(response.text)
        return False

    return True


if __name__ == '__main__':
    endpoint_json = 'data.json'
    private_key = os.environ['WOOS_PRIVATE_APIKEY']
    api_server_host = os.environ['WOOS_URL']
    with open(endpoint_json, 'rb') as f:
        data = json.loads(f.read())
        session = requests.Session()

        try:
            import_location(data["stores"])

        except InvalidGeometry:
            pass
