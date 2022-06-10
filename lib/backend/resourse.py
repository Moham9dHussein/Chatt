stop_words = [
        'they', 'a', 'is', 'hadn', "you'd", 'an', 'has', 'did', 'm', 'y', 'me',
        'here', 'which', "shan't", 'our', "hasn't", 'by', 'its', "that'll", 'at',
        't', 'yourself', 'myself', 'these', 'because', 'should', 'to', 'he', "mustn't",
        'am', 'not', 'with', 'was', 'you', 'from', 'd', "mightn't", 'further', 'down',
        'but', 'other', 'more', 'then', "haven't", 'will', 'while', 'doing', 'him',
        'who', 'do', 'his', 'only', 'few', 'couldn', 'shan', 'and', 'isn', 'having',
        'i', 'just', 'wasn', "weren't", 's', 'under', "needn't", 'there', 'wouldn',
        'out', 'such', 'why', 'any', 'yourselves', 'some', 'them', 'needn', 'off',
        'didn', 'of', 'or', 'weren', 're', 'about', 'before', "you'll", 'when',
        'below', 'in', "isn't", 'her', 'theirs', 'be', 'she', 'herself', 'ourselves',
        "it's", 'doesn', "couldn't", 'ma', 'won', 'themselves', 'yours', 'those', 'were',
        "you've", 'no', 'very', 'your', "aren't", 'nor', 'had', 'on', "she's", 'until',
        'during', 'aren', 'through', 'hasn', 'itself', 'all', 'have', 'are', 'if', 'shouldn',
        'once', 'does', 'it', 'each', "shouldn't", "wasn't", 'above', 'between', 'over', "don't",
        'haven', "wouldn't", 'can', 'both', 'now', 'my', 'we', "hadn't", 'same', 'been', 'mustn', 'being',
        'most', 'the', "didn't", 'll', 've', 'as', 'o', 'this', 'that', 'up', 'into', 'too', "should've",
        'against', 'mightn', 'again', 'hers', 'how', 'than', 'whom', 'himself', 'ours', 'for', 'ain', "doesn't",
        'what', "won't", 'own', 'don', 'so', 'their', "you're", 'after', 'where']

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}


possible_answer = {
    "hi hey hello": "hey Dude",
    "name": "Hey, My Name is Magnom",
    "old created creator program programmed programer programming": "I'm a chatbot, My Creator 'Mohamed Hussein'\nwrite my Code at 10/5/2020 1:00AM:)",
    "sad upset disappointed": "Hey, Don't be weak",
    "happy": "that's great",
    "weather climate": "it's fine",
    "happy good well fine": "that's great",
    "love": "i love you <3",
    "sorry": "Its OK, never mind",
    "health": "I'm Eating the RAM ;)",
    "sports sport game fun entertainment": "I'm a very big fan of Football",
    "yes ok okay": "okay",

}



block_answer = {
    "how are you": "i'm Fine, and you?",
    "how are you?": "i'm Fine, and you?",
    "how are you ?": "i'm Fine, and you?",
    "how are you": "i'm Fine, and you?",
    "i love you": "i love you too <3",
    "hey magnom": "yeah, what ?",
}

