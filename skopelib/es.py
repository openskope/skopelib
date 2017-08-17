def add_arguments(parser):
    """Add extra arguments specific to the MetadataExtractor class."""

    parser.add_argument('--elasticsearch-url', 
            default=os.environ.get('ELASTICSEARCH_URL', 
                                   'http://elasticsearch:9200'),
            help='set the location of ElasticSearch (default='
                 'ELASTICSEARCH_URL | http://elasticsearch:9200)')
    parser.add_argument('--elasticsearch-index',
            default=os.environ.get('ELASTICSEARCH_INDEX', 'products'),
            help='name of the ElasticSearch index to be updated (default='
                 'ELASTICSEARCH_INDEX | products)')

