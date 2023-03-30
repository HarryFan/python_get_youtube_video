import re
import requests
import os
import json

def download_video(url, output_path='video/vimeo'):
    try:
        print(f'正在下載影片: {url}')
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("無法訪問網頁")

        html_content = response.text
        video_title = re.search('<title>(.*?)</title>', html_content).group(1)

        config_url_match = re.search(r'config_url":"(.*?)"', html_content)
        if not config_url_match:
            raise Exception("無法找到 config_url")

        config_url = config_url_match.group(1).replace('\\/', '/')
        config_response = requests.get(config_url)
        if config_response.status_code != 200:
            raise Exception("無法訪問 config_url")

        config_data = json.loads(config_response.text)
        video_url = config_data["request"]["files"]["progressive"][0]["url"]
        video_ext = video_url.split(".")[-1]

        # 創建儲存路徑，如果不存在
        os.makedirs(output_path, exist_ok=True)

        video_response = requests.get(video_url)
        if video_response.status_code != 200:
            raise Exception("無法訪問影片文件")

        with open(f"{output_path}/{video_title}.{video_ext}", "wb") as f:
            f.write(video_response.content)

        print(f'下載完成，已儲存到 {output_path}')
    except Exception as e:
        print(f'下載時發生錯誤: {e}')

if __name__ == '__main__':
    video_url = input('請輸入 Vimeo 影片網址: ')
    output_path = input('請輸入儲存路徑（預設為當前目錄的 video/vimeo 資料夾）: ') or 'video/vimeo'
    download_video(video_url, output_path)
