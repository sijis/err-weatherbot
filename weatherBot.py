from weather import get_weather_for_location
from errbot import BotPlugin, botcmd

__author__ = 'AP'


class WeatherBot(BotPlugin):

    def get_configuration_template(self):
        """ configuration entries """
        config = {
            'api_key': '',
        }
        return config

    @botcmd
    def weather(self, mess, args):
        """ Shows weather info for given location.
        Example: !weather San Francisco, CA
        or !weather brussels
        """
        if not args:
            return 'Am I supposed to guess the location?...'

        try:
            api = self.config['api_key']
        except:
            return 'Please set an api key'

        return get_weather_for_location(args.strip(), api)
