# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
import pytest
from pytest_selenium_pdiff import screenshot_matches


class TestSmokeTests:

    @pytest.mark.nondestructive
    def test_can_this_work(self, base_url, selenium):
        selenium.get(base_url)
        selenium.execute_script(open("./src/aria-highlighter.js").read())
        assert screenshot_matches(selenium, "/home/mbrandt/workspace/sux/highlighter/screenshots/test_can_this_work")

    @pytest.mark.xfail(reason="This is expected to fail")
    @pytest.mark.nondestructive
    def test_this_should_fail(self, base_url, selenium):
        selenium.get(base_url)
        selenium.execute_script(open("./src/aria-highlighter.js").read())
        assert screenshot_matches(selenium, '/home/mbrandt/workspace/sux/highlighter/screenshots/test_this_should_fail')
