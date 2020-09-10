# -*- coding: utf-8 -*-

LAYOUT_B3 = {
    'TIPREG': (0, 2),
    'DATA': (2, 10),
    'CODBDI': (10, 12),
    'CODNEG': (12, 24),
    'TPMERC': (24, 27),
    'NOMRES': (27, 39),
    'ESPECI': (39,49),
    'PRAZOT': (49, 52),
    'MODREF': (52, 56),
    'PREABE': (56, 69),
    'PREMAX': (69, 82),
    'PREMIN': (82, 95),
    'PREMED': (95, 108),
    'PREULT': (108, 121),
    'PREOFC': (121, 134),
    'PREOFV': (134, 147),
    'TOTNEG': (147, 152),
    'QUATOT': (152, 170),
    'VOLTOT': (170, 188),
    'PREEXE': (188, 201),
    'INDOPC': (201, 202),
    'DATVEN': (202, 210),
    'FATCOT': (210, 217),
    'PTOEXE': (217, 230),
    'CODISI': (230, 242),
    'DISMES': (242, 245),
}

LAYOUT_B3_UTILIZADO = [
    'DATA', 'CODNEG', 'NOMERES', 'PREABE', 'PREMAX', 'PREMIN', 'PREMED', 'PREULT', 'PREOFC', 'PREOFV', 'TOTNEG', 'QUATOT',
    'VOLTOT', 'FATCOT'
]


class LayoutB3(object):
    def get_campos(self):
        return [i for i in LAYOUT_B3.keys()]

    def get_campos_remover(self):
        return set(self.get_campos()) - set(LAYOUT_B3_UTILIZADO)
    
    def get_posicoes(self):
        return [i for i in LAYOUT_B3.values()]