# PawfectMatch

PawfectMatch connects families looking to adopt a pet in Thailand with stray animals. Only a small number of animal shelters run out of actual facilities. To operate without a shelter, many rescuers try to place stray animals in local foster homes. Establishing a network like this in Thailand could facilitate the connection of more foster families and families who are looking to adopt a stray in various districts.  

This semester, I'm taking two courses: CSCI E-33a Web Programming with Python and Javascript and CS 50 - Introduction to Computer Science.  Several topics in CS50 were discussed in depth in CSCI E-33a such as Python, SQL, HTML, Javascript, and Flask.  As a result, I chose the Django Framework for the PawfectMatch web application, which served as both classes' final capstone project. 

## DATA MODELS
The default User model is extended with additional fields to support the registration of the shelter staff and foster families. Registered users are allowed to create a profile for the stray animal. The onboarding of the shelters is currently done by hand through the Django admin interface. 

As of the initial release, the Pet Model only supports stray dogs because adopting a stray dog among the expat communities requires more considerations due to their size and the potential cost of transporting them back to the expat’s home countries. However, the model can be simply extended to support other animals like cats, turtles, hampers, and such. 

One of my earliest issues was configuring the Pet model to handle both the search pet screen and the creation/update of pet forms. Because both screens employ separate user controls to enable the search and form input functions, two Django forms Python classes are created from the same Pet model to handle the two functionalities. 

## HOME PAGE
The PawfectMatch home page consists of two main components: a list of the most recently registered animals and the ability to browse animals from a particular rescue group that is already location-specific. To read the animal’s detailed profile, click on its name or photo. 

## PET PROFILE PAGE
Apart from the typical physical attributes such as size, age, and breed, the Pet Profile page strives to provide more important information about the animals’s training, temperament, and health status.

The comment session allows users to contact the shelter staff or foster families for more information or to plan a visit with the animal.

The Edit button is only visible to the user if the user previously created the pet profile. 

Clicking on the Adopt or Foster Buttons only pops up an alert model window for now. In the future release, the notification module will send notifications to the shelter staff or foster families to initiate the adoption process. 

## SEARCH PAGE
The Pet Search Page allows interested families to search for animals depending on their training, health status, and temperament. 

## FAVORITE PAGE
The favorite page provides easy access to a list of the current user’s favorite animals. 


## CREATE PET PROFILE FORM
Shelter officials or foster families create a specific profile for the animal.  As previously indicated, the Pet model is designed primarily for dogs in the initial release. 

In the future release, the system will enable users to upload multiple images or videos of the animal, enhancing the level of detail available. 


## FUTURE STATE
I would like to enhance the following functionality in the future release:
- Ability to upload multiple images/video of the animal
- Ability for the foster family or shelter staff to arrange pet transport between districts within Thailand. 
