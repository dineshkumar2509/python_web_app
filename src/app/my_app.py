import json
import sys
from html import escape
from urllib.parse import parse_qs

headers = [('content-type', 'application/json')]


def option1_request(method, data):
    print("option1 request start - " + method)

    return True, {}


def option2_request(method, data):
    print("option2 request start - " + method)

    return True, {}


def my_app(env, start_response):
    print("my_app app request start")

    req_method = env.get('REQUEST_METHOD')
    req_uri = env.get('PATH_INFO')
    if not req_method or not req_uri or (req_method != 'GET' and req_method != 'POST'):
        print("Unknown method")
        start_response('200 OK', headers)
        return [bytes(json.dumps({'status': 'error: Unknown method'}), 'utf-8')]

    if req_method.upper() == 'POST':
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
        request_body = env['wsgi.input'].read(request_body_size)
        request_dict = json.loads(request_body.decode("utf-8"))
    else:
        request_dict = parse_qs(env['QUERY_STRING'])

    response_dict = {}
    is_success = False
    if req_uri == '/option1':
        (is_success, response_dict) = option1_request(req_method, request_dict)
    elif req_uri == '/option2':
        (is_success, response_dict) = option2_request(req_method, request_dict)

    if is_success:
        response_dict.update({'status': 'success'})
    else:
        response_dict.update({'status': 'error'})
    start_response('200 OK', headers)
    return [bytes(json.dumps(response_dict), 'utf-8')]
