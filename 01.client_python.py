import os
from elasticsearch import Elasticsearch

client = Elasticsearch(
    "http://localhost:9200"
)

# client.indices.create(index="curs_index_python")

# client.index(
#     index="curs_index_python",
#     id="789",
#     document={
#         "foo": "foo",
#         "bar": "bar",
#     }
# )

response = client.get(index="curs_index_python", id="789")
print(response)

from pprint import pprint

pprint(response.body)