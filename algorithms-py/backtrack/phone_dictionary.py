'''
Created on Jul 31, 2013

@author: mstepanenko
'''

keypads_dic = {
               2 : ('a', 'b', 'c'),
               3 : ('d', 'e', 'f'),
               4: ('g', 'h', 'i'),
               5: ('j', 'k', 'l'),
               6: ('m', 'n', 'o'),
               7: ('p', 'q', 'r', 's'),
               8: ('t', 'u', 'v'),
               9: ('w', 'x', 'y', 'z')               
            }

words = frozenset( ["max", "olesia", "zorro", "mars"] )

def _collectWords(keypads_seq, index, partial_word, res):
    
    if index >= len(keypads_seq):        
        if partial_word in words:
            res.append(partial_word)         
        return
    
    digit = keypads_seq[index]
    
    for next_ch in keypads_dic[digit]:
        _collectWords(keypads_seq, index+1, partial_word+next_ch, res)
        
'''
Telephone keypads have letters on each numerical key. Write a program that
generates all possible words resulting from translating a given digit sequence (e.g.,145345) into letters.
'''     
def findPossibleWords(keypads_seq):
    
    for key_number in keypads_seq:
        if not key_number in keypads_dic:
            raise ValueError( "Incorrect keypad '%s' passed" %key_number )
    
    res = []
    _collectWords(keypads_seq, 0, "", res)
    return res