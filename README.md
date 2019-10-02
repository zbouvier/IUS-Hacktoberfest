   * [IUS-Hacktoberfest](#ius-hacktoberfest)
      * [How do I get my name added](#how-do-i-get-my-name-added)
      * [Running IUS-Hacktoberfest in a python virtual environment](#running-ius-hacktoberfest-in-a-python-virtual-environment)
         * [Pre-work](#pre-work)
         * [Install dependencies](#install-dependencies)
         * [Run the app](#run-the-app)
         * [Done!](#done)
     * [Running IUS-Hacktoberfest in Docker](#running-ius-hacktoberfest-in-docker)
         
# IUS-Hacktoberfest

A collection of data points and a data visualization model for the 2019 Hacktoberfest at IUS

The goal of this program is to provide IUS data science students with some information about our local hacktoberfest participation.

To have your name added to the JSON you must be an IU student, but if anyone wants to think of interesting ways to show that data, they are welcome to.


## How do I get my name added

The format for your new addition should look like this: (TODO)
First: Open the data.json file. You should see something simliar to this:

```json
{
    "people":
    [
    {
        "name": "Zach Bouvier",
        "major": "Computer Science - Math and Science",
        "role": "Student",
        "year": "Freshman",
        "profile": "https://github.com/zbouvier",
        "optionalInformation":
        {
            "favoriteLanguages": ["Python", "Chef", "F#"],
            "hobbies": ["Long walks on the beach", "Yelling at everybody", "Big Data"]
        }
    },
    {
        "name": "Chris Sexton",
        "major": "Computer Science",
        "role": "Professor",
        "year": "",
        "profile": "https://github.com/chrissexton",
        "optionalInformation":
        {
            "favoriteLanguages": ["Go", "F#"],
            "hobbies": ["Cats", "Giving Hard Homework Assignments", "Reddit"]
        }
    }
    ]
}
```

Secondly, you want to add a comma after the previous person



```json
{
    "people":
    [
    {
        "name": "Zach Bouvier",
        "major": "Computer Science - Math and Science",
        "role": "Student",
        "year": "Freshman",
        "profile": "https://github.com/zbouvier",
        "optionalInformation":
        {
            "favoriteLanguages": ["Python", "Chef", "F#"],
            "hobbies": ["Long walks on the beach", "Yelling at everybody", "Big Data"]
        }
    },
    {
        "name": "Chris Sexton",
        "major": "Computer Science",
        "role": "Professor",
        "year": "",
        "profile": "https://github.com/chrissexton",
        "optionalInformation":
        {
            "favoriteLanguages": ["Go", "F#"],
            "hobbies": ["Cats", "Giving Hard Homework Assignments", "Reddit"]
        }
    },  <-------------------------------- like this
    ]
}
```

Thirdly, copy the code of the previous person, and edit it to your heart's content. Like so:

```json
{
    "people":
    [
    {
        "name": "Zach Bouvier",
        "major": "Computer Science - Math and Science",
        "role": "Student",
        "year": "Freshman",
        "profile": "https://github.com/zbouvier",
        "optionalInformation":
        {
            "favoriteLanguages": ["Python", "Chef", "F#"],
            "hobbies": ["Long walks on the beach", "Yelling at everybody", "Big Data"]
        }
    },
    {
        "name": "Chris Sexton",
        "major": "Computer Science",
        "role": "Professor",
        "year": "",
        "profile": "https://github.com/chrissexton",
        "optionalInformation":
        {
            "favoriteLanguages": ["Go", "F#"],
            "hobbies": ["Cats", "Giving Hard Homework Assignments", "Reddit"]
        }
    },
    {
        "name": "John Smith",
        "major": "Informatics",
        "role": "Student",
        "year": "Senior",
        "profile": "https://github.com/<yourGithubUsername>",
        "optionalInformation":
        {
            "favoriteLanguages": ["Python", "JavaScript"],
            "hobbies": [""]
        }
    }
    ]
}
```

Please note that there **is not** a comma at the end of your new person.

Once you've successfull added your person. Please run py dataPresenter.py to make sure your json was formatted correctly.


## Running IUS-Hacktoberfest in a python virtual environment

### Pre-work

We need to set up a [python venv](https://docs.python.org/3/library/venv.html) first. We'll need to do this in Python 3.

So, using your Python 3 installation (verify version with `python --version` or `python3 --version`), change into this source directory and run:

`python -m venv .venv` or `python3 -m venv .venv` depending on your set up. You can name your venv folder whatever you wish (.venv is just a convention), and even create them elsewhere besides this directory. It only matters that you do create it and activate the venv so you keep your global python install clean. Good python hygiene. ;)

Then let's activate the venv.  This needs to happen EVERY time we want to run this project, so don't forget:

`source .venv/bin/activate`

### Install dependencies

Haven't installed the dependencies before?

`pip install -r requirements.txt`

This only needs to be done on fresh install, or if dependencies change obviously.

### Run the app

Now we just run the app:

`python dataPresenter.py`

### Done!

Since we're now done, we can deactivate the venv (or just close your terminal session):

`deactivate`
## Running IUS-Hacktoberfest in Docker
1. Clone the repo, and enter the directory
2. Build the Docker image: `docker build -t NAME .`
3. Run the container: `docker run -it --rm NAME`