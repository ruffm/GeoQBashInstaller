import flickrapi
import flickr_api
import json
import os

api_key = u' '
api_secret = u' '

f = flickrapi.FlickrAPI(api_key, api_secret, format='etree')
# flickr.authenticate_via_browser(perms='read')

for photo in f.walk(tags=' '): # put tag to search for in ' '
    info=[photo.get('id'), photo.get('owner'), photo.get('title')]

    photo_id=str(info[0])
    ownerNum=str(info[1])
    picTitle=str(info[2])

    exif=f.photos_getExif(photo_id=photo_id)

    print(photo_id) # type is str
    print(ownerNum) # type is str
    print(picTitle) # type is str'
    print("")

    openFile=open('outputFile.txt', 'a')
    openFile.write(photo_id + " " + ownerNum + " " + picTitle + "\n")
    openFile.close()

    # POTENTIAL CODE BELOW:
    # model = exif.photo[0].exif[1].raw[0].text
    # date_taken = exif.photo[0].exif[2].raw[0].text
    # exposure = exif.photo[0].exif[4].raw[0].text
    # aperture = exif.photo[0].exif[5].clean[0].text
    # exposure_prg = exif.photo[0].exif[6].clean[0].text
    # iso = exif.photo[0].exif[7].raw[0].text
    # exif_details = dict(model=model, date_taken=date_taken, exposure=exposure, aperture=aperture,
    #                    exposure_prg=exposure_prg, iso=iso)
    # get_photo_info(api_key, photo_id)


