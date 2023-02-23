
ADD RESPONSIVE IMAGE OF WEBSITE ON ALL DEVICES AND A LINK TO THE SITE BELOW THE IMAGE

# Viktoria's bake house 

For my fourth milestone project with Code Institute I have created a full-stack restaurant website called Viktoria's bake house, using the Agile plannnig approach and CRUD operations through a relational database.

The website idea is to give the user a look at the menu options and to sign up and leave a like or comment for the competiton page.

---

# List of contents

<li><a href="#target-audience">Target audience</a></li>
<li><a href="#user-stories">User stories</a></li>
<li><a href="#scope">Scope</a></li>
<li><a href="#structure">Structure</a></li>
<li><a href="#data-base">Data-base</a></li>
<li><a href="#wire-frames">wireframes</a></li>
<li><a href="#design">Design</a></li>
<li><a href="#base-page">Base page</a></li>
<li><a href="#home-page">Home page</a></li>
<li><a href="#blog-page">Blog page</a></li>
<li><a href="#menu">Menu</a></li>
<li><a href="#contact-page">Contact page</a></li>
<li><a href="#authentication">Authentication</a></li>
<li><a href="#authentication"></a></li>






---


# Target Audience

When planning this project, one important part was to consider what type of user audience this would attract
and what key featuers could I use to benift that audience.


 - People of any ages
 - People that enjoy food
 - People that injoy creativity with food
 - People that enjoy dinning out and fine dinning

 I wanted to find people that would enjoy more than eating a nice cake. But to go out and enjoy some fine dinning with a variety of classic and modern cakes. To keep things more interesting, I added a cake competition tot he website. Users can register and leave comment or just like the best of three cakes displayed every month. 
 
---

# User stories
![](assets/user%20stories.png)

---

# Scope

 I tried to take in to account that all ages can use the site, so simplicity is the main goal here. 

 - The header and footer of each page is kept the same throughout all the pages, to keep symetry and repetitive UX experience. 

 - The nav bar will send a user to the required pages label within the nav bar. I have given a drop down menu for the all menu pages. This keepsthe nav bar small and with more functions. 

 - A registration form for users to make an account. Users information is then saved in the data base. Once registered, a user can see clearly that they are logged in. When a used chooses to log out, a second reminded message is asked before the user fully commits to being logged out.

 - Three menu pages which can be created, updated and deleted by a site administrator. 

 - A blog page where users can read and post from a cake competition. Users that are registered can create, read, update and delete a post they have made.

 - A contact form where users can send a message that is saved in the data base and for the site administrator to read. 

 - 
  
# Structure

This website is made for three apps
1. Cake menus app - display menus
2. Blog app - post images and comments
3. Contact app - customer support

The menu, blog and contact apps all use a data base to store the users information. For this I have built 5 models.

---

# Data base

### Menu models
I have created three serpate models for the cake menus. Each model is identical with displaying information on cake name, description, dietary and allergens.
Once a product has been added to the data base, the site administor can select when the product is added to the menu with an on_menu option.
A created_on date is also logged to the  data base for when the product was added and a time feild. 

---

![](assets/menu%20model.png)

---

### Blog models

### Post model
This model consists of the follwing fields for a site administrator:
- A title and matching slug field

- Description field in which I installed Django summernotes libary for better text styling

- Status option for a darft post which is not posted or a pulished option to display the post

- An updated on field giving a date and time

- Feature image for an image to be uploaded with the post

- Approved field to give a final approval to diplay the post

- Likes function of the user to like a post

I wanted the administrator to control what was being posted and for future development, a user will get the option to post their own cakes.

![](assets/Post%20model.png)
---

### Comments model
This model is focused towards the user to display a comment. The model is controlled with the administors panel in the back end.
I wanted all post to be approved this way before being posted.
The data fields consist of the following:

- A CASCADE on delete function for when a comment is deleted by the user, is will be deleted from the data base also.
This is following django'sway of maintainind data integrity.

- Name field for a user to a their name, and a minimum of 80 characters

- an email feild for users email

- a body text field for the user to add a comemnt

- Created on to give a date and time of the post

- Approved option for the site administrator to approve to be posted

I have tried to follow some of the modern techniques within a comment being shown. By adding a time, date, like and to unlike a post. 

![](assets/Comment%20model.png)

---

### Contact 
The contact form is more towards a general enquiry’s form. For this reason I wanted the enquiry to be sent to the database.

I have added the following fields:

- Name - Customers full name 

- Email - Customers email

- Messgae - input box text field for any enquiries 

- Not read - for administrative purposes to show now read

- read - for administrative purposes to select when the enquiry ahs been read

![](assets/contacts%20model.png)

---

# Wire frames

### Home page
![](assets/wireframe%20home%20page.png)

![](assets/wireframes%20moblie%20home%20page.png)

---

### Menu page
![](assets/wireframe%20menus%20page.png)

![](assets/wireframes%20mobile%20menu%20page%20.png)

---

### Post detail page
![](assets/wireframe%20post%20detail%20page.png)

![](assets/framework%20mobile%20post%20detail%20page%20.png)

---

### Edit post page
![](assets/wireframe%20edit%20post%20page.png)

![](assets/wireframe%20mobile%20edit%20post%20page%20.png)

--- 

### Contact page
![](assets/wireframe%20contact%20form%20page.png)

![](assets/wireframe%20mobile%20contact%20form%20page.png)

---

- Please be aware that the wireframes may be slightly different from the original site. 

# Design

---

# Base page

- nav bar & header

- Footer

# Home page
- After getting good design ideas and information from https://elementor.com/blog/, who review website designs. I decided to keep a blank canvas in white for a background colour and then add colour with images.

![](assets/home%20page%20header.png)

### Cake competition 

![](assets/Competition%20section.png)

---

### Blog page
![](assets/post%20detail%20page.png)


---

### Menu

![](assets/menus%20-%20page.png)

---

### Contact Page
I wanted the contact for to be tested for a POST request. I used a free email service to test that the contact form can be sent to the provider.
I used a MailTrap.io https://mailtrap.io/
![](assets/email%20testing%20Mailtrap.iio.png)

![](assets/contact%20-%20form.png)

---


# Authentication

- Registration 
![](assets/registration%20page.png)

- Sign in
![](assets/sign%20in.png)


- Sign out
![](assets/log%20out%20confom.png)

---