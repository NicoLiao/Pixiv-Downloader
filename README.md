<p align=center>
<img target = "banner" src="https://github.com/NicoLiao/Pixiv-Downloader/blob/main/img/banner.png?raw=true">
</p>

<p align=center>
<a target="badge" href="https://github.com/NicoLiao/Pixiv-Downloader" title="python version"><img src="https://img.shields.io/badge/python-v3.9.6-blue"></a>
<a target="badge" href="https://github.com/NicoLiao/Pixiv-Downloader" title="windows badge"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" width=85/></a>  
</p>

>This is a software to download pictures from pixiv. It can download the top 50 pictures per day from the daily ranking page.

All images comes from https://www.pixiv.net/ranking.php/

# Install
## Release 
Download exe as follow: https://github.com/NicoLiao/Pixiv-Downloader/releases/tag/v1.0


## Download source code
In order to use Pixiv Downloader, make sure that you have python 3.9.6 and python packages as below:
requests 2.27.1
pyinstaller 4.10
regex 2022.1.18
```
$ git clone https://github.com/NicoLiao/Pixiv-Downloader
```
## Usage
### Visual Studio Code
Download VSCode https://code.visualstudio.com/
Download python https://www.python.org/
After installing VScode and Python, download the extension in VSCode as follow:
* python
* python for vscode
* code runner

Done it and Run code

### Build exe
Using terminal and pyinstaller to build exe
```
$ pyinstaller -F crawlpixiv.py -c --icon=logo.ico
```
