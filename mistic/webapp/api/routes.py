from flask_restx import fields, Resource, Api, Namespace, reqparse

from mistic import configs
from mistic.webapp.api import blueprint, variant_scoring, blueprint


api = Api(app=blueprint,
          version='1.0',
          title='{} API'.format(configs['FLASK_APP_NAME']),
          contact='kchennen',
          contact_email='kchennen@unistra.fr',
          license='Apache 2.0',
          license_url='https://www.apache.org/licenses/LICENSE-2.0',
          )


ns = Namespace(name='MISTIC',
               description='Retrieve {} score based on the genomic coordinates of the variant '.format(configs['FLASK_APP_NAME'])
               )

variants = api.model('Variant',
                     {
                         'chrom': fields.String(required=True),
                         'pos': fields.Integer(required=True),
                         'ref': fields.String(required=False),
                         'alt': fields.String(required=False),
                         '{}_score'.format(configs['FLASK_APP_NAME']): fields.Float(required=False),
                         '{}_pred'.format(configs['FLASK_APP_NAME']): fields.String(required=False),
                     })


@ns.route('/score')
class Score(Resource):
    parser = ns.parser()
    parser.add_argument('release', type=int, choices=(37, 38), required=True, default=37, help='Genome version')
    parser.add_argument('chromosome', type=str, required=True, help='Chromosome')
    parser.add_argument('position', type=int, required=True, help='Chromosomic position')
    parser.add_argument('reference', type=str, required=False, help='Reference allele')
    parser.add_argument('alternative', type=str, required=False, help='Alternative allele')

    @staticmethod
    @ns.response(code=200, description='Success')
    @ns.response(code=400, description='Unknown missense variant position')
    @ns.expect(parser, validate=True)
    def get():
        """Score missense variant"""
        # Define parser
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('release')
        parser.add_argument('chromosome')
        parser.add_argument('position')
        parser.add_argument('reference')
        parser.add_argument('alternative')
        args = parser.parse_args()

        results = {'meta': {'query': '(GRCh{rel}){ch}:{pos}{ref}>{alt}'.format(rel=args.get('release'),
                                                                               ch=args.get('chromosome'),
                                                                               pos=args.get('position'),
                                                                               ref=args.get('reference'),
                                                                               alt=args.get('alternative'),
                                                                               ),
                            },
                   }

        # Execute query
        data = variant_scoring.annotate_variant(release=args.get('release'),
                                                chrom=args.get('chromosome'),
                                                pos=args.get('position'),
                                                ref=args.get('reference'),
                                                alt=args.get('alternative'),
                                                )

        if len(data):
            status_code = 200
            results['meta']['status'] = 'success'
            results['data'] = data
        else:
            status_code = 400
            results['meta']['status'] = 'error'
            results['meta']['message'] = 'Unknown missense variant position'

        return results, status_code


api.add_namespace(ns=ns)
