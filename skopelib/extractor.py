#!/usr/bin/env python

"""Example extractor based on the clowder code.""" 
import os
import logging 
import json
from pyclowder.extractors import Extractor


def add_arguments(parser):
    """Add extra arguments specific to ALL skope extractors."""
    pass


class SkopeExtractor(Extractor):
    """A basic extension to the pyclowder Extractor class providing
    the basic capabilities for interacting with SKOPE infrastructure.

    Note: the pyclowder extractor is responsible for setting up the 
    argparser and parsing command line args. This should be removed 
    or handled better.
    """

    def __init__(self):

        super(SkopeExtractor, self).__init__()

        add_arguments(self.parser)


    def setup(self):
        """initialization phase 2 - required by pyclowder Extractor"""

        super(SkopeExtractor, self).setup()

        self.clowder = Clowder(args=self.args)


    def check_message(self, connector, host, secret_key, resource,
                      parameters):

        #TODO: Later can be used to check the integrity of the metadata info
        return CheckMessage.bypass

    
    def process_message(self, connector, host, secret_key, resource, 
                        parameters):

        logger = logging.getLogger(__name__)

        #TODO: Make sure that all the metadata info are relavant only 
        # to the dataset

        #TODO: Check that the dataset info that we get is actualy related 
        #TODO: to the newly added metadata

        # Get dataset info and all the newly added metadata info
        ds_info = pyclowder.datasets.get_info(connector, host, secret_key, 
                                              resource['parent']['id'])
        index_id = resource['parent']['id']
        logger.debug("The relevant dataset name is "+ ds_info['name'])
        newly_added_metadata = resource['metadata']
        
        #TODO: Check that the newly_added_metadata info actully has
        #TODO: All the info

        #TODO: Connect through container
        #TODO: Do we have a unified doc type?
        es = Elasticsearch()
        es.index(index=ds_info['name'], doc_type='dataset_meta', id=index_id, 
                body=json.loads(resource['metadata']))
        logger.debug("Finished uploading the metadata to the elastic serach")
       
