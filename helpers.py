import re
from pickle import load
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.layers import Input, Dense, Flatten, Dropout, Embedding
from keras.layers.convolutional import Conv1D, MaxPooling1D
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import callbacks

# clean text
def clean_text(text):
    special_ch = re.compile('[-\+!~@#$%^_&*()={}\[\]:;<.>?؟/\'"]')
    english_l = re.compile('[a-zA-Z]')
    new_lines = re.compile('\s+')
    numbers = re.compile('[0-9]')
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    arabic_formation = re.compile('[~ًٌٍَُِّ،ـ×]')

    text = special_ch.sub("", text)
    text = english_l.sub("", text)
    text = new_lines.sub(" ", text)
    text = numbers.sub("", text)
    text = emoji_pattern.sub("", text)
    text = arabic_formation.sub('', text)

    return text.strip()

# load a clean dataset
def load_dataset(filename):
    return load(open(filename, 'rb'))

# fit a tokenizer
def create_tokenizer(lines):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer

# calculate the maximum document length
def max_length(lines):
    return max([len(s.split()) for s in lines])

# encode a list of lines
def encode_text(tokenizer, lines, length):
    # integer encode
    encoded = tokenizer.texts_to_sequences(lines)
    # pad encoded sequences
    padded = pad_sequences(encoded, maxlen=length, padding='post')
    return padded

# fit an encoder
def create_encoder(labels):
    encoder = LabelEncoder()
    return encoder.fit(labels)

# encode a list of labels
def encode_label(encoder, labels):
    return encoder.transform(labels)


# define the model
def define_model(length, vocab_size):
    callback = callbacks.EarlyStopping(monitor='val_loss', patience=3)
    # Model Architecture
    inputs1 = Input(shape=(length,))
    embedding1 = Embedding(vocab_size, 100)(inputs1)
    conv1 = Conv1D(filters=32, kernel_size=4, activation='relu')(embedding1)
    drop1 = Dropout(0.5)(conv1)
    pool1 = MaxPooling1D(pool_size=2)(drop1)
    flat1 = Flatten()(pool1)
    dense1 = Dense(10, activation='relu')(flat1)
    drop2 = Dropout(0.5)(dense1)
    outputs = Dense(18, activation='softmax')(dense1)
    model = Model(inputs=inputs1, outputs=outputs)
    # compile
    model.compile(loss='sparse_categorical_crossentropy', optimizer= 'adam', metrics=['accuracy'])
    # summarize
    print(model.summary())

    return model, callback
