const puzzle_types = {
	aho: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	amibo: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	akari: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	aqre: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: true }
		},
	aquarium: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '1001', border: true }
		},
	balanceloop: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	battleship: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '1001', border: false }
		},
	binairo: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	castlewall: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false },
		},
	cave: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10},
			'Product': {name: 'Product', value:false} },
		properties: { outside: '0000', border: false },
		},
	chocona: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: true },
		},
    countryroad: {
        params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
        properties: { outside: '0000', border: true }
        },
	doppelblock: {
		params: { n: {name: 'Grid size', value: 6} },
		properties: { outside: '1001', border: false }
		},
    easyas: {
    	params: { n: {name: 'Grid size', value: 6}, letters: {name: 'Letters', value: 'ABC'} },
    	properties: { outside: '1111', border: false }
		},
	fillomino: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	gokigen: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false },
		display: {no_border_lines: true}
		},
	haisu: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: true }
		},
	hashi: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	heteromino: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	heyawake: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: true }
		},
	hitori: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	hotaru: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false },
		display: {no_border_lines: true}
		},
	kakuro: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false },
		},
	kurotto: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	kuromasu: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	lits: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: true }
		},
	magnets: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '1111', border: true }
		},
	masyu: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	minesweeper: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	moonsun: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: true }
		},
	nagare: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
    nanro: {
        params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
        properties: { outside: '0000', border: true }
        },
    ncells:
        {
        params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10}, region_size: {name: 'Size of region', value: 5} },
        properties: { outside: '0000', border: true }
        },
	nonogram: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '1001', border: false }
		},
	norinori: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: true }
		},
	numberlink: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10},
			'Use all cells': {name: 'Use all cells', value:false} },
		properties: { outside: '0000', border: false },
		},
    nuribou: {
        params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
        properties: { outside: '0000', border: false }
        },
	nurikabe: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	nurimisaki: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	nonogram: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '1001', border: false }
		},
    onsen: {
        params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
        properties: { outside: '0000', border: true }
		},
	rippleeffect: {
        params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
        properties: { outside: '0000', border: true }
		},
	shakashaka: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	shikaku: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	shimaguni: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: true }
		},
	skyscrapers: {
		params: { n: {name: 'Grid size', value:6} },
		properties: { outside: '1111', border: false }
		},
	slitherlink: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	spiralgalaxies: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	starbattle: {
		params: { n: {name: 'Grid size', value: 10}, stars: {name: 'Number of stars', value:2} },
		properties: { outside: '0000', border: true }
		},
	statuepark: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10}, 
				  shapeset: {name: 'Shape set', value:'Tetrominoes', options:['Tetrominoes', 'Pentominoes', 'Double Tetrominoes']} 
				},
		properties: { outside: '0000', border: false }
		},
	stostone: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: true }
		},
	sudoku: {
		params: {
			'Diagonal': {name: 'Diagonal', value:false},
			'Untouch': {name: 'Untouch', value:false},
			'Antiknight': {name: 'Antiknight', value:false}
		},
		properties: { outside: '0000', border: false }
		},
	tapa: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	tatamibari: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	tents: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '1001', border: false }
		},
	tll: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	yajilin: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	yajilin_transparent: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	yajisankazusan: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
	yinyang: {
		params: { r: {name: 'Rows', value: 10}, c: {name: 'Columns', value: 10} },
		properties: { outside: '0000', border: false }
		},
};

