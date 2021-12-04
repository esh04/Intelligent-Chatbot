# Intelligent-Chatbot

A chatbot is an intelligent piece of software that is capable of communicating and performing actions similar to a human. Chatbots are used a lot in customer interaction, marketing on social network sites and instantly messaging the client. 
Our chatbot is a **COVID CHATBOT**. The primary focus of the bot is to guide people in the ongoing pandemic, answer questions regarding vaccinations, symptoms, live covid statistics, probability of being infected to name a few. 

To run the chatbot locally: `python3 chatgui.py` 

`chatgui.py` contains the GUI of the chatbot using which the user can interact with the bot. `Tkinter` has been used to make this.


### Training of the Chatbot
- Run `python3 train_chatbot.py` in the terminal to train the chatbot. 
    - `words.pkl`, `classes.pkl` and `chatbot_model.h5` will be generated.
    - `words.pkl` stores the the words Python object that contains a list of our vocabulary, `classes.pkl` contains the categories and `chatbot_model.h5` contains the trained model that contains information about the model and has weights of the neurons.
- We have trained our chatbot using the `keras` module and`nltk` wordnets to the intents.json present in the Data folder.  
- A special recurrent neural network (LSTM) is used to classify which category the user’s message belongs to and then we will give a random response from the list of responses.

## Functionalities
### Probability of being infected
An existing dataset was used to collect data regarding 7 features and the state of the patient(i.e. if she/he has COVID or not). Using the data, a Naive Bayes Classifier from the `sklearn` module was trained in order to predict new cases of COVID. The user is asked to input the details in a specific format after which the classifier predicts probability of the user having COVID.

### Live covid statistics
The statistics for the mentioned state are being scraped live from https://www.oneindia.com/coronavirus-affected-cities-districts-in-india.html using `BeautifulSoup`.

### Covid news
News regarding covid for the mentioned state are being scraped live from Bing news using `BeautifulSoup`.

### Information regarding vaccinations 
The bot tries to answer questions regarding vaccinations and directs further questions to the cowin website of the Government of India. 

-----