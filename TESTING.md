# Testing

Testing was carried out throughout the development of Cornered Wisdom to ensure that the application's core functionality worked as intended.

Testing covered authentication, CRUD functionality, form validation, quote sorting, quote shuffling, user-specific data access, responsiveness and deployment.

## Manual Testing

### Authentication

| Test | Expected Result | Result |
| --- | --- | --- |
| Register with valid details | Account is created successfully | Pass |
| Register with invalid/mismatched passwords | Django displays validation errors and account is not created | Pass |
| Log in with valid credentials | User is authenticated and redirected to the home page | Pass |
| Log in with invalid credentials | Login is rejected and an error is displayed | Pass |
| Log out | User session ends and user is redirected to the login page | Pass |
| Attempt to access authenticated pages while logged out | User is redirected to login | Pass |

### Quote CRUD

| Test | Expected Result | Result |
| --- | --- | --- |
| Add a quote with valid information | Quote is saved successfully | Pass |
| Add a quote without quote text | Submission is rejected | Pass |
| Add a quote without a book title | Submission is rejected | Pass |
| Add a quote without an author | Quote can still be saved because author is optional | Pass |
| Add a quote without a page number | Quote can still be saved because page number is optional | Pass |
| Add a quote with page number below 1 | Submission is rejected | Pass |
| Add notes to a quote | Notes are stored and displayed | Pass |
| View My Quotes | Logged-in user's saved quotes are displayed | Pass |
| Edit a quote | Updated quote information is saved | Pass |
| Delete a quote | Confirmation page is shown and quote is deleted after confirmation | Pass |

### Quote Ownership and Security

| Test | Expected Result | Result |
| --- | --- | --- |
| View saved quotes while logged in | Only quotes belonging to the current user are displayed | Pass |
| Home page quote selection | Random quote is selected only from the current user's quotes | Pass |
| Edit a quote | User can only edit a quote belonging to their account | Pass |
| Delete a quote | User can only delete a quote belonging to their account | Pass |
| Submit POST forms | Django CSRF protection is present | Pass |

### Sorting and Shuffle

| Test | Expected Result | Result |
| --- | --- | --- |
| Sort by newest | Newest quotes appear first | Pass |
| Sort by oldest | Oldest quotes appear first | Pass |
| Sort by book | Quotes are ordered by book | Pass |
| Sort by author | Quotes are ordered by author | Pass |
| Click Shuffle | Another saved quote is displayed without a full-page reload | Pass |
| Shuffle when multiple quotes exist | Current quote is avoided where another quote is available | Pass |



## Responsive Design Testing

The application was manually tested at a range of viewport sizes using Chrome DevTools. During testing, responsive CSS was adjusted to ensure that the main content remained readable and usable across desktop, tablet and mobile layouts.

| Device / Viewport | Test | Result |
| --- | --- | --- |
| Desktop | Pages display correctly at full desktop width | Pass |
| iPad Pro 13 | Book layout, content and forms remain usable | Pass |
| Surface Pro | Page layout adapts to the tablet-sized viewport | Pass |
| Pixel 10 / 9 Pro | Content fits the mobile viewport and remains readable | Pass |
| Galaxy Fold | Content adapts to the narrow mobile viewport | Pass |

Responsive testing identified several layout issues during development, including desktop-width content being scaled down on mobile devices, background image cropping/repetition and inconsistent spacing at tablet sizes.

These issues were addressed by:

- Adding the viewport meta tag to all complete HTML templates.
- Adding responsive CSS media queries for tablet and mobile widths.
- Removing the desktop horizontal offset from the book wrapper at smaller viewport sizes.
- Adjusting page padding and typography for mobile screens.
- Adjusting background image sizing and positioning to provide a more consistent book layout across different aspect ratios.

Minor differences in the decorative background occur between screen aspect ratios because the book artwork is a fixed image. This does not affect the functionality or readability of the application.





## Browser Testing

Cornered Wisdom was manually tested in multiple browsers to check that the application's functionality and styling behaved consistently.

| Browser | Test | Result |
| --- | --- | --- |
| Google Chrome | Core functionality, forms, navigation, styling and responsiveness | Pass |
| Mozilla Firefox | Core functionality, forms, navigation and styling | Pass |

The majority of development and responsive testing was carried out using Google Chrome and Chrome DevTools. Mozilla firefox was also used to check that the application remained functional and visually consistent.



### HTML Validation

HTML pages were tested using the W3C Nu HTML Checker.

The registration page reports validation errors relating to the HTML generated by Django's `UserCreationForm` when rendered using `{{ form.as_p }}`. In particular, Django-generated password help text contains list markup within the form's generated help-text structure.

This markup is generated by Django rather than being manually written into the template. The registration form remains functional and the validation messages and password requirements display correctly to the user.



### CSS

CSS was tested using the W3C CSS Validation Service.

Validation identified an incorrect use of:

`font-weight: italic`

This was corrected to:

`font-style: italic`

After correction, the stylesheet passed validation.

### JavaScript

JavaScript was checked using JSHint.

JSHint initially produced warnings for `const` and arrow functions because it was checking against an older JavaScript version. The validator was configured for ES6 using:

`/* jshint esversion: 6 */`

No JavaScript errors remained after using the appropriate ECMAScript version.

### Python / Django

Django's built-in system check was run using:

`python manage.py check`

Result:

`System check identified no issues (0 silenced).`



| Bug | Cause | Fix |
| --- | --- | --- |
| Pages appeared as a very small desktop layout on mobile devices | The viewport meta tag was missing from some templates | Added `<meta name="viewport" content="width=device-width, initial-scale=1.0">` to the full HTML templates |
| Decorative book background repeated incorrectly on narrow screens | The background image was allowed to repeat vertically | Responsive background sizing was adjusted and background repetition was disabled |
| Tablet layouts retained too much of the desktop positioning | The original responsive breakpoint was too narrow | The tablet media query was extended to cover screens up to 1200px and desktop offsets were removed at smaller sizes |
| Static CSS and images disappeared when `DEBUG` was set to `False` | The Heroku `DISABLE_COLLECTSTATIC` configuration variable was still enabled, preventing production static files from being collected | Removed `DISABLE_COLLECTSTATIC`, retained the WhiteNoise configuration and redeployed the application |
| HTML validation identified missing language information | Full HTML templates did not specify a document language | Added `lang="en"` to the `<html>` element |
| HTML validation identified incorrectly nested elements | Some closing `div` elements were positioned after the closing `main` element | Corrected the HTML nesting so elements close in the correct order |
| CSS validation reported `font-weight: italic` as invalid | `italic` is a `font-style` value rather than a `font-weight` value | Changed the declaration to `font-style: italic` |
| JSHint initially reported warnings for `const` and arrow functions | JSHint was validating against an older JavaScript version by default | JSHint was configured to validate the script as ES6 |


## Known Issues

- The decorative book background is based on a fixed image, so its appearance can vary slightly between unusual screen aspect ratios. This does not prevent the application from being used.
- The registration page produces HTML validator messages relating to markup generated by Django's `UserCreationForm` when rendered with `{{ form.as_p }}`. The registration form remains functional and displays the required password guidance.