import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
            }
        return headers

    def get_upload_url(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        parameters = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(url=upload_url, headers=headers, params=parameters)
        return response.json()

    def upload(self, path_to_file: str):
        json_data = self.get_upload_url(path_to_file)
        print(json_data)
        link_to_upload = json_data['href']
        requests.put(link_to_upload, data=open(path_to_file, 'r'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'file67d.txt'
    token = '...'
    uploader = YaUploader(token)
    uploader.upload(path_to_file)

