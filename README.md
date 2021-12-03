# Intelligent-Chatbot
to run the file locally: `python3 chatgui.py` 

`chatgui.py` contains the GUI of the chatbot using which the user can interact with the bot. 

### Training of the Chatbot
- run `python3 train_chatbot.py` in the terminal to train the chatbot. 
    - `words.pkl`, `classes.pkl` and `Chatbot_model.h5` will be generated.
    - `words.pkl` stores the the words Python object that contains a list of our vocabulary, `classes.pkl` contains the categories and `Chatbot_model.h5` contains the trained model that contains information about the model and has weights of the neurons.
- We have trained our chatbot using the `keras` module and`nltk` wordnets to the intents.json present in the Data folder.  
- A special recurrent neural network (LSTM) is used to classify which category the user’s message belongs to and then we will give a random response from the list of responses.

## Functionalities
### Probability of being infected

`sklearn`
### Live covid statistics
The statistics for the mentioned state are being scraped live from https://www.oneindia.com/coronavirus-affected-cities-districts-in-india.html using `BeautifulSoup`.

### Covid news
News regarding covid for the mentioned state are being scraped live from Bing news using `BeautifulSoup`.

### Information regarding vaccinations 
The bot tries to answer questions regarding vaccinations and directs further questions to the cowin website of the Government of India. 