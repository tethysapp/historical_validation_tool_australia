from tethys_sdk.base import TethysAppBase, url_map_maker


class HistoricalValidationToolAustralia(TethysAppBase):
    """
    Tethys app class for Historical Validation Tool Australia.
    """

    name = 'Historical Validation Tool Australia'
    index = 'historical_validation_tool_australia:home'
    icon = 'historical_validation_tool_australia/images/icon.gif'
    package = 'historical_validation_tool_australia'
    root_url = 'historical-validation-tool-australia'
    color = '#d35400'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='historical-validation-tool-australia',
                controller='historical_validation_tool_australia.controllers.home'
            ),
        )

        return url_maps
