from scholarly import scholarly

print(next(scholarly.search_author('Steven A. Cholewiak')))
print(next(scholarly.search_author('Jorge Luis Camas Anzueto')))
print(next(scholarly.search_author('MADAIN PEREZ PATRICIO')))
# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('MADAIN PEREZ PATRICIO')
author = next(search_query).fill()
print(author)

# Print the titles of the author's publications
print([pub.bib['title'] for pub in author.publications])

# Take a closer look at the first publication
pub = author.publications[0].fill()
print(pub)

# Which papers cited that publication?
print([citation.bib['title'] for citation in pub.citedby])
