from lxml import etree
import re
import sys
import time
import urllib.error
import urllib.request

def usage():
    print('USAGE: python3 parse.py <YOUTUBE_playlist_url>')
    print('       YOUTUBE_playlist_url: link to a youtube playlist (mandatory)')
    exit(1)

def get_video_name(url):
    youtube = etree.HTML(urllib.request.urlopen(url).read())
    video_title = youtube.xpath("//span[@id='eow-title']/@title")
    # print (''.join(video_title))
    return (''.join(video_title))

def extract_playlist_url(url):
    if 'list=' in url:
        eq_pos = url.index('=') + 1
        cPL = url[eq_pos:]
        if '&' in url:
            amp = url.index('&')
            cPL = url[eq_pos:amp]
        return cPL
    else:
        print('Incorrect Playlist link. Please Check the playlist url.')
        exit(1)

def get_video_url_list(url, cPL):
    try:
        yTUBE = urllib.request.urlopen(url).read()
        sTUBE = str(yTUBE)
    except urllib.error.URLError as e:
        print(e.reason)

    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    return re.findall(tmp_mat, sTUBE)

def clean_video_url(PL):
    yPL = str(PL)
    if '&' in yPL:
        yPL_amp = yPL.index('&')
    return ('http://www.youtube.com/' + yPL[:yPL_amp])

def crawl(url):
    sTUBE = ''
    cPL = ''
    amp = 0
    final_url = []
    song_titles = []
    # Exract the part that identifies the playlist from the playlist url
    cPL = extract_playlist_url(url)

    # Extract all the videos urls
    mat = get_video_url_list(url, cPL)
    if mat:
        mat_set = set(mat)
        for PL in mat_set:
            final_url.append(clean_video_url(PL))
        url_set = set(final_url)

        for url in url_set:
            # sys.stdout.write(url + '\n')
            song_titles.append(get_video_name(url))
            time.sleep(0.04)
    else:
        print('No videos found. Please check playlist url.')
        exit(1)

    return song_titles

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        usage()
    else:
        url = sys.argv[1]
        if 'http' not in url:
            url = 'http://' + url
        song_titles = crawl(url)
        for title in song_titles:
            print (title)