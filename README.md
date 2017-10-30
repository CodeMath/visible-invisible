# visible-invisible
2017 한양대학교 엔터테인먼트디자인학과 인터렉티브 작품

## must install
<pre><code>Python2.7
opencv
zbar
redis-server</pre></code>
[refr link1](https://github.com/zplab/zbar-py) and  [refer link2](https://sourceforge.net/p/zbar/discussion/664595/thread/875f2242/) and [refer link3](https://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/)

## pip install list
<pre><code>certifi==2017.7.27.1
chardet==3.0.4
click==6.7
Flask==0.12.2
idna==2.5
itsdangerous==0.24
Jinja2==2.9.6
MarkupSafe==1.0
numpy==1.13.1
olefile==0.44
pathlib==1.0.1
Pillow==4.2.1
redis==2.10.5
requests==2.18.3
urllib3==1.22
Werkzeug==0.12.2
zbar==0.10</code></pre>

## how to run
<pre><code>
1) run redis-server
2) we need a two terminal on virtual enviorment.
- run flask web server.
- run opencv for detecting qr-code image to return center of the image.
3) send a data that center of the qr-code image through SSE.
4) cool.
</pre></code>

## result image
<figure>
<img src="https://github.com/CodeMath/visible-invisible/tree/master/download/screencapture-127-0-0-1-5000-fin-1508513193141.png">
<img src="https://github.com/CodeMath/visible-invisible/tree/master/download/screencapture-127-0-0-1-5000-fin-1508567557016.png">

</figure>

