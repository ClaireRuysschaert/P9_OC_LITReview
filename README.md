### Application Goal 
 
- Request reviews of books or articles by creating tickets
- Read reviews of book or article
- Publish reviews of books or articles
- Provide a simple interface that corresponds to [wireframes](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/Python%20FR/P7%20-%20D%C3%A9veloppez%20une%20application%20Web%20en%20utilisant%20Django/LITReview%20-%20Wireframes%20-%20FR.pdf).
- Maintain a simple and minimalist user interface

### Features

# Authentication
Users can log in, log out, and sign up.
Unauthenticated users can only access the login and signup pages.
![Login/Out/Signup Page](images/images/login-out-signup_page.PNG)


# Tickets (Review Request from a user)
- User can request a review for a book or articles
- Followers of the user can post reviews in response
- User can create a ticket and a review simultaneously


# Feed (Home Page)
The feed displays the following in reverse chronological order :
- All tickets and reviews from users followed by the user
- All tickets and reviews from the user
- Reviews in response to the user's tickets from the user's followers (even if the user is not following them)
- Option to create a ticket to request a review
- Option to create a review
- Option to create a ticket and a review at the same time
- Option to view, modify and delete it's own tickes and reviews
![](images/images/feed.PNG)


# Subscriptions
A user can follow other users to see their requests and critiques. 
Users can search for usernames to follow them.
There is a page listing all the users a user is following and all the users who are following the user. 
A user can unfollow another user.
![](images/images/subscription.PNG)


### Technical specifications
- Use Django
- Use SQLite
- Adhere to PEP8

### How to launch me ? 
- Install Python 3.10. Launch the console and, in the folder of your choice, clone this repository :
```
git clone https://github.com/ClaireRuysschaert/P9_OC_LITReview.git
```
- In the LITReview folder, create and activate a new virtual environment:
```
(linux)
python3 -m venv .venv
source .venv/bin/activate
(windows) 
python -m venv .venv
.\.venv\Scripts\activate
```
- Then, install the required packages :
```
pip install -r requirements.txt
```
- Finally, launch the server:
```
python manage.py runserver
```
Congrats! You can now access this application to http://127.0.0.1:8000