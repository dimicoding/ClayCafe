# Testing

## Table of contents:

- [Validator Testing](#validator-testing)
    - [Lighthouse](#lighthouse)
    - [W3C](#w3c-html)
    - [Jigsaw](#jigsaw-css)
    - [JS Validation](#js-validation)
    - [Pep8 Validation](#pep8-validation)
- [Responsiveness](#responsiveness)
- [Manual Testing](#manual-testing)
- [Testing Aknowledgments](#testing-aknowledgments)

## Validator Testing

### Lighthouse Testing

<br>

- Home page lighthouse testing
![index](media/readme/readme/lighthouse/home-page-lh.png)

<br>

- Products page lighthouse testing
![products](media/readme/readme/lighthouse/products-lh.png)

<br>

- Workshops page lighthouse testing
![workshops](media/readme/readme/lighthouse/workshops-lh.png)

<br>

- Workshop Detail page lighthouse testing
![workshop-details](media/readme/readme/lighthouse/workshop-details-lh.png)

<br>

- Blog page lighthouse testing
![blog](media/readme/readme/lighthouse/blog-lh.png)

<br>

- Blog Detail page lighthouse testing
![Blog detail](media/readme/readme/lighthouse/blog-details-lh.png)

<br>

- Contact page lighthouse testing
![contact](media/readme/readme/lighthouse/contact-lh.png)

<br>

- Profile page lighthouse testing
![profile](media/readme/readme/lighthouse/profile-lh.png)

<br>

- Product managemant page lighthouse testing
![product management](media/readme/readme/lighthouse/product-management-lh.png)

<br>

- Shopping bag page lighthouse testing
![shopping bag](media/readme/readme/lighthouse/shopping-bag-lh.png)

<br>



### W3C HTML validator
The Markup Validation Service was used to identify errors in an HTML file. Validation was performed through direct input and by using a URL.

Syntax errors were corrected, while irrelevant errors that don't affect the functioning of the website were ignored.

For example:

Errors remaining:

``Bad value {% url 'products' %}?category=Cu...`` <br>
Error: Duplicate ID "user-options" used for dropdown menus in the navigation, derived from Bootstrap.
Errors fixed:

Error: The element "button" must not appear as a descendant of the "a" element.


### W3C Jigsaw validator
The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the website. The CSS passes with 0 errors.

<br>

![css](media/readme/readme/css.png)

### JS Validation
To ensure the quality of the JavaScript/JQuery, I used JSHint for validation. It helps identify any potential issues or mistakes in the code. The majority of the JavaScript code in this project follows the guidelines provided in the walkthrough.
### PEP8 Validation
To verify python in this project i used the command `flake8 --statistics`

Many issues were identified and resolved during the project, such as unidentified imports and duplicates. However, to meet the project submission deadline, some non-critical issues were left unresolved. The screenshot below provides a visual representation of the remaining issues. These issues primarily affect code readability and consistency rather than the functionality of the project.

![flake-statistics](media/readme/readme/flake8%20--statistics.png)

## Responsiveness

- All website pages have been designed to be responsive, ensuring they adapt to different screen sizes and devices.

- The design has been tested on multiple browsers, including Microsoft Edge, Chrome, Opera GX, and Mi(phone-Xiaomi), to ensure that it looks and functions well across different platforms.

- Bootstrap responsive classes were utilized to create a responsive design for this project.

- The design was tested using Chrome DevTools, a browser-based tool for testing and debugging responsive designs.

- Navigation has been simplified for smaller screens, with a hamburger menu replacing the desktop navigation bar, making it easier for users to navigate the site on mobile devices.

<br>

**Additionaly following media queries were used:**
- @media (min-width: 1200px)
- @media (min-width: 992px)
- @media (min-width: 576px) 
- @media (max-width: 576px) 

## Manual Testing

## Testing aknowledgments

During this phase, I came to the realization that for a project of this scale and with a tight deadline of approximately three weeks, I needed to adopt a different approach. I realize the importance of testing each individual app once its main functionality was implemented would have produce a better result, rather than attempting to test everything simultaneously. This approach would have prevented me from feeling overwhelmed and allowed for better testing and early error correction. Unfortunately, I only realized this now, but it has served as a valuable lesson for future projects.