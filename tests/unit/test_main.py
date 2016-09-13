import unittest
import righter

sample1 = '\n            \n            \n            \n            \n            Hi, Mr. Blight, There are four candidated properties as  your requirement. The first one I would like to recommend is a property that you will see anywhere in the world. It has intergrated functional rooms, bedroom, living room, kitchen and bathroom, which needs a new roof renovation. The size land is 288.45 sq m and cottage is 54.15 sq with  extension  up to 150 sqm permissible with  price  $200,000. If you are interested in another property with history, I can recommend one owned by Lady Elizabeth Hamilton. It is much larger than  first one,  land of 1200 sqm approx and  house of 224.76 sq m upstairs and down stairs, including more rooms. This house cannot be demolished and the price is $1.5M. Another new apartments, 67 sqm / 78 sqm can be introduced to you. The price is $160,000 each, including the fittings you choose. Now there are only 3x2 bedroom ones avilable. The last one is a luxurious property for investing. It located in a quiet and traditional corner of the twon with bay, village and mountain scapes surrounding it. Only a few minutes walk to the centre and close to surrounding beaches. The land size is 453.20 sq m and house size is 111.78 sq m. All related facilities are provided with the price of $450.000. Whenever you have the decision, you can call me for the following events. Best regards,\n            '

sample2 = '\n            \n            \n            \n            \n            Hi Aunt Jane  How are you! welcome come to The USA!  first ,you can book the ticket throught ticket agent. when you arrive airport,you can take e-ticket by you ID.then check in  .next you need prepare you ID.thanks!  Wuhui\n            '

sample3 = '\n            \n            \n            \n            \n            Dear Polris                                                                                                                                                    I am sorry to hear that you have shoping addiction.now,the following is my suggestion.Firstly, you should  bring  little money when you go out.                                                                      Secondly, you should attand a support group.                                                                                     Finally, in your spare time, you my do some exercise                                                                              yours sincerly\n            '

sample4 = '\n            \n            \n            \n            \n            Hi aunt Jane  How are you! welcome come to The USA!  first ,you can book the ticket throught ticket agent. when you arrive airport,you can take e-ticket by you ID.then check in  .next you need prepare you ID.thanks!  Wuhui\n            '


sample5 = "On  wednesday"

sample_C191561 = "\n            Hi:\n\nMy name is Yichen.I am 27 years old.I am from China.But i live in Taiyuan.I am a teacher.I like my job.\n\nYichen\n            """


class SpellingTestCase(unittest.TestCase):

    maxDiff = None

    def test_spelling_sample1(self):
        response = righter.check_spelling(sample1)
        expected_response = [
            {
                'selection': 'candidated',
                'start': 96
            },
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
                'selection': 'Polris',
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
                'selection': 'How',
                'start': 79
            },
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

    def test_capitalization_sample5(self):
        response = righter.check_capitalization(sample5)
        expected_response = [
            {
                "selection": "wednesday",
                "start": 4
            }
        ]
        self.assertEqual(response, expected_response)

    def test_capitalization_im(self):
        sample = "Dear mum and dad, I'm in the USA"
        response = righter.check_capitalization(sample)
        expected_response = []
        self.assertEqual(response, expected_response)

    def test_capitalization_saturday(self):
        sample = "On saturday, my friends visit me"
        response = righter.check_capitalization(sample)
        expected_response = [
            {
                'selection': 'saturday',
                'start': 3
            }
        ]
        self.assertEqual(response, expected_response)

    def test_capitalization_position(self):
        sample = "i working at china,  i am a fireman."
        response = righter.check_capitalization(sample)
        expected_response = [
            {
                'selection': 'i',
                'start': 0
            },
            {
                'selection': 'china',
                'start': 13
            },
            {
                'selection': 'i',
                'start': 21
            }
        ]
        self.assertEqual(response, expected_response)
        
    def test_capitalization_position2(self):
        response = righter.check_capitalization(sample_C191561)
        expected_response = [
            {
                "selection": "i",
                "start": 74
            }
        ]
        self.assertEqual(response, expected_response)
        
    def test_article_sample_a_old(self):
        sample = "A old  sister"
        response = righter.check_article(sample)
        expected_response = [
            {
                "selection": "A",
                "start": 0
            }
        ]
        self.assertEqual(response, expected_response) 
        
    def test_article_sample_an_doctor(self):
        sample = "I'm an doctor"
        response = righter.check_article(sample)
        expected_response = [
            {
                "selection": "an",
                "start": 4
            }
        ]
        self.assertEqual(response, expected_response) 

    def test_article_sample_a_idea(self):
        sample = "She has a idea"
        response = righter.check_article(sample)
        expected_response = [
            {
                "selection": "a",
                "start": 8
            }
        ]
        self.assertEqual(response, expected_response) 
        
    def test_article_two_spaces(self):
        sample = '. An  model of my workmates and proud of my parents and leader.\n' 
        response = righter.check_article(sample)
        expected_response = [
            {
                'selection': 'An',
                'start': 2
            }
        ]
        self.assertEqual(response, expected_response) 

    def test_article_problem(self): 
        sample =  "\n            Career Plan                Name : Cindy\nFirst, I will do my best to play an outstanidng  roll  on  my recent job. To do an suitalbe  JE accountand  and study  more knowledge abount  our financia  system.       \nNext, I will study AP and AR accountant work to develop my accountant experience.\nAnother thing, I should study the economic law (my weakness) and pass the examination, at last get the accountant title certificate.\nThe fouth  stage, I hope I could improve my management ability and could do some   manage   job.\nFinally, I will do an  financial manager or controller. An  model of my workmates and proud of my parents and leader.\n            "
        response = righter.check_article(sample)
        expected_response = [
            {
                'selection': 'an',
                'start': 133
            },
            {
                "selection": "an",
                "start": 555
            },
            {
                "selection": "An",
                "start": 592
            }
        ]
        self.assertEqual(response, expected_response) 
