BOT_NAME = 'permanenttsb'

SPIDER_MODULES = ['permanenttsb.spiders']
NEWSPIDER_MODULE = 'permanenttsb.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'permanenttsb.pipelines.PermanenttsbPipeline': 100,

}