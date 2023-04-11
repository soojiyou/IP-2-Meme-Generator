import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeGenerator.MemeEngine import MemeEngine
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []

    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory

    valid_extensions = [".jpg", ".jpeg", ".png"]
    imgs = [os.path.join(images_path, file) for file in os.listdir(images_path)
            if os.path.splitext(file)[1].lower() in valid_extensions]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    # quote = random.choice(quotes)
    if not quotes:
        # Default quote if the quotes list is empty
        quote = QuoteModel("No quotes found", "Unknown")
    else:
        quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    tmp = f'./tmp/{random.randint(0, 10e10)}.png'
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(tmp, 'wb') as f:
            f.write(response.content)
    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
