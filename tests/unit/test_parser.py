import unittest
import io

from righter import parser


class ParserTestCase(unittest.TestCase):

    def setUp(self):
        self.template = """
<selection id="17864a3e5735e496ff55c5527947410f">
    <meta>
        <title>Education First - Cambridge Open Language Database</title>
        <version>EFCamDat_0.90 (EF20130315)</version>
        <url>http://corpus.mml.cam.ac.uk/efcamdat/</url>
        <key>x</key>
        <user>Yutaka Ishii</user>
        <date>Mon, 17 Feb 14 00:02:35 +0000</date>
        <nationalities>cn</nationalities>
        <units>4</units>
    </meta>
    <writings>
        <writing id="C17863" level="10" unit="4">
            <learner id="19148897" nationality="cn"/>
            <topic id="179">Applying to be a fitness trainer</topic>
            <date>2011-10-22 11:14:04.960</date>
            <grade>95</grade>
            <text><![CDATA[{}]]></text>
        </writing>
    </writings>
</selection>"""

    def test_check_sample(self):
        sample = io.BytesIO("""
<selection id="17864a3e5735e496ff55c5527947410f">
    <meta>
        <title>Education First - Cambridge Open Language Database</title>
        <version>EFCamDat_0.90 (EF20130315)</version>
        <url>http://corpus.mml.cam.ac.uk/efcamdat/</url>
        <key>ZHosYW8sYmYsY20sdGQsa20sY2csY2ksZGosZWcsZXQsZ2EsZ20sZ2gsbWcsbWwsbXIsbXUsbWEsbXosbmcsc3Qsc24semEsc2QsYWYsYW0sYXosYmgsa2gsY24saGssbW8sdHcsY3gsY2MsY3ksZ2UsaW4saWQsaXIsaXEsaWwsanAsam8sa3osa3csa2csbGEsbGIsbXksbW4sbW0sbnAsb20scGsscHMscGgscWEsc2Esc2csa3Isc3ksdGgsdHIsdG0sYWUsdXosdm4seWUsYWwsYXQsYnksYmUsYmEsYmcsaHIsY3osZGssZWUsZmksZnIsZGUsZ3IsZ3AsaHUsaWUsaXQsbHQsbHYsbWssbXQsbWQsbmwsbm8scGwscHQscm8scnUsc2ssc2ksZXMsc2UsY2gsdWEsZ2IsYXcsYnosY2EsY3IsY3UsZG0sZG8sc3YsZ2wsZ3QsaG4sbXgsbmkscGEscHIsdmMsdXMsYXIsYm8sYnIsY2wsY28sZWMscHkscGUsdXksdmUsYXUsZmoscGYsbnIsbmMsbnoscGcsd2ZfMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTksMjAsMjEsMjIsMjMsMjQsMjUsMjYsMjcsMjgsMjksMzAsMzEsMzIsMzMsMzQsMzUsMzYsMzcsMzgsMzksNDAsNDEsNDIsNDMsNDQsNDUsNDYsNDcsNDgsNDksNTAsNTEsNTIsNTMsNTQsNTUsNTYsNTcsNTgsNTksNjAsNjEsNjIsNjMsNjQsNjUsNjYsNjcsNjgsNjksNzAsNzEsNzIsNzMsNzQsNzUsNzYsNzcsNzgsNzksODAsODEsODIsODMsODQsODUsODYsODcsODgsODksOTAsOTEsOTIsOTMsOTQsOTUsOTYsOTcsOTgsOTksMTAwLDEwMSwxMDIsMTAzLDEwNCwxMDUsMTA2LDEwNywxMDgsMTA5LDExMCwxMTEsMTEyLDExMywxMTQsMTE1LDExNiwxMTcsMTE4LDExOSwxMjAsMTIxLDEyMiwxMjMsMTI0LDEyNSwxMjYsMTI3LDEyOF9fc3NfX19vbg==</key>
        <user>Yutaka Ishii</user>
        <date>Mon, 17 Feb 14 00:02:35 +0000</date>
        <nationalities>ae,af,al,am,ao,ar,at,au,aw,az,ba,be,bf,bg,bh,bo,br,by,bz,ca,cc,cg,ch,ci,cl,cm,cn,co,cr,cu,cx,cy,cz,de,dj,dk,dm,do,dz,ec,ee,eg,es,et,fi,fj,fr,ga,gb,ge,gh,gl,gm,gp,gr,gt,hk,hn,hr,hu,id,ie,il,in,iq,ir,it,jo,jp,kg,kh,km,kr,kw,kz,la,lb,lt,lv,ma,md,mg,mk,ml,mm,mn,mo,mr,mt,mu,mx,my,mz,nc,ng,ni,nl,no,np,nr,nz,om,pa,pe,pf,pg,ph,pk,pl,pr,ps,pt,py,qa,ro,ru,sa,sd,se,sg,si,sk,sn,st,sv,sy,td,th,tm,tr,tw,ua,us,uy,uz,vc,ve,vn,wf,ye,za</nationalities>
        <units>1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128</units>
    </meta>
    <writings>
        <writing id="C17863" level="10" unit="4">
            <learner id="19148897" nationality="cn"/>
            <topic id="179">Applying to be a fitness trainer</topic>
            <date>2011-10-22 11:14:04.960</date>
            <grade>95</grade>
            <text><![CDATA[
            Dear Mr. Harry Martin, Thanks for giving me the opportunity to apply for the fitness instructor position, which I have desired to achieve for a long time. I believe I am the perfect candidate for this position. My education and ten years' work history are all related to this position. Furthermore, I have all the necessary certificates for this position. I indeed wish I can help other people who need such help to become healthy too. Therefore, I am confident that my passion, ability and excellent communication skills will let my clients get most professional services. Thanks for your time and I will look forward to your feedback. Sincerely, Weihui
            ]]></text>
        </writing>
        <writing id="C17864" level="10" unit="5">
            <learner id="19148897" nationality="cn"/>
            <topic id="322">Finding a home for a wealthy client</topic>
            <date>2011-12-25 08:42:32.930</date>
            <grade>85</grade>
            <text><![CDATA[
            Hi, Mr. Blight, There are four <change><selection>candidated</selection><tag><symbol>D</symbol><correct></correct></tag></change> properties as <change><selection></selection><tag><symbol>MW</symbol><correct>per</correct></tag></change> your requirement. The first one I would like to recommend is a property that you will see anywhere in the world. It has <change><selection>intergrated</selection><tag><symbol>SP</symbol><correct>integrated</correct></tag></change> functional rooms, bedroom, living room, kitchen and bathroom, which needs a new roof renovation. The <change><selection>size land</selection><tag><symbol>WO</symbol><correct>land size</correct></tag></change> is 288.45 sq m and cottage is 54.15 sq with <change><selection></selection><tag><symbol>AR</symbol><correct>an</correct></tag></change> extension <change><selection></selection><tag><symbol>PR</symbol><correct>of</correct></tag></change> up to 150 sqm <change><selection>permittable</selection><tag><symbol>SP</symbol><correct>permissible</correct></tag></change> with <change><selection></selection><tag><symbol>AR</symbol><correct>a</correct></tag></change> price <change><selection></selection><tag><symbol>PR</symbol><correct>of</correct></tag></change> $200,000. If you are interested in another property with history, I can recommend one owned by Lady Elizabeth Hamilton. It is much larger than <change><selection></selection><tag><symbol>AR</symbol><correct>the</correct></tag></change> first one, <change><selection></selection><tag><symbol>AR</symbol><correct>the</correct></tag></change> land <change><selection>of</selection><tag><symbol>x>>y</symbol><correct>is</correct></tag></change> 1200 sqm approx and <change><selection></selection><tag><symbol>AR</symbol><correct>the</correct></tag></change> house <change><selection>of</selection><tag><symbol>x>>y</symbol><correct>is</correct></tag></change> 224.76 sq m upstairs and down stairs, including more rooms. This house cannot be demolished and the price is $1.5M. <change><selection>Another</selection><tag><symbol>x>>y</symbol><correct>Other</correct></tag></change> new apartments, 67 sqm / 78 sqm can be introduced to you. The price is $160,000 each, including the fittings you choose. Now there are only 3x2 bedroom ones <change><selection>avilable</selection><tag><symbol>SP</symbol><correct>available</correct></tag></change>. The last one is a luxurious property for investing. <change><selection></selection><tag><symbol>I(x)</symbol><correct>Word Limit</correct></tag></change>It located in a quiet and traditional corner of the twon with bay, village and mountain scapes surrounding it. Only a few minutes walk to the centre and close to surrounding beaches. The land size is 453.20 sq m and house size is 111.78 sq m. All related facilities are provided with the price of $450.000. Whenever you have the decision, you can call me for the following events. Best regards, XXX
            ]]></text>
        </writing>
    </writings>
</selection>""".encode('utf-8'))
        writings = list(parser.parse(sample))
        self.assertEqual(len(writings), 2)
        self.assertFalse(writings[0]['changes'])
        expected = [
            {'selection': 'candidated', 'symbol': 'D', 'start': 44},
            {'symbol': 'MW', 'correct': 'per', 'start': 69},
            {'selection': 'intergrated', 'symbol': 'SP', 'correct': 'integrated', 'start': 190},
            {'selection': 'size land', 'symbol': 'WO', 'correct': 'land size', 'start': 303},
            {'symbol': 'AR', 'correct': 'an', 'start': 357},
            {'symbol': 'PR', 'correct': 'of', 'start': 368},
            {'selection': 'permittable', 'symbol': 'SP', 'correct': 'permissible', 'start': 383},
            {'symbol': 'AR', 'correct': 'a', 'start': 400},
            {'symbol': 'PR', 'correct': 'of', 'start': 407},
            {'symbol': 'AR', 'correct': 'the', 'start': 551},
            {'symbol': 'AR', 'correct': 'the', 'start': 563},
            {'selection': 'of', 'symbol': 'x>>y', 'correct': 'is', 'start': 569},
            {'symbol': 'AR', 'correct': 'the', 'start': 592},
            {'selection': 'of', 'symbol': 'x>>y', 'correct': 'is', 'start': 599},
            {'selection': 'Another', 'symbol': 'x>>y', 'correct': 'Other', 'start': 718},
            {'selection': 'avilable', 'symbol': 'SP', 'correct': 'available', 'start': 883},
            {'symbol': 'I(x)', 'correct': 'Word Limit', 'start': 945}
        ]
        self.assertEqual(writings[1]['changes'], expected)

    def test_extract_plain_text(self):
        text = "    \nThe sun came up, but it did not dawn\n\nWhy did God make me this way and my brother that way?"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(writings[0]['text'], text)

    def test_merge_nsw_into_sp(self):
        text = "The <change><symbol>NSW</symbol><selection>sunn</selection><correct>sun</correct></change> came up"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(writings[0]['text'], "The sunn came up")
        self.assertEqual(writings[0]['changes'], [{"symbol": "SP", "selection": "sunn", "correct": "sun", "start": 4}])

    def test_extract_sp(self):
        text = "The <change><symbol>SP</symbol><selection>sunn</selection><correct>sun</correct></change> came up"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(writings[0]['text'], "The sunn came up")
        self.assertEqual(writings[0]['changes'], [{"symbol": "SP", "selection": "sunn", "correct": "sun", "start": 4}])

    def test_handle_punctuation(self):
        text = "I like the <change><symbol>SP</symbol><selection>sunn</selection><correct>sun</correct></change>. Don't you?"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(writings[0]['text'], "I like the sunn. Don't you?")

    def test_handle_no_space(self):
        text = "I like the <change><symbol>SP</symbol><selection>sunn</selection><correct>sun</correct></change>Don't you?"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(writings[0]['text'], "I like the sunn Don't you?")

    def test_handle_no_space_beginning(self):
        text = "I like the<change><symbol>SP</symbol><selection>sunn</selection><correct>sun</correct></change> Don't you?"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(writings[0]['text'], "I like the sunn Don't you?")

    def test_handle_no_space_punctuation_beginning(self):
        text = "I like the,<change><symbol>SP</symbol><selection>sunn</selection><correct>sun</correct></change> Don't you?"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(writings[0]['text'], "I like the, sunn Don't you?")

    def test_handle_no_space_at_all(self):
        text = "I like the<change><symbol>SP</symbol><selection>sunn</selection><correct>sun</correct></change>don't you?"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(writings[0]['text'], "I like the sunn don't you?")

    def test_handle_punctuation_in_selection(self):
        text = "I like the<change><symbol>SP</symbol><selection>sunn,</selection><correct>sun</correct></change>don't you?"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(writings[0]['text'], "I like the sunn, don't you?")

    def test_ignore_bad_xml(self):
        text = "The <change> came up"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertFalse(writings)

    def test_skip_bad_changes(self):
        text = "The <change><symbol>SP</symbol><correct>sun</correct></change> came up"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertFalse(writings[0]['changes'])

    def test_skip_changes_with_null_symbol(self):
        text = "The <change><selection>sunn</selection><correct>sun</correct></change> came <change><selection>up</selection><correct>up.</correct><symbol>PU</symbol></change>"
        sample = self.template.format(text)
        writings = list(parser.parse(io.BytesIO(sample.encode('utf-8'))))
        self.assertEqual(len(writings[0]['changes']), 1)
