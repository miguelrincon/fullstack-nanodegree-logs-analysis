#!/usr/bin/env python3

# Analysis of visits in a new website

import psycopg2
import datetime


def main():
    """Displays a series of results of analysis of news logs."""
    print('Analysis will start...\n')
    conn = psycopg2.connect(dbname='news')
    most_popular_articles(conn)
    most_popular_authors(conn)
    days_more_than_1_percent_errors(conn)
    days_more_than_1_percent_errors_b(conn)
    conn.close()
    print('\nAnalysis is finished.')


def most_popular_articles(conn):
    """Displays the 3 most popular articles by views."""
    cur = conn.cursor()
    cur.execute('''
    SELECT articles.title, count(*) AS views
    FROM articles, log
    WHERE log.path = '/article/' || articles.slug
    GROUP BY articles.title
    ORDER BY views DESC
    LIMIT 3;
    ''')
    result = cur.fetchall()
    cur.close()

    print_results(
        'Answer 1 - What are the most popular three articles of all time?:',
        result
    )
    return result


def most_popular_authors(conn):
    """Displays the most popular authors of all time by views."""
    cur = conn.cursor()
    cur.execute('''
    SELECT authors.name, count(*) as views
    FROM authors, articles, log
    WHERE authors.id = articles.author
    AND log.path = '/article/' || articles.slug
    GROUP BY authors.name
    ORDER BY views DESC;
    ''')
    result = cur.fetchall()
    cur.close()

    print_results(
        'Answer 2 - Who are the most popular article authors of all time?:',
        result
    )
    return result


def days_more_than_1_percent_errors(conn):
    """Displays days which have more than 1% of errors using nested queries."""
    cur = conn.cursor()
    cur.execute('''
    SELECT
        views.day,
        round((errors.count * 100.0 / views.count), 2) as percent_errors
    FROM
      (SELECT time::date as day, count(*) as count
      FROM log
      GROUP BY day) as views
    JOIN
      (SELECT time::date as day, count(*) as count
      FROM log
      WHERE status NOT LiKE '2__ %'
      GROUP BY day) as errors
    ON views.day = errors.day
    WHERE round((errors.count * 100.0 / views.count), 2) > 1;
  ''')
    result = cur.fetchall()
    cur.close()

    print_results(
        'Answer 3 - On which days did more than 1% \
of requests lead to errors?:',
        result,
        '% errors'
    )
    return result


def days_more_than_1_percent_errors_b(conn):
    """Displays days which have more than 1% of errors using a single join."""
    cur = conn.cursor()
    cur.execute('''
    SELECT time::date as day,
      round(count(errors.is_error) * 100.0 / count(log.id), 2) as perc_errors
    FROM log
    LEFT JOIN (
      SELECT log.id, 1 as is_error
      FROM log
      WHERE status NOT LIKE '2__ %'
    ) as errors
    ON errors.id = log.id
    GROUP BY day
    HAVING count(errors.is_error) * 100.0 / count(log.id) > 1;
  ''')
    result = cur.fetchall()
    cur.close()

    print_results(
        'Answer 3 - On which days did more than 1% \
of requests lead to errors? (Alternative solution):',
        result, '% errors')
    return result


def print_results(header, results, units=' views'):
    print(header)
    for row in results:
        label = row[0]
        if isinstance(label, datetime.date):
            label = label.strftime("%B %d, %Y")
        print('  "{}" -- {}{}'.format(label, row[1], units))


if __name__ == '__main__':
    main()
