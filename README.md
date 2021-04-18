This is a simple API written in a django rest framework.
Here you can view a list of publications (title, link to the main source, author, date of creation) and create them (only for authorized users). You can also leave comments for a specific post (authorized users only) and you can view comments and posts for all users.

The following url addresses can be used:

registration on the site
api/accounts/register/

login (go to the site with a password and username)
api/accounts/login/


list of publications
api/posts/

create a publication
api/posts/create/

publication by id
api/posts/id

edit post by id
api/posts/id/edit/

delete post by id
api/posts/id/delete/


list of comments to the publication
api/posts/comments/

create a comment to the post
api/posts/comments/create/

edit or delete comment before posting
api/posts/comments/id/

You can run on your own server as follows:

1. create a folder in which to clone the project
2. In the command line of the interpreter in the appropriate folder, insert the following command

git clone https://github.com/BoichukN/app_news_api.git

The project was cloned to your folder.

3. run the migration commands on the command line to create a database (make sure you have the PostgreSQL database installed).
The first create a database with a name 'list_of_news' and username 'admin' and password 'cr72013'.
Then in the command line python of your directory enter the following commands.

python manage.py makemigrations
python manage.py migrate

4. create a superuser

python manage.py createsuperuser

5. start the server

python manage.py runserver

6. At the address / admin / go to the profile.

7. Using the urls above, you can create other posts and comments.


Link to my site on Heroku below:

https://tranquil-headland-90957.herokuapp.com/
