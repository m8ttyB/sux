# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
import time

import pytest


class TestSmokeTests:

    @pytest.mark.nondestructive
    def test_can_this_work(self, base_url, selenium):
        selenium.get(base_url)
        selenium.execute_script(open("./src/aria-highlighter.js").read())
        selenium.save_screenshot('screenshot.png')
        # add a sleep so the test run is visible for presentation purposes
        time.sleep(10)
        assert pytest.idiff('baseline.png', 'screenshot.png', tolerance=0.2)
