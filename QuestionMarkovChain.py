import json, urllib, collections, random, itertools

#https://www.reddit.com/r/Python/comments/2ife6d/pykov_a_tiny_python_module_on_finite_regular/cl3bybj/
class QMC():
    def __init__(self, sentences):
        self.starts = collections.Counter()
        self.states = collections.defaultdict(collections.Counter)
        for sentence in sentences:
            words = sentence.split()
            self.starts[words[0]] += 1
            for i in range(len(words)-1):
                self.states[words[i]][words[i+1]] += 1
    def generate(self):
        try:
            i = random.randrange(sum(self.starts.values()))
            cur = next(itertools.islice(self.starts.elements(), i, None))
            result = cur
            while result[-1] != '?' and result[-1] != '.':
                i = random.randrange(sum(self.states[cur].values()))
                cur = next(itertools.islice(self.states[cur].elements(), i, None))
                result += " " + cur
            return result
        except:
            return '🤔'
if __name__ == '__main__':
    with urllib.request.urlopen('https://raw.githubusercontent.com/regalhotpocket/questions/master/questions.json') as data:
        sentences = json.loads(data.read().decode())
        model = QMC(sentences)
        for x in range(10):
            print(model.generate())
