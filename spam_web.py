import streamlit as st
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle

stemmer = PorterStemmer()
st.title('Welcome to Spam Classifer')
st.subheader('I can help you to classify spam messages ',divider='rainbow')
with st.container(height=250):
    message = st.text_area('Enter your message here',)
    but= st.button('Check')

def clean_message(message):
  message= message.lower()
  message= nltk.word_tokenize(message)

  m=[]
  for i in message:
    if i.isalnum():
        m.append(i)
  message=m[:]
  m.clear()
  for i in message:
    if i not in stopwords.words('english') and i not in string.punctuation:
        m.append(i)
  message=m[:]
  m.clear()
  m = []
  for i in message:
      m.append(stemmer.stem(i))


  return " ".join(m)

vec = pickle.load(open('vectorizer.sav','rb'))
spam_df = pickle.load(open('spam_webapp.sav','rb'))
message_df = clean_message(message)
vec = vec.transform([message_df])
pred = spam_df.predict(vec)[0]
if but:
    if pred ==1:
        st.subheader('The message is spam ❌')
    else:
        st.subheader('The message is not spam ✅')
