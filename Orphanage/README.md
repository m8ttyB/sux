# Orphanage
DOM Element highlighter tool, updates role attributes of document elements.
This project is an experiment that looks to improve site accessibility for screen reader users. Through the span of this project I've read through W3C documentation (not all of it!), blog posts, courses, etc. all discussing the importance of role attributes in the navigation of sites for people with disabilities.

According to the [National Federation of The Blind] (https://nfb.org/blindness-statistics) based on information collected from various government agencies, the number of non-instutionalized Americans with some form of visual disability is around 7.3 million people or about 2.3% of the population in 2015, not an insignificant number. This figure accounts *only* for males and females 16 through 75+ of all races, ethnicities and education levels. Additionally, [Web Accessibility in Mind] (https://webaim.org/projects/screenreadersurvey6/) conducts a small annual survey (2015 latest available) with several interesting and telling statistics with screen readers and users with disabilities at it's core. 

Despite all the available documentation that speaks to the importance of web accessibility and the role attribute/value, many, a great deal of websites actually, either don't use role attributes at all or are only used sparingly throughout. These elements and in cases entire sites left without roles are abandoned to a sort of orphanage for role-less and as a result sometimes impossible to use sites. This project aims to help in those situations.

##Project Scope: 

Purpose of role attribute: identifies exact function of an element and its children, allows for accessibility of screen reader users, also useful for screen scrapers. Native semantic element; assigns purpose to element it is within. Browsers will apply first recognized role in list. Custom roles can be used as long as they don't conflict with any defined ARIA roles but will not be functional.

WAI-ARIA roles: element types that must not be changed over time or with user actions. Assistive technologies (e.g. screen readers) are unable to detect role value change. In order to reflect content in the DOM, user agents should map the role attribute to appropriate value.

The purpose of script is to highlight elements on any HTML document that do not contain ARIA roles but that should have an assigned role and value. The JS script will inject CSS into the document to briefly highlight any and all elements missing a role attribute and value.
are update the DOM. Role attribute and value needs to be added.

Main function (IIFE) of script:
1. run through and read all elements in DOM.
2. check to see if each element has role attributes.
3. alert pop-up messages inform user of site's accessibility.
3. element(s) without role attributes highlighted.
4. element(s) with role attributes not highlighted.
5. element(s) without role attr later injected with role attr.
6. remove highlighting from element once role attr injected.


##Running Script in Developer Console:
Simply copy all code and paste into dev console and hit enter.
Page elements will be highlighted and role added 3 seconds after. 
Orphange code in effect until page is refreshed or url changes.


##Linking Script to HTML Document:
Script does not need libraries to run.
Script needs to be wrapped in function like below in order to link to HTML file or run inline.

window.onload = function() { 
  //orphanage code here 
  }

*This is a work in progress. Future goal/direction is to possibly turn it into a browser extension and have it work along with element role additions provided by HTML5.*
  

