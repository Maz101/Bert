LANG_CODE="en" #@param {type:"string"}
wget http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2016/mono/OpenSubtitles.raw.'$LANG_CODE'.gz -O dataset.txt.gz
gzip -d dataset.txt.gz
tail dataset.txt
