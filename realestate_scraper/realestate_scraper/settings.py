# settings.py

BOT_NAME = "realestate_scraper"
SPIDER_MODULES = ["realestate_scraper.spiders"]
NEWSPIDER_MODULE = "realestate_scraper.spiders"

# Enable Splash
SPLASH_URL = "http://localhost:8050"

# Enable middleware
DOWNLOADER_MIDDLEWARES = {
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
}

# Enable Splash as a downloader backend
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"
HTTPCACHE_STORAGE = "scrapy_splash.SplashAwareFSCacheStorage"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
