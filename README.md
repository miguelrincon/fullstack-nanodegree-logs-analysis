
## Log Analysis Project

The Log Analysis Project aims to solve 3 questions to report on the visits and popularity of a newspaper site.

The project is split in several methods which solve each of the questions required:

1. What are the most popular three articles of all time?
1. Who are the most popular article authors of all time?
1. On which days did more than 1% of requests lead to errors? 

For each question the result will be displayed in the format. An additional `results.txt` file is included with the output of the program.

### Setup

#### Using a VM

Requirements:

* Vagrant
* VirtualBox

Get the Vagrantfile from: https://github.com/udacity/fullstack-nanodegree-vm and run
```
$ vagrant up
$ vagrant ssh
```

#### Using your machine

Requirements:

* Python 3
* PostgreSQL
* psycopg2

### Run the project

The project works by connecting to a PostgreSQL database called `news`. You can downlad the data, import to a new database and run the analysis script.

1. Get the data zip file from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2. Unzip the file to your working directory, the file is called `newsdata.sql`
3. Load the data to a new `news` database with the command: `psql -d news -f newsdata.sql`
4. Run the script by using `python3 logs_analysis.py` and see the output

### Design

The connection to the database is opened by the `main` method and passed to each of the methods which answer a single question each.

Each method, e.g. `most_popular_articles` runs an outputs the result of the query.

An alternative has been provided for question 3, as I found interesting to use 2 approaches to this problem.