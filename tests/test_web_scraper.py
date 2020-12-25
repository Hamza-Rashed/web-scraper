from web_scraper import __version__
from web_scraper.secraper import *

def test_version():
    assert __version__ == '0.1.0'

def test_citations_counting():
    assert get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico") == 5

def test_citations_report():
    assert get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico") == ['The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][7] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.\n', 'The Mexica people arrived in the Valley of Mexico in 1248 AD. They had migrated from the deserts north of the Rio Grande[citation needed] over a period traditionally said to have been 100 years. They may have thought of themselves as the heirs to the prestigious civilizations that had preceded them.[citation needed] What the Aztec initially lacked in political power, they made up for with ambition and military skill. In 1325, they established the biggest city in the world at that time, Tenochtitlan.\n', 'The Spanish had no intention to turn over Tenochtitlan to the Tlaxcalteca. While Tlaxcalteca troops continued to help the Spaniards, and Tlaxcala received better treatment than other indigenous nations, the Spanish eventually disowned the treaty. Forty years after the conquest, the Tlaxcalteca had to pay the same tax as any other indigenous community.[citation needed]\n', "During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico.[citation needed] Europeans, Africans, and indigenous intermixed, creating a mixed-race casta population in a process known as mestizaje. Mestizos, people of mixed European-indigenous ancestry, constitute the majority of Mexico's population.\n"]
