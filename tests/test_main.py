import unittest
import righter

sample1 = '\n            \n            \n            \n            \n            Hi, Mr. Blight, There are four candidated properties as  your requirement. The first one I would like to recommend is a property that you will see anywhere in the world. It has intergrated functional rooms, bedroom, living room, kitchen and bathroom, which needs a new roof renovation. The size land is 288.45 sq m and cottage is 54.15 sq with  extension  up to 150 sqm permittable with  price  $200,000. If you are interested in another property with history, I can recommend one owned by Lady Elizabeth Hamilton. It is much larger than  first one,  land of 1200 sqm approx and  house of 224.76 sq m upstairs and down stairs, including more rooms. This house cannot be demolished and the price is $1.5M. Another new apartments, 67 sqm / 78 sqm can be introduced to you. The price is $160,000 each, including the fittings you choose. Now there are only 3x2 bedroom ones avilable. The last one is a luxurious property for investing. It located in a quiet and traditional corner of the twon with bay, village and mountain scapes surrounding it. Only a few minutes walk to the centre and close to surrounding beaches. The land size is 453.20 sq m and house size is 111.78 sq m. All related facilities are provided with the price of $450.000. Whenever you have the decision, you can call me for the following events. Best regards, XXX\n            '

sample2 = '\n            \n            \n            \n            \n            Hi Aunt Jane  How are you! welcome come to The USA!  first ,you can book the ticket throught ticket agent. when you arrive airport,you can take e-ticket by you ID.then check in  .next you need prepare you ID.thanks!  Wuhui\n            '

sample3 = '\n            \n            \n            \n            \n            Dear Polris                                                                                                                                                    I am sorry to hear that you have shoping addiction.now,the following is my suggestion.Firstly, you should  bring  little money when you go out.                                                                      Secondly, you should attand a support group.                                                                                     Finally, in your spare time, you my do some exercise                                                                              yours sincerly\n            '

sample4 = '\n            \n            \n            \n            \n            Hi Aunt Jane  How are you! welcome come to The USA!  first ,you can book the ticket throught ticket agent. when you arrive airport,you can take e-ticket by you ID.then check in  .next you need prepare you ID.thanks!  Wuhui\n            '

class SpellingTestCase(unittest.TestCase):

    maxDiff = None

    def test_spelling_sample1(self):
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
                'selection': 'twon', # teacher didn't catch'
                'start': 1049
            }
        ]
        self.assertEqual(response, expected_response)

    def test_spelling_sample2(self):
        response = righter.check_spelling(sample2)
        expected_response = [
            {
                'selection': 'throught',
                'start': 149
            }
        ]
        self.assertEqual(response, expected_response)


    def test_spelling_sample3(self):
        response = righter.check_spelling(sample3)
        expected_response = [
            {
                'selection': 'polris',
                'start': 70
            },
            {
                'selection': 'shoping',
                'start': 257
            },
            {
                'selection': 'attand',
                'start': 458
            },
            {
                'selection': 'sincerly',
                'start': 702
            }
        ]
        self.assertEqual(response, expected_response)

    def test_capitalization_sample4(self):
        response = righter.check_capitalization(sample4)
        expected_response = [
            {
                'selection': 'welcome', # start of the phrase
                'start': 92
            },
            {
                'selection': 'The', # middle phrase in English dict
                'start': 108
            },
            {
                'selection': 'first', # start of the phrase
                'start': 118
            },
            {
                'selection': 'when',# start of the phrase
                'start': 172
            },
            {
                'selection': 'then',# start of the phrase
                'start': 228
            },
            {
                'selection': 'next',
                'start': 244
            },
            {
                'start': 273,
                'selection': 'thanks'
            }
        ]
        self.assertEqual(response, expected_response)
