from django.conf import settings

# The minimum time between two counted visits (in minutes)
MIN_TIME_BETWEEN_VISITS = getattr(settings, 'MIN_TIME_BETWEEN_VISITS', 24 * 60)
IGNORE_URLS = getattr(settings, 'IGNORE_URLS', [])
IGNORE_USER_AGENTS = getattr(settings, 'IGNORE_USER_AGENTS', [])
BOTS_USER_AGENTS = getattr(
    settings,
    'BOTS_USER_AGENTS',
    [
        "Teoma", "alexa", "froogle", "Gigabot", "inktomi", "looksmart", "URL_Spider_SQL", "Firefly",
        "NationalDirectory", "Ask Jeeves", "TECNOSEEK", "InfoSeek", "WebFindBot", "girafabot", "crawler",
        "www.galaxy.com", "Googlebot", "Googlebot/2.1", "Google", "Webmaster", "Scooter", "James Bond",
        "Slurp", "msnbot", "appie", "FAST", "WebBug", "Spade", "ZyBorg", "rabaz", "Baiduspider",
        "Feedfetcher-Google", "TechnoratiSnoop", "Rankivabot", "Mediapartners-Google", "Sogou web spider",
        "WebAlta Crawler", "MJ12bot", "Yandex/", "YaDirectBot", "StackRambler", "DotBot", "dotbot"
    ]
)

REQUEST_FIELDS_FOR_HASH = getattr(settings, 'REQUEST_FIELDS_FOR_HASH', ['REMOTE_ADDR', 'HTTP_USER_AGENT'])
URI_WITH_GET_PARAMS = getattr(settings, 'URI_WITH_GET_PARAMS', False)
VISITS_OBJECTS_AS_COUNTERS = getattr(settings, 'VISITS_OBJECTS_AS_COUNTERS', True)
