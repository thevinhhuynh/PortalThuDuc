import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

SITEURL = "http://thuduc-portal.hcmgis.vn/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "geonode",
        "USER": "geonode",
        "PASSWORD": "geonode",
        "HOST" : "192.168.1.107",
        "PORT" : "6432",
    },
    # vector datastore for uploads
    "datastore" : {
       "ENGINE": "django.contrib.gis.db.backends.postgis",
       "NAME": "geonode_imports",
       "USER" : "geonode",
       "PASSWORD" : "geonode",
       "HOST" : "192.168.1.107",
       "PORT" : "6432",
    }
}

# OGC (WMS/WFS/WCS) Server Settings
# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    "default": {
        "BACKEND": "geonode.geoserver",
        "LOCATION": "http://localhost:8080/geoserver/",
        "PUBLIC_LOCATION": "http://thuduc-portal.hcmgis.vn/geoserver/",
        "USER": "admin",
        "PASSWORD": "S@g0g1s273",
        "MAPFISH_PRINT_ENABLED": True,
        "PRINT_NG_ENABLED": True,
        "GEONODE_SECURITY_ENABLED": True,
        "GEOGIG_ENABLED": False,
        "WMST_ENABLED": False,
        "BACKEND_WRITE_ENABLED": True,
        "WPS_ENABLED": False,
        "LOG_FILE": "%s/geoserver/data/logs/geoserver.log" % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to name of database in DATABASES dictionary to enable
        "DATASTORE": "datastore",
        "TIMEOUT": 2000  # number of seconds to allow for HTTP requests
    }
}
