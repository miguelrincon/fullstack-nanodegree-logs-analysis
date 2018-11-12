#!/usr/bin/env python3

# Analysis of visits in a new website

import psycopg2

def main():
  print('Analysis will start...')
  conn = psycopg2.connect(dbname='news')
  most_popular_articles(conn)
  most_popular_authors(conn)
  conn.close()
  print('Analysis is finished.')

def most_popular_articles(conn):
  cur = conn.cursor()
  cur.execute('''
    SELECT articles.title, count(*) AS views
    FROM articles, log
    WHERE log.path LIKE '/article/' || articles.slug
    GROUP BY articles.title
    ORDER BY views DESC
    LIMIT 10;
    ''')
  result = cur.fetchall()
  cur.close()

  print_results('Answer 1 - Top 3 articles are:', result)
  return result

def most_popular_authors(conn):
  cur = conn.cursor()
  cur.execute('''
    SELECT authors.name, count(*) as views
    FROM authors, articles, log
    WHERE authors.id = articles.author
      AND log.path LIKE '/article/' || articles.slug
    GROUP BY authors.name
    ORDER BY views DESC
    ''')
  result = cur.fetchall()
  cur.close()

  print_results('Answer 2 - Top authors by views are:', result)
  return result

def print_results(header, results, units='views'):
  print(header)
  for row in results:
    print ('  \"%s\" -- %s %s' % (row[0], row[1], units))

if __name__ == '__main__':
  main()
