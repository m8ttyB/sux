[![Updates](https://pyup.io/repos/github/m8ttyB/sux/shield.svg)](https://pyup.io/repos/github/m8ttyB/sux/)
[![Python 3](https://pyup.io/repos/github/m8ttyB/sux/python-3-shield.svg)](https://pyup.io/repos/github/m8ttyB/sux/)

# SUX Highlighter

Thank you for checking out the highlighter experiement. The goal of this experiement is to make ARIA `role` attributes in the DOM visibile to browsers that are not screen readers. Once these elements have been exposed, diff the webpage (a screenshot) against a baseline image for visual regressions.



## Getting involved as a contributor

This is currently a prototype meant to help us have a discussion around this problem space. Contribution is always welcome, but just know that active development on this tool won't be happening on a specific timeline. Or may not happen at all.

If you'd like to have a conversation reach out to me (:mbrandt) in [irc.mozilla.org](https://wiki.mozilla.org/IRC) ([#fx-test](http://chat.mibbit.com/?server=irc.mozilla.org&channel=#fx-test)).

## Questions are always welcome

While we take pains to keep our documentation updated, the best source of information is those of us who work on the project. Don't be afraid to join us in irc to ask questions.

## How to set up and build highlighter tests locally


You will need to install the following:

* **Git**: If you have cloned this project already then you can skip this! GitHub has excellent guides for [Windows](https://help.github.com/articles/set-up-git/#platform-windows), [OS X](https://help.github.com/articles/set-up-git/#platform-mac) and [Linux](https://help.github.com/articles/set-up-git/#platform-linux).
* **Python27**: Before you will be able to run these tests you will need to have [Python 2.7.12](https://www.python.org/downloads/release/python-2712/) installed.
* **Python36**: Before you will be able to run these tests you will need to have [Python 3.6.1](https://www.python.org/downloads/release/python-361/) installed.
* **Tox**: You will need to [install Tox](https://testrun.org/tox/latest/install.html) to manage the virtual environments and run the tests.
* **Geckodriver**: To run the tests in Firefox you will need to [download Geckodriver](https://github.com/mozilla/geckodriver/releases) and add it to your PATH. For example, `export PATH=$PATH:/directory/containing/geckodriver/`.

### Running tests locally

To run these tests, simply type `tox` in your shell:

```bash
tox
```

## License

This software is licensed under the MPL 2.0:

```
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
```
