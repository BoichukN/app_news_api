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



Link to my site on Heroku below:

https://tranquil-headland-90957.herokuapp.com/
