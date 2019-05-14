from robot.libraries.BuiltIn import BuiltIn
import os
import percy

class RobotFrameworkPercy():

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.percy_runner = None

    def Percy_Initialize_Build(self, **kwargs):
        driver = BuiltIn().get_library_instance('Selenium2Library')._current_browser()
        loader = percy.ResourceLoader(
            root_dir=kwargs.get('root_dir'),
            base_url=kwargs.get('base_url'),
            webdriver=driver
        )
        # api_url
        # access_token
        # default_widths
        config = percy.Config(**kwargs)
        self.percy_runner = percy.Runner(loader=loader, config=config)
        # branch
        # pull_request_number
        # parallel_nonce
        # parallel_total_shards
        # commit_data
        self.percy_runner.initialize_build(**kwargs)

    def Percy_Snapshot(self, name=None, **kwargs):
        self.percy_runner.snapshot(
            name=name,
            widths=kwargs.get('widths'),
            enable_javascript=kwargs.get('enable_javascript')
        )

    def Percy_Finalize_Build(self):
        self.percy_runner.finalize_build()
