def count_words(string, stop_words=""):
    import re
    tmp = {}
    skip_words = stop_words
    words = re.split('\W+',string.lower())

    for i in words:
        if i not in skip_words:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] = tmp[i] + 1
        else:
            pass
        
                
    #Task does not require sorting :)
    return tmp


test_me = """cried his the as a one under first established wall and For \
bitterly eyes he the of had and the in from its and one tried appears by \
to in which their himself however once express given dark hands ages end \
and his hands paupers the the himself impious To surface in he It \
assembled all of a by crouching to prediction came even was handkerchief \
close and suppose on order out the to waking waistcoat impious to seals \
hard There profane anon the when himself other character the to the \
There dismal prophetic He still by closer prophetic room he and and \
individual been luxury ever and of the and articles was commission that \
of and loneliness before of times under to gentleman for character \
profane of more in s tried the corner future decided solitary s in \
namely the week close his pocket by for little tremble the after and to \
once the of and this wall pocket Oliver and been if that in To \
protection from assembled Oliver the of council sleep little appears of \
and closer individual solemnly on solitary first s if hook a corner when \
start for drawing of prediction and sage board sleep to not of a a of \
surface in the week solemnly unreasonable if darkness the with one \
pronounced childishness if even sight obstacle all feat waistcoat the in \
to dismal had gloom Oliver articles for surrounded a paupers being \
bitterly offence the spread at shut a handkerchiefs order crouching the \
himself for tying suppose board in youth and of ever unreasonable had \
end long to sight one hands noses at feel only respect room respect all \
a he start for closer were offence day prisoner obstacle to board and \
and a in in wall he waking For a white the a becoming noses \
handkerchiefs consigned its entertained mercy have and feeling and that \
established and and long to pocket gentleman wisdom given remained he \
more to mercy ever namely shut came there a gloom the their of which his \
the in entertained obstacle times and seals future s of being hands \
express performance of by It had performance commission hard to other \
and the the would white and all as of He ever tremble drawing board the \
removed of night council feel greater wisdom asking for and after in a \
feeling luxury prisoner handkerchief and have cried remained not and by \
attaching cold the had the before the had anon which and pronounced the \
greater was obstacle only to there ages with his wall was the dark would \
however this been for that the the loneliness of to and a been his still \
removed Oliver night protection hook tying childishness pocket of the \
asking that day him surrounded in were him attaching sage youth feat \
becoming and and eyes the which darkness closer out cold that the \
decided the the  consigned spread"""

stop_words = ["a", "able", "about", "above", "abroad", "according",
"accordingly", "across", "actually", "adj", "after", "afterwards",
"again", "against", "ago", "ahead", "ain't", "all", "allow", "allows",
"almost", "alone", "along", "alongside", "already", "also", "although",
"always", "am", "amid", "amidst", "among", "amongst", "an", "and",
"another", "any", "anybody", "anyhow", "anyone", "anything", "anyway",
"anyways", "anywhere", "apart", "appear", "appreciate", "appropriate",
"are", "aren't", "around", "as", "a's", "aside", "ask", "asking",
"associated", "at", "available", "away", "awfully", "b", "back",
"backward", "backwards", "be", "became", "because", "become", "becomes",
"becoming", "been", "before", "beforehand", "begin", "behind", "being",
"believe", "below", "beside", "besides", "best", "better", "between",
"beyond", "both", "brief", "but", "by", "c", "came", "can", "cannot",
"cant", "can't", "caption", "cause", "causes", "certain", "certainly",
"changes", "clearly", "c'mon", "co", "co.", "com", "come", "comes",
"concerning", "consequently", "consider", "considering", "contain",
"containing", "contains", "corresponding", "could", "couldn't",
"course", "c's", "currently", "d", "dare", "daren't", "definitely",
"described", "despite", "did", "didn't", "different", "directly", "do",
"does", "doesn't", "doing", "done", "don't", "down", "downwards",
"during", "e", "each", "edu", "eg", "eight", "eighty", "either", "else",
"elsewhere", "end", "ending", "enough", "entirely", "especially", "et",
"etc", "even", "ever", "evermore", "every", "everybody", "everyone",
"everything", "everywhere", "ex", "exactly", "example", "except", "f",
"fairly", "far", "farther", "few", "fewer", "fifth", "first", "five",
"followed", "following", "follows", "for", "forever", "former",
"formerly", "forth", "forward", "found", "four", "from", "further",
"furthermore", "g", "get", "gets", "getting", "given", "gives", "go",
"goes", "going", "gone", "got", "gotten", "greetings", "h", "had",
"hadn't", "half", "happens", "hardly", "has", "hasn't", "have",
"haven't", "having", "he", "he'd", "he'll", "hello", "help", "hence",
"her", "here", "hereafter", "hereby", "herein", "here's", "hereupon",
"hers", "herself", "he's", "hi", "him", "himself", "his", "hither",
"hopefully", "how", "howbeit", "however", "hundred", "i", "i'd", "ie",
"if", "ignored", "i'll", "i'm", "immediate", "in", "inasmuch", "inc",
"inc.", "indeed", "indicate", "indicated", "indicates", "inner",
"inside", "insofar", "instead", "into", "inward", "is", "isn't", "it",
"it'd", "it'll", "its", "it's", "itself", "i've", "j", "just", "k",
"keep", "keeps", "kept", "know", "known", "knows", "l", "last",
"lately", "later", "latter", "latterly", "least", "less", "lest", "let",
"let's", "like", "liked", "likely", "likewise", "little", "look",
"looking", "looks", "low", "lower", "ltd", "m", "made", "mainly",
"make", "makes", "many", "may", "maybe", "mayn't", "me", "mean",
"meantime", "meanwhile", "merely", "might", "mightn't", "mine", "minus",
"miss", "more", "moreover", "most", "mostly", "mr", "mrs", "much",
"must", "mustn't", "my", "myself", "n", "name", "namely", "nd", "near",
"nearly", "necessary", "need", "needn't", "needs", "neither", "never",
"neverf", "neverless", "nevertheless", "new", "next", "nine", "ninety",
"no", "nobody", "non", "none", "nonetheless", "noone", "no-one", "nor",
"normally", "not", "nothing", "notwithstanding", "novel", "now",
"nowhere", "o", "obviously", "of", "off", "often", "oh", "ok", "okay",
"old", "on", "once", "one", "ones", "one's", "only", "onto", "opposite",
"or", "other", "others", "otherwise", "ought", "oughtn't", "our",
"ours", "ourselves", "out", "outside", "over", "overall", "own", "p",
"particular", "particularly", "past", "per", "perhaps", "placed",
"please", "plus", "possible", "presumably", "probably", "provided",
"provides", "q", "que", "quite", "qv", "r", "rather", "rd", "re",
"really", "reasonably", "recent", "recently", "regarding", "regardless",
"regards", "relatively", "respectively", "right", "round", "s", "said",
"same", "saw", "say", "saying", "says", "second", "secondly", "see",
"seeing", "seem", "seemed", "seeming", "seems", "seen", "self",
"selves", "sensible", "sent", "serious", "seriously", "seven",
"several", "shall", "shan't", "she", "she'd", "she'll", "she's",
"should", "shouldn't", "since", "six", "so", "some", "somebody",
"someday", "somehow", "someone", "something", "sometime", "sometimes",
"somewhat", "somewhere", "soon", "sorry", "specified", "specify",
"specifying", "still", "sub", "such", "sup", "sure", "t", "take",
"taken", "taking", "tell", "tends", "th", "than", "thank", "thanks",
"thanx", "that", "that'll", "thats", "that's", "that've", "the",
"their", "theirs", "them", "themselves", "then", "thence", "there",
"thereafter", "thereby", "there'd", "therefore", "therein", "there'll",
"there're", "theres", "there's", "thereupon", "there've", "these",
"they", "they'd", "they'll", "they're", "they've", "thing", "things",
"think", "third", "thirty", "this", "thorough", "thoroughly", "those",
"though", "three", "through", "throughout", "thru", "thus", "till",
"to", "together", "too", "took", "toward", "towards", "tried", "tries",
"truly", "try", "trying", "t's", "twice", "two", "u", "un", "under",
"underneath", "undoing", "unfortunately", "unless", "unlike",
"unlikely", "until", "unto", "up", "upon", "upwards", "us", "use",
"used", "useful", "uses", "using", "usually", "v", "value", "various",
"versus", "very", "via", "viz", "vs", "w", "want", "wants", "was",
"wasn't", "way", "we", "we'd", "welcome", "well", "we'll", "went",
"were", "we're", "weren't", "we've", "what", "whatever", "what'll",
"what's", "what've", "when", "whence", "whenever", "where",
"whereafter", "whereas", "whereby", "wherein", "where's", "whereupon",
"wherever", "whether", "which", "whichever", "while", "whilst",
"whither", "who", "who'd", "whoever", "whole", "who'll", "whom",
"whomever", "who's", "whose", "why", "will", "willing", "wish", "with",
"within", "without", "wonder", "won't", "would", "wouldn't", "x", "y",
"yes", "yet", "you", "you'd", "you'll", "your", "you're", "yours",
"yourself", "yourselves", "you've", "z", "zero"]

print(count_words(test_me, stop_words))
