from utils import loadPrimes
import tiktoken
class PrimeFastFourierTransform(object):

    def __init__(self):
        self.primes = loadPrimes()
        self.primesSet = set(self.primes)
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def encode(self, inputText):
        tokenIds = self.tokenizer.encode(inputText)
        sequence = [0] * len(tokenIds)
        for i, tokenId in enumerate(tokenIds):
            sequence[i] = complex(tokenId, self.primes[i])

        return PrimeFastFourierTransform._fft(sequence)


    def decode(self, pfftOutput):
        sentence = PrimeFastFourierTransform._fft(pfftOutput, inverse=True)
        tokenIds = [int(complexNumber.real) for complexNumber in sentence]
        return self.translateIdsToTokens(tokenIds)
