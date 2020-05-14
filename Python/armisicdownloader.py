import requests
import urllib.request

def downloader(errorIds=[]):
    url = 'https://isic-archive.com/api/v1/image?limit=0&sort=name&sortdir=1&offset=0'
    # Get the images metadata
    response = requests.get(url, stream=True)
    # Parse the metadata
    meta_data = response.json()
    ids = [meta_data[index]['_id'] for index in range(len(meta_data))]
    names = [meta_data[index]['name'] for index in range(len(meta_data))]
    print("Total Images: " + str(len(ids)))

    #save the image ids of failed downloads here
    errorIds = errorIds
    for i in range(len(ids)):
        try:
            id = ids[i]
            name = str(names[i]) + ".jpg"
            url = 'https://isic-archive.com/api/v1/image/{id}/download'.format(id=id)
            urllib.request.urlretrieve('https://isic-archive.com/api/v1/image/{id}/download'.format(id=id), name)
            
            print("Downloaded " + str(i) +" items, last is " + name)

        except Exception as e:
            print('An exception occurred with')
            print(e)
            print('ID: {id}')
            #save the error in a list to reiterate over them again
            errorIds.append(id)
            # Open a file with access mode 'a'
            file_object = open('errors.txt', 'a')

            file_object.write(id)
            file_object.write("\n")
            file_object.write(str(e))
            file_object.write("\n")
            file_object.write(name)
            file_object.write("\n")
            file_object.write("-------------")
            
            # Close the file
            file_object.close()
    return errorIds

errorIds = downloader()
while len(errorIds) != 0:
    errorIds = downloader(errorIds)


