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
