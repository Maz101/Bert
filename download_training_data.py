AVAILABLE =  {'af','ar','bg','bn','br','bs','ca','cs',
              'da','de','el','en','eo','es','et','eu',
              'fa','fi','fr','gl','he','hi','hr','hu',
              'hy','id','is','it','ja','ka','kk','ko',
              'lt','lv','mk','ml','ms','nl','no','pl',
              'pt','pt_br','ro','ru','si','sk','sl','sq',
              'sr','sv','ta','te','th','tl','tr','uk',
              'ur','vi','ze_en','ze_zh','zh','zh_cn',
              'zh_en','zh_tw','zh_zh'}

LANG_CODE = "en" #@param {type:"string"}

assert LANG_CODE in AVAILABLE, "Invalid language code selected"

!wget http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2016/mono/OpenSubtitles.raw.'$LANG_CODE'.gz -O dataset.txt.gz
!gzip -d dataset.txt.gz
!tail dataset.txt
