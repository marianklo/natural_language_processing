# Read the introduction about garden path sentences and study a few of the examples on Wikipedia.
# Create a new Python file called garden.py.
# Find at least 2 garden path sentences from the web or create them.
# Store the sentences you have identified or created in a list called gardenpathSentences
# Add the following sentences to your list:
# ○ Mary gave the child a Band-Aid.
# ○ That Jill is never here hurts.
# ○ The cotton clothing is made of grows in Mississippi.
# Tokenise each sentence in the list and perform named entity recognition.
# Examine how spaCy has categorised each sentence. 
# Using spacy.explain to print the meaning of entities.
# At the bottom of the file is writen a comment about two entities. 
# For each entity answer the following questions:
# ○ What was the entity and its explanation that you looked up?
# ○ Did the entity make sense in terms of the word associated with it?



# Import spacy and load english language model
import spacy
nlp = spacy.load("en_core_web_sm")

# Add all sentences under gardenpathSentences variable.
gardenpathSentences = ["The complex houses married and single soldiers and their families.",
"The complex houses married and single soldiers and their families.",
"Mary gave the child a Band-Aid.",
"That Jill is never here hurts.",
"The cotton clothing is made of grows in Mississippi."]


# ANSI escape code for yelow colour.
yelow = "\033[93m"
# ANSI escape code for resetting the colour.
reset = "\033[0m"



# Iterate through each sentence in the list.
for sentence in gardenpathSentences:

# Print original sentence.
    print(f"{yelow}Sentence: {reset}","\n", sentence, )

# Apply NLP to the gardenpathSentences with spaCy.
    nlp_sentence = nlp(sentence)

# Tokenise each sentence.
    print(f"{yelow}Tokenise:{reset} ")
    for token in nlp_sentence:
        print(token.orth_, "--", token.tag_,"--", spacy.explain(token.tag_))

# Find entities for each sentence and explain the entity.
    print(f"{yelow}Entities and explanation:{reset} ")
    for entity in nlp_sentence.ents:
        print(entity, "/", entity.label_,"/", entity.label,"/", spacy.explain(entity.label_))

# Create a blank space after each iteration.
    print("\n")

# Entities looked up:
# ○ What was the entity and its explanation that you looked up?
# ○ Did the entity make sense in terms of the word associated with it?

# 1."GPE" (Geo-Political Entity) - Represents countries, cities, and states.
#   In the sentence "The cotton clothing is made of grows in Mississippi.",
#   "Mississippi" is correctly categorised as a GPE, indicating the state name.
#   It makes sense as Mississippi is a state in the United States.

# 2."PERSON" -Represent person name, people.
#   In the sentence "That Jill is never here hurts."
#   "Jill" is correctly categorised as a PERSON, indicating a person name. 
#   It makes sense as Jill is a common name for a person.
