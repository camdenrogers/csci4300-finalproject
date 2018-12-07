# UGA Nvite
## Team Name
- The International Justice League of Super Acquaintances

## Team Members
- Alex Kimbrell
- Francis Mazzolini
- Camden Rogers
## Project Proposal
- UGA Nvite (An event app that coordinates UGA students with similar interests)
Have you ever wanted to go a concert or sporting event but are unable to rally enough friends to join you? Forget your lame friends! UGA Nvite provides you with a platform to sign up for events with other sensible people. What makes UGA Nvite different? You don’t have to know anyone. Just have a genuine interest in attending an event of your choice and you’ll join a small group (usually between 4-6) of college students (enough to where it isn’t a date, but that you’ll still be a vital member of the group). 
### User Account Login Page 
- Provide users with a portal to login to their account with appropriate username/password fields.
- Provide users the ability to create a new account. New accounts require a username, password, phone number, and email to complete the account registration.
- Must login to an account in order to proceed past the homepage.
- New users will be added to a database table containing a list of site users.
### Available Events Page 
- Contains a list of upcoming events that the user can sign up for.
- Each event is stored in a table record and contains the name of the event, a short description (if available/applicable), the date of the event, the location of the event, and how many users are signed up for the event.
- Events are gathered from a variety of websites and combined into one timeline.
- Events are scrollable and will gather more events when the user reaches the bottom of the list.
- Events will fill up and become unavailable after the maximum number of attendees is reached.
- Events can be sorted in different ways by the user, but the default is to be ordered by date with the most recent upcoming events at the top of the list.
- Under an events page there will be an option to join a random group or to form a new group with a specific maximum size.
### My Events Page 
- Contains a list of upcoming events that the user is currently signed up for.
- Shows the user other members that are signed up for the same event and provides contact information (Phone number and/or Email) of each member.
- Shows a list of past events that the user has attended along with the group you attended the event with. You will be able to submit reviews (out of 5 stars) of the members of the group you attended with as well.
- Event Review Page 
- Gives users the ability to write reviews about their experience at X event and rate it out of 5 stars.
- Shows a list of reviews completed by other users for past events.
- Each user will also have a user rating (out of 5 stars) displayed next to their name.
### Previous Projects Used
- PJ00: HTML
- PJ01: CSS
- PJ02: Mako/uwsgi
- PJ03: MySQL
- PJ04: Django

Licensing request: All code produced as a result of, and in accordance to, this assignment proposal will be the sole property of "The International Justice League of Super Acquaintances" and its members as listed above. This code will be licensed under the Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA).

## Requirements

- **(10 points) Login Page:** The project must contain a functional, well-designed login page for existing users to sign in, and new users to create a new account 
  - **(3.33 points) Login Form with username and password fields:** A standard login form requiring an existing user's username and password
  - **(3.33 points) Create New User Form with the following required fields:**
    - Username
    - Password
    - First name
    - Last name
    - Phone number
    - Email Address
  - **(3.33 points) Account passwords are properly hidden and secured:** Account passwords are hashed for security and hidden on the form

- **(10 points) Main user interface**
  - **(5 points) Website includes a clean, user friendly layout with the following pages:**
    - Event Feed
    - Individual Event pages 
    - Event Reviews page
  - **(5 points) Proper format of Individual Event pages:** The Individual Event pages are well-organized and provide a description of the event, other users who are attending event, and a photo of the event (if available)

- **(10 points) Google Maps interface**: A Google Maps widget is included on each individual event page. A map will be displayed on the event page that shows the location of the venue or event. A link to directions may also be included based off of the widget.

- **(10 points) Event Feed format and functionality(10 pts)**
  - Events will be gathered from Ticketmaster and Stubhub with XHR (using stubhubs developer api which allows retrieval of event listings and information) and stored in our database with the following information: unique id, name of event, date of event, and the location of the event (5 pts)
  - Event feed should include more events when the users scroll to the bottom of the feed using XHR requests. This will be a same domain request in which our app will generate an html fragment of 20 or so events, and be requested by the main feed webpage. After receiving this fragment, it will be appended to the webpage for the user to see (5 pts)

- **(10 points) Event Reviews:** When on an event page, a user will be able to leave a comment and rating for that specific event for all other users to see

- **(10 points) Event Groups:** When on an event page, a user will be able to register to attend an event by joining or creating a group (around 4-6) of people also attending the event. These groups will be displayed at the bottom of the event page

- **Django (10 pts):** Project is consistent and uses Django throughout (10 pts)

- **(10 points) MySQL Tables (subject to adjustment for functionality purposes)**
  - **(2.5 points) Users**
    - Unique id
    - username
    - Email
    - Hashed password
    - Phone number
    - First name
    - Last Name
  - **(2.5 points) Events**
    - Unique id
    - Name
    - Date
    - Location
    - Number of Registered Users 
  - **(2.5 points) EventRatings**
    - Event id
    - User id
    - Comment
    - Rating
  - **(2.5 points) EventGroups**
    - Event id
    - User id
    - Group idRequirements
