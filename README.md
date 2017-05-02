[![Updates](https://pyup.io/repos/github/m8ttyB/sux/shield.svg)](https://pyup.io/repos/github/m8ttyB/sux/)
[![Python 3](https://pyup.io/repos/github/m8ttyB/sux/python-3-shield.svg)](https://pyup.io/repos/github/m8ttyB/sux/)

# Automate Web Accessibility Testing
The goal of SUX (Some User Experience) is to automate testing of accessibility issues and have a suite of regression tests that run as a component in a Jenkins build pipeline.

### Contents
- [What is Web Accessibility?](#what-is-web-accessibility)
- [A Few Available Resources](#a-few-available-resources)
- [Project Scope](#project-scope)
- [License](#license)


## What is Web Accessibility?
Web Accessibility means, quite plainly, that everyone who is able to access the web can also navigate and utilize the available resources.

This includes those with limited vision or hearing, as well as those with physical or neurological conditions that may affect their ability to operate a computer or its peripherals.

#### Why Web Accessibility is Important
The internet today offers the possibility of **unprecedented access to information and interaction** for those with disabilities,<sup>[[1]](https://www.w3.org/WAI/intro/accessibility.php#important)</sup> giving them a freedom and independence that may never have been possible before. The [UN Convention on the Rights of Persons with Disabilities](https://www.un.org/development/desa/disabilities/convention-on-the-rights-of-persons-with-disabilities.html) recognizes access to information and communications technologies, including the web, as a **basic human right**<sup>[[2]](https://www.w3.org/standards/webdesign/accessibility/#case)</sup>.

Approximately 20% of the population in the United States have a disability or limitation<sup>[[3]](https://www.cdc.gov/media/releases/2015/p0730-us-disability.html)</sup>.

This means that up to 60 million people may have trouble accessing and navigating the web. It is essential that the web be accessible, in order to provide equal access and equal opportunity to all users.

Accessibility supports **social inclusion** for people of diverse abilities and those with diverse socioeconomic backgrounds.

#### What Web Accessibility Looks Like

> There is extensive documentation on the Web Content Accessibility Guidelines (WCAG) here at [How to Meet WCAG 2.0](https://www.w3.org/WAI/WCAG20/quickref/).


## A Few Available Resources
* [Web Content Accessibility Guidelines](https://www.w3.org/WAI/intro/wcag)
* [Web Accessibility Checklist:](https://www.wuhcag.com/wcag-checklist)
* [axe-core](https://github.com/dequelabs/axe-core)
* [Pytest Plugins](https://docs.pytest.org/en/latest/writing_plugins.html)
* [Jenkins Pipeline](https://jenkins.io/doc/book/pipeline/getting-started)


## Project Scope
Create a suite of regression tests that check for a curated list of accessibility guidelines:

* Create a Python wrapper for [axe-core](https://github.com/dequelabs/axe-core)
* Write several highlevel smoketests for mozillians.org
* Run tests as part of a Jenkins job
* Stretch goal: move the previous completed work into a pytest module
* Stretch goal: create an ARIA highlighter script and automate checking of images for visual regressions or changes.


## License
This software is licensed under the MPL 2.0:

```
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
