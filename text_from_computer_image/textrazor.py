import textrazor as textrazor
textrazor.api_key = "aeb1da41d8e2f608f805c35ca1e4467722a6607047352f6c5689aff8"

client = textrazor.TextRazor(extractors=["entities", "topics"])
response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")

for entity in response.entities():
    print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)