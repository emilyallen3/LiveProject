# LiveProject
This repository showcases my final project for The Tech Academy's Python Developer Bootcamp.
For two weeks I completed several user stories to create a functioning app focused on something I am passionate about.
I chose to create an app that can help Magic: The Gathering players keep track of their Commander Decks.
In this README I will explain what features I included in the app using explanations, code snippets, and videos.

#About the Live Project:<br>
This Live Project at the Tech Academy was unique because it simulated what it would be like to work on a development team. We had a sprint planning meeting, daily stand ups, and a sprint retrospective. The overall project had already been created before I joined in. I got hands-on experience with version control using Azure DevOps. The IDE I used was PyCharm. I was able to bounce ideas back and forth with instructors and learn from my peers and their code. The Live Project experience has prepared me in multiple ways to work as a contributing developer.

#Creating the App:<br>
This project was created using the Django framework. I used Python, sqlite3, JavaScript, CSS, and HTML. Because the project had already been created, I started by creating my own app within the main project. I chose to make an app about Magic: The Gathering because I am passionate about the game and enjoy playing it with my husband. It is a hobby we got into after we got married and it has brought us lots of fun and happiness during our marriage. 
I knew I wanted the app to focus on creating and viewing a database of Commander Decks (100-card collections) and interact with an API to get more information about certain Magic Cards.

#Creating a Deck:<br>
After registering the app in the main settings, creating basic templates and styling with HTML and CSS, I made a Deck model and a form for creating a Deck. This form lets user the choose the commander of the deck (the card that sets the theme and color of the deck), give it a title, a description, and list out the other key cards that will go in the 100-card deck.


#Viewing the Decks:<br>
Next, I created a template that would show which decks were created and stored in the database and display some of the information about the decks.


#Viewing Deck Details and Comments:<br>
When a user clicks on a deck on the View Decks page, they are brought to a Deck Details page that shows them more information about the deck. On this page I wanted to add the functionality to leave a comment associated with the specific deck. It's always great to get advice about decks from other players and learn about other potential card combinations that might go well in your deck. To do this I needed to create a Comment model and another form. I learned a lot through this process. In the Comment model I created a Foreign Key that corresponds to the Deck model - that way the comment would save to the specific deck. I researched a lot and asked my instructors for help. It felt so good when we were able to get it working the way I intended it to work. Instead of taking the user to a new page to leave a comment I created a pop-up modal using JavaScript.

#Editing and Deleting Decks and Comments:<br>
Next, I wanted to give the user the ability to edit and delete decks. I did this by getting the Deck primary key and returning the form that created the deck. There the user could make changes to the deck and save those changes. Also, on the edit page the user could select to delete the deck. Doing so would take the user to another page where they could confirm that they really did want to delete the deck from the database permanently. This functionality also inspired me to add the ability to delete comments. Again, I had to reference both the Comment primary key and the Deck primary key. I was able to get the Deck primary key by way of the Foreign Key in the Comment model. The ability to edit comments is a feature I was not able to complete during the two weeks but is a feature I would like to add in the future.

#Connecting to the API:<br>
Before this project I had very little understanding of an API. I knew I wanted to use it on my project, so I really threw myself into learning more about it. At first it was very complex and complicated, but after working with an instructor and really testing it out in my code I was finally able to get it working! I was so excited! I gained more confidence in myself that I can do this job. I can come up against difficult problems and persevere to find a solution. I used the Scryfall API. Scryfall is my favorite Magic: The Gathering website. It is a robust search engine of Magic Cards. I have found it so helpful when building decks.

#Using the API:<br>
There is so much you can get out of the Scryfall API. On my app I opted for giving the user the ability to search for a card by name and getting the image of the card to appear. In the future I would like to add more integration with the API - such as giving the user the ability to select cards from the Scryfall database to add to their commander deck on the Create Deck Form. 

#Conclusion:<br>
I am quite pleased with my app. I am proud of myself. 8 months ago, I had never coded a thing in my life and here I have a created a fully functioning website in two weeks! I feel like Hercules, going from Zero to Hero. Like I mentioned above there are more features I would like to add, which is exciting to me! The ability to create, solve problems, and improve brings me joy. I am only going to get better from here. I am eager to continue creating more tools that can help people.
