# Vivo Music 歌单导出器

## 简介
Vivo Music 歌单导出器是一个用于从Vivo Music网站的公开歌单中提取歌曲信息，并将其导出为Excel文件的Python脚本。此项目旨在帮助用户以电子表格形式管理和分析他们的音乐收藏。

## 功能
- 从Vivo Music的公开歌单页面抓取歌曲信息。
- 提取歌曲名称和艺术家信息。
- 将提取的数据导出到Excel文件。

## 安装
确保您的系统已安装Python 3.x。此外，您需要安装以下库：
- BeautifulSoup4
- pandas
- openpyxl

您可以使用pip安装所需的库：
```bash
pip install beautifulsoup4 pandas openpyxl
```

##使用方法
1.打开你的歌单分享链接，按下F12检查网页元素，找到songlist元素，编辑HTML内容，再将您的Vivo Music歌单页面的HTML内容保存到脚本代码的对应变量中。
2.运行脚本，它会解析HTML内容并提取歌曲信息。
3.提取的信息将被输出至终端并保存在同目录下的songs.xlsx文件中。

### 说明
- **目的**：因为某人的歌单在vivo手机里面的imusic，我试了一下看怎么能把它弄出来，于是用了这个仓库。
