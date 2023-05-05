import streamlit as st
import nltk
import string
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
import pickle
def transform(message):
    message=message.lower()
    message=nltk.word_tokenize(message)
    for i in message:
        if i in nltk.corpus.stopwords.words('english'):
            message.remove(i)
        if i.isalnum()==False:
            message.remove(i)
    message=[ps.stem(word) for word in message]
    return ' '.join(message)
cv=pickle.load(open(r'C:\Users\aravi\Desktop\github\sms_spam\vectorizer.pkl','rb'))
model=pickle.load(open(r'C:\Users\aravi\Desktop\github\sms_spam\model.pkl','rb'))
st.title('SMS Spam detector')
sms=st.text_input('Enter your message')
new_sms=transform(sms)
input=cv.transform([new_sms])
if st.button('Predict'):
    result=model.predict(input)[0]
    if result==0:
        st.header('Not spam')
    else:
        st.header('Spam')