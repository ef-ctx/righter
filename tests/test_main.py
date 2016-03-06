import unittest
import righter

sample1 = '\n            \n            \n            \n            \n            Hi, Mr. Blight, There are four candidated properties as  your requirement. The first one I would like to recommend is a property that you will see anywhere in the world. It has intergrated functional rooms, bedroom, living room, kitchen and bathroom, which needs a new roof renovation. The size land is 288.45 sq m and cottage is 54.15 sq with  extension  up to 150 sqm permittable with  price  $200,000. If you are interested in another property with history, I can recommend one owned by Lady Elizabeth Hamilton. It is much larger than  first one,  land of 1200 sqm approx and  house of 224.76 sq m upstairs and down stairs, including more rooms. This house cannot be demolished and the price is $1.5M. Another new apartments, 67 sqm / 78 sqm can be introduced to you. The price is $160,000 each, including the fittings you choose. Now there are only 3x2 bedroom ones avilable. The last one is a luxurious property for investing. It located in a quiet and traditional corner of the twon with bay, village and mountain scapes surrounding it. Only a few minutes walk to the centre and close to surrounding beaches. The land size is 453.20 sq m and house size is 111.78 sq m. All related facilities are provided with the price of $450.000. Whenever you have the decision, you can call me for the following events. Best regards, XXX\n            '

class SpellingTestCase(unittest.TestCase):

    def test_spelling_intergrated_and_avilable(self):
        response = righter.check_spelling(sample1)
        expected_response = [
            {
                'selection': 'intergrated',
                'start': 242,
            },
            {
                'selection': 'avilable',
                'start': 935,
            },
            {
                'selection': 'twon',
                'start': 1049
            }
        ]
        self.assertEqual(response, expected_response)
