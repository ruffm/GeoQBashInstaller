#import os

#api_key = u'd391941c0e04c8364c436e7a78e431a4'
#api_secret = u'e9ce6c0073370b8c'

#f = flickrapi.FlickrAPI(api_key, api_secret, format='etree')
#flickr.authenticate_via_browser(perms='read')

#for photo in f.walk(tags='sra111'):
#info=[photo.get('id'), photo.get('owner'), photo.get('title')]

#photo_id=str(info[0])
#ownerNum=str(info[1])
#picTitle=str(info[2])

#exif=f.photos_getExif(photo_id=photo_id)

#print(photo_id) # type is str
#print(ownerNum) # type is str
#print(picTitle) # type is str'
#print("")

#openFile=open('output3File.txt', 'a')
#openFile.write(photo_id + " " + ownerNum + " " + picTitle + "\n")
#openFile.close()



api_key = u'd391941c0e04c8364c436e7a78e431a4'
api_secret = u'e9ce6c0073370b8c'

def get_photo_info(api_key, photo_id): f = flickrapi.FlickrAPI(api_key)


#flickr.authenticate_via_browser(perms='read')

info=f.photos_getInfo(photo_id=photo_id)
title = info.photo[0].title[0].text
desc = info.photo[0].description[0].text
url = info.photo[0].urls[0].url[0].text
#tags = ' '.join([&quot;%s&quot; % (tag.text) for tag in info.photo[0].tags[0].tag])

exif = f.photos_getExif(photo_id=photo_id)
model = exif.photo[0].exif[1].raw[0].text
date_taken = exif.photo[0].exif[2].raw[0].text
exposure = exif.photo[0].exif[4].raw[0].text
aperture = exif.photo[0].exif[5].clean[0].text
exposure_prg = exif.photo[0].exif[6].clean[0].text
iso = exif.photo[0].exif[7].raw[0].text
exif_details = dict(model=model, date_taken=date_taken, exposure=exposure, aperture=aperture, exposure_prg = exposure_prg, iso=iso)
#we need to add a line for lat and long

#getSize gets both size (thumbnails etc) and corresponding urls
sizes = f.photos_getSizes(photo_id=photo_id, format='json')
#there should be a better way to do the below
#flickr returns jsonflickrapi(....) as string
#i am retriving the values
sizes = simplejson.loads(sizes[14:-1])['sizes']['size']
for size in sizes:
    if size.has_key('label'):
    	if size['label'] == 'Square':
            thumb_url    = size['url']
            thumb_height = size['height']
            thumb_width  = size['width']
            thumb_source = size['source']
    	if size['label'] == 'Large':
            photo_url    = size['url']
            photo_height = size['height']
            photo_width  = size['width']
            photo_source = size['source']
		#return dict(title=title, desc=desc, tags = tags, exif=exif_details, thumb=thumb_details, photo=photo_details)
	
	
thumb_details = dict(url=thumb_url, height=thumb_height, width = thumb_width, source=thumb_source)
photo_details = dict(url=photo_url, height = photo_height, width = photo_width, source=photo_source)	

return dict(title=title, desc=desc, tags = tags, exif=exif_details, thumb=thumb_details, photo=photo_details)
