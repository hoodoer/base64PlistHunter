# base64PlistHunter

Sometimes extracting PLIST files from cache.db provides you with PLISTs that have binary PLISTs base64 encoded in them. <br>
plistsubstractor and plistsubstractor3 aren't going to catch these, as biplist libraries can't really work with bplists in this <br>
format. <br><br>
This script will take an ascii PLIST/XML file, extract all base64 strings from it, create binary PLIST files from it<br>
and test to see if its a valid binary plist. It cleans up after itself, and leaves you with extracted binary plist files. <br><br>

@hoodoer<br>
hooder@bitwisemunitions.dev
