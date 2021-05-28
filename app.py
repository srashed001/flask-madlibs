from flask import Flask, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story_list, story_title_list

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.secret_key = 'okayyyyyy'

debug = DebugToolbarExtension(app)

@app.route("/")
def pick_story():
    stories_titles = story_title_list

    return render_template('home.html', stories = stories_titles)

@app.route("/words")
def create_words_input():
    """ creates dynamic homepage with inputs for the words you want in your story"""
    story_title = request.args['story']

    if story_title == "tropical island":
        story = story_list[0]
    if story_title == "long ago":
        story = story_list[1]
    if story_title == "bettys story":
        story = story_list[2]
    if story_title == "anthem":
        story = story_list[3]
    if story_title == "painting thief":
        story = story_list[4]

    session['current_story'] = story
    
    

    # session['nickname'] = variableName
    
    
    words = story.prompts

    return render_template('words.html', story_words = words)

@app.route("/story")
def create_story():
    """ takes the input value for all of your words and generates a story based on text"""
    answers = dict(request.args)

    new_story = session['current_story']

    story_text = new_story.generate(answers)

    return render_template('story.html', text = story_text )