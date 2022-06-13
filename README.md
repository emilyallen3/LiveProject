# LiveProject
This repository showcases my final project for The Tech Academy's Python Developer Bootcamp.
For two weeks I completed several user stories to create an functioning app focused on something I am passionate about.
I chose to create an app that can help Magic: The Gathering players keep track of their Commander Decks.
In this README I will explain what features I included in the app using explanations, code snippets, and videos.

About the Live Project:
This Live Project at the Tech Academy was unique because it simulated what it would be like to work on a development team. We had a sprint planning meeting, daily stand ups, and a sprint retrospective.The overall project had already been created before I joined in. I got hands on experience with verion control using Azure DevOps and PyCharm. I was able to bounce ideas back and forth with instructors, and learn from my peers and their code. The Live Project experience has prepared me in multiple ways to work as a contributing developer.

Creating the App:
This project was created using the Django framework. I used Python, sqlite3, JavaScript, CSS, and HTML. Becuase the project had already been created, I started by creating my own app within the main project. I chose to make an app about Magic: The Gathering because I am passionate about the game and enjoy playing it with my husband. It is a hobby we got into after we got married and it has brought us lots of fun and happiness during our marriage. 
I knew I wanted the app to focus on creating and viewing a database of Commander Decks(100 card collections) and also interact with an API to get more information about certain Magic Cards.

Creating a Deck:  
Aftering registering the app in the main settings, creating basic templates and styling, I made a Deck model and a form for creating a Deck. This form lets the choose the commander of the deck(the card that sets the theme and color of the deck), give it a title, a description, and list out the other key cards that will go in the 100-card deck.


Viewing the Decks:
Next I created template that would show which decks were created and stored in the database and display some of the information about the decks.


Viewing Deck Details and Comments:
When a user clicks on a deck on the view deck page they are brought to a Deck Details page that shows them more information about the deck. On this page I wanted to add the functionality to leave a comment associated with the specific deck. It's always great to get advice about decks and other potential cards that might go well int he deck that you have not thought of before. To do this I needed to create a Comment model and another form. I learned a lot through this process. In the Comment model I created a Foreign Key that coresponded to the Deck model - that way the comment would save to the specific deck. I researched a lot and asked my instructors for help. It felt so good when we were able to get it working the way I intended it to work. 

Editing and Deleting Decks and Comments:
Next I wanted to give the user the ability to edit and delete decks. 
