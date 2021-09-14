from ..api.aradial_gateway.create_user import AradialAPIGatewayCreateUser
from ..api.aradial_gateway.get_user import AradialAPIGatewayGetUser
from ..api.aradial_gateway.update_user import AradialAPIGatewayUpdateUser
from odoo import api, fields, models, exceptions, _
from psycopg2.extensions import AsIs
import datetime
import logging

from awb_aradial_connector.api.aradial_gateway import update_user

_logger = logging.getLogger(__name__)

class AWBAradialConnector(models.Model):

    _name = 'aradial.connector'
    _description = 'AWB Aradial Connector'

    def __init__(self):
        params = self.env['ir.config_parameter'].sudo()
        self.aradial_url = params.get_param('aradial_url')
        self.aradial_username = params.get_param('aradial_username')
        self.aradial_password = params.get_param('aradial_password')


    def create_user(
        self, 
        data
    ):

        _logger.info("Create User")
        
        user = AradialAPIGatewayCreateUser(
            url=self.aradial_url,
            username=self.aradial_username,
            password=self.aradial_password,
            data=data
        )
        created_user = user.create_user()

        _logger.info("User Creation: %s" % created_user)

        if created_user == "Success":
            return True
        else:
            return False

    def get_remaining_time(
        self, 
        sms_id_username
    ):
        _logger.info("Get Remaining Time")
        
        user = AradialAPIGatewayGetUser(
            url=self.aradial_url,
            username=self.aradial_username,
            password=self.aradial_password
        )
        timebank = user.get_user(sms_id_username)

        # _logger.info("User Creation: %s" % created_user)

        return timebank        

    def update_user(
        self, 
        data
    ):
        _logger.info("Update User's Timebank")
        
        user = AradialAPIGatewayUpdateUser(
            url=self.aradial_url,
            username=self.aradial_username,
            password=self.aradial_password,
            data=data
        )
        updated_user = user.update_user()

        # _logger.info("User Creation: %s" % created_user)

        return updated_user        
    