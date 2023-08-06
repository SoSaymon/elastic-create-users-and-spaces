import os

from dotenv import load_dotenv


ElasticUrl = str
KibanaUrl = str
Username = str
Password = str


load_dotenv()
get_env = os.environ.get


def get_all_env() -> (ElasticUrl, KibanaUrl, Username, Password):
    """
        Get all environment variables.

        :return:  A tuple of environment variables.
    """
    elastic_url = get_env('ELASTICSEARCH_URL')
    kibana_url = get_env('KIBANA_URL')
    username = get_env('ELASTICSEARCH_USERNAME')
    password = get_env('ELASTICSEARCH_PASSWORD')

    return elastic_url, kibana_url, username, password