const examples = {
	cave: {
		1: {
			data: {"param_values":{"r":11,"c":11},"grid":{"1,1":"9","1,5":"7",
			"1,17":"6","1,21":"5","3,3":"7","3,19":"5","5,1":"5","5,5":"6","5,17":"7","5,21":"6",
			"9,9":"6","9,13":"7","11,11":"9","13,9":"6","13,13":"7","17,1":"5","17,5":"5","17,17":"10",
			"17,21":"6","19,3":"11","19,19":"3","21,1":"6","21,5":"8","21,17":"7","21,21":"6"}},
			link: 'https://www.gmpuzzles.com/blog/2019/04/cave-by-michael-tang'
		},
		2: {
			data: {"param_values":{"r":"10","c":"10"},"grid":{"1,9":"7","3,1":"2",
			"3,17":"3","5,11":"3","7,5":"7","7,9":"5","7,15":"4","7,19":"5",
			"9,1":"5","11,19":"9","13,1":"4","13,5":"6","13,11":"4","13,15":
			"7","15,9":"3","17,3":"6","17,19":"2","19,11":"8"}},
			link: 'https://www.gmpuzzles.com/blog/2019/05/cave-by-michael-tang-2/'
		}
	},
	countryroad: {
		1: {
			data: {"param_values":{"r":"7","c":"7"},"grid":{"1,1":"1","2,3":"black","1,6":"black","2,5":"black","2,7":"black","1,12":"black","3,2":"black","4,3":"black","4,5":"black","3,8":"black","4,7":"black","4,9":"black","3,12":"black","4,11":"black","5,2":"black","6,1":"black","5,4":"black","5,6":"black","5,8":"black","5,10":"black","6,11":"black","5,11":"2","6,13":"black","8,1":"black","7,4":"black","8,3":"black","7,6":"black","7,8":"black","7,10":"black","8,13":"black","9,1":"3","9,4":"black","10,3":"black","9,6":"black","10,5":"black","9,8":"black","10,7":"black","9,10":"black","10,9":"black","9,12":"black","10,11":"black","11,2":"black","11,6":"black","12,7":"black","12,9":"black","11,12":"black","12,11":"black","13,2":"black","13,8":"black"}}
		},
	    2: {
	        data: {"param_values":{"r":"13","c":"13"},"grid":{"0,1":"black","2,1":"black","1,0":"black","0,3":"black","2,3":"black","0,5":"black","1,6":"black","0,7":"black","1,7":"5","0,9":"black","0,11":"black","0,13":"black","0,15":"black","0,17":"black","1,18":"black","2,17":"black","0,19":"black","0,21":"black","1,22":"black","0,23":"black","1,24":"black","0,25":"black","1,26":"black","3,0":"black","3,1":"5","3,4":"black","3,6":"black","4,5":"black","4,7":"black","4,9":"black","4,11":"black","4,13":"black","3,16":"black","4,15":"black","3,18":"black","3,22":"black","3,24":"black","4,23":"black","3,26":"black","5,0":"black","5,4":"black","6,5":"black","6,7":"black","6,9":"black","5,12":"black","6,13":"black","5,18":"black","6,17":"black","6,19":"black","5,22":"black","5,23":"5","5,26":"black","8,1":"black","7,0":"black","7,4":"black","8,3":"black","7,10":"black","7,12":"black","8,11":"black","7,14":"black","7,16":"black","7,20":"black","7,22":"black","8,23":"black","7,26":"black","8,25":"black","9,0":"black","9,1":"5","9,4":"black","10,5":"black","10,7":"black","9,10":"black","10,9":"black","9,14":"black","9,16":"black","10,15":"black","9,20":"black","9,22":"black","9,23":"5","9,26":"black","11,0":"black","11,4":"black","11,6":"black","11,5":"5","11,8":"black","11,7":"5","12,9":"black","11,9":"5","12,11":"black","11,14":"black","12,13":"black","12,15":"black","11,15":"5","12,17":"black","11,20":"black","12,19":"black","11,22":"black","12,21":"black","12,23":"black","11,26":"black","14,1":"black","13,0":"black","13,4":"black","14,3":"black","13,6":"black","14,7":"black","14,9":"black","14,11":"black","14,13":"black","14,15":"black","14,17":"black","14,19":"black","14,21":"black","13,24":"black","14,23":"black","13,26":"black","15,0":"black","15,1":"5","15,4":"black","16,5":"black","16,7":"black","16,9":"black","16,11":"black","16,13":"black","16,15":"black","16,17":"black","16,19":"black","16,21":"black","15,24":"black","16,23":"black","15,26":"black","17,0":"black","17,8":"black","17,9":"5","17,14":"black","18,17":"black","18,19":"black","17,24":"black","18,23":"black","17,26":"black","18,25":"black","20,1":"black","19,0":"black","20,3":"black","20,5":"black","19,8":"black","20,7":"black","20,9":"black","20,11":"black","19,14":"black","20,13":"black","19,16":"black","19,17":"5","19,20":"black","19,22":"black","20,21":"black","19,26":"black","22,1":"black","21,0":"black","21,8":"black","22,7":"black","21,10":"black","21,14":"black","21,16":"black","22,15":"black","22,17":"black","22,19":"black","21,22":"black","22,21":"black","21,26":"black","23,2":"black","23,0":"black","23,1":"5","24,3":"black","23,6":"black","24,5":"black","24,7":"black","23,10":"black","24,9":"black","24,11":"black","24,13":"black","24,15":"black","23,18":"black","24,17":"black","23,19":"5","23,22":"black","24,23":"black","23,26":"black","24,25":"black","26,1":"black","25,0":"black","26,3":"black","26,5":"black","25,8":"black","26,7":"black","26,9":"black","26,11":"black","26,13":"black","26,15":"black","25,18":"black","26,17":"black","26,19":"black","26,21":"black","26,23":"black","25,26":"black","26,25":"black"}}
	        }
	    },
	doppelblock: {
		1: {
			data: {"param_values":{"n":"7"},"grid":{"-1,3":"11","-1,5":"11","-1,7":"13","-1,9":"6",
			"3,-1":"3","5,-1":"2","7,-1":"7","9,-1":"8"}},
			link: 'https://mspuzzles.wordpress.com/2019/02/03/puzzle-12-doppelblock/'
		}
	},
	fillomino: {
		1: {
			data: {"param_values":{"r":"6","c":"6"},"grid":{"3,1":"1","3,3":"5","3,5":"2","3,9":"5","5,3":"1","5,9":"1","7,3":"2","7,9":"5","9,3":"1","9,7":"5","9,9":"1","9,11":"2"}}
		},
	},
	heyawake: {
		1: {
			data: {"param_values":{"r":"5","c":"5"},"grid":{"1,1":"2","1,6":"black","1,9":"2","4,1":"black","4,3":"black","3,6":"black","4,5":"black","4,7":"black","4,9":"black","5,1":"1","8,1":"black","8,3":"black","8,5":"black","8,7":"black","8,9":"black","9,6":"black","9,7":"0"}}
		}
	},
	lits: {
		1: {
			data: {"param_values":{"r":"11","c":"11"},"grid":{"1,2":"black","2,3":"black","2,5":"black","1,8":"black","1,12":"black","1,14":"black","0,15":"black","2,15":"black","0,17":"black","2,17":"black","0,19":"black","1,20":"black","4,3":"black","3,6":"black","4,5":"black","3,8":"black","3,12":"black","4,15":"black","3,18":"black","4,17":"black","3,20":"black","5,2":"black","6,3":"black","6,5":"black","5,8":"black","5,12":"black","5,14":"black","6,15":"black","6,17":"black","5,20":"black","8,1":"black","8,3":"black","7,6":"black","8,5":"black","7,8":"black","7,12":"black","8,11":"black","8,15":"black","7,18":"black","8,17":"black","7,20":"black","9,2":"black","10,3":"black","10,5":"black","9,8":"black","10,7":"black","9,10":"black","10,9":"black","10,11":"black","9,14":"black","10,13":"black","10,15":"black","10,17":"black","9,20":"black","10,19":"black","12,3":"black","12,5":"black","12,7":"black","12,9":"black","11,12":"black","11,16":"black","12,15":"black","12,17":"black","12,19":"black","12,21":"black","13,2":"black","14,3":"black","14,5":"black","13,8":"black","13,10":"black","13,12":"black","13,14":"black","14,15":"black","14,17":"black","13,20":"black","16,3":"black","15,6":"black","16,5":"black","15,8":"black","15,10":"black","15,12":"black","16,11":"black","16,15":"black","15,18":"black","16,17":"black","15,20":"black","17,2":"black","18,1":"black","18,3":"black","18,5":"black","17,8":"black","17,10":"black","17,12":"black","17,14":"black","18,13":"black","18,15":"black","18,17":"black","17,20":"black","20,3":"black","19,6":"black","20,5":"black","19,8":"black","19,10":"black","20,11":"black","20,15":"black","19,18":"black","20,17":"black","19,20":"black","21,2":"black","22,3":"black","22,5":"black","21,8":"black","22,7":"black","21,12":"black","21,14":"black","21,20":"black"}}
		}
	},
	masyu: {
		1: {
			data: {"param_values":{"r":"10","c":"10"},"grid":{"1,3":"w","1,13":"w","3,9":"b",
			"3,19":"b","5,5":"w","5,15":"w","7,1":"b","7,11":"w","9,7":"b","9,17":"w",
			"11,3":"w","11,13":"b","13,9":"w","13,19":"w","15,5":"b","15,15":"b",
			"17,1":"w","17,11":"b","19,7":"b","19,17":"w"}},
		}
	},
    nanro: {
        1: {
        data: {"param_values":{"r":"11","c":"11"},"grid":{"0,1":"black","1,0":"black","1,1":"2","0,3":"black","1,4":"black","0,5":"black","2,5":"black","0,7":"black","0,9":"black","1,10":"black","2,9":"black","1,9":"2","0,11":"black","0,13":"black","1,14":"black","2,13":"black","0,15":"black","1,16":"black","0,17":"black","1,18":"black","0,19":"black","2,19":"black","0,21":"black","1,22":"black","4,1":"black","3,0":"black","3,4":"black","4,3":"black","3,6":"black","3,8":"black","4,7":"black","3,10":"black","3,12":"black","4,11":"black","4,13":"black","3,16":"black","4,15":"black","4,17":"black","3,20":"black","4,19":"black","3,22":"black","5,0":"black","5,4":"black","6,3":"black","6,5":"black","5,5":"2","5,8":"black","6,7":"black","6,9":"black","5,12":"black","6,11":"black","6,13":"black","6,17":"black","5,20":"black","6,19":"black","5,22":"black","6,21":"black","7,2":"black","8,1":"black","7,0":"black","7,4":"black","7,6":"black","7,8":"black","8,9":"black","8,11":"black","7,14":"black","7,16":"black","7,17":"2","7,20":"black","7,22":"black","9,0":"black","9,4":"black","9,6":"black","9,5":"2","10,9":"black","9,12":"black","10,11":"black","9,14":"black","9,16":"black","10,17":"black","9,20":"black","10,19":"black","9,22":"black","12,1":"black","11,0":"black","11,4":"black","12,3":"black","11,6":"black","11,8":"black","12,11":"black","11,11":"2","11,14":"black","12,13":"black","11,16":"black","11,20":"black","12,19":"black","11,22":"black","12,21":"black","13,0":"black","14,3":"black","13,6":"black","14,5":"black","13,8":"black","14,7":"black","13,7":"2","13,10":"black","14,11":"black","13,14":"black","14,13":"black","13,16":"black","13,18":"black","14,17":"black","14,19":"black","13,19":"2","13,22":"black","15,2":"black","16,1":"black","15,0":"black","16,3":"black","15,8":"black","16,7":"black","16,9":"black","16,11":"black","15,14":"black","16,13":"black","15,16":"black","16,15":"black","15,15":"2","15,18":"black","15,20":"black","16,19":"black","15,22":"black","17,0":"black","17,4":"black","17,6":"black","18,5":"black","17,8":"black","17,10":"black","17,12":"black","18,13":"black","17,16":"black","18,15":"black","17,18":"black","18,19":"black","17,22":"black","20,1":"black","19,0":"black","20,3":"black","20,5":"black","19,8":"black","20,7":"black","19,7":"2","19,10":"black","19,14":"black","20,13":"black","19,16":"black","19,18":"black","19,20":"black","20,19":"black","19,22":"black","20,21":"black","22,1":"black","21,0":"black","22,3":"black","21,6":"black","22,5":"black","21,5":"2","22,7":"black","21,10":"black","22,9":"black","21,12":"black","22,11":"black","22,13":"black","21,16":"black","22,15":"black","21,18":"black","22,17":"black","22,19":"black","21,22":"black","22,21":"black"}}
        }
    },
	nagare: {
		1: {
			data: {"param_values":{"r":"8","c":"8"},"grid":{"1,7":"l","3,9":"L","3,13":"u","5,5":"L","7,5":"D","7,9":"black","9,7":"u","9,11":"l","11,11":"D","13,3":"u","13,7":"R","15,9":"black"}}
		}
	},
    ncells: {
        1: {
            data: {"param_values":{"r":"11","c":"10","region_size":"5"},"grid":{"3,5":"1","3,7":"2","3,9":"3","3,11":"1","3,13":"2","3,15":"2","5,5":"1","5,15":"2","7,5":"3","9,5":"2","11,5":"1","11,7":"2","11,9":"1","11,11":"3","11,13":"1","11,15":"2","13,5":"2","13,15":"3","15,5":"1","15,15":"2","17,5":"1","17,15":"3","19,5":"3","19,7":"2","19,9":"3","19,11":"3","19,13":"1","19,15":"2"}}
        },
    },
	nonogram: {
		1: {
			data: {"param_values":{"r":"4","c":"4"},"grid":{"-1,1":"? ?","-1,3":"? ?","-1,5":"? 1","-1,7":"1 2","1,-1":"? ?","3,-1":"?","5,-1":"1 1","7,-1":"? ?"}}
		},
		2: {
			data: {"param_values":{"r":"11","c":"8"},"grid":{"-1,1":"0","-1,3":"9","-1,5":"9","-1,7":"2 2","-1,9":"2 2","-1,11":"4","-1,13":"4","-1,15":"0","1,-1":"0","3,-1":"4","5,-1":"6","7,-1":"2 2","9,-1":"2 2","11,-1":"6","13,-1":"4","15,-1":"2","17,-1":"2","19,-1":"2","21,-1":"0"}},
			link: 'https://en.wikipedia.org/wiki/Nonogram'
		}
	},
	numberlink: {
		1: {
			data: {"param_values":{"r":"5","c":"5"},"grid":{"1,3":"1","3,3":"2","3,7":"4","5,3":"3","5,5":"4","7,7":"3","7,9":"2","9,9":"1"}}
		},
	},
	nuribou: {
		1: {
			data: {"param_values":{"r":"11","c":"11"},"grid":{"1,3":"10","3,19":"7","7,3":"2","7,11":"1","9,19":"12","11,11":"1","13,3":"10","15,11":"1","15,19":"15","19,3":"8","21,19":"7"}}
		}
	},
	nurikabe: {
		1: {
			data: {"param_values":{"r":"10","c":"10"},"grid":{"1,3":"6","3,5":"1","3,17":"6",
			"5,19":"1","7,11":"4","9,9":"3","13,13":"2","15,3":"6","15,9":"2","15,15":
			"5","17,1":"1","17,11":"5"}},
			link: 'https://www.gmpuzzles.com/blog/2019/09/nurikabe-by-michael-tang/'
		}
	},
    onsen: {
        1: {
            data: {"param_values":{"r":"9","c":"15"},"grid":{"0,1":"black","1,2":"black","1,0":"black","0,3":"black","0,5":"black","0,7":"black","2,7":"black","0,9":"black","1,10":"black","2,9":"black","0,11":"black","0,13":"black","0,15":"black","1,16":"black","0,17":"black","2,17":"black","0,19":"black","2,19":"black","0,21":"black","0,23":"black","2,23":"black","0,25":"black","2,25":"black","0,27":"black","2,27":"black","0,29":"black","1,30":"black","2,29":"black","3,2":"black","3,0":"black","3,6":"black","4,5":"black","4,9":"black","4,11":"black","4,13":"black","3,16":"black","4,15":"black","4,17":"black","3,20":"black","3,22":"black","4,21":"black","4,23":"black","4,25":"black","3,30":"black","4,29":"black","5,2":"black","5,0":"black","5,4":"black","6,3":"black","5,6":"black","5,8":"black","5,10":"black","5,12":"black","6,15":"black","5,18":"black","6,17":"black","5,20":"black","5,26":"black","5,28":"black","5,30":"black","8,1":"black","7,0":"black","7,4":"black","7,6":"black","7,8":"black","7,7":"7","7,10":"black","7,12":"black","7,14":"black","8,15":"black","8,17":"black","7,20":"black","7,23":"4","7,26":"black","7,28":"black","7,30":"black","9,2":"black","9,0":"black","9,4":"black","9,6":"black","9,8":"black","9,10":"black","9,12":"black","10,13":"black","10,15":"black","9,18":"black","9,20":"black","10,19":"black","10,23":"black","9,26":"black","9,28":"black","10,27":"black","9,30":"black","11,2":"black","11,0":"black","11,4":"black","12,3":"black","11,6":"black","11,8":"black","12,7":"black","11,10":"black","12,13":"black","11,16":"black","12,15":"black","11,18":"black","11,20":"black","11,22":"black","11,24":"black","11,26":"black","11,30":"black","13,0":"black","13,4":"black","14,5":"black","14,7":"black","13,10":"black","14,9":"black","13,12":"black","14,13":"black","14,15":"black","13,18":"black","14,17":"black","13,20":"black","13,22":"black","14,21":"black","13,24":"black","13,26":"black","14,25":"black","14,27":"black","13,30":"black","14,29":"black","16,1":"black","15,0":"black","15,4":"black","16,3":"black","15,8":"black","15,10":"black","16,11":"black","16,13":"black","16,15":"black","15,18":"black","16,17":"black","15,22":"black","16,21":"black","16,25":"black","15,28":"black","16,27":"black","15,30":"black","18,1":"black","17,0":"black","18,3":"black","18,5":"black","17,8":"black","18,7":"black","18,9":"black","18,11":"black","18,13":"black","17,16":"black","18,15":"black","18,17":"black","17,20":"black","18,19":"black","18,21":"black","17,24":"black","18,23":"black","18,25":"black","18,27":"black","17,30":"black","18,29":"black"}},
        	link: 'https://www.mstang.xyz/blog/8/',
        }
    },
    tapa: {
    	1: {
    		data: {"param_values":{"r":"11","c":"11"},"grid":{"1,13":[1,"?"],"3,1":[2],"3,17":[2,3],"5,7":[6],"5,21":[3],"7,15":[1,1,3],"9,3":[5],"11,9":["?",4],"11,13":[4],"13,19":[1,1,2],"15,7":[1,3],"17,1":[3],"17,15":[1,1,1,1],"19,5":[2,2],"19,21":[3],"21,9":[3]}}
    	},
    	2: {
    		data: {"param_values":{"r":"10","c":"10"},"grid":{"1,7":[1],"1,9":[1,1],"3,1":[3],"3,15":[3],"5,5":[2,2],"7,13":[1,3],"9,3":[3,1],"9,15":[2,2],"11,5":[1,1],"11,17":[1,3],"13,7":[2,1],"15,15":[5],"17,5":[2,3],"17,19":[3],"19,11":[2,1],"19,13":[2]}}
    	}
    },
	skyscrapers: {
		1: {
			data: {"param_values":{"n":"6"},"grid":{"-1,3":"2","-1,9":"2",
			"-1,11":"2","1,-1":"3","3,13":"3","5,-1":"3","7,13":"2","9,13":"3",
			"11,-1":"2","11,13":"2","13,1":"3","13,3":"3","13,5":"3","13,7":"2"}},
			link: 'https://www.gmpuzzles.com/blog/2019/07/skyscrapers-by-michael-tang/'
		}
	},
	slitherlink: {
		1: {
			data: {"param_values":{"r":"13","c":"13"},"grid":{"1,1":"1","1,13":"3","3,5":"3","3,7":"2","3,9":"0","3,17":"0","3,19":"2","5,3":"3","5,11":"2","5,15":"3","7,1":"1","7,7":"0","7,13":"3","7,19":"3","9,1":"2","9,7":"1","9,19":"2","11,1":"2","11,5":"1","11,7":"3","11,19":"0","13,1":"0","13,9":"3","13,17":"0","15,3":"2","15,9":"1","15,17":"1","17,5":"3","17,11":"2","17,15":"1","19,1":"0","19,7":"1","19,13":"3","19,19":"2","3,21":"3","11,21":"2","17,21":"1","21,5":"2","21,9":"0","21,17":"2","21,21":"1","1,25":"0","5,23":"2","7,25":"1","9,25":"2","11,25":"1","13,25":"3","15,23":"1","23,1":"2","23,5":"2","23,11":"2","23,15":"2","25,3":"3","25,13":"3","19,25":"3","23,21":"3","23,25":"1","25,23":"1"}}
		}
	},
	sudoku: {
		1: {
			data: {"param_values":{"Diagonal":false},"grid":{"1,1":"1","1,3":"6","1,5":"3","3,5":"4","3,15":"6","5,5":"5","5,7":"6","5,9":"7","7,9":"8","9,1":"6","9,3":"7","9,5":"8","9,9":"9","9,11":"1","9,13":"2","11,5":"9","11,13":"3","13,5":"1","13,7":"2","13,9":"3","13,13":"4","13,15":"5","13,17":"6","15,9":"4","15,17":"7","17,1":"4","17,9":"5","17,17":"8"}},
		},
		2: {
			data: {"param_values":{"Diagonal":true},"grid":{"1,7":"1","1,15":"6","3,1":"2","3,3":"9","3,13":"4","3,15":"7","5,3":"3","5,11":"2","7,5":"7","7,7":"6","7,17":"5","11,1":"5","11,11":"8","11,13":"7","13,7":"7","13,15":"5","15,3":"5","15,5":"9","15,15":"1","15,17":"8","17,3":"8","17,11":"9"}},
		},
		3: {
			data: {"param_values":{"Diagonal":false,"Untouch":true,"Antiknight":true},"grid":{"1,7":"2","1,15":"1","3,5":"3","3,13":"2","5,3":"4","5,11":"3","13,7":"6","13,15":"5","15,5":"7","15,13":"6","17,3":"8","17,11":"7"}},
			link: 'https://prasannaseshadri.wordpress.com/2013/12/13/puzzle-no-475-untouch-antiknight-sudoku-daily-league/'
		}
	},
	yajilin: {
		1: {
			data: {"param_values":{"r":"10","c":"10"},"grid":{"3,3":[["2","d"],"gray"],"3,9":[["1","r"],"gray"],"3,19":[["2","l"],"gray"],"7,15":[["2","d"],"gray"],"9,9":[["2","l"],"gray"],"11,11":[["1","d"],"gray"],"13,5":[["1","d"],"gray"],"17,1":[["0","r"],"gray"],"17,11":[["1","d"],"gray"],"17,17":[["0","d"],"gray"]}},
			link: 'https://mspuzzles.wordpress.com/2019/03/12/puzzle-15-yajilin/'
		},
		2: {
			data: {"param_values":{"r":"10","c":"10"},"grid":{"1,1":"gray","3,15":[["1","l"],"gray"],"5,11":[["3","d"],"gray"],"7,17":[["1","d"],"gray"],"9,13":[["3","l"],"gray"],"11,7":[["2","r"],"gray"],"13,3":[["2","r"],"gray"],"15,9":[["3","u"],"gray"],"17,5":[["2","u"],"gray"],"19,19":"gray"}},
			link: 'https://dj-puzzles.blogspot.com/2021/05/puzzle-38-two-squares-yajilin.html'
		}
	}
};
