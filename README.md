This is Django Project .
<br> 
In this project we are making models and adding it in admin.
<br>
in urls.py: Dynamic url - post/<int:post_id>/'
<br>
in blog.html: inside the for loop, we are using an anchor tag and giving url to post_details and the 'post.id'is passing a variable from the view  (id is the primary key)
<br>
in post.html: inside the for loop ' post.comments.all' is the comments of all posts  
<br>
in models: Category, BlogPost, and Comment are the different tables. Category is the foreign key for the BlogPost table 
           comment - is associated with a particular post, whenever the delete comment will delete using models.CASCADE
<br>
after adding the posted_by var in models - makemigratioins and provide option 1 ..  and give name of person and enter


