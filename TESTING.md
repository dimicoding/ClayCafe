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

**Navbar**

| Feature | Action             | Expected Result                 |
| :-----: | :-----------------:| :------------------------------:|
| **Home Link Logo** | While not on homepage, click logo. | User is redirected back to homepage. |
| **"Home" Link** | While not on homepage, click "Home". | User is redirected back to homepage. |
| **"Shop" dropdown** | Click dropdown in navbar | User is presented with a list of links (all categories, Vases, Cups, Plates &  Bowls) |
| **Product- Category** | From "Shop" dropdown, select sub-link | User is directed to page listing all products of same category |
| **"Workshop" link** | Click Workshop link in navbar | User is directed to workshop page listing all entries |
| **"Blog" link** | Click Blog link in navbar | User is directed to the blog page with all the blog posts |
| **"Contact** | Click Contact link in navbar | User is directed to Contact page with the form to send to the administrator|
| **"Workshops icon" link** | Click Workshop link in navbar | User is directed to workshop page listing all user's selected entries (This function is in development, more time is needed)|
| **"Profile" dropdown** | Click Profile dropdown | Authenticated user sees option to "My Profile" and  "Logout". Admin user sees option to "Product Managment", "My Profile", and "Logout"|
| **"Login" Link** | While not authenticated, click "Login". | User is directed to Login form. |
| **"Register" Link** | While not authenticated, click "Register". | User is directed to Sign Up form. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to page with Sign Out button. |
| **"Basket" Link** | Click Basket link in navbar | User is directed to shopping basket page. |

<br>

**Footer:**

| Feature | Action             | Expected Result                 |
| :-----: | :-----------------:| :------------------------------:|
| **"Home" Link** | While not on homepage, click "Home". | User is redirected back to homepage. |
| **"Shop" dropdown** | Click dropdown in footer | User is presented with a list of links (all categories, Vases, Cups, Plates &  Bowls) |
| **Product- Category** | From "Shop" dropdown, select sub-link | User is directed to page listing all products of same category |
| **"Workshop" link** | Click Workshop link in footer | User is directed to workshop page listing all entries |
| **"Blog" link** | Click Blog link in footer | User is directed to the blog page with all the blog posts |
| **"Contact** | Click Contact link in footer | User is directed to Contact page with the form to send to the administrator|
| **"Newsletter** | Enter valid e-mail and Click subscribe link in footer | User is presented with confirmation success mesage if email is valid|
| **"Map" link** | Click map link in footer | User is directed to the google maps page with location of the bussiness. |

**Authentication**

| Feature | Action             | Expected Result                 |
| :-----: | :-----------------:| :------------------------------:|
| **Login**    | As an already registered user, go to the login page, complete the login form, and click the login button. | Form validation is applied to ensure the required fields are filled correctly. If the login is successful, the user is directed to the homepage, and a success message is displayed, mentioning the "username" |
| **Forgot Password function** | On the login page, click the "Forgot Password" link. | User is directed to the Reset Password page. Form validation is applied to ensure the required fields are filled correctly. A password reset link is sent to the user's email for resetting the password. |
| **Sign Up**   | As an unregistered user, go to the Sign Up page, complete the form, and submit it.  | Form validation is applied to ensure the required fields are filled correctly. After successful submission, the user receives a confirmation email containing a registration verification link. Clicking the link directs the user to the Login page. A success message informs the user about the successful account registration. |
| **Logout**    | As an authenticated user, go to the Logout page and click the "Sign out" button.   | User is directed to the homepage. A success message informs the user about the successful sign out. |

## Testing aknowledgments

During this phase, I came to the realization that for a project of this scale and with a tight deadline of approximately three weeks, I needed to adopt a different approach. I realize the importance of testing each individual app once its main functionality was implemented would have produce a better result, rather than attempting to test everything simultaneously. This approach would have prevented me from feeling overwhelmed and allowed for better testing and early error correction. Unfortunately, I only realized this now, but it has served as a valuable lesson for future projects.