from pytube import YouTube

def download_youtube_video(video_url, output_path='.'):
    try:
        # 建立 YouTube 物件
        yt = YouTube(video_url)

        # 選擇最高畫質的影片版本
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # 下載影片
        print(f'正在下載影片: {yt.title}')
        video.download(output_path)
        print(f'下載完成: {yt.title}.mp4 已儲存到 {output_path}')

    except Exception as e:
        print(f'下載時發生錯誤: {e}')

if __name__ == '__main__':
    video_url = input('請輸入 YouTube 影片網址: ')
    output_path = input('請輸入儲存路徑（預設為當前目錄）: ') or '.'
    download_youtube_video(video_url, output_path)