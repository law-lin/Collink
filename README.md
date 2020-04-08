# Collink

During Google's Computer Science Summer Institute program, I worked with Alex (MIT '23) and Charles (Seton Hall University '23) to develop a website that allows students to connect with each other on their own college campuses.
The technologies we used were:
* Python
* HTML/CSS
* JavaScript
* Google App Engine
* Datastore
* Git
* Atom

While developing this site, we came across these issues:
* Auto-populating the Google Calendar site upon clicking "Add to Google Calendar" button </li>
* The counter for the Sign Up/Drop Out buttons would not update until page refresh</li>
* Upload image functionality - not attaching an image to the form would result in a string of errors</li>
* Integrating Gmail sign in with the site</li>

My primary role was to work on back end web development utilizing the Jinja environment with Python and JavaScript. I worked on structring the database models so that Alex could query information from the database and display the info on their respective pages. I also worked on redirecting the pages based on the category they clicked on the "Add Event" page, as well as fixing image functionality and the Google Calendar feature.

My secondary role was to assist Charles with the JavaScript code for the Sign Up/Drop Out feature and making sure that Alex's code would work with everything else.

We were able to resolve all our issues and complete the website by the deadline. We structured our site to be scalable, like having individual college site instances of Collink (Ex: Stanford has their own Collink and Harvard has their own Collink, where only users with school-specific email addresses can access their respective sites (somewhat like the original Facebook).
