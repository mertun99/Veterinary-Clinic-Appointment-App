# Veterinary clinic website with appointment reservation system
#### Description:


This project is a fullstack, web-based application in python, using JavaScript and
SQL (from CS50 library). It also features one additional python program,
more on that later.

The web application is for a general veterinary clinic, it provides basic information to the clients,
such as services, contact, information about the clinic and it also features an online
appointment reservation system.

The main design features of the website are build by using bootstrap library.
Some of the default components of bootstrap library are also modified in
custom.css file, which overwrites some of the bootstrap values (like colors) while rendering the website.

#### Dependencies
Can be found in **requirements.txt**

#### app.py
The main programm. It features most of the logic and defines all of the routes.
There are 9 main routes:
<br>
/ (index), /services, /pricing, /appointments, /map, /admin (login), /logout, /console and /clear.
<br>
Most of these are however to provide general information to the clients (pet owners),
such as location of the clinic, opening hours, services provided by the staff..
Some, however are to handle specific components of the website:
**/admin** lets you (clinic staff) log in to the website <i>(by default usr: admin pswrd: admin)</i>.
<br> While they are logged in, they can manage appointment request made by the public.
This can be made through **/console** route.
The public doesnt need to make an account and the appointment requests can be made through /appointments route.
**/logout** logs veterinary clinic staff out and clears the session.

#### functions.py
In this file, there are defined some functions imported by app.py.
One function is to render an apology, if something goes wrong on the website.
Other one is to define a current date and time (used by the appointment system). There is also one
function that require users (veterinary staff) to be logged in, in order to manage the appointment requests.
This function is the same as in some of the CS50 course problems.
<br>
Lastly, there is a prototype function that sends emails regarding any updates on ones appointment request.
It doesnt really send the emails, just prints them to the console.

#### admin manager.py
This simple python file lets you manage admins (veterinary staff), their accounts and create a new one.
The information about the admins, including their hashed passwords are stored in **all.db**

#### all.db
This database contains 2 main tables. <br>
1) admins
2) appointments

Admins table stores information mentioned before, such as username, passwords and IDs of the veterinary clinic staff.
Appointments on the other hand stores all the relative information about appointment requests -
their date, time, id, status, email and name of the requester etc..

#### /static/custom.css
This file edits some of the css attributes of bootstrap, like custom colors..

#### /static/images
This folder stores all the images that are displayed on the website.
There is also a .txt file with the picture references.

#### /templates
In the template folder, there are many templates that are used to render the application.
<br> The main template - **layout.html** is extended using **Jinja**.
This template uses components of bootstrap library, such as:
1) navbar
2) custom buttons
3) footer
4) etc..

Here are some of the templates in a closer look:

#### /templates/index.html
The "home" page for the project. It features carousel from bootstrap
templates and featurettes. It is used as introductory page for the whole website or app.

#### /templates/appointments.html
The online appointment reservation system. It uses form to request the user to select a day,
time, reason of visit, name and other important parameters and then passes
them into **appointments.db**.
<br>
So far, it only features mostly only client-side validation, as all the requests are handled
by the veterinary staff anyway. Some of the validators include a day that is
either the day of the request or in some time in the future
(until 90 days from the day of the registration), a correct email format and a time
of the appointment that is in between working hours.
<br>
This validation is achieved with previously mentioned function defined in **functions.py**
that checks for current time, and specific input type requirements of the html.
<br> The server-side validation checks for conflicting dates of appointments. It's located in **app.py**.
When user tries to make an appointment for already occupied date and time, or a date somewhere in the past, they are denied.

#### /templates/console.html
This template is accesible only to logged in users (veterinary staff). It can be redirected either
directly after the staff logs in to the website, or by clicking "manage appointments" button that 
renders in the **layout.html** template after the admin has been logged in.
<br>
It features a 3 tables, each for:
1) pending appointments
2) accepted appointments
3) rejected appointments

It also features a button to clear old & rejected appointments.
These appointments are ordered by time in ascending order.
<br>
In the 1) pending requests, admins are able to either accept or reject the appointment.
After that, the appointments status is changed to either "accepted" or "rejected", and
the whole page is refreshed, rendering it again but with updated status of the appointment that
has been handled.

#### Some final thoughts:
Overall, I believe this website allows pet owners to get valuable information
about the veterinary clinic in a user-friendly way, as it also allows to make a simple appointment
request without the need of making a phone call or writing a whole email.

#### Acknowledgment
1) Freepik - https://www.freepik.com/ - source of pictures for the website
2) Code formatter - https://freetools.textmagic.com/source-code-formatter - to make things prettier
3) ChatGPT - https://chat.openai.com/ - gave me advices from time to time
4) Bootstrap - https://getbootstrap.com/ - to make things prettier once again
5) Stack Overflow - https://stackoverwlow.com/ - found answers on some of the problems ive encountered there
6) W3schools - https://www.w3schools.com/ - helped me with learning some principles of HTML, CSS and Javascript in more detail
7) CS50 - https://pll.harvard.edu/course/cs50-introduction-computer-science - used some functions for the website from there
8) Other references from **references.txt**
