# television plugin edited by notec
# -*- coding: utf-8 -*-

# for more info please visit www

import xbmcgui,xbmcplugin 
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty( "Fanart_Image", img )
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)


add_video_item('https://nrk1us-f.akamaihd.net/i/nrk1us_0@102847/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': '  - [B][COLOR yellowgreen] - [/COLOR] [COLOR red]NORWAY [/COLOR] [COLOR white]- [/B][/COLOR] -'},img='special://home/addons/plugin.video.nodktv/resources/art/no.png')

add_video_item('https://nrk1us-f.akamaihd.net/i/nrk1us_0@102847/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 1 (NO)'},img='special://home/addons/plugin.video.nodktv/resources/art/nrk1.png')
add_video_item('https://nrk2us-f.akamaihd.net/i/nrk2us_0@107231/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 2 (NO)'},img='special://home/addons/plugin.video.nodktv/resources/art/nrk2.png')
add_video_item('https://nrk3us-f.akamaihd.net/i/nrk3us_0@107233/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 3 (NO)'},img='special://home/addons/plugin.video.nodktv/resources/art/nrk3.png')

add_video_item('http://dr01-lh.akamaihd.net/i/dr01_0@147054/master.m3u8?b=100-2000|X-Forwarded-For=77.66.34.57',{ 'title': '  - [B][COLOR yellowgreen] - [/COLOR] [COLOR white]DENMARK [/COLOR] [COLOR white]- [/B][/COLOR] -'},img='special://home/addons/plugin.video.nodktv/resources/art/dk.png')

add_video_item('http://dr01-lh.akamaihd.net/i/dr01_0@147054/master.m3u8?b=100-2000|X-Forwarded-For=77.66.34.57',{ 'title': 'DR 1 (DK)'},img='special://home/addons/plugin.video.nodktv/resources/art/dr_1.png')
add_video_item('http://dr02-lh.akamaihd.net/i/dr02_0@147055/master.m3u8?b=100-2000|X-Forwarded-For=77.66.34.57',{ 'title': 'DR 2 (DK)'},img='special://home/addons/plugin.video.nodktv/resources/art/dr_2.png')
add_video_item('http://dr03-lh.akamaihd.net/i/dr03_0@147056/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DK 3 (DK)'},img='special://home/addons/plugin.video.nodktv/resources/art/dr_3.png')
add_video_item('http://dr04-lh.akamaihd.net/i/dr04_0@147057/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DR K (DK)'},img='special://home/addons/plugin.video.nodktv/resources/art/dr_k.png')
add_video_item('http://dr06-lh.akamaihd.net/i/dr06_0@147059/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DK Ultra (DK)'},img='special://home/addons/plugin.video.nodktv/resources/art/dr_u.png')

add_video_item('http://tv2danmark-tv2fri-live.hls.adaptive.level3.net/tv2danmark/tv2fri/master.m3u8',{ 'title': 'TV 2 Fri(DK)'},img='special://home/addons/plugin.video.nodktv/resources/art/tv2f.png')
add_video_item('http://tv2danmark-tv2zulu-live.hls.adaptive.level3.net/tv2danmark/tv2zulu/master.m3u8',{ 'title': 'TV 2 Zulu(DK)'},img='special://home/addons/plugin.video.nodktv/resources/art/tv2z.jpg')
add_video_item('http://tv2danmark-tv2charlie-live.hls.adaptive.level3.net/tv2danmark/tv2charlie/master.m3u8',{ 'title': 'TV 2 Charlie (DK)'},img='special://home/addons/plugin.video.nodktv/resources/art/tv2c.png')
add_video_item('http://tv2danmark-tv2lorry-live.hls.adaptive.level3.net/tv2danmark/tv2lorry/master.m3u8',{ 'title': 'TV 2 (Lorry)'},img='special://home/addons/plugin.video.nodktv/resources/art/tv2l.png')

add_video_item('https://svt11-lh.akamaihd.net/i/svt11_0@77506/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': '  - [B] - [COLOR yellowgreen] MORE CHANNELS [/COLOR] - [/B] -'},img='special://home/addons/plugin.video.nodktv/resources/art/flag.png')
add_video_item('http://dr05-lh.akamaihd.net/i/dr05_0@147058/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DR Ramasjang (DK)'},img='special://home/addons/plugin.video.nodktv/resources/art/dr_r.png')
add_video_item('https://nrksuper-lh.akamaihd.net/i/nrksupertvus_0@108447/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK Super (NO)'},img='special://home/addons/plugin.video.nodktv/resources/art/nrk_s.png')
add_video_item('https://nrktegnsprak-lh.akamaihd.net/i/nrktegnsprak_0@111177/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK Tegnsprak (NO)'},img='special://home/addons/plugin.video.nodktv/resources/art/nrk_t.png')


xbmcplugin.endOfDirectory(plugin_handle)
