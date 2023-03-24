# -*- coding: utf-8 -*-
import os
import sqlite3

from mistic import configs


def annotate_variant(release, chrom, pos, ref, alt):
    # set release database
    if release == 38:
        db = os.path.join(configs['data_path']['root'],
                          configs['data_path']['processed'],
                          configs['FLASK_APP_RES']['db'][38])
    else:
        db = os.path.join(configs['data_path']['root'],
                          configs['data_path']['processed'],
                          configs['FLASK_APP_RES']['db'][37])

    # Init db connection
    conn = sqlite3.connect(db)

    # Define query
    cur = conn.cursor()
    sql_query = 'SELECT CHROM, POS, REF, ALT, MISTIC_score, MISTIC_pred, MAX(MISTIC_score)' \
                'FROM MISTIC ' \
                'WHERE CHROM = {} AND POS = {} '.format(chrom, pos)
    if ref:
        sql_query += 'AND REF = {} '.format(ref)
    if alt:
        sql_query += 'AND ALT = {} '.format(alt)

    sql_query += 'GROUP BY ALT'

    # Executre query
    cur.execute(sql_query)

    # Process results
    results = list()
    for r in cur.fetchall():
        result = dict()
        result['chrom'] = r[0]
        result['pos'] = r[1]
        result['ref'] = r[2]
        result['alt'] = r[3]
        # result['score'] = r[7]
        result['score'] = round(number=float(r[4]), ndigits=3)
        result['prediction'] = 'deleterious' if r[5] == 'D' else 'benign'

        results.append(result)

    return results
