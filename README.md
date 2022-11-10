# nft_scripts
Repo for scripts that aid with the creation, normalization, or verification of NFTs on the Chia blockchain. Most of these scripts are standalone and a culmination of multiple developers efforts.

# scripts included:
## hashlips metadata converter
This script converts the metadata created by the generative art software [hashlips](https://github.com/HashLips/hashlips_art_engine) into metadata that is compliant with CHIP-0007 from Chia.

To use this script you will need to identify the file locations where Hashlips created the metadata files then fill in the fields within the script pertaining to your project.

Open this script to review where and how files need to be stored, contact the NFTr team with any questions.

### Contributors:
This script was originally created by Maxim Goods and later updated by the MonkeyZoo team, the NFTr team, and a number of other devs. Message the NFTr team if you would like to be included in the contributors list.

## metadata attributes updater
This script updates the values of attributes based on an update.csv file.
The update.csv file should contain the old and new values separated by a comma (do not use spaces around the comma)
All of the metadata files you need to update should be in a folder named "old_metadata"
This script and update.csv file will need to be in the same directory as your old_metadata folder

Contact the NFTr team with any questions.

### Contributors:
This script was originally created by ClydeWallace for use by the MonkeyZoo team.
Message the NFTr team if you would like to be included in the contributors list.
