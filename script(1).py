# import required modules
import os
import json
import shutil

# assign input / output directories
directory_in = 'hashlips_images'
directory_out = 'images'
json_directory_in = 'hashlips_json'
json_directory_out = 'json'

# set project specifics
chiaCHIP = 'CHIP-0007'
nftNameConstant = 'Monkeyzoo_collection #'
nftDescription = 'NFT1 special edition Monkeyzoo collection'
mintingTool = 'NFTr minting tool'
sensitiveFlag = False
collectionName = 'Monkeyzoo_collection'
collectionID = '3d63a115-c341-471c-8e50-377c4cb67f40'
collectionDescription = 'The first ever Monkeyzoo NFTs. A Monkeyzoo special edition to commemorate the launch of NFT1 launching on the Chia blockchain'
collectionIcon = 'https://pbs.twimg.com/profile_images/1542615309969985536/wK9gfnMV_400x400.png'
collectionBanner = 'https://pbs.twimg.com/profile_banners/14711228/1656623125/600x200'
collectionTwitter = 'https://twitter.com/monkeyzoo'
collectionWebsite = 'https://www.monkeyzoo.net'

# globals
index = 1
metadata = []
 
# iterate over files in directory_in
for filename in os.listdir(directory_in):
    f = os.path.join(directory_in, filename)
    # checking if it is a file
    if os.path.isfile(f):
        filename_json_in = os.path.splitext(filename)[0] + ".json"
        filename_img_out = os.path.splitext(filename)[0] + ".png"
        filename_json_out = os.path.splitext(filename)[0] + ".json"
        print(filename)    # output to user that we're making progress, can be commented out

        # read json
        f = open(os.path.join(json_directory_in, filename_json_in))
        data_in = json.load(f)
        f.close()
        
        # create output json
        data_out = {}
        data_out['format'] = chiaCHIP
        data_out['name'] = nftNameConstant + os.path.splitext(filename)[0]
        data_out['description'] = nftDescription
        data_out['minting_tool'] = mintingTool
        data_out['sensitive_content'] = sensitiveFlag
        data_out['attributes'] = data_in['attributes']

        data_out['collection'] = {}
        data_out['collection']['name'] = collectionName
        data_out['collection']['id'] = collectionID
        data_out['collection']['attributes'] = [
            {'type':'description', 'value' : collectionDescription},
            {'type':'icon', 'value': collectionIcon},
            {'type':'banner', 'value': collectionBanner},
            {'type':'twitter', 'value': collectionTwitter},
            {'type':'website', 'value': collectionWebsite}
        ]
        
        # write json for the image
        with open(os.path.join(json_directory_out, filename_json_out), 'w') as outfile:
            json.dump(data_out, outfile, indent=2)

        # add json to metadata.json file (contains all individual image json files combined)
        metadata.append(data_out)

        # copy img to final folder
        shutil.copyfile(os.path.join(directory_in, filename), os.path.join(directory_out, filename_img_out))        
        
        index = index + 1
  
# write metadata
with open(os.path.join(json_directory_out, 'metadata.json'), 'w') as outfile:
    json.dump(metadata, outfile, indent=2)