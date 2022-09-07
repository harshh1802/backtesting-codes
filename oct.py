from six.moves import urllib
import json
import os

class GraphQLClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None
        self.headername = None

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token, headername='token'):
        self.token = token
        self.headername = headername

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        if self.token is not None:
            headers[self.headername] = '{}'.format(self.token)

        req = urllib.request.Request(self.endpoint, json.dumps(data).encode('utf-8'), headers)

        try:
            response = urllib.request.urlopen(req)
            return response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            print((e.read()))
            print('')
            raise e

def get_parts(client, ids):
    query = '''
    query get_parts($ids: [String!]!) {
        parts(ids: $ids) {
            id
            total_avail

            manufacturer {
                name
                is_verified
            }

            sellers{
                company{
                name
                }
            }
            mpn
            category {
                name
            }
        }
    }
    '''

    ids = [str(id) for id in ids]
    resp = client.execute(query, {'ids': ids})
    return json.loads(resp)['data']['parts']

def match_mpns(client, mpns):
    dsl = '''
    query match_mpns($queries: [PartMatchQuery!]!) {
        multi_match(queries: $queries) {
            hits
            reference
            parts {


                manufacturer {
                    name
                }
                mpn
            }
        }
    }
    '''

    queries = []
    for mpn in mpns:
        queries.append({
            'mpn_or_sku': mpn,
            'start': 0,
            'limit': 5,
            'reference': mpn,
        })
    resp = client.execute(dsl, {'queries': queries})
    return json.loads(resp)['data']['multi_match']

def demo_part_get(client):
    print('\n---------------- demo_part_get')
    ids = ["1", "2", "asdf", "4"]
    parts = get_parts(client, ids)

    for id, part in zip(ids, parts):
        print(id, '\t', part)

def demo_match_mpns(client):
    print('\n---------------- demo_match_mpns')
    mpns = [

        'B45197A6476K509V10'
    ]
    matches = match_mpns(client, mpns)

    for match in matches:
        for part in match['parts']:
            print(match['reference'], '\t', part['manufacturer']['name'], '\t', part['mpn'])

if __name__ == '__main__':
    client = GraphQLClient('https://octopart.com/api/v4/endpoint?token=bf42337c-bdb6-4190-9f3d-65ae1536659f')
    client.inject_token(os.getenv('OCTOPART_TOKEN'))
    demo_part_get(client)
    # demo_match_mpns(client)