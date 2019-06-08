### Data Query

This document refers to the *data.py* script, more precisely the query inside the script.

The query has the base URL [https://data.gov.in/](https://data.gov.in/) and following attributes (the order matters):

1. query

The value that will be used to search documents

2. field_search

Filter to search in a specific attribute of the documents that are returned on search

  - title: search only in the document's title
  - body: search only in the document's body
  - field_keywords: search only in the document's keywords

If the field is empty, all the field_search types are going to be used

3. item
  
  The amount of documents returned in each page of the query made: 10, 20, 30, 50 or 100

4. exact_match
   
Specify if the query value needs to be exactly the same in the document, i.g in the field_search chosen

5. page

The number of the page: 1, 2, 3...

### Example

The following its an example of a query:
 
[https://data.gov.in/search/site?query=maharajganj&field_search=title%5E2&item=100&exact_match=1](https://data.gov.in/search/site?query=maharajganj&field_search=title%5E2&item=100&exact_match=1)