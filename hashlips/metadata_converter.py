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
chiaCHIP = 'CHIP-0007' #enter the CHIP standard that your metadata follows (default is chip-0007)
nftNameConstant = 'NFT #' #enter the constant which appears in the NFT name, ex: "Monkeyzoo_collection #"
nftDescription = 'An NFT created by me' #enter the general description to be used for all NFTs
mintingTool = 'NFTr minting tool' #enter the tool to be used for minting the NFTs
sensitiveFlag = False #enter either True or False for whether your NFT has sensitive or explicit content
collectionName = 'My NFT Collection' #enter your NFT collection name
collectionID = 'a59a1a18-bce3-4688-9857-3a6cd4877745' #enter the NFT collection ID, this should be a UUID and you can generate one here: https://www.uuidgenerator.net/
collectionDescription = 'The first of many NFT collections that I will make on the Chia blockchain' #enter the NFT collection description
collectionIcon = 'https://www.nftr.pro/icon.png' #enter a url for the collection icon (pfp sized icon)
collectionBanner = 'https://www.nftr.pro/banner.png' #enter a url for the collection banner (wide image)
collectionTwitter = 'https://twitter.com/nftr_pro' #enter the twitter link of the collection or project
collectionWebsite = 'https://www.nftr.pro' #enter the collection or projects main website

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
