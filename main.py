import pandas as pd
from bs4 import BeautifulSoup

def extract_songs_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找所有包含歌曲信息的div
    songs_divs = soup.find_all('div', class_='list-item')
    songs_info = []

    for div in songs_divs:
        song_name = div.find('p', class_='songName').get_text()
        artist = div.find('div', class_='singers').p.get_text()
        songs_info.append({'song': song_name, 'artist': artist})

    return songs_info


# 用您的HTML内容替换这里的html_content
html_content = """<div class="song-list-content"><div class="list-item"><div class="cover"><img src="https://image.tingmall.com/album/394/3948481-JPG-320X320-ALBUM.jpg?t=1691743155000" alt=""></div> <div class="song"><p class="songName">潮湿的心(DJ版)</p> <div class="singers"><span class="vip-icon"></span> <p class="line-clamp-1 last">寂悸</p> <span class="line">-</span> <p class="line-clamp-1 mw4">潮湿的心(DJ版)</p></div></div> <div class="play"><img src="https://imusich5static.vivo.com.cn/imusich5static.vivo.com.cn/static/img/h5_button_play.fe5be54.png" alt=""></div></div><div class="list-item"><div class="cover"><img src="https://image.tingmall.com/album/101/1012557-JPG-320X320-ALBUM.jpg?t=1698226818000" alt=""></div> <div class="song"><p class="songName">多幸运</p> <div class="singers"><span class="vip-icon"></span> <p class="line-clamp-1 last">韩安旭</p> <span class="line">-</span> <p class="line-clamp-1 mw4">多幸运</p></div></div> <div class="play"><img src="https://imusich5static.vivo.com.cn/imusich5static.vivo.com.cn/static/img/h5_button_play.fe5be54.png" alt=""></div></div><div class="list-item"><div class="cover"><img src="https://image.tingmall.com/album/373/3738712-JPG-320X320-ALBUM.jpg?t=1691743154000" alt=""></div> <div class="song"><p class="songName">殇雪(DJ版)</p> <div class="singers"><span class="vip-icon"></span> <p class="line-clamp-1 last">暴林</p> <span class="line">-</span> <p class="line-clamp-1 mw4">殇雪(DJ版)</p></div></div> <div class="play"><img """

songs = extract_songs_from_html(html_content)
for song_info in songs:
    print(f"歌曲: {song_info['song']}, 艺术家: {song_info['artist']}")

# 将歌曲信息打印到控制台
for song_info in songs:
    print(f"歌曲: {song_info['song']}, 艺术家: {song_info['artist']}")

# 将歌曲信息保存到DataFrame
df = pd.DataFrame(songs)

# 将DataFrame保存为Excel文件
df.to_excel('songs.xlsx', index=False)