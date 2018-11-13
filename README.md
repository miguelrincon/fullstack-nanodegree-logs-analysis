
## Log Analysis Project

The Log Analysis Project aims to solve 3 questions to report on the visits and popularity of a newspaper site.

The project is split in several methods which solve each of the questions required:

1. What are the most popular three articles of all time?
1. Who are the most popular article authors of all time?
1. On which days did more than 1% of requests lead to errors? 

For each question the result will be displayed in the format. An additional `results.txt` file is included with the output of the program.

### Design

The connection to the database is opened by the `main` method and passed to each of the methods which answer a single question each.

Each method, e.g. `most_popular_articles` runs an outputs the result of the query.

An alternative has been provided for question 3, as I found interesting to use 2 approaches to this problem.