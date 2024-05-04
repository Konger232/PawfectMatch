# PawfectMatch

PawfectMatch is a service that allows users to easily adopt dogs based on their search criteria. The website is intended to help non-profit animal rescue organizations and shelters in Thailand. These groups frequently have limited space and resources. By connecting these rescuers and shelters, the website may help to spread the message to interested persons. 


## Description

The intial phrase of this project provide the following functionalities:
 
- **Search Pet Page:** Users can search by animal type, gender, age, location, and more. Currently the system only supports search for dog. It can be easily expanded for other animals in the future. 

- **Search result page:** Display searched results based on the user's input criteria.

- **Pet Profile page:** Each pet has a dedicated profile page featuring adoption status, name, color, age, size, gender, etc. Users can add pets to their favorites and interact via a form to schedule an in-person visit/tele-visit or request more photos.

- **My Favorites:** Users can view and manage their list of favorite pets.

- **Register and Login screens:** Users can create a new account or log in to one that already exists.  

- **Images:** The media path is configured to store all uploaded photos. However, as of the initial phrase, the Pet model only accepts the image path as a CharField. In the future, this capability will be expanded to allow for the posting of multiple photos or videos per Pet. 


## Getting Started

### Built with

* [![Python][Python-img]][Python-url]
* [![Django 5.0.1][Django-img]][Django-url]
* [![SQLite][Sqlite-img]][Sqlite-url]
* [![Bootstrap 5.2.3][Bootstrap-img]][Bootstrap-url]

### Installing

* Unzip PawfectMatch zip file. And you should see the following directory structure:
```
    - Final_Project
    |_ PawfectMatch
      |_ adopt
        |_ admin.py
        |_ apps.py
        |_ forms.py
        |_ migrations\
        |_ models.py
        |_ static\
        |_ templates\
        |_ urls.py
        |_ views.py
      |_ db.sqlite3
      |_ manage.py
      |_ media
        |_ uploads
          |_ adopt
            |_ ....sample pet photos
      |_ PawfectMatch
        |_ settings.py
        |_ urls.py
      |_ Readme.md
      |_ Design.md
      |_ requirements.txt


```

* You will need at least Pyhon 3.12.1. Check your version by typing 
```
     python3 --version
```

* Check if you have the Django version.
```
      django-admin --version
```

* Install Django in the final project directory.
```
      python3 -m pip install Django
```

### Executing program

* Change the working directory to the /pawfectMatch folder. Create the Django migrations by running 
```
      cd pawfectmatch
      python3 manage.py makemigration adopt
```
* Once the migration files created, apply the migration configuration to the Django project
```
      python3 manage.py migrate
```

* Now you should be ready to run the PawfectMatch Django application
```
      python3 manage.py runserver 
```
* Copy the URL http://127.0.0.1:8000/ to your browser


## Help

Refer to the [PawfectMatch Demo Video](https://youtu.be/yzmfJwC22MY) for more resources. 


## Authors

Ping Kong

Please reach out to [@Ping Kong](mailto:yek089@g.harvard.edu) for any question you might have. 

## Version History

* 0.1
    * Initial Release


## Acknowledgments

Inspiration, code snippets, etc.
* [DomPizzie](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [PetFinger](https://www.petfinder.com/)
* [Nonthaburi Animal Welfare Alliance - NAWA](https://www.facebook.com/NAWAlliance/)
* [The Adoptable Puppy Cafe](https://www.facebook.com/theadoptablepuppycafe/)
* [Soi Dog Foundation](https://www.soidog.org/)
* [Lanta Animal Welfare](https://lantaanimalwelfare.com/)
* [Geeksforgeeks](https://www.geeksforgeeks.org/how-to-make-the-background-of-a-div-clickable-in-html/)




<!-- LINKS and IMAGES -->
[Django-img]: https://img.shields.io/badge/django-blue?style=for-the-badge&logo=Django&logoColor=white
[Django-url]: https://docs.djangoproject.com/en/5.0/
[Bootstrap-img]:https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]:https://getbootstrap.com
[Python-img]:https://img.shields.io/badge/Python-green?style=for-the-badge&logo=Python&logoColor=white
[Python-url]:https://www.python.org/
[Sqlite-img]:https://img.shields.io/badge/SQLite-lightblue?style=for-the-badge&logo=Sqlite&logoColor=white
[sqlite-url]:https://www.sqlite.org/
