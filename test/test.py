import argparse
import glob
import sys
import unittest
from os.path import dirname, basename, isfile, join
from solvers.claspy import *

modules = glob.glob(join(dirname(dirname(__file__)), 'solvers', '*.py'))
submodules = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
for submodule in submodules:
    exec(f'import solvers.{submodule} as {submodule}')

all_test_cases = {
    'akari': [(1, '''{"param_values":{"r":"7","c":"7"},"grid":{"1,5":"black","1,13":"black","3,3":"4","3,9":"1","3,13":"black","5,7":"2","7,3":"black","7,11":"black","9,7":"black","11,1":"black","11,5":"black","11,11":"1","13,1":"1","13,9":"1"},"puzzle_type":"akari","properties":{"outside":"0000","border":false}}''')],
    'aqre': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":"0","2,1":"black","2,3":"black","1,6":"black","2,5":"black","1,7":"1","2,7":"black","2,9":"black","2,11":"black","3,1":"2","4,1":"black","4,3":"black","3,6":"black","4,5":"black","3,7":"3","4,7":"black","4,9":"black","4,11":"black","5,1":"4","5,6":"black","5,7":"5","8,1":"black","8,3":"black","7,6":"black","8,5":"black","8,7":"black","8,9":"black","8,11":"black"},"puzzle_type":"aqre","properties":{"outside":"0000","border":true}}''')],
    # Aquapelago: test 1x1; 3x3 with '1' clue in center; 5x5 with empty black cell and a '3' clue in bottom middle; Penpa example with combined 4s near a (separate) 2; 1 large example that really covers everything (I still had bugs after making Penpa work)
    'aquapelago': [(2, '''{"param_values":{"r":"1","c":"1"},"grid":{},"puzzle_type":"aquapelago","properties":{"outside":"0000","border":false}}'''), (1, '''{"param_values":{"r":"3","c":"3"},"grid":{"3,3":"1"},"puzzle_type":"aquapelago","properties":{"outside":"0000","border":false}}'''), (3, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,1":"black","9,5":"3"},"puzzle_type":"aquapelago","properties":{"outside":"0000","border":false}}'''), (1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,9":"black","9,5":"4","9,9":"2","11,3":"4"},"puzzle_type":"aquapelago","properties":{"outside":"0000","border":false}}'''), (1, '''{"param_values":{"r":"16","c":"16"},"grid":{"1,1":"11","1,11":"1","1,27":"1","5,9":"4","5,19":"7","7,31":"1","13,27":"2","15,23":"12","17,9":"11","19,5":"2","25,1":"3","27,13":"3","27,23":"1","31,5":"2","31,21":"5","31,31":"3"},"puzzle_type":"aquapelago","properties":{"outside":"0000","border":false}}''')],
    'aquarium': [(3, '''{"param_values":{"r":"4","c":"4"},"grid":{"-1,7":"3","1,-1":"2","2,1":"black","1,4":"black","2,7":"black","3,-1":"1","3,2":"black","3,4":"black","3,6":"black","4,5":"black","5,-1":"3","5,2":"black","5,4":"black","6,3":"black","5,6":"black","7,6":"black"},"puzzle_type":"aquarium","properties":{"outside":"1001","border":true}}''')],
    'balanceloop': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,3":["4","b"],"3,9":["","b"],"7,1":["","w"],"9,7":["4","w"]},"puzzle_type":"balanceloop","properties":{"outside":"0000","border":false}}''')],
    'battleship': [(1, '''{"param_values":{"r":"10","c":"10"},"grid":{"-1,1":"3","-1,3":"2","-1,5":"1","-1,7":"3","-1,9":"0","-1,11":"4","-1,13":"0","-1,15":"3","-1,17":"1","-1,19":"3","1,-1":"1","3,-1":"7","5,-1":"1","7,-1":"4","7,15":"w","9,-1":"1","9,7":"o","11,-1":"0","13,-1":"1","13,7":"d","15,-1":"1","17,-1":"3","19,-1":"1"},"puzzle_type":"battleship","properties":{"outside":"1001","border":false}}''')],
    'binairo': [(1, '''{"param_values":{"r":"4","c":"4"},"grid":{"1,3":"1","1,7":"0","3,5":"0","5,3":"0","7,1":"1","7,3":"1","7,7":"0"},"puzzle_type":"binairo","properties":{"outside":"0000","border":false}}''')],
    'castlewall': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,7":["0","l","b"],"1,9":["1","d","g"],"7,3":["1","u","w"],"7,7":["0","u","b"]},"puzzle_type":"castlewall","properties":{"outside":"0000","border":false}}''')],
    # Cave: test "product" mode and ?s
    'cave': [(1, '''{"param_values":{"r":"6","c":"6","Product":false},"grid":{"1,3":"3","5,3":"2","5,9":"3","7,7":"11","9,5":"3","11,1":"3","11,9":"2"},"puzzle_type":"cave","properties":{"outside":"0000","border":false}}'''), (1, '''{"param_values":{"r":"4","c":"4","Product":true},"grid":{"1,1":"?","3,3":"12","3,7":"4","5,5":"6","7,1":"3"},"puzzle_type":"cave","properties":{"outside":"0000","border":false}}''')],
    'chocona': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":"3","1,4":"black","2,3":"black","1,5":"3","2,5":"black","2,7":"black","2,9":"black","2,11":"black","3,2":"black","4,1":"black","3,3":"1","4,3":"black","4,5":"black","4,7":"black","4,9":"black","4,11":"black","5,1":"2","5,2":"black","5,3":"2","5,4":"black","5,6":"black","5,7":"2","5,8":"black","5,9":"1","7,2":"black","7,4":"black","8,3":"black","7,6":"black","7,8":"black","8,7":"black","8,9":"black","8,11":"black","9,2":"black","10,3":"black","9,6":"black","10,5":"black","9,8":"black","9,9":"3","10,9":"black","11,2":"black","11,3":"2","11,6":"black","11,10":"black"},"puzzle_type":"chocona","properties":{"outside":"0000","border":true}}''')],
    'countryroad': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,1":"2","1,4":"black","1,8":"black","4,1":"black","3,4":"black","4,3":"black","4,5":"black","3,8":"black","4,7":"black","5,1":"1","5,2":"black","5,3":"2","6,3":"black","6,5":"black","5,8":"black","6,7":"black","6,9":"black","7,2":"black","7,6":"black","9,2":"black","9,6":"black"},"puzzle_type":"countryroad","properties":{"outside":"0000","border":true}}''')],
    'doppelblock': [(1, '''{"param_values":{"n":"5"},"grid":{"-1,3":"6","-1,7":"3","-1,9":"4","3,-1":"1","5,-1":"0"},"puzzle_type":"doppelblock","properties":{"outside":"1001","border":false}}''')],
    'easyas': [(1, '''{"param_values":{"n":"4","letters":"ABC"},"grid":{"-1,1":"A","1,-1":"B","3,9":"C","7,-1":"C"},"puzzle_type":"easyas","properties":{"outside":"1111","border":false}}''')],
    'fillomino': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"3,1":"1","3,3":"5","3,5":"2","3,9":"5","5,3":"1","5,9":"1","7,3":"2","7,9":"5","9,3":"1","9,7":"5","9,9":"1","9,11":"2"},"puzzle_type":"fillomino","properties":{"outside":"0000","border":false}}''')],
    'gokigen': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,7":"0","3,3":"4","5,1":"2","5,9":"2","9,3":"1","9,7":"0"},"puzzle_type":"gokigen","properties":{"outside":"0000","border":false}}''')],
    'haisu': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,3":"2","1,6":"black","1,8":"black","1,9":"G","2,9":"black","3,6":"black","4,7":"black","5,1":"1","5,5":"2","5,8":"black","5,9":"3","8,1":"black","8,5":"black","7,8":"black","8,7":"black","9,1":"S","9,2":"black","9,4":"black","9,7":"1"},"puzzle_type":"haisu","properties":{"outside":"0000","border":true}}''')],
    # Hashi: test ?s
    'hashi': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,1":"?","1,5":"2","3,3":"3","3,9":"2","5,1":"3","7,3":"3","7,7":"?","9,1":"3","9,5":"4","9,9":"3"},"puzzle_type":"hashi","properties":{"outside":"0000","border":false}}''')],
    'heteromino': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,9":"darkgray","3,5":"darkgray","3,9":"darkgray","5,5":"darkgray","7,1":"darkgray","7,3":"darkgray","9,1":"darkgray"},"puzzle_type":"heteromino","properties":{"outside":"0000","border":false}}''')],
    'heyawake': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":"2","1,2":"black","1,3":"2","1,6":"black","1,7":"2","1,10":"black","1,11":"2","3,2":"black","3,6":"black","3,10":"black","5,2":"black","6,1":"black","6,3":"black","5,6":"black","6,5":"black","6,7":"black","5,10":"black","6,9":"black","8,1":"black","8,3":"black","8,5":"black","8,7":"black","7,10":"black","8,9":"black","9,6":"black","9,10":"black","10,11":"black","11,6":"black","11,10":"black"},"puzzle_type":"heyawake","properties":{"outside":"0000","border":true}}''')],
    'hitori': [(1, '''{"param_values":{"r":"4","c":"4"},"grid":{"1,1":"1","1,3":"1","1,5":"1","1,7":"4","3,1":"1","3,3":"4","3,5":"2","3,7":"3","5,1":"3","5,3":"3","5,5":"2","5,7":"1","7,1":"4","7,3":"2","7,5":"1","7,7":"3"},"puzzle_type":"hitori","properties":{"outside":"0000","border":false}}''')],
    'hotaru': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,1":["0","r"],"1,9":["1","d"],"3,3":"l","3,7":["0","l"],"7,3":["0","u"],"7,7":["2","d"],"9,1":["1","u"],"9,9":["1","u"]},"puzzle_type":"hotaru","properties":{"outside":"0000","border":false}}''')],
    'kakuro': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":"black","1,3":"black","1,5":[0,12],"1,7":[0,4],"1,9":"black","1,11":"black","3,1":"black","3,3":[8,4],"3,9":[0,10],"3,11":"black","5,1":[10,0],"5,11":[0,10],"7,1":[3,0],"7,7":[3,17],"9,1":"black","9,3":[21,0],"11,1":"black","11,3":"black","11,5":[12,0],"11,11":"black"},"puzzle_type":"kakuro","properties":{"outside":"0000","border":false}}''')],
    # Kuromasu: test ?s
    'kuromasu': [(1, '''{"param_values":{"r":"7","c":"7"},"grid":{"1,3":"2","1,5":"6","1,13":"3","7,1":"?","7,7":"5","7,13":"?","13,1":"2","13,9":"7","13,11":"4"},"puzzle_type":"kuromasu","properties":{"outside":"0000","border":false}}''')],
    # Kurotto: test empty circle
    'kurotto': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,1":"3","1,3":"black","3,9":"4","5,5":"6","7,1":"4","9,7":"0","9,9":"2"},"puzzle_type":"kurotto","properties":{"outside":"0000","border":false}}''')],
    'lits': [(1, '''{"param_values":{"r":"4","c":"4"},"grid":{"1,4":"black","2,7":"black","3,4":"black","4,3":"black","3,6":"black","5,2":"black","6,1":"black","6,3":"black","5,6":"black","6,5":"black"},"puzzle_type":"lits","properties":{"outside":"0000","border":true}}''')],
    # Magnets: test some empty clue cols / rows
    'magnets': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"-1,1":"2","-1,3":"1","-1,5":"2","-1,7":"2","-1,11":"2","1,-1":"2","1,2":"black","2,3":"black","1,6":"black","2,5":"black","2,7":"black","1,10":"black","2,9":"black","1,13":"1","3,2":"black","4,1":"black","3,4":"black","4,5":"black","3,8":"black","4,7":"black","3,10":"black","4,11":"black","3,13":"2","5,-1":"2","5,2":"black","5,4":"black","6,3":"black","6,5":"black","5,8":"black","6,7":"black","5,10":"black","6,9":"black","5,13":"1","7,-1":"1","7,2":"black","8,1":"black","7,4":"black","7,6":"black","8,7":"black","7,10":"black","8,9":"black","8,11":"black","7,13":"3","9,-1":"1","9,2":"black","9,4":"black","10,3":"black","9,6":"black","10,5":"black","9,8":"black","10,9":"black","10,11":"black","11,-1":"2","11,2":"black","11,6":"black","11,8":"black","11,13":"1","13,1":"2","13,5":"1","13,7":"2","13,9":"3","13,11":"1"},"puzzle_type":"magnets","properties":{"outside":"1111","border":true}}''')],
    'masyu': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,5":"w","3,3":"b","3,9":"w","7,7":"b","9,3":"w"},"puzzle_type":"masyu","properties":{"outside":"0000","border":false}}''')],
    # Minesweeper: test ?s
    'minesweeper': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,3":"2","3,9":"1","5,1":"3","7,5":"1","7,7":"2","9,1":"0","9,9":"?"},"puzzle_type":"minesweeper","properties":{"outside":"0000","border":false}}''')],
    'moonsun': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":"s","1,3":"m","1,6":"black","1,11":"s","4,1":"black","3,3":"m","4,3":"black","3,5":"s","3,6":"black","3,9":"m","5,3":"m","5,4":"black","5,5":"s","5,6":"black","5,7":"s","6,7":"black","6,9":"black","6,11":"black","8,1":"black","7,3":"s","7,4":"black","8,3":"black","7,6":"black","8,5":"black","8,7":"black","7,11":"m","9,1":"m","9,4":"black","9,7":"m","9,8":"black","11,4":"black","11,5":"s","11,8":"black","11,11":"m"},"puzzle_type":"moonsun","properties":{"outside":"0000","border":true}}''')],
    'nagare': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":"R","3,1":"black","3,9":"L","5,11":"d","7,1":"u","9,5":"U","9,7":"R","11,1":"black"},"puzzle_type":"nagare","properties":{"outside":"0000","border":false}}''')],
    # Nanro: TODO(mstang: Test both "normal" and "signpost" clues? (Can the same puzzle have both types?)
    # NCells: currently this only tests 4 cells; adding more seems optional.
    'ncells': [(1, '''{"param_values":{"r":"6","c":"6","region_size":"4"},"grid":{"1,5":"1","3,3":"2","3,7":"3","5,7":"3","7,5":"1","9,7":"2","11,1":"2","11,5":"3","11,11":"2"},"puzzle_type":"ncells","properties":{"outside":"0000","border":true}}''')],
    # Nonogram: test ?s
    'nonogram': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"-1,1":"2 1","-1,3":"1 1 1","-1,5":"1","-1,7":"1 1 1","-1,9":"? 1","-1,11":"0","1,-1":"2 1","3,-1":"1 1","5,-1":"1 2","7,-1":"0","9,-1":"1 1","11,-1":"?"},"puzzle_type":"nonogram","properties":{"outside":"1001","border":false}}''')],
    'norinori': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"2,1":"black","1,4":"black","2,3":"black","1,6":"black","4,3":"black","3,6":"black","4,5":"black","5,2":"black","6,1":"black","5,6":"black","6,7":"black","6,9":"black","8,1":"black","8,3":"black","9,4":"black"},"puzzle_type":"norinori","properties":{"outside":"0000","border":true}}''')],
    # Numberlink: test "use all cells"
    'numberlink': [(2, '''{"param_values":{"r":"5","c":"5","Use all cells":true},"grid":{"1,1":"1","3,1":"2","3,7":"2","5,3":"1","5,9":"3","9,1":"3"},"puzzle_type":"numberlink","properties":{"outside":"0000","border":false}}'''), (4, '''{"param_values":{"r":"5","c":"5","Use all cells":false},"grid":{"1,1":"1","3,1":"2","5,7":"3","7,3":"1","7,9":"2","9,9":"3"},"puzzle_type":"numberlink","properties":{"outside":"0000","border":false}}''')],
    # Nuribou: add a bigger test because I'm worried I'll break it
    'nuribou': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,1":"1","1,5":"2","3,9":"1","5,3":"4","9,9":"7"},"puzzle_type":"nuribou","properties":{"outside":"0000","border":false}}'''), (1, '''{"param_values":{"r":"10","c":"10"},"grid":{"1,1":"1","1,5":"5","1,19":"4","5,13":"1","5,17":"2","7,3":"11","7,11":"2","9,19":"6","11,3":"2","13,1":"1","13,15":"10","15,3":"6","15,9":"4","19,1":"2","19,15":"3"},"puzzle_type":"nuribou","properties":{"outside":"0000","border":false}}''')],
    # Nurikabe: test ?s
    'nurikabe': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,3":"5","3,5":"?","7,5":"1","9,7":"3"},"puzzle_type":"nurikabe","properties":{"outside":"0000","border":false}}''')],
    # Nurimisaki: test ?s
    'nurimisaki': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,3":"?","3,1":"?","5,7":"2","9,1":"?"},"puzzle_type":"nurimisaki","properties":{"outside":"0000","border":false}}''')],
    # Onsen: TODO(jhimawan): Add ?s and then add a test for https://puzz.link/rules.html?onsen
    'rippleeffect': [(1, '''{"param_values":{"r":"4","c":"4"},"grid":{"2,1":"black","1,4":"black","2,3":"black","2,7":"black","4,1":"black","3,3":"1","3,4":"black","4,3":"black","3,5":"4","3,6":"black","6,1":"black","5,3":"3","5,4":"black","5,5":"2","5,6":"black","6,5":"black","7,2":"black","7,6":"black"},"puzzle_type":"rippleeffect","properties":{"outside":"0000","border":true}}''')],
    # Shakashaka: test black cells w/o clues
    'shakashaka': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":"black","1,9":"1","3,7":"3","5,5":"4","7,1":"3","11,7":"black"},"puzzle_type":"shakashaka","properties":{"outside":"0000","border":false}}''')],
    # Shikaku: test ?s
    'shikaku': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,9":"3","3,1":"5","3,3":"?","3,9":"6","9,3":"6","9,9":"2","9,11":"3","11,3":"5"},"puzzle_type":"shikaku","properties":{"outside":"0000","border":false}}''')],
    'shimaguni': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":"3","2,1":"black","2,3":"black","1,6":"black","2,5":"black","1,8":"black","1,9":"3","1,10":"black","3,1":"2","3,4":"black","3,6":"black","3,8":"black","3,10":"black","4,11":"black","6,1":"black","5,4":"black","6,3":"black","5,6":"black","5,8":"black","8,1":"black","8,3":"black","7,6":"black","8,5":"black","7,8":"black","8,7":"black","8,9":"black","8,11":"black","9,1":"4","10,5":"black","10,7":"black","10,9":"black","10,11":"black","11,4":"black","11,5":"3"},"puzzle_type":"shimaguni","properties":{"outside":"0000","border":true}}''')],
    # Skyscrapers has ? support but IDK why it's needed
    'skyscrapers': [(1, '''{"param_values":{"n":"4"},"grid":{"3,-1":"4","5,9":"3","9,3":"1","9,5":"3"},"puzzle_type":"skyscrapers","properties":{"outside":"1111","border":false}}''')],
    'slitherlink': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,1":"2","1,7":"1","3,3":"2","3,9":"1","5,5":"2","7,1":"3","7,7":"3","9,3":"0","9,9":"3"},"puzzle_type":"slitherlink","properties":{"outside":"0000","border":false}}''')],
    'spiralgalaxies': [(1, '''{"param_values":{"r":"7","c":"7"},"grid":{"2,1":"yup","1,6":"yup","1,13":"yup","4,10":"yup","5,5":"yup","9,3":"yup","10,9":"yup","9,13":"yup","12,1":"yup","11,3":"yup","13,10":"yup"},"puzzle_type":"spiralgalaxies","properties":{"outside":"0000","border":false}}''')],
    # Starbattle: test n = 1 and 2
    'starbattle': [(1, '''{"param_values":{"n":"6","stars":"1"},"grid":{"2,3":"black","1,6":"black","2,5":"black","2,9":"black","2,11":"black","3,2":"black","4,3":"black","4,5":"black","3,8":"black","4,7":"black","4,9":"black","5,2":"black","6,1":"black","6,3":"black","5,6":"black","6,7":"black","5,10":"black","7,4":"black","8,3":"black","8,5":"black","7,8":"black","8,7":"black","7,10":"black","9,2":"black","10,3":"black","10,5":"black","10,7":"black","9,10":"black","10,9":"black","11,2":"black"},"puzzle_type":"starbattle","properties":{"outside":"0000","border":true}}'''), (1, '''{"param_values":{"n":"10","stars":"2"},"grid":{"2,3":"black","1,6":"black","2,5":"black","2,7":"black","1,10":"black","2,11":"black","2,15":"black","2,19":"black","3,2":"black","4,3":"black","4,5":"black","3,8":"black","3,10":"black","3,12":"black","3,14":"black","3,16":"black","3,18":"black","4,17":"black","6,3":"black","5,6":"black","6,5":"black","5,8":"black","5,10":"black","5,12":"black","5,14":"black","6,13":"black","5,16":"black","7,2":"black","8,5":"black","7,8":"black","8,7":"black","7,10":"black","8,9":"black","8,11":"black","8,13":"black","7,16":"black","8,17":"black","9,2":"black","9,4":"black","10,5":"black","10,7":"black","9,10":"black","9,12":"black","9,14":"black","9,16":"black","9,18":"black","11,2":"black","12,3":"black","12,5":"black","11,8":"black","12,7":"black","11,10":"black","11,12":"black","11,14":"black","11,16":"black","12,15":"black","11,18":"black","14,1":"black","13,4":"black","14,3":"black","14,7":"black","13,10":"black","14,9":"black","13,12":"black","14,13":"black","14,15":"black","13,18":"black","15,4":"black","15,6":"black","16,7":"black","16,9":"black","16,11":"black","16,13":"black","15,16":"black","15,18":"black","17,4":"black","18,5":"black","18,7":"black","17,10":"black","18,9":"black","17,12":"black","17,14":"black","17,16":"black","18,15":"black","17,18":"black","18,17":"black","19,12":"black"},"puzzle_type":"starbattle","properties":{"outside":"0000","border":true}}''')],
    # Statue park: test with tetrominos
    'statuepark': [(1, '''{"param_values":{"r":"7","c":"7","shapeset":"Tetrominoes"},"grid":{"1,9":"b","1,11":"w","3,1":"b","3,3":"b","3,5":"b","3,11":"b","5,5":"b","11,7":"b","11,9":"w","13,7":"w","13,9":"b"},"puzzle_type":"statuepark","properties":{"outside":"0000","border":false}}''')],
    'stostone': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":"3","2,1":"black","2,3":"black","1,6":"black","2,5":"black","2,7":"black","2,9":"black","3,1":"4","3,8":"black","3,9":"3","3,10":"black","6,1":"black","6,3":"black","5,8":"black","5,10":"black","6,11":"black","7,1":"3","7,4":"black","8,5":"black","7,8":"black","8,7":"black","10,1":"black","9,4":"black","9,8":"black","11,2":"black","11,4":"black","11,8":"black"},"puzzle_type":"stostone","properties":{"outside":"0000","border":true}}''')],
    # Sudoku: test standard, diagonal, untouch, antiknight
    'sudoku': [(1, '''{"param_values":{"Diagonal":false,"Untouch":false,"Antiknight":false},"grid":{"1,1":"1","1,3":"6","1,5":"3","3,5":"4","3,15":"6","5,5":"5","5,7":"6","5,9":"7","7,9":"8","9,1":"6","9,3":"7","9,5":"8","9,9":"9","9,11":"1","9,13":"2","11,5":"9","11,13":"3","13,5":"1","13,7":"2","13,9":"3","13,13":"4","13,15":"5","13,17":"6","15,9":"4","15,17":"7","17,1":"4","17,9":"5","17,17":"8"},"puzzle_type":"sudoku","properties":{"outside":"0000","border":false}}'''), (1, '''{"param_values":{"Diagonal":true,"Untouch":false,"Antiknight":false},"grid":{"1,7":"1","1,15":"6","3,1":"2","3,3":"9","3,13":"4","3,15":"7","5,3":"3","5,11":"2","7,5":"7","7,7":"6","7,17":"5","11,1":"5","11,11":"8","11,13":"7","13,7":"7","13,15":"5","15,3":"5","15,5":"9","15,15":"1","15,17":"8","17,3":"8","17,11":"9"},"puzzle_type":"sudoku","properties":{"outside":"0000","border":false}}'''), (1, '''{"param_values":{"Diagonal":false,"Untouch":true,"Antiknight":true},"grid":{"1,7":"2","1,15":"1","3,5":"3","3,13":"2","5,3":"4","5,11":"3","13,7":"6","13,15":"5","15,5":"7","15,13":"6","17,3":"8","17,11":"7"},"puzzle_type":"sudoku","properties":{"outside":"0000","border":false}}''')],
    # Tapa: test ?s
    'tapa': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,1":["?"],"3,9":[5],"5,5":[3,1,1],"7,1":[3,1],"9,9":[2]},"puzzle_type":"tapa","properties":{"outside":"0000","border":false}}''')],
    'tatamibari': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"3,5":"%2B","3,9":"%7C","5,1":"%7C","5,9":"-","7,3":"%2B","7,5":"%7C","9,1":"%7C","9,3":"%2B","9,7":"%2B"},"puzzle_type":"tatamibari","properties":{"outside":"0000","border":false}}''')],
    # Tents & Trees: test placing both tents and trees
    'tents': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"-1,1":"2","-1,5":"0","1,-1":"1","1,5":"e","5,3":"e","5,9":"e","7,7":"e","7,9":"n","9,1":"n","9,3":"e"},"puzzle_type":"tents","properties":{"outside":"1001","border":false}}''')],
    # TLL: test ?s
    'tll': [(3, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,3":[3],"5,9":[1,3,"?"],"7,3":[3,3],"11,9":[2]},"puzzle_type":"tll","properties":{"outside":"0000","border":false}}''')],
    # Yajilin: test empty gray cells
    'yajilin': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"1,9":"gray","5,7":[["2","l"],"gray"],"9,9":[["0","u"],"gray"]},"puzzle_type":"yajilin","properties":{"outside":"0000","border":false}}''')],
    # Yajisan-Kazusan: TODO(mstang): test empty gray cells (I'm not sure what they are for or if they even work)
    'yajisankazusan': [(1, '''{"param_values":{"r":"6","c":"6"},"grid":{"1,1":["0","r"],"1,11":["3","d"],"3,1":["99","u"],"5,9":["2","l"],"9,3":["2","u"],"9,9":["2","l"],"11,1":["2","u"],"11,5":["1","u"]},"puzzle_type":"yajisankazusan","properties":{"outside":"0000","border":false}}''')],
    'yinyang': [(1, '''{"param_values":{"r":"5","c":"5"},"grid":{"3,1":"w","3,5":"b","5,1":"b","5,9":"w","7,5":"b","7,9":"w"},"puzzle_type":"yinyang","properties":{"outside":"0000","border":false}}''')]
}

# We define a "results" object here and populate it by "pre-running" the tests.
# This is so that we don't get a ton of errors about still-running subprocesses.
# Definitely not best practice but ¯\_(ツ)_/¯

results = {}

class Test(unittest.TestCase):
    def test(self):
        for (puzzle_name, puz_test_cases_results) in results.items():
            print(f'verifying {puzzle_name}')
            for i in range(len(puz_test_cases_results)):
                puz_test_case_results = puz_test_cases_results[i]
                expected_num_solutions, json = all_test_cases[puzzle_name][i]
                self.assertEqual(expected_num_solutions, len(puz_test_case_results), 
                    f'expected {expected_num_solutions} solutions, but got {len(puz_test_case_results)}; {puzzle_name} test failed')
                if expected_num_solutions == len(puz_test_case_results):
                    print('    OK')
                else:
                    print('    FAILED')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('puzzle_names', help='The "names" ("IDs") of puzzles to test. For example, "easyas tll".', nargs='*', type=str)
    args = parser.parse_args()

    if args.puzzle_names:
        del sys.argv[1:] # Don't pass any command line args to unit tests

    puzzle_names = args.puzzle_names if args.puzzle_names else all_test_cases

    def solver(puzzle_name, json):
        reset()
        module = globals()[puzzle_name]
        puzzle_encoding = module.encode(json)
        solutions_encoded = module.solve(puzzle_encoding)
        return solutions_encoded

    for puzzle_name in puzzle_names:
        puz_test_cases = all_test_cases[puzzle_name]
        results[puzzle_name] = [solver(puzzle_name, json) for (expected_num_solutions, json) in puz_test_cases]

    print('\n\n')

    unittest.main()