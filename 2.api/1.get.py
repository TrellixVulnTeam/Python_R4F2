import requests

if __name__ == '__main__':
    #url = 'http://httpbin.org/get?nombre=jose&curso=python'
    url = 'http://httpbin.org/get'
    args = {'nombre': 'jose', 'curso': 'python'}
    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        content = response.content
        print(content)
