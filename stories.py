"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story_list = [
    Story(["adjective", "noun1", "verb", "noun2", "plural_noun"],
    """I once went to a {adjective} tropical island. I came across
        a {noun1} which made me {verb}. I wasn't sure what to do, so I ran 
        to the {noun2} and grabbed some {plural_noun}"""),

    Story(["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""),

    Story(["place", "body_part", "verb", "adjective", "plural_noun", "liquid"],
    """Betty went to the {place} to {verb}. She saw an {adjective} 
        man carrying {plural_nouns}.She scratched her {body_part} and 
        jumped into a pool of {liquid}."""),
        
    Story(["color", "noun1", "noun2", "plural_noun"],
    """And the rockets' {color} glare, the {plural_noun} bursting 
        in {noun1}, Gave proof throught the night that our {noun2} was still there."""),
        
    Story(["place", "noun1", "noun2", "number", "adjective"],
    """After hiding the painting in his {noun1} for {number} years, he grew
        {adjective} and tried to sell it to a/an {noun2} in {place}, but was
        caught""")]

story_title_list = ["tropical island", "long ago", "bettys story", "anthem", "painting thief"]