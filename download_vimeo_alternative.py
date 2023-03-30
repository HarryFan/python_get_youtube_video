import re
import requests

def download_video(url, output_path='.'):
    try:
        print(f'正在下載影片: {url}')
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("無法訪問網頁")
        
        html_content = response.text
        video_title = re.search('<title>(.*?)</title>', html_content).group(1)
        video_url = re.search(',"url":"(.*?)"', html_content).group(1).replace('\\/', '/')
        video_ext = video_url.split(".")[-1]

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
    output_path = input('請輸入儲存路徑（預設為當前目錄）: ') or '.'
    download_video(video_url, output_path)
