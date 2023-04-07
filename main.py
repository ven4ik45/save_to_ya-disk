import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать

    def get_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
            }
        return headers

    # def get_files_list(self, path_to_file):
    #     headers = self.get_headers()
    #     response = requests.get(url=path_to_file, headers=headers)
    #     return response.json()

    def get_upload_url(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        parameters = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(url=upload_url, headers=headers, params=parameters)
        return response.json()

    def upload(self, path_to_file):
        json_data = self.get_upload_url(path_to_file)
        print(json_data)
        headers = self.get_headers()
        parameters = {'path': path_to_file, 'overwrite': 'true'}
        link_to_upload = json_data['href']
        abc = requests.put(link_to_upload, data=open(path_to_file, 'r'))
        print()




if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'file67d.txt'
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

