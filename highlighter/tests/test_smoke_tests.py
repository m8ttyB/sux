# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
import time
from PIL import Image, ImageChops, ImageDraw

import pytest


class TestSmokeTests:

    @pytest.mark.nondestructive
    def test_can_this_work(self, base_url, selenium):
        baseline = 'baseline.png'
        selenium.get(base_url)
        selenium.execute_script(open("./src/aria-highlighter.js").read())
        selenium.save_screenshot('screenshot.png')
        assert pytest.idiff(baseline, 'screenshot.png', tolerance=0.002), self.create_image_diff_overlay(baseline, 'screenshot.png')

    @pytest.mark.nondestructive
    @pytest.mark.xfail(reason='Negative case: should fail, uses a tampered baseline image')
    def test_this_should_fail(self, base_url, selenium):
        baseline = 'baseline_tampered.png'
        selenium.get(base_url)
        selenium.execute_script(open("./src/aria-highlighter.js").read())
        selenium.save_screenshot('screenshot.png')
        assert pytest.idiff(baseline, 'screenshot.png', tolerance=0.002), self.create_image_diff_overlay(baseline, 'screenshot.png')

    def create_gray_image(self, size, color):
        img = Image.new('L', size)
        dr = ImageDraw.Draw(img)
        dr.rectangle((0, 0) + size, color)
        return img

    def create_image_diff_overlay(self, img_a, img_b, opacity=0.85):
        img_a = Image.open(img_a)
        img_b = Image.open(img_b)
        diff = ImageChops.difference(img_a, img_b)
        diff = diff.convert('L')
        thresholded_diff = ImageChops.add(diff, diff)
        size = diff.size
        mask = self.create_gray_image(size, int(255 * (opacity)))
        shade = self.create_gray_image(size, 0)
        new = img_a.copy()
        new.paste(shade, mask=mask)
        # To show the original image in the result, use mask=diff instead
        new.paste(img_b, mask=thresholded_diff)
        new.save('diff.png')
