import os
from importlib import reload

from django.test import SimpleTestCase

import lostfound.settings as settings_module


class DeploymentSettingsTests(SimpleTestCase):
    def test_render_host_is_allowed(self):
        os.environ['RENDER_EXTERNAL_HOSTNAME'] = 'myapp.onrender.com'
        os.environ['ALLOWED_HOSTS'] = 'localhost,127.0.0.1'
        os.environ['CSRF_TRUSTED_ORIGINS'] = 'https://example.com'

        reloaded_settings = reload(settings_module)

        self.assertIn('myapp.onrender.com', reloaded_settings.ALLOWED_HOSTS)
        self.assertIn('https://myapp.onrender.com', reloaded_settings.CSRF_TRUSTED_ORIGINS)
        self.assertIn('https://example.com', reloaded_settings.CSRF_TRUSTED_ORIGINS)
