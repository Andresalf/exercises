from collections import OrderedDict, defaultdict

'''
input_data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']
'''

class Anagram(object):

    def are_anagrams(self, str1, str2):
        char_counter_map = [0] * 26
        str1 = str1.lower()
        str2 = str2.lower()
        for c in str1:
            char_counter_map[ord(c) % 97] += 1
        for c in str2:
            char_counter_map[ord(c) % 97] -= 1
        
        return not any(char_counter_map)
        
    def group_anagrams(self, items):
        if items is None:
            raise TypeError
        
        anagrams = defaultdict(list)
        for i in range(len(items)):
            for j in range(i+1, len(items)):
                if self.are_anagrams(items[i], items[j]):
                  anagrams[items[i]].append(items[j])
                  
        result = []
        for k, v in anagrams.items():
            result.append(k)
            result.extend(v)
        
        return result