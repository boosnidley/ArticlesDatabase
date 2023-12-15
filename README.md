## Databases Project 2
### Group 4: Brady, Ian, and Tyler

To run this code, first create a virtual environment.

Then run `python -m pip install "pymongo[srv]"` to install the python mongodb library in your virtual environment. Create a file in the project called "password.py" and create a variable inside that file called "password" and set it equal to your password to access the mongodb instance.

The connection string file contains the connection string with a reference to the password you just created. You should now have access to the database. If you have trouble with access, contact Tyler.

The application allows you to query a sample news article database. You can bookmark articles that you find interesting and view your bookmarks at any time. Enjoy!


### Database Schema

{
    publisher: String,
    title: String,
    authors: String[],
    tags: String[],
    date: String ("yyyy-mm-dd")
}

Example:

{
    publisher: "CNN",
    title: "Today on the Hill",
    authors: ["Bubba", "Sally"],
    tags: ["Politics", "USA", "News"],
    date: "2023-12-07"
}
