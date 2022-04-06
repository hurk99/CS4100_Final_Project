from SummarizerRobot import SummarizerRobot

txt = """Ukraine has updated its extensive wishlist of additional military assistance from the US government in the past several days to include hundreds more anti-aircraft and anti-tank missiles than previously requested, according to a document provided to CNN that details the items needed.
The Ukrainians have submitted similar lists in recent weeks but a recent request provided to US lawmakers appears to reflect a growing need for American-made Stinger anti-aircraft missiles and Javelin anti-tank missiles -- with Ukraine saying it urgently needs 500 of each, daily. 
In both cases, Ukraine is asking for hundreds more missiles than were included in a similar list recently provided to US lawmakers, according to a source with knowledge of both requests.

The new list comes as the Ukrainians have claimed they face potential weapons shortages amid an ongoing Russian assault -- prompting some pushback from US and NATO officials who stress that more military aid is already going into the country.

By March 7, less than two weeks into Russia's invasion of Ukraine, the US and other NATO members had sent about 17,000 anti-tank missiles and 2,000 anti-aircraft missiles into Ukraine.

Since then, NATO countries, including the US, have kept the pipeline of weapons and equipment flowing, even as Russia has threatened to target the shipments.
The last of a US $350 million security assistance packaged approved in late February arrived in Ukraine within the last few days, a senior defense official said, while the next two packages totaling $1 billion have already started to arrive.
"""

r = SummarizerRobot(txt)

r.create_similarity_matrix()
print(r.similarity_matrix)
print()

r.create_frequency_table()
print(r.word_frequency_table)
print()

r.set_sentence_value_table()
print(r.sentence_value_table)
print()

print(r.summarize(1.1))
print()