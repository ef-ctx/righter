typos = r"""
===New additions===
:''For ease of correcting errors in newly added rules, please add new rules at the top of this section or its appropriate sub-section.''
<source lang="xml">
<Typo word="September 2016" find="\b(?:the\s+)?(January|February|March|April|May|June|July|August|September|October|November|December)\s+of\s+([12]\d\d\d)\b" replace="$1 $2"/>
<Typo word="non-title bout/fight/match" find="\bnon\s+title(?=\s+(?:bout|fight|match)\b)" replace="non-title"/>
<Typo word="nth-round something" find="\b([0-9]+(?:st|nd|rd|th)|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|thirtieth|fortieth|fiftieth|sixtieth|seventieth|eightieth|ninetieth|hundredth|thousandth)\b\s+round(?=\s+(?:decision|(?:technical\s+)?knockout|T?KO))" replace="$1-round"/>
<Typo word="World-famous" find="\b([Ww])orld\s+famous\b" replace="$1orld-famous"/>
<Typo word="Archrival" find="\b([Aa])rch\s+rival(s|ry)?\b" replace="$1rchrival$2"/>
<Typo word="High-profile" find="\b(?<!(?:[Bb]ecause\s+of\s+(?:his|her|its|their)|(?:achiev(?:es?|ed|ing)|creat(?:es?|ed|ing)|display(?:s?|ed|ing)|has|have|keep(?:s?|ing)|kept|(?:main|re)tain(?:s?|ed|ing)|with)\s+a)\s+)([Hh])igh(?<!(?:[A-Z][A-Za-z]+|specified|the)\s+High)\s+profile(?!,|\s+(?:and|as|in|of))\b" replace="$1igh-profile"/>
<Typo word="Halfway" find="\b([Hh])alf[-\s]+way(?=\s+(?:across|between|down|through|up)\b)" replace="$1alfway"/>
<Typo word="Midway" find="\b([Mm])id[-\s]+way(?=\s+(?:across|between|down|through|up)\b)" replace="$1idway"/>
<Typo word="Mezzo-soprano" find="\b([Mm])ezzo\s*soprano(s?)\b" replace="$1ezzo-soprano$2"/>
<Typo word="Oversize(d)" find="\b([Oo]ver|[Uu]nder)[-\s]+size(d?)\b" replace="$1size$2"/>
<Typo word="Top-grossing" find="\b([Tt]op|[Hh]ighest|[Ll]owest)\s+grossing(?=\s+(?:film|movie|concert)s?\b)" replace="$1-grossing"/>
<Typo word="Long-awaited" find="\b([Ll])ong\s+awaited\b" replace="$1ong-awaited"/>
<Typo word="First half" find="\b([Ff]irst|[Ss]econd)-half(?=\s+(?:and|as|for|in|of|to|was)\b)" replace="$1 half"/>
<Typo word="Us Weekly" find="\bUS Weekly\b" replace="Us Weekly"/>
<Typo word="Constituency" find="\b([Cc])onsistuenc(y|ies)\b" replace="$1onstituenc$2"/>
<Typo word="Hurricane-force" find="\b([Hh])urricane\s+force(?=\s+(?:winds?|windspeeds?|gusts?|storms?)\b)" replace="$1urricane-force"/>
<Typo word="Billboard" find="\b([Bb])il(?:lboa|boar|l?bora?)d(s?)\b" replace="$1illboard$2"/>
<Typo word="Widely" find="\b([Ww])idely-(?=[a-z]+ed\b)(?![a-z]+-)" replace="$1idely "/>
<Typo word="Native Americans" find="\bnative\s+[Aa]merican(s?)\b" replace="Native American$1"/>
<Typo word="Open-air" find="\bopen\s+air(?<=\b[Aa]n\s+open\s+air)(?=\s+(?:amphitheater|amphitheatre|area|auditorium|bath|church|cinema|courtyard|dance|display|exhibition|festival|mall|market|mass|meeting|music|pavilion|performance|pool|production|restaurant|service|shopping|site|stadium|stage|structure|swimming|theater|theatre|venue))" replace="open-air"/>
<Typo word="Low-lying" find="\b([Ll])ow\s+lying(?=\s+(?:area|cloud|coastal|field|flat|ground|hill|island|land|nature|part|plains|region))" replace="$1ow-lying"/>
<Typo word="Telangana" find="\b(?:tela|tele|Tele)ngana\b" replace="Telangana"/>
<Typo word="Performance-enhancing" find="\b([Pp])erformance\s+enhancing(?=\s+(?:drug|effect|steroid|substance))" replace="$1erformance-enhancing"/>
<Typo word="made-for-TV" find="\bmade\s+for\s+(TV|television)\s+(film|movie)\b" replace="made-for-$1 $2"/>
<Typo word="Chhattisgarh" find="\b[Cc]hh?att?is(?<!Chhattis)garh(i)?" replace="Chhattisgarh$1"/>
<Typo word="Grammy Award" find="\bgrammy\s+[Aa]ward(s?)\b" replace="Grammy Award$1"/>
<Typo word="Relay" find="\b4(?: ?x ?| ×|× ?)(100|200|400|800|1500)\s*m\b" replace="4 × $1 m"/>
<Typo word="Multimillion-dollar" find="\b([Mm])ulti[-\s]*([mb])illion[-\s]+(dollar|euro|pound)\b(?<!ulti[mb]illion-[a-z]+)" replace="$1ulti$2illion-$3"/>
<Typo word="nth-minute something" find="\b([0-9]+(?:st|nd|rd|th)|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|thirtieth|fortieth|fiftieth|sixtieth|seventieth|eightieth|ninetieth|hundredth|thousandth)\b\s+minute(?=\s+(?:equaliser|goal|header|lead|opener|penalty|strike|substitute|winner))" replace="$1-minute"/>
<Typo word="Worldwide" find="\b([Ww])orld\s+wide\b(?!\s+(?:[Ww]eb|receiver)\b)" replace="$1orldwide"/>
<Typo word="led" find="\blead(?=\s+to\s)(?<=(?:(?:That|This)|[;\.] that|[,;\.] this)\s+lead)" replace="led"/>
<Typo word="Colleague" find="\bwork\s+colleague(s?)\b" replace="colleague$1"/>
<Typo word="Offshoot" find="\b([Oo])ff[-\s]+shoot(s?)\b" replace="$1ffshoot$2"/>
<Typo word="Swapp(ed/ing)" find="\b([Ss])wap(ed|ing)\b" replace="$1wapp$2"/>
<Typo word="Encompass" find="\b([Ee])(?:mcom|nco)pass(e[sd]|ing)?\b" replace="$1ncompass$2"/>
<Typo word="first-come, first-served" find="\bfirst[-\s]come,?[-\s\/]+first[-\s]serve\b" replace="first-come, first-served"/>
<Typo word="present-day" find="\b(present|modern)\s+day\b(?=\s)(?<=\b(?:[Aa]|[Bb]y|[Ii]n|[Ii]ts|[Nn]ear|of|[Tt]heir|with)\s+(?:present|modern)\s+day)" replace="$1-day"/>
<Typo word="Swordplay" find="\b([Ss])word[-\s]+play\b(?<!\band[-\s]+[Ss]word[-\s]+play)" replace="$1wordplay"/>
<Typo word="Sword fight" find="\b([Ss])wordfight([a-z]*)\b" replace="$1word fight$2"/>
<Typo word="associate degree" find="\b[Aa]ssociate['’]?s?['’]?\s+[Dd]egree(s?)\b(?<=[a-z]\s+[Aa]s[a-z'’]+\s+[Dd]egrees?)(?<!associate\s+degrees?)" replace="associate degree$1"/>
<Typo word="bachelor's degree" find="\b[Bb]at?chelor['’]?s?['’]?\s+[Dd]egree(s?)\b(?<=[a-z]\s+[Bb]a[a-z'’]+\s+[Dd]egrees?)(?<!bachelor's\s+degrees?)" replace="bachelor's degree$1"/>
<Typo word="master's degree" find="\b[Mm]aster['’]?s?['’]?\s+[Dd]egree(s?)\b(?<=[a-z]\s+[Mm]a[a-z'’]+\s+[Dd]egrees?)(?<!master's\s+degrees?)" replace="master's degree$1"/>
<Typo word="Million" find="\b(\d+)(\s|&nbsp;)+millions\s+(dollars|[Ee]uros|pounds|tons)\b" replace="$1$2million $3"/>
<Typo word="In comparison," find="\bIn\s+comparison(?=\s)(?!\s+(?:to|with)\b)" replace="In comparison,"/>
<Typo word="incredible" find="\bincreadibl([ey])\b" replace="incredibl$1"/>
<Typo word="shown" find="\bshowed\b(?<=\b(?:is|are|was|were|be|been)\s+showed)" replace="shown"/>
<Typo word="bachelor's and master's degrees" find="\bbachelor['’]?s? and master['’]?s? degree(s?)\b" replace="bachelor's and master's degree$1"/>
<Typo word="Furthermore," find="\b(Accordingly|Consequently|Even\s+so|Furthermore|In\s+other\s+words|Indeed|Meanwhile(?!\s+Gardens)|Moreover|Nevertheless|On\s+the\s+other\s+hand|Therefore|For\s+example|Subsequently(?!\s+(?:enacted|renamed|told)))(?=\s)" replace="$1,"/>
<Typo word="As a result," find="\bAs\s+a\s+result(?=\s)(?!\s+of\b)" replace="As a result,"/>
<Typo word="However," find="\bHowever\s+(?=(?:according|after|as|because|before|by|despite|due|during|for|from|if|in|later|not|on|only|since|sometimes|there|when|with)\b)" replace="However, "/>
<Typo word="Commercially" find="\b([Cc])ommercially-(?=[a-z]+(?:ed|ble|ful)\b)(?![a-z]+-)" replace="$1ommercially "/>
<Typo word="Water-soluble" find="\b([Ww])ater\s+soluble\b" replace="$1ater-soluble"/>
<Typo word="rule of thumb" find="\bgeneral\s+rule[ -]of[ -]thumb\b" replace="rule of thumb"/>
<Typo word="Snow-covered" find="\b([Ss]now|[Ii]ce|[Ss]lush)\s+(covered|capped)(?=(?:[,;\.\)]|\s+(?:area|bluff|cape|except|field|forest|ground|headland|highway|hill|island|landscape|mountain|peak|peninsula|plateau|point|ridge|road|rock|runway|saddle|slope|terrain|water)s?\b))" replace="$1-$2"/>
<Typo word="Warren Buffett" find="\bWarren (E\. )?Buffet\b" replace="Warren $1Buffett"/>
<Typo word="Locally" find="\b([Ll])ocally-(?=[a-z]+ed\b)(?![a-z]+-)" replace="$1ocally "/>
<Typo word="Anytown-based" find="\b([A-Z][a-z]+)\s+based\b(?<=\b(?:[Tt]he|[Aa]n?|of|from|by|for|with|other|between|to|his)\s+[A-Z][a-z]+,?(?:\s+[A-Z][a-z]+)?\s+based)(?!\s+(?:in|on|at|upon|along|his|her|their|its|largely|mostly|partially|a|an)\b)" replace="$1-based"/>
<Typo word="Milli- SI prefix" find="\b([Mm])ili-?(meter|metre|liter|litre|gram|second|ampere|kelvin|candela|mole)(s)?"\b replace="$1illi$2$3"/>
<Typo word="Statewide/Nationwide" find="\b([Nn]ation|[Ss]tate)[- ]+wide\b(?<!all-state\s+wide)" replace="$1wide"/>
<Typo word="one of" find="\ba\s+one\b(?<= a\s+one)(?=\s+of\b)(?!\s+of\s+a\s+kind)" replace="one"/>
<Typo word="n-year-old" find="\b([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand)(?:\s+year\s+|\s+year-|-year\s+)old\s+(boy|bridge|brother|building|church|college|company|(?:grand)?(?:daughter|father|mother|son)|design|facility|girl|(?:farm)?house|institution|landmark|law|(?:fe)?male|man|mansion|patient|(?:world\s+)?record|(?:high\s+)?school|sister|structure|students?|theat(?:er|re)|tradition|tree|woman)\b" replace="$1-year-old $2"/>
<Typo word="World-renowned" find="\b([Ww])orld-renown\s+" replace="$1orld-renowned "/>
<Typo word="Soft-spoken" find="\b([Ss])oft\s+(boiled|edged|headed|hearted|nosed|spoken)" replace="$1oft-$2"/>
<Typo word="All-time" find="\b([Aa])ll\s+time(?=\s+(?:American\sLeague|appearance|assists|attendance|average|best|biggest|blockbuster|career|classic|club|famous|favou?rite|franchise|great|greatest|greats?|high|highest|hit|lead|leaders?|leading|league|list|low|Major|maximum|most|music|National\sLeague|NCAA|NFL|opening|peak|points|popular|receiving|record|rushing|sack|saves|scoring|series|single|table|[Tt]op|total|winningest|wins|world|worst)\b)" replace="$1ll-time"/>
<Typo word="nth-place something" find="\b([0-9]+(?:st|nd|rd|th)|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|thirtieth|fortieth|fiftieth|sixtieth|seventieth|eightieth|ninetieth|hundredth|thousandth)\b\s+(placed?|rate)(?=\s+(?:effort|(?:(?:best|points|team)\s+)?finish|performance|position|power|ranking|result|run\b|troph(?:y|ies)|victory|winner))" replace="$1-$2"/>
<Typo word="centuries-old" find="\b(centuries|decades)\s+old\b(?<=\b(?:[Tt]heir|[Tt]he|[Aa])\s+[a-z]+\s+old)" replace="$1-old"/>
<Typo word="intertribal" find="\binter[-\s]+tribal\b" replace="intertribal"/>
<Typo word="Passageway" find="\b([Pp])assage[-\s]+way(s)?\b" replace="$1assageway$2"/>
<Typo word="A n-something" find="\b([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand)\b(?<=\b(?:[Aa]n?|first|second|third|[Aa]dditional|[Hh]is|[Hh]er|[Tt]heir|[Ii]ts)\s+[0-9a-z]+)\s+(?!member\s+[a-z]+s\b)(inch|foot|yard|mile|meter|metre|acre|ounce|pound|ton|second|minute|hour|day|week|month|year|point|game|goal|liter|litre|gallon|door|cylinder|wheel(?:e[dr])?|seat(?:er)?|decker|horsepower|stage|person|man|woman|page|member|vote|room|hole|passenger|bed|round|runner)(?=[,\s]|(-(?:long|high|tall|wide|deep|old)\b))(?!\s+(?:long|high|tall|wide|deep|old|of|for|at|as|in|with|by|is|was)\b)(?<!\b\d{4}\s+(?:game|second|stage|vote))(?<!told her one day)" replace="$1-$2"/>
<Typo word="n-year" find="\b([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand)\s+(year|month)\b(?<= [0-9a-z]+\s+[a-z]+)(?=\s+(?:absence|affair|agreement|assignment|association|ban|battle|break|campaign|career|ceasefire|closure|coma|competition|contract|course|cruise|cycle|deadline|deal|delay|deployment|drought|duration|effort|engagement|enlistment|exhibit|exhibition|exile|existence|expedition|extension|feasibility|gap|gestation|guest|hiatus|history|hospital|illness|incumbent|injury|internship|investigation|jail|journey|lay-off|layoff|lease|leave|lifespan|loan|lockout|maintenance|military|mission|modernization|moratorium|notice|overhaul|partnership|period|plan|posting|prison|process|professional|program|programme|project|recovery|recurring|refit|regular|reign|relationship|research|residency|restricted|rotation|run|sabbatical|scholarship|school|season|sentence|siege|sojourn|span|speaking|spell|starter|stay|stint|strike|struggle|study|subscription|subsidy|suspended|suspension|tenure|term|tour|training|treatment|trial|trip|truce|veteran|visit|voyage|wait|waiting|war|workshop)\b)" replace="$1-$2"/>
<Typo word="Muhammad Ali" find="\bMuhammed Ali\b" replace="Muhammad Ali"/> 
<Typo word="Hachette Book Group" find="\bHatchette\s+Book\s+Group\b" replace="Hachette Book Group"/> 
<Typo word="One-night stand" find="\bone\b(?<=\b[Aa]\s+one)[-\s]+night[-\s]+stand\b(?<!one-night\s+stand)" replace="one-night stand"/>
<Typo word="Long-standing" find="\blong\s+standing\b(?<=\b(?:[Aa]|[Tt]he)\s+long\s+standing)(?!\s+(?:of|in|ovation)\b)" replace="long-standing"/>
<Typo word="Stand-alone" find="\bstand\s+alone\b(?<=\b(?:A|a|The|the)\s+stand\s+alone)" replace="stand-alone"/>
<Typo word="Medium-sized" find="\b([Mm])edium\s+sized\b" replace="$1edium-sized"/>
<Typo word="fewer" find="\bless\s+(people)\b" replace="fewer $1"/>
<Typo word="a while" find="\b([Ff]or|[Aa]fter)\s+awhile\b" replace="$1 a while"/>
<Typo word="had run" find="\bhad\s+ran\b" replace="had run"/>
<Typo word="Ongoing" find="\b([Aa]n|[Tt]he)\s+on[- ]+going\b" replace="$1 ongoing"/>
<Typo word="Associate degree" find="\b([Aa]ssociate)'?s\s+[Dd]egree(s?)\b" replace="$1 degree$2"/>
<Typo word="Bachelor's/Master's degree" find="\b([Bb]achelor|[Mm]aster)s?'?\s+[Dd]egree(s?)\b" replace="$1's degree$2"/>
<Typo word="Feature-length" find="\b([Ff])eature\s+length(?=\s+(?:animated|adaptation|anime|comedy|comedies|documentary|documentaries|drama|episode|film|motion|movie|musical|pilot|production|screenplay|script|silent|special|television|TV|version)s?\b)" replace="$1eature-length"/>
<Typo word="Full-length" find="\b([Ff])ull\s+length(?=\s+(?:album|studio|release|feature|film|LP|solo|novel|record|CD|live|book|work|recording|play|movie|biography|animated|documentary|comedy|debut|motion|music|show)s?\b)" replace="$1ull-length"/>
<Typo word="Acquisition" find="\b([Aa])c?qu(?:isit?o|sitio|isit|istio)n(s?)\b" replace="$1cquisition$2"/>
<Typo word="Full-scale" find="\b([Ff])ull\s+scale(?=\s+(?:replica|war|invasion|assault|attack|model|civil|production|mock-?up|battle|musical|administrative|riot|rebellion|reconstruction|nuclear|military|tour|test|revolt|opera|mockup|rehearsal|prototype|offensive|investigation|conflict|version|evacuation|counter-?attack|campaign|revolution|renovation|insurrection)s?\b)" replace="$1ull-scale"/>
<Typo word="Ottoman Empire" find="\b[Oo]ttoman\s+empire\b" replace="Ottoman Empire"/>
<Typo word="Last week's episode" find="\b([Ll])ast weeks['’]? episode\b" replace="$1ast week's episode"/>
<Typo word="This week's" find="\b([Tt])his weeks['’]?\s" replace="$1his week's "/>
<Typo word="Japan's" find="\bJapans['’]?\s" replace="Japan's "/>
<Typo word="Second-half substitute" find="\bsecond\s+half\s+(substitutes?|replacements?)\b" replace="second-half $1"/>
<Typo word="De facto" find="\b([Dd])e-?facto\b" replace="$1e facto"/>
<Typo word="Full-fledged" find="\b([Ff])ull\s+fledged\b" replace="$1ull-fledged"/>
<Typo word="Panorama" find="\b([Pp])anar[ao]m(ic|a)\b" replace="$1anoram$2"/>
<Typo word="T-shirt" find="\b[Tt][-\s][Ss]hirt(?<!T-shirt)(s?)\b" replace="T-shirt$1"/>
<Typo word="UTC−" find="\bUTC-([0-9])\b" replace="UTC−$1"/><!-- e.g. UTC−05:00 -->
<Typo word="Marxism–Leninism" find="\b[Mm]arxis(t|m)-[Ll]eninis(t|m)\b" replace="Marxis$1–Leninis$2"/>
<Typo word="Louisville" find="\bLousiville\b" replace="Louisville"/>
<Typo word="Different" find="\b([Dd])ifferents\b(?!\s+of\b)" replace="$1ifferent"/>
<Typo word="Remarry" find="\b([Rr])e-marr(iages?|ie[ds]|ying|y)\b" replace="$1emarr$2"/>
<Typo word="Hand-to-hand" find="\b([Hh])and\s+to\s+hand\b(?=\s+(?:combat|fight|struggle|weapon|battle|warfare))" replace="$1and-to-hand"/>
<Typo word="Above-mentioned" find="\babove(?<=\b[Tt]he\s+above)\s+mentioned" replace="above-mentioned"/>
<Typo word="Easily" find="\b([Ee])asily-(?=[a-z]+(?:ed|able)\b)(?![a-z]+-)" replace="$1asily "/>
<Typo word="Smallpox" find="\b([Ss])mall[-\s]+pox\b" replace="$1mallpox"/>
<Typo word="La Tène" find="\bLa Tene\b" replace="La Tène"/>
<Typo word="dependent" find="\b(are|be(?:en)?|is|was|were)\s+((?:all|also|becoming|more|no[tw]|often|still|very|[a-z]+ly)\s+)?dependant\s+on\b" replace="$1 $2dependent on"/>
<Typo word="dependent" find="\b(bec[ao]me)\s+dependant\s+on\b" replace="$1 dependent on"/>
<Typo word="Dependent upon" find="\b([Dd])ependant\s+upon\b" replace="$1ependent upon"/>
<Typo word="Right-hand man" find="\b([Rr])ight\s+hand\s+man\b" replace="$1ight-hand man"/>
<Typo word="Worst-case" find="\b([Ww])orst\s+case(?=\s+(?:scenario|performance))" replace="$1orst-case"/>
<Typo word="Life-threatening" find="\b([Ll])ife\s+threatening\b" replace="$1ife-threatening"/>
<Typo word="Reassign" find="\b([Rr])e-assign(s?|ed|ing|ments?)\b" replace="$1eassign$2"/>
<Typo word="Buildup" find="\bbuild\s+up(?=\s+of\b)|\bbuild\s+up\b(?<=\b(?:[Tt]he|[Aa]|[Aa]ny|military|eventual|dangerous|gradual|slow|rapid|large|major|massive|naval|significant|dramatic|huge)\s+build\sup)" replace="buildup"/>
<Typo word="Internationally" find="\b([Ii]nternationally)-(?=[a-z]+ed\b)" replace="$1 "/>
<Typo word="Fuentes de Oñoro" find="\bFuentes de Onoro\b" replace="Fuentes de Oñoro"/>
<Typo word="His/Her Majesty's Stationery Office" find="\b((His|Her) Majesty'?s|H\.? ?M\.?) Stationary Office\b" replace="$1 Majesty's Stationery Office"/>
<Typo word="Idiosyncrasy" find="\b([Ii])diosyncrac(y|ies)\b" replace="$1diosyncras$2"/>
<Typo word="Activities" find="\b([Aa])ci?tivites\b" replace="$1ctivities"/>
<Typo word="Activity" find="\b([Aa])c(?:itivit|tivt|tvit)(y|ies)\b" replace="$1ctivit$2"/>
<Typo word="(Infra/Re)structure" find="\b([Ii]nfras|[Rr]es|[Ss])(?:tuctur|tru[tc]ur|trucutr|tructrur?)(alis[mt]s?|ing|ally|al|e[sd]?)\b" replace="$1tructur$2"/>
<Typo word="॥" find="\s।।|।।" replace="॥"/>
<Typo word="।" find="&nbsp;।|\s।" replace="।"/>
<Typo word="॥" find="&nbsp;॥|\s॥" replace="॥"/>
<Typo word="॥" find="\s।।" replace="॥"/>
<Typo word="Highly" find="\b([Hh])ighly-(?=[a-z]+ed\b)" replace="$1ighly "/>
<Typo word="Day-to-day" find="\b([Dd])ay\s+to\s+day\b(?=\s+(?:operation|running|life\b|lives\b|activit|operation|management|basis|business|responsibilit|work\b|govern|administration|function(s|ing)?\b|government|decision|affairs|working|events?|needs|maintenance|duties|routine))" replace="$1ay-to-day"/>
<Typo word="exact revenge" find="\bextract(s|ed|ing)?(\shis|\sher)?\s+revenge\b" replace="exact$1$2 revenge"/>
<Typo word="Eyewear, Eyelash, etc." find="\b([Ee])ye(?<!-[Ee]ye)[- ](glasses|wear|balls?|brows?|lash(?:es)?|lids?|sores?|witness(?:es))\b" replace="$1ye$2"/>
<Typo word="The number of times" find="\b([Tt])he\s+amount\s+of\s+times\b" replace="$1he number of times"/>
<Typo word="Between him and" find="\b([Bb])etween\s+he\s+and\b" replace="$1etween him and"/>
<Typo word="Between her and" find="\b([Bb])etween\s+she\s+and\b" replace="$1etween her and"/>
<Typo word="have yet" find="\bstill\s+hav(e|ing)\s+yet\b" replace="hav$1 yet"/>
<Typo word="Contribute" find="\b([Cc])on[tr]ibut(e[sd]?|ing|ions?|ors?)\b" replace="$1ontribut$2"/>
<Typo word="Elderly" find="\b([Ee])ldery\b" replace="$1lderly"/>
<Typo word="National Register of Historic Places" find="\b[Nn]ational\s+[Rr]egistry\s+[Oo]f\s+[Hh]istoric\s+[Pp]laces\b" replace="National Register of Historic Places"/>
<Typo word="National Park Service" find="\bNational\s+Parks\s+Services?\b" replace="National Park Service"/>
<Typo word="Palm OS" find="\bPalmOS\b" replace="Palm OS"/>
<Typo word="Juridical" find="\b([Jj])uridicial(ly)?\b" replace="$1uridical$2"/>
<Typo word="Brazilian jiu-jitsu" find="\bBrazi(?:llian [Jj]i?u[- ]?[Jj]|lian Ji?u[- ]?[Jj]|lian ju[- ]?[Jj]|lian jiu[ ]?[Jj]|lian jiu-J)itsu\b" replace="Brazilian jiu-jitsu"/>
<Typo word="Duty-free" find="\b([Dd])uty\s+free(?=[\.,]|\s+(?:shop|store|sale|area|zone|trade|item|lunch|access|goods|port|import|status|treatment|section))" replace="$1uty-free"/>
<Typo word="Kuomintang" find="\bKuomingtang\b" replace="Kuomintang"/>
<Typo word="*–American War" find="\b(Spanish|Mexican|Philippine)(?:[- ]American [Ww]ar|–American war)\b" replace="$1–American War"/>
<Typo word="Adams–Onís Treaty" find="\bAdams(?:-On[íi]s [Tt]|–Onis [Tt]|–Onís t)reaty\b" replace="Adams–Onís Treaty"/>
<Typo word="en masse" find="\ben[-\s]?mass\b" replace="en masse"/>
<Typo word="(In/Un)Dis/Extinguish" find="\b([Dd]is|[IiUu]ndis|[Ee]x)tin?[gq]i?ui?sh?((?:ab[li]|e[drs]|ing|ment)[a-z]*)?\b(?<!tinguish[a-z]*)" replace="$1tinguish$2"/>
<Typo word="Lent" find="\b([Ll])ended\b" replace="$1ent"/>
<Typo word="Labor-intensive" find="\b([Ll])abo(u?)r\s+intensive\b" replace="$1abo$2r-intensive"/>
<Typo word="(A/S)uspicious" find="\b([AaSs])uspicous(ly)?\b" replace="$1uspicious$2"/>
<Typo word="August" find="\b([Aa])ugu(?:es|as?)t\b" replace="$1ugust"/>
<Typo word="contract" find="\bsigned\s*a\s*contact\b" replace="signed a contract"/>
<Typo word="Transcribe" find="\b([Tt])ra[nscr]{3,5}i(?<!anscri)(b(?:e[ds]?|ers?|ing)|pt(?:s?|ases?|ion(ist)?s?|ional(ly)?))\b" replace="$1ranscri$2"/>
<Typo word="Currency symbol before number" find="\b([\d,\.]+)([£€$])(?!\d)" replace="$2$1"/><!-- don't change prices in escudos and reis (escudos$centavos such as 20$00) -->
<Typo disabled="except for" find="\bwith\s*the\s*exception\s*of\b" replace="except for"/>
<Typo disabled="Except for" find="\bWith\s*the\s*exception\s*of\b" replace="Except for"/>
<Typo disabled="whether" find="\bas\s*to\s*whether\b" replace="whether"/>
<Typo disabled="Whether" find="\bAs\s*to\s*whether\b" replace="Whether"/>
<Typo disabled="to" find="\bso\s*as\s*to\b" replace="to"/>
<Typo disabled="To" find="\bSo\s*as\s*to\b" replace="To"/>
<Typo disabled="different" find="\b([Ss]everal|[Mm]any)\s*different\b" replace="$1"/>
<Typo disabled="remain" find="\bcontinue\s*to\s*remain\b" replace="remain"/>
<Typo word="Earlier" find="\b([Ee])a(?:r[li]|rly|li)er\b(?<!Earler)" replace="$1arlier"/>
<Typo word="Pipeline" find="\b([Pp])ipline(s?)\b" replace="$1ipeline$2"/>
<Typo word="Debuted" find="\bfirst\s+d([eé])but(ed|ing)\b" replace="d$1but$2"/>
<Typo word="Consists" find="\bis\s+consisted\b(?= of\b)" replace="consists"/>
<Typo word="Behind" find="\b([Bb])ehin(g|ed)\b" replace="$1ehind"/>
<Typo word="Perpetrate" find="\b([Pp])erpertrat([a-z]+)\b" replace="$1erpetrat$2"/>
<Typo word="Phillips (Andover/Exeter)" find="\bPhilips\s+(Andover|Exeter)\b" replace="Phillips $1"/>
<Typo word="Decades apostrophes" find="\b((?:1\d|20)\d0)['’′]?s(?<=\b(?:[Aa]n?|[Oo]n|[Tt]he)\s{1,9}(?:later?|earl(?:y|ier)|mid(?:dle)?)?[-\s]{0,9}(?:1\d|20)\d0['’′]?s)\s{1,9}and\s{1,9}((later?|earl(?:y|ier)|mid(?:dle)?)?[-\s]{0,9}(?:1\d|20)\d0)['’′]s" replace="$1s and $2s"/>
<Typo word="Debtors' prison" find="\b([Dd])ebtor'?s\s+prison\b" replace="$1ebtors' prison"/>
<Typo word="Amalgamate" find="\b([Aa])m(?:[al]{1,3}g[aou]?ma?t(?<!malgamat)|alagat)(e[sd]?|ions?|ing)\b" replace="$1malgamat$2"/>
<Typo word="Splinter group" find="\b([Ss])plinter-group(s?)\b" replace="$1plinter group$2"/>
<Typo word="Enterprise" find="\b([Ee])nte(?:rp|pr)ise(s?)\b" replace="$1nterprise$2"/>
<Typo word="Losing on penalties" find="\b([Ll])oosing\s+on\s+penalties\b" replace="$1osing on penalties"/>
<Typo word="Anthropology" find="\b([Aa])(?:n?thr?|ntr)o?p[ol]{1,3}(?<!nthropolo)g(y|ically|ical|ic|ists?)\b" replace="$1nthropolog$2"/>
<Typo word="of xxx of xxx" find="\bof ([a-z]+) of (?!(classes|consciousness|copies|friends|funds|representations|sets|systems))\1\b" replace="of $1"/>
<Typo word="Manuscript" find="\b([Mm])anu?[scr]{2,4}i[rpt]{1,3}(?<!nuscrip?t)(s?|ed)\b" replace="$1anuscript$2"/>
<Typo word="Lawsuit" find="\b([Ll])aw[- ]suit(s?)\b" replace="$1awsuit$2"/>
<Typo word="Facsimile" find="\b([Ff])a[cs]+i?mili?e(?<!acsimile)(s?)\b" replace="$1acsimile$2"/>
<Typo word="Honorary" find="\b([Hh])ono(?:u?ra|urar)y\b" replace="$1onorary"/>
<Typo word="Prodigy" find="\b([Pp])rogid(y|al|ies)\b" replace="$1rodig$2"/>
<Typo word="Nemesis" find="\barch[\s-]?nemesis\b" replace="nemesis"/>
<Typo word="Emerge from" find="\bemerge([ds])?\s+out\s+of\b" replace="emerge$1 from"/>
<Typo word="Wreak havoc" find="\b(?:reek|wrea?ck)(ed|s|ing)?\s+havoc\b" replace="wreak$1 havoc"/>
<Typo word="Moroccan" find="\b[Mm]oroc+oa?n(s?)\b" replace="Moroccan$1"/>
<Typo word="who has been" find="\bwhose\s+been\b" replace="who has been"/>
<Typo word="Republic" find="\b([Rr])e(?:pup|bub)lic(s?|ans?)\b" replace="$1epublic$2"/>
<Typo word="Also (twice)" find="\balso\s+(is|was|are|were|[cw]ould)\s+also\b" replace="$1 also"/>
<Typo word="Also (2 times)" find="\balso\s+(ha[sd]|have)\s+also\b" replace="also $1"/>
<Typo word="Newly" find="\b([Nn])ewly-(?=[a-z]+ed\b)(?![a-z]+-|wed)" replace="$1ewly "/>
<Typo word="Recently" find="\b([Rr])ecently-(?=[a-z]+ed\b)(?![a-z]+-)" replace="$1ecently "/>
<Typo word="Horse-drawn" find="\b([Hh])orse\s+drawn(?= (?:carriage|vehicle|wagon|tram(way)?|cart|streetcar|railway|hearse|fire|coache?|(omni)?buse?|transport|boat|sleigh|chariot)s?\b)" replace="$1orse-drawn"/>
<Typo word="Mason–Dixon line" find="\bMason[-\s]Dixon\s+[Ll]ine\b" replace="Mason–Dixon line"/>
<Typo word="Double pounds" find="(£[0-9\.–]+)((?: |&nbsp;)[mbtr]{1,2}illion| thousand)? pounds\b(?: sterling\b)?" replace="$1$2"/>
<Typo word="Nearby" find="\bnear[- ]by\b(?<=\b(?:[Aa]|[Tt]he|[Ii]n|[Tt]o) near[- ]by)" replace="nearby"/>
<Typo word="Double dollars" find="(\$[0-9\.–]+)((?: |&nbsp;)[mbtr]{1,2}illion| thousand)? dollars?\b" replace="$1$2"/>
<Typo word="Dolce & Gabbana" find="\bDolce\s+(?:(?:e|and)\s+Gabb?an?|& Gab(?:ban|an?))na\b" replace="Dolce & Gabbana"/>
<Typo word="Congregate" find="\b([Cc])ong(?:r?egr|eg|erg)at([a-z]+)\b" replace="$1ongregat$2"/>
<Typo word="Thereafter" find="\b([Tt])h(?:reaft|er[ea]ft|ereat?f)er\b" replace="$1hereafter"/>
<Typo word="Without" find="\b([Ww])h?it?houth?\b(?<![Ww]ithout)" replace="$1ithout"/>
<XXXX word="Mid-" find="\b([Mm]id)\s+(\d{4}s?)\b" replace="$1-$2"/> <!-- disabled -->
<Typo word="-leigh" find="\b(Ray?l|L|[Ss]l)iegh\b" replace="$1eigh"/>
<Typo word="Executive" find="\b([Ee])x(?:cuti|cecuti|ectui?|ecu[ti]|ecti)ve(ly|s)?\b" replace="$1xecutive$2"/>
<Typo word="Granddaughter" find="\b([Gg])ran[-d]+?au[ght]{2,4}er(?<!nddaughter)(s?)\b" replace="$1randdaughter$2"/>
<Typo word="Monstrous" find="\b([Mm])onsteru?ous(ly)?\b" replace="$1onstrous$2"/>
<Typo word="Psychology" find="\b([Pp])(?:[sych]{3,5}[ol]{2,4}|sicholo)g(?<![Pp](?:sych|hyc)olog)(y|ies|ical(ly)?|ists?)\b" replace="$1sycholog$2"/>
<Typo word="called up" find="\bcalled-up(?=\s+(?:to|for|by|since|as|from|on|within|at|again|into|in|during|with)\b)" replace="called up"/>
<Typo word="-century" find="\b(an?\s+\d\d?(?:st|nd|rd|th))\s+century\b" replace="$1-century"/>
<Typo word="Labyrinth" find="\b([Ll])ab[yrin]+th(?<!byrinth)([a-z]*)\b" replace="$1abyrinth$2"/>
<Typo word="Psychedelic" find="\b([Pp])sychadelic(s?)\b" replace="$1sychedelic$2"/>
<Typo word="Pharmacy" find="\b([Pp])h?a(?:[rm]+|ram)[aei]?c(?<![Pp]harmac)(y|ies|ists?|eutic[a-z]+|ologi[cs][a-z]+|ology|op[oeia]+l?|othera[a-z]+)\b" replace="$1harmac$2"/>
<Typo word="(Pro/Re/Intro)duce" find="\b([Pp]ro|[Rr]e|[Ii]ntro)duct(e[ds]?|ing)\b" replace="$1duc$2"/>
<Typo word="Schuylkill" find="\bSchuykill\b" replace="Schuylkill"/>
<Typo word="Sovereign" find="\b([Ss])ove?r[ei]*[gn]+i?(ty|t?is[tm]s?|s?)\b(?<!vereign(?:ty|t?is[tm]s?|s?))" replace="$1overeign$2"/>
<Typo word="(Re/E)volution" find="\b([Rr]e|[Ee])v(?:[olutin]{3,9})n+(?<!volution)(ary|aries|ize[ds]?|s)?\b" replace="$1volution$2"/>
<Typo word="Underground" find="\b([Uu])nd([er]groun|ergoun|ergro[nu])d\b" replace="$1nderground"/>
<Typo word="Elementary" find="\b([Ee])lem(?:ntar|etnar|e[nt]ar|entra?|enter)y\b" replace="$1lementary"/>
<Typo word="Agriculture" find="\b([Aa])(?:g+i?r[ia]?|rgr?i|ri|gi)c+(?:ult[ui]r|u[lt]+ur|lu?tur|ultrur|ult[ru]|ultar|ulutr)(?<![Aa]gricultur)(es?|ists?|ism|ally|alists?|alism|al)\b" replace="$1gricultur$2"/>
<Typo word="Pulitzer" find="\b[Pp]ul(?:tiz|l?itz|izt?)(?<!Pulitz)er\b" replace="Pulitzer"/>
<Typo word="Major" find="\b([Mm])ajour(ity)?\b" replace="$1ajor$2"/>
<Typo word="Subsequent" find="\b([Ss])ub?p?[seu]*q[uent]{2,5}(?:(l)e?(y))?(?<!ubsequentl?y?)\b" replace="$1ubsequent$2$3"/>
<Typo word="Finance" find="\b([Ff])ia?(?:ni?an[ai]?n?|na?)c(e[ds]?|ing|ially|ials?)(?<!iance|inanc(?:e[ds]?|ing|ially|ials?))\b" replace="$1inanc$2"/>
<Typo word="Financial" find="\b([Ff])inan(?:ial|i?cal|cail)(ly)?\b" replace="$1inancial$2"/>
<Typo word="Previously" find="\b([Pp])rei?v(?:[eious]+(?<=s[eiou]*)|iou)e?l+e?y(?<!reviously)\b" replace="$1reviously"/>
<Typo word="Dominican" find="\b[Dd]omini?ci?an(s?)\b(?<!Dominicans?)" replace="Dominican$1"/><!--relig. & geogr.-->
<Typo word="Simultaneous" find="\b([Ss])im[aiu](?:la?t|[lt])(?<!im[ai]t)(?:[aeiount]{3,10}s|aneou)(?:e?(l)e?(y)|)(?<!multaneous|multaneously|imulates|imulations|imulants|imultaneities|milanus)\b" replace="$1imultaneous$2$3"/>
<Typo word="Overwhelm" find="\b([Oo])ver[- ]?wh?el?e?m(?<!verwhelm)(s?|ingly|ing|ed)\b" replace="$1verwhelm$2"/>
<Typo word="Czechoslovakia" find="\b[Cc]zec[a-z]+ak(?<!Czechoslovak)(s?|ian?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Czechoslovak$1"/>
<Typo word="Presidency" find="\b([Pp]?[Rr]esiden)t?ship\b" replace="$1cy"/>
<Typo word="I.B. Tauris" find="\bI\.?\s*B\.?\s+Taurus\b" replace="I.B. Tauris"/>
<Typo word="Dolphin" find="\b([Dd])ophin(s?)\b" replace="$1olphin$2"/>
<Typo word="Croatian" find="\b[Cc]roation(s?)\b" replace="Croatian$1"/>
<Typo word="Missionary" find="\b(M|m)issionair(y|ies)\b" replace="$1issionar$2"/>
<Typo word="Portugal" find="\bPort(gu?a|uag|ugua)l\b" replace="Portugal"/>
<Typo word="Portuguese" find="\bPort(?:gu|ug)ese\b" replace="Portuguese"/>
<Typo word="Barack Obama" find="\bBar(a[ck]|rack)\s*Obama\b" replace="Barack Obama"/>
<Typo word="-ball" find="\b([Bb]asket|[Cc]annon|[Ff]oot|[Hh]and|[Vv]olley)[-\s]+ball(s?)\b" replace="$1ball$2"/>
<Typo word="Alongside" find="\b([Aa])lon(?:[gs]i|g[- ]si|gis)de(?: with)?\b" replace="$1longside"/>
<Typo word="Prospective" find="\b([Pp])erspective\s+((applicant|buyer|client|student)s?)\b" replace="$1rospective $2"/>
<Typo word="Outstanding" find="\b([Oo])u(?:st|tst?)a(?:nd?|d)(?<!utstand)ing(ly)?\b" replace="$1utstanding$2"/>
<Typo word="Mass-produce" find="\b([Mm])ass produc(e[sd]?|ing)\b" replace="$1ass-produc$2"/>
<Typo word="Gunpowder" find="\b([Gg])un[- ]powder\b" replace="$1unpowder"/>
<Typo word="Therapeutic" find="\b([Nn]ont|[Uu]nt|T|t)heraputic(al(ly)?)?\b" replace="$1herapeutic$2"/>
<Typo word="Buccaneer" find="\b([Bb])u(?:c+ann|can+)e+r(s?)\b" replace="$1uccaneer$2"/>
<Typo word="Parameter" find="\b([Pp])aramater([a-z]*)\b" replace="$1arameter$2"/>
<Typo word="Athletic" find="\b([Aa])theltic(s?)" replace="$1thletic$2"/> 
<Typo word="Bombardier" find="\b([Bb])ombadier(s?)\b" replace="$1ombardier$2"/>
<Typo word="McCune–Reischauer" find="\bMcCune-Reischauer\b" replace="McCune–Reischauer"/>
<Typo word="Wade–Giles" find="\bWade-Giles\b" replace="Wade–Giles"/>
<Typo word="Mountainous" find="\b([Mm])ounta(?:i?ne|ne?)ous\b" replace="$1ountainous"/>
<Typo word="Return/Revert" find="\b([Rr])e(turn|vert)(s|ed|ing|\s+it)?\s+back\b" replace="$1e$2$3"/>
<Typo word="Billiard" find="\b([Bb])illard(s?)\b(?<!\bConstance Billard)" replace="$1illiard$2"/>
<Typo word="Presbyterian" find="\b[Pp]resbytarian(s|ism)?\b" replace="Presbyterian$1"/>
<Typo word="Tariff" find="\b([Tt])arrif+(s?)\b" replace="$1ariff$2"/>
<Typo word="(M/P)atriarch" find="\b([MmPp])atriach(s|y|ies|al(?:ism)?|ate|ic|is[mt]s?)?\b" replace="$1atriarch$2"/>
<Typo word="Digital" find="\b([Dd])igi(?:ti)?al(ly)?\b" replace="$1igital$2"/>
<Typo word="En route" find="\b([Ee])n-?route(?=(\.|,|\s+(back|home|in|for|from|through|to|via)\b))" replace="$1n route"/><!-- Avoid [[EnRoute (credit card)]] etc; avoid "Sailing directions (enroute)"; avoid [[En-route chart]]/beacon/frequency/controller/etc -->
<Typo word="Up-and-coming" find="\b([Uu])p and(?<=\b(?:[Tt]he|[Aa]n|[Hh]is|[Hh]er|[Ii]ts|[Tt]heir) up and) coming\b" replace="$1p-and-coming"/>
<Typo word="Ex-" find="\b([Ee])x\s?(husbands?|wi(?:fe|ves)|(?:boy|girl)friends?)\b" replace="$1x-$2"/>
<Typo word="Winston-Salem" find="\bWinston\s+Salem\b" replace="Winston-Salem"/>
<Typo word="KeyArena" find="\bKey\s[Aa]rena\b" replace="KeyArena"/>
<Typo word="Sculpt(ure/or)" find="\b([Ss])cl?u[lpt]{2,4}(?<!culpt|cuttl?|cull)(ure[sd]?|urally|ural|ors?|ed|ing|s?)\b" replace="$1culpt$2"/> <!-- Avoid Scuttls, scuttle, scull -->
<Typo word="Synthesi(s/z)e" find="\b([Ss])[yi](?:nth|th|nt)(?<!ynth)esi([zs](?:er?s?|ed|ing)|s)\b" replace="$1ynthesi$2"/>
<Typo word="Wide range" find="\bwide-range(?= of\b)" replace="wide range"/>
<Typo word="In the" find="\b([Ii])nt\she\b" replace="$1n the"/>
<Typo word="(North/South/East/West)ernmost" find="\b(?:([Nn]orth)|([Ss]outh)|([Ee]ast)|([Ww]est))er(?:n[- ])?most(?=\s(?:part|point|portion|end|of|tip|district)\b)" replace="$1$2$3$4ernmost"/>
<Typo word="Northernmost" find="\bNor(?<=\b[Tt]he Nor)thernmost\b" replace="northernmost"/>
<Typo word="Southernmost" find="\bSou(?<=\b[Tt]he Sou)thernmost\b" replace="southernmost"/>
<Typo word="Easternmost" find="\bEas(?<=\b[Tt]he Eas)ternmost\b" replace="easternmost"/>
<Typo word="Westernmost" find="\bWes(?<=\b[Tt]he Wes)ternmost\b" replace="westernmost"/>
<Typo word="Select" find="\b([Ss])(?:lect|elct)(ions?|ors?|ed|ing|men|s|able|ively|ive)?\b" replace="$1elect$2"/>
<Typo word="Stair-" find="\b([Ss])tair[- ](case|step|way|well)(s?)\b" replace="$1tair$2$3"/>
<Typo word="Unbeknownst" find="\b([Uu])nbe(?:knowst|nown?st)\b" replace="$1nbeknownst"/>
<Typo word="Suspense" find="\b([Ss])u(?:sp|ps?)en[st](?<!uspens)(e|ions?|ory|ive)\b" replace="$1uspens$2"/>
<Typo word="Phospho-" find="\b([Pp])ho(?!spohor\b)(?:spoh?o?|pho)(?!n[iy])([a-z]+)\b" replace="$1hospho$2"/>
<Typo word="Acknowledge" find="\b([Aa])c?kn?o(?:lw?|wl?)e?(?:deg|dg?|gd?)(?<!cknowledg)(e[sd]?|e?ments?|ing|e?able)\b" replace="$1cknowledg$2"/>
<Typo word="Municipal" find="\b([Mm])uni?(?:c[ai]?p[ai]?[ai]?la?l?e?|p[ai]?c[ai]?[ai]?la?l?e?)(?<!nicipal)([ai]?[aei]?t(?:y|es|ies))?(?<!nicipale)\b" replace="$1unicipal$2"/>
<Typo word="Collision" find="\b([Cc])ol+i?s+i?on(?<![Cc]ollision|Collison|Colson)(s?)\b" replace="$1ollision$2"/>
<Typo word="Declare" find="\b([Dd])e(?:lc|cl|c|l)[ae](?<!ecla)r(e[ds]?|ing|ations?)(?<!ecares?)\b" replace="$1eclar$2"/>
<Typo word="Approach" find="\b([Aa])p(?:poa|p?o?r(?:ao?|oa?))ch(?<!pproach)(e[ds]|ing)?\b" replace="$1pproach$2"/><!--doesn't replace "Approaches"-->
<Typo word="Giuseppe" find="\bGuiseppe\s+(Verdi|Garibaldi|Peano|Tartini|Anselmi)\b" replace="Giuseppe $1"/>
<Typo word="Fulbright" find="\bFullbright\s+([Ss]cholar(?:ship)?s?|[pP]rograms?)\b" replace="Fulbright $1"/>
<Typo word="Counter-" find="\bcounter[- ](attack(s|ed|ing)?|parts?|point)(?<!counter-attac[a-z]{1,99})\b" replace="counter$1"/>
<Typo word="Reflect" find="\b([Rr])efele?ct(?!oq)([a-z]*)\b" replace="$1eflect$2"/>
<Typo word="Technology" find="\b([Tt])ech(?:nol|ono?lo?|olo|nalo)g(y|ies|ic|ically|ical|is[mt]s?|ized?)\b" replace="$1echnolog$2"/>
<Typo word="Synonym" find="\b([Ss])yno[nm]+[aioy][mn]+(?<!ynonym)([a-z]*)(?<!ynomones?)\b" replace="$1ynonym$2"/>
<Typo word="Business" find="\b([Bb])ui?s+i?n+i?e+s+([a-z]{0,99})(?<!usiness[a-z]{0,99}|Busnes)\b" replace="$1usiness$2"/><!--Fuzzy rule, extends & completely replaces existing rule of the same name-->
<Typo word="Subsidiary" find="\b([Ss])ubi?si?a?d[iaeu]+(?:ra)?r(?<!bsidiar)(y|ies|ity)\b" replace="$1ubsidiar$2"/><!--extends & completely replaces "Subsidiary"-->
<Typo word="(Un)necessary" find="\b([Uu]n)?([Nn])ec+a?i?e?a?s+[ea]+r+[ae]?(?<![Nn]ecessar)(y|ily)\b" replace="$1$2ecessar$3"/><!--Fuzzy rule, extends & completely replaces existing rule "Unnecessary"-->
<Typo word="Inaugurate" find="\b([Ii])n+a[aeiou]?g+[aeiou]?[aeiou]?r+[eiou]?(?<![Ii]naugur)a(l|tions?|te[ds]?|ting)\b" replace="$1naugura$2"/><!--Fuzzy rule, extends & completely replaces existing rule of the same name-->
<Typo word="Interview" find="\b([Ii])n(?:ter|er|tr|te)(?:view|vew|viw|iew)(?<!nterview)(s?|e[er]s?|ed|ing)\b" replace="$1nterview$2"/>
<Typo word="(Un)Successful" find="\b([Uu]n)?([Ss])u+c+e+s+[aeiou]?f?f?u+(l+)(?<![Ss]uccessful{1,9})(y)?\b" replace="$1$2uccessfu$3$4"/><!--Fuzzy rule, extends & completely replaces existing rule "(Un)Successful"-->
<Typo word="Research" find="\b([Rr])ea?s(?:[aeiu]?[aeiu]?r[aeiou]?ch?|each)(?<![Rr]esearch|[Rr]esura?c)(es|ed|ers?|ing)?\b" replace="$1esearch$2"/><!--Fuzzy rule, extends & completely replaces existing rule "Research"-->
<Typo word="(Dis/Re)Organi(s/z)ation" find="\b([Oo]|[Dd]iso|[Rr]eo)r[aeiou]?g[aeiou]?[aeiou]?n[aeiou]?[aeiou]?([sz])[aeiou]?[aeiou]?ti?(?<!rgani[sz]ati)on(s|ally|al)?\b" replace="$1rgani$2ation$3"/><!--Fuzzy rule, extends & completely replaces existing rule "Organization"-->
<Typo word="so-called_" find="\bso\scalled\b(?<=\b([Aa]|by|of|[Tt]he|[Tt]hese|[Hh]er|[Tt]heir|[Tt]his|[Hh]is)\sso\scalled)" replace="so-called"/><!--don't fix variants of "it is so called because"-->
<Typo word="(At/Con/Dis/Re(dis))Tribute" find="\b([Aa]tt|[Cc]ont|[Dd]ist|[Rr]e(?:dis)t|T|t)t?(?:ribu(ed|ing|es|ion)\b|(?:[aeiou]?r(?:[iu]+)?b(?:[aeiu]+)?t(?<![Tt]ribut|arbat)|ritut)([a-z]+)\b(?<!trubed|buit[aeiou](gli(de)?|le|r)?|buutti|ko[iy]s?|kaya|tax|urbitt?s?|bat(as?|alis|aria|e|ella|ejamae|ia?|ion|or?|rix|um|us)|b[eiou]tt(ite)?|bet(ek|sk[iy]?s?|isonios)|bit(an?|h|kan|o)|but(aline|h|it|r[oy]n|hylazine|ts)|buatur|Attribates|conturbat(ed|um)|disturbator(e|y)|Tarb(et[hs]|iat(e|ul)|it[sz]a?)|Tarbutt(on)?|Terb(aatar|atas|itlah)|Teribithia|Terubetaake|Tor(bateheydarieh|iibata|bi?at[io]|but(rol|ton)|bitch|batross)|Tribat(e|io)|Tribet(ek|t|oo?n|oy)|Tribitch|Trubatch(ov)?|Trubits[iy]na?|Trub(ats?a|itt|eats|et(a|chin(o|sky)|sk(a|oj|ogo)|zin)|tensee|thob|ute)|Turb(at([aiou]|hi|or|rix|ross)|[eu]tt)|Turbet(li|ts)|Turbit(ity|een)))(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1ribut$2$3"/>
<Typo word="Individual*" find="\b([Ii])n[aeiou]?d[aeiou]?[aeiou]?v[aeiou]?[aeiou]?d?[aeiou]?d?[aeiou]?[aeiou]?l(?<!ndevel|ndavl)(?!los|le|es|e\b)[aeou]?(?<!ndividual|ndividuel)([a-z-\']{0,99})" replace="$1ndividual$2"/><!--Fuzzy rule to supplement existing "Individual" rule-->
<Typo word="Self-" find="\b([Ss])elf\s+(?<=\s[Ss]elf\s{1,9})\b(abandon(ed|ment)?|abasement|abnegati(ng|on)|absor(bed|ption)|abuse|accusat(ion|ory)|acting|activ(ity|ating)|actuali[sz](e[ds]?|ation)|addressed|adhesive|adjust(ing|ment)|administ(ered|ering|ers?|ration)|admir(ation|er|ing)|advancement|advertise(r|ment)|adverting|advocacy|affirmation|aggrandi[sz](ement|ing)|alienation|aligning|analy(sis|[sz]ing)|annihilation|appointed|approbation|approv(al|ing(ly)?)|assembl[ey]|asserti(ng|on|ve(ness)?)|assessment|assur(ance|ed|edly)|aware(ness)?|balancing|betrayal|build(er)?|cancell?ing|catering|censorship|cente?red(ly|ness)?|certificat(e|ion)|certify|cleaning|closing|cocking|colou?red|command|compatible|conceit(ed)?|concept|condemn(ation|ed|ing)|confess(ed|edly|ion(al)?)|confiden(ce|t|tly)|congratulat(ion|ory)|conscious(ly|ness)?|consisten(t|cy|tly)|contain(ed|ment)|contempt(uous)?|contradict(ing|ion|ory)|control(led)?|correct(ing|ion|s?)|creat(ed|ing|ion)|critic(al|ism)|deceit|deceiv(er|ing)|decepti(ve|on)|defeating|defen[cs](iv)?e|definition|delight|delusion|den(ial|ying)|dependen(ce|t)|depreci?at(ing|ingly|ion|ory)|despair|destroying|destruct(s?|ion|ive|ively)|determination|development|devotion|diagnose|diffusion|direct(ed|ion|ing)|disciplined?|discovery|disgust|doubt|dramati[sz]ation|drive|educat(ed|ion)|effac(ing(ly)?|ement)|employ(ed|ment)|enclosed|esteem|evaluation|eviden(t|ce|tly)|examination|excited|executing|existent|explanatory|expressi(on|ve)|faced|feed(er|ing)|fertil(e|ity|i[sz]ation|ized|izing)|financ(ed|ing)|flagellation|flatter(ing|y)|forgetful(ness)?|fulfil(ling|l?ment)|generating|glorification|govern(ed|ing|ment)|gravitation|guided|harm(er)?|hate|hatred|help|identi(fication|ty)|image|immolation|importan(ce|t|tly)|imposed|improvement|incompatib(le|ility)|induced|induct(ance|ion|ive)|indulgen(ce|t|tly)|inflicted|insurance|interest(ed)?|involve(d|ment)|justificat(ion|ory)|justifying|knowledge|knowing|limiting|liquidating|load(er|ing)|loathing|locking|love|loving|zzNotzzmadezz|manag(ement|ing)|mastery|medicat(e[ds]?|ion)|mock(ery|ing(ly)?)|mortification|motion|moving|motivat(ed|ing|ion)|murder(er)?|mutilation|neglect|observation|obsess(ed|ion)|opinion(ated)?|parod(ic|y|ying)|perpetuati(ng|on)|pity(ing(ly)?)?|policing|pollinat(ed|ing|ion|or)|portrait(s?|ure)|possess(ed|ion)|praise|preservation|proclaimed|produced|promot(er|ing|ion)|propagat(es?|ing|ion)|propell(ed|ing)|protecti(on|ve)|proving|publish(e[drs])?|ra?ising\sflour|rating|reali[sz]ation|recorded|referen(ce|tial(ity|ly)?)|reflecti(on|ve)|reflexive|regard(ing)?|regulat(ing|ion|ory)|releas(ed?|ing)|relian(ce|t|tly)|renew(al|ing)|renunciation|report|reproach(ful)?|respect(ing)?|restrain(t|ed)|revealing|revelat(ion|ory)|righteous(ly|ness)?|righting|rule|sacrific(e|ial|ing)|satisf(action|ied)|sealing|see[dk](er|ing)?|select(s?|ing|ion)|servi(ce|ng)?|shifter|similar(ity)?|slaughter|sown?|start(er|ing)?|steril(e|ity)|stick|stimulation|storage|styled|subsistent|sufficien(cy|t|tly)|suggestion|support(ing)?|surrender|sustain(ing|ed)|system|tailing|tann(er|ing)|tapping|taught|timer|titled|torture|tracking|transcendence|understanding|zzNotzzwillzz|willed|winding|worth)\b(?!-)" replace="$1elf-$2"/>
<Typo word="Each other's" find="\beach\s+others['’]?(?= )" replace="each other's"/>
<Typo word="Owing to" find="\b([Oo])wning\s+to\b" replace="$1wing to"/>
<Typo word="Piraeus" find="\bPire(?:au?|u)s\b" replace="Piraeus"/>
<Typo word="Rio de Janeiro" find="\b[Rr](i|í)o\s+[Dd]e\s+[Jj]ane?i?e?ro?\b(?<!R(i|í)o de Janeiro)" replace="R$1o de Janeiro"/>
<Typo word="(In|Re)volve_" find="\b([Rr]e|[Ii]n)vovlv?(e[ds]?|rs?|ements?|ing)\b" replace="$1volv$2"/>
<Typo word="Spokes-" find="\b([Ss])poke(m[ae]n|wom[ae]n|persons?|people)\b" replace="$1pokes$2"/>
<Typo word="A to An" find="\b([Aa])  ?([Aa](?!nd\b|AA?T?|s\b|ldo|lguien\b|pagar\b|probat\b|rtelor\b|tahualpa\b|ustriei\b|\b|ED|FN|LL|MD|NG|OA|RS|UD|WG|ZN)[A-Za-z0-9]{0,99}|[Ee](?!u|dil\b|mpezar\b|ncore\b|nse[nñ]ar|ntenderse\b|sa\b|spa[nñ]|st(a\b|é|e\b)|vrop|w[abei]|\b|GP|RN|TB|URO?)[A-Za-z0-9]{0,99}|h(?:aut[besu]|eir|our|ones|onou?r|ors\sd)[A-Za-z0-9]{0,99}|[Ii](?![0-9]|[nst]\b|[IiVvXx]\b|[Ii]|greja|nglat|nstitucí|mmagini\b|ts\b|ure\b|\b|DR|LS|NR|QD|RR|SK)[A-Za-z0-9]{0,99}|[Oo](?!ax|bra|cho|d\b|f\b|ggi|kol[íi]e?\b|[Nn][Cc][Ee]|[Nn][Ee](\b|[A-Fa-fHhJ-Qj-qS-Zs-z0-9]|r[a-np-z])|rfu\b|opa|raşului|ra[sș]ului|ui|MR)[A-Za-z0-9]{0,99}|u(?!b[aio]|[ef]|ga[ln]|in|itz|k|lu|n(\s|:)|na(\b|n|r)|nes|ni([^m]|mo|\b)|[rst][aeiou]|rl\b|v[aeiru]|\b)[a-z]{0,99})(?<=\b[A-Za-z]{2,99}(?<!:|\btoda|\bpara|\b[Ii]nterpreta|\b[Vv]olta|\bva|\bund|\brecibe|\bde|[Vv]eche|\bque|\b[Rr]oi|\b[Ii]l|\scom|\bllevan|\btren|\b[Vv]olver|\be[nst]|\bnous)(?:\.\s?\s[Aa] |\,?\;?\sa ) ?\2)" replace="$1n $2"/><!--'A to An' correction, [[User:Sun_Creator/A_to_An]] document. Occurring often.-->
<Typo word="King Philip's War" find="\bKing Phil(?:lip['’]?s [Ww]|ip’?s [Ww]|ip's w)ar\b" replace="King Philip's War"/>
<Typo word="(Life/Death/Child/Lady/Father)like" find="\b([Ll]ife|[Dd]eath|[Cc]hild|[Ll]ady|[Ff]ather)-like\b" replace="$1like"/><!--but many -like suffixes keep the hyphen-->
<Typo word="Decade apostrophe" find="\b((?:1\d|20)\d0)['’′]s(?<=\b(?:[Aa]n?|[Oo]n|[Tt]he)\s{1,9}(?:later?|earl(?:y|ier)|mid(?:dle)?)?[-\s]{0,9}(?:1\d|20)\d0['’′]s)" replace="$1s"/>
<Typo word="Rebirth/reborn" find="\b([Rr])e-b(irth|orn)\b" replace="$1eb$2"/>
<Typo word="Restart_" find="\b([Rr])e-start(s?|ed|ing)\b" replace="$1estart$2"/>
<Typo word="(Full/Part)-time" find="\b([Ff]ull|[Pp]art)\s?time\b(?![- ]limit)(?<!at full time)" replace="$1-time"/><!-- don't match "at full time" in association football articles -->
<Typo word="UNICEF" find="\bUnicef\b(?<!Sterntale-Unicef)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="UNICEF"/>
<Typo word="Overarching" find="\b([Oo])ver-arching\b" replace="$1verarching"/>
<Typo word="Agency" find="\b([Aa])geng(y|ies)\b" replace="$1genc$2"/>
<Typo word="Adapted/ing" find="\b([Aa])dapat(ed|ing)\b" replace="$1dapt$2"/>
<Typo word="Approximately (expansion)" find="\bapprox(?<=located approx|situated approx)\.?(?=\s)" replace="approximately"/><!--unlikely to be in small spaces-->
<Typo word="Approx." find="\b([Aa])prox\.?(?=[ \)\n])" replace="$1pprox."/>
<Typo word="Flixster" find="\bFlixter\b" replace="Flixster"/>
<Typo word="Elegiac" find="\b([Ee])legaic\b" replace="$1legiac"/>
<Typo word="(C/W/Sh)ould have (2)" find="\b(c|w|sh)ould\s+(?:had|of)\s+(been|[a-z]+ed)\b" replace="$1ould have $2"/>
<Typo word="August" find="\baugust\s(\d{4}\D|([1-9]|[12]\d|3[01])(,?\s\d{4}\D|(st|[nr]d|th)\D))" replace="August $1"/>
<Typo word="Ma(rch/y)" find="\bma(rch|y)\s(\d{4}\D|[1-3]\d?(,?\s\d{4}\D|(st|[nr]d|th)\D))" replace="Ma$1 $2"/>
<Typo word=" ," find=" +,(?<=[A-Za-z0-9\)] +,)\s?" replace=", "/><!--change space before comma to space after comma, for eventual move to punctuation section-->
<Typo word=",," find="\s?,\s?\s?,\s?" replace=", "/><!--fixes double commas-->
<Typo word="n00" find="\b(\d{1,2})(00)[- ][Hh]undred(s)?(?!\s?euro)\b" replace="$1$2$3"/><!--fix "400 hundred men", "in the 1600 hundreds"-->
<Typo word="Wrongdoing" find="\b([Ww])rong[- ]doing(s)?\b" replace="$1rongdoing$2"/>
<Typo word="Carriage" find="\b([Cc])arr?age((e?|[Ww](ay|ork))s?)\b" replace="$1arriage$2"/>
<Typo word="Arch(a)eology" find="\b([Aa])rche?(a?)[eol]{1,6}go?(?<!ha?eolog)(y|ically|ical|ists?)\b" replace="$1rch$2eolog$3"/>
<Typo word="Psychiatry" find="\b([Pp])s(?:y|i)ch?(?:i|a|ai)tr([a-z]*)\b(?<!Psycatron)" replace="$1sychiatr$2"/><!--Not Psycatron-->
<Typo word="Fare(s) well" find="\bfair(s)? (well|so well|poorly|better)\b" replace="fare$1 $2"/>
<Typo word="Far(ed|ing) well" find="\bfair(ed|ing)\s+((?:as|so) well|well|poorly|better)\b" replace="far$1 $2"/>
<Typo word="Umayyad" find="\b(?:Omm?ayy?[aei]|Ummayy?[aei]|Umay[aei]|Umayy[ei])d(s?)\b" replace="Umayyad$1"/>
<Typo word="Frostbite" find="\b([Ff])rost[- ]bit(e|ten)\b" replace="$1rostbit$2"/>
<Typo word="game-winning" find="\bgame\s+winning\s+(goal|hit|home|move|play)\b" replace="game-winning $1"/>
<Typo word="walk-off" find="\bwalkoff\b" replace="walk-off"/>
<Typo word="On board" find="\b([Oo])n-?board(?<!-onboard)(?= the\b| a[nst]?\b| in\b| to\b| with\b| when\b| that\b| for\b|,|\.)" replace="$1n board"/><!--see talk page 23 July 2012-->
<Typo word="High-ranking officials" find="\b([Hh])igh(?<![Vv]ery high)(est|er)? rank(ing|ed) (officials?|officers?|military|members?)\b" replace="$1igh$2-rank$3 $4"/>
<Typo word="Skyrocket" find="\b([Ss])ky[- ]rocket(ed|ing)\b" replace="$1kyrocket$2"/>
<Typo word="Grief-stricken" find="\b([Gg])rief stricken\b" replace="$1rief-stricken"/>
<Typo word="Liv Ullmann" find="\bLiv\s+Ull?man\b" replace="Liv Ullmann"/>
<Typo word="Overdevelopment" find="\b([Oo])ver-develop(ed|ment)\b" replace="$1verdevelop$2"/><!--do not change 'under-development'-->
<Typo word="War of Jenkins' Ear" find="\bWar of Jenkin(?:[’']s|s[’]?) Ear\b" replace="War of Jenkins' Ear"/>
<Typo word="Spearhead" find="\b([Ss])pear[- ]head(ed|ing)\b" replace="$1pearhead$2"/><!--but 'spear head' might be a noun-->
<Typo word="(Pre/Re/Un)Format" find="\b([Ff]|[Pp]ref|[Rr]ef|[Uu]nf)omat(?!\s?[Mm]artin)(t?(able|anks?|ed?|ers?|s?(ky|kii)|ings?|ion(\b|als?|s)|iv(e|ely|es|ity)|or(y|ies)|s?))" replace="$1ormat$2"/><!--don't match MŠK Fomat Martin-->
<Typo word="(Working/upper/middle/lower)-class" find="\b([Ww]orking|[Uu]pper|[Mm]iddle|[Ll]ower)\s+class\s+(neighbou?rhoods?|famil(y|ies)|people|homes|backgrounds?)\b" replace="$1-class $2"/> 
<Typo word="(Upper/lower)-middle-class" find="\b([Uu]pp|[Ll]ow)er\s+middle-class\s+(neighbou?rhoods?|famil(y|ies)|people|backgrounds?)\b" replace="$1er-middle-class $2"/> 
<Typo word="Postscript" find="\b([Pp])ostcript\b" replace="$1ostscript"/> 
<Typo word="Counterbalance" find="\b([Cc])ounter[- ]balanc(e[ds]?|ing)\b" replace="$1ounterbalanc$2"/> 
<Typo word="A cappella" find="\b([Aa])(?: ca|cap|ca)pella\b(?= group| version | choir| singing| chorus)" replace="$1 cappella"/> 
<Typo word="Outside" find="\b([Oo])utisde\b" replace="$1utside"/> 
<Typo word="Anjelica Huston" find="\bAn(?:gelica Ho?|jelica Ho)uston\b" replace="Anjelica Huston"/> 
<Typo word="Sam Elliott" find="\bSam Elliot\b" replace="Sam Elliott"/> 
<Typo word="Gregg Allman" find="\bGreg Allman\b" replace="Gregg Allman"/> 
<Typo word="Kirsty MacColl" find="\bKirsty M(?:c[Cc]?|acc)oll\b" replace="Kirsty MacColl"/> 
<Typo word="Shane MacGowan" find="\bShane M(?:c[Gg]|acg)owan\b" replace="Shane MacGowan"/> 
<Typo word="Ramsay MacDonald" find="\bRamsay M(?:c[Dd]|acd)onald\b" replace="Ramsay MacDonald"/> 
<Typo word="Jean-Claude Van Damme" find="\bJean(?: Claude [Vv]|-Claude v)an Damme\b" replace="Jean-Claude Van Damme"/> 
<Typo word="Midsection" find="\b([Mm])id[- ]section(s)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1idsection$2"/> 
<Typo word="Lifelong" find="\b([Ll])ife[- ]long(?!(evity|\s?\-?(ago\b|since|gone|before|lived|after)))\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1ifelong"/> 
<Typo word="Disease" find="\b([Dd])iesease([ds])?\b" replace="$1isease$2"/> 
<Typo word="de' Medici" find="\b(Catherine|Cosimo|Lorenzo|Marie) de(?:` ?| |')Medici\b" replace="$1 de' Medici"/>
<Typo word="Fireplace" find="\b([Ff])ire[- ]place(s)?\b" replace="$1ireplace$2"/> 
<Typo word="Midpoint" find="\b([Mm])id[- ]point(s)?\b" replace="$1idpoint$2"/> 
<Typo word="Johnny Hallyday" find="\bJohnny Halliday\b" replace="Johnny Hallyday"/> 
<Typo word="Buttress" find="\b([Bb])utress(e[ds]|ing)?\b" replace="$1uttress$2"/>
<Typo word="Birthplace" find="\b([Bb])irth[- ]place\b" replace="$1irthplace"/>
<Typo word="Privately" find="\bprivately-(?<= is a privately-)" replace="privately "/>
<Typo word="Lifetime" find="\b((?:[Dd]uring|[Ii]n)\s*(?:his|her|its|their))\s*life[-\s]+time\b" replace="$1 lifetime"/>
<Typo word="Lifetime" find="\b([Ll])ife[-\s]+time\s*((?:[Aa])chievement|[Bb]an|[Mm]ember)\b" replace="$1ifetime $2"/>
<Typo word="Atlanta Journal-Constitution" find="\bAtlanta(?:-Journal(?: and |-| )| Journal(?: and)? )Constitution\b" replace="Atlanta Journal-Constitution"/>
<Typo word="GeoCities" find="\b[Gg]eocit(?<!\S[Gg]eocit)(?:ie|i|e)s(\S?\s)" replace="GeoCities$1"/>
<Typo word="Governed" find="\b([Gg])overen(ed|s|ing|ment|ors|or)\b" replace="$1overn$2"/>
<Typo word="Phillip ..." find="\bPhilip (Noyce|Schofield|Whitehead)\b" replace="Phillip $1"/>
<Typo word="Edmund Hillary" find="\bEdmund Hilary\b" replace="Edmund Hillary"/>
<Typo word="Hilary" find="\bHillary\s+(Swank|Duff)\b" replace="Hilary $1"/>
<Typo word="Merge(d/s/ing)" find="\b([Mm])erg(e[ds]?|ing) together\b" replace="$1erg$2"/>
<Typo word="Uilleann pipes" find="\b(U|u)il(?:eann?\s+[Pp]|lean\s+[Pp]|leann\s+P)ipes\b" replace="$1illeann pipes"/>
<Typo word="Purported" find="\b([Pp])roport(edly|s|ed|ing)\b" replace="$1urport$2"/><!--don't match Proport (a business term)-->
<Typo word="B'nai B'rith" find="\bB(?:’?[Nn]ai\s+B[’']?|'Nai\s+B[’']?|'nai\s+B’?)rith\b" replace="B'nai B'rith"/>
<Typo word="MacMillan" find="\b(James|Kenneth) Macmillan\b" replace="$1 MacMillan"/>
<Typo word="Harold Macmillan" find="\bHarold MacMillan\b" replace="Harold Macmillan"/>
<Typo word="André de Toth" find="\bAndr(?:e\s+[Dd]e\s?[Tt]|é\s+De\s?[Tt]|é\s+de[Tt])oth\b" replace="André de Toth"/>
<Typo word="Rodgers and" find="\bRogers (?:and|&) (Hammerstein|Hart)\b" replace="Rodgers and $1"/>
<Typo word="Frank De Vol" find="\bFrank\s+(?:de\s?[Vv]|De[Vv]|De\s+v)ol\b" replace="Frank De Vol"/>
<Typo word="Gene de Paul" find="\bGene\s+(?:De\s?[Pp]|de[Pp]|de\s+p)aul\b" replace="Gene de Paul"/>
<Typo word="Frederick Law Olmsted" find="\bFrederick Law Olmstead\b" replace="Frederick Law Olmsted"/>
<Typo word="Shelley Winters" find="\bShelly Winters\b" replace="Shelley Winters"/>
<Typo word="Humphrey Lyttelton" find="\bHumphrey Lyttleton\b" replace="Humphrey Lyttelton"/>
<Typo word="Erroll Garner" find="\bErrol Garner\b" replace="Erroll Garner"/>
<Typo word="Benny Andersson" find="\bBenny Anderson\b" replace="Benny Andersson"/>
<Typo word="Björn Ulvaeus" find="\bBjorn Ulvaeus\b" replace="Björn Ulvaeus"/>
<Typo word="Glenn Miller" find="\bGlen Miller\b" replace="Glenn Miller"/>
<Typo word="Bryan Ferry" find="\bBrian Ferry\b" replace="Bryan Ferry"/>
<Typo word="Mathematician" find="\b(M|m)athemetician(s?)\b" replace="$1athematician$2"/>
<Typo word="Hans Christian Andersen" find="\bHans Christian Anderson\b" replace="Hans Christian Andersen"/>
<Typo word="Walter de la Mare" find="\bWalter (?:De ?[Ll]|de ?L)a ?Mare\b" replace="Walter de la Mare"/>
<Typo word="Lloyd's of London" find="\bLloyds of London\b" replace="Lloyd's of London"/>
<Typo word="TransPennine Express" find="\bTranspennine Express\b" replace="TransPennine Express"/>
<Typo word="King's Lynn" find="\bKings Lynn\b" replace="King's Lynn"/>
<Typo word="Poets' Corner" find="\bPoet(?:[’']s[’']?|s[’]?) Corner\b" replace="Poets' Corner"/>
<Typo word="British Columbia" find="\bBritish Colombia\b" replace="British Columbia"/>
<Typo word="Leonardo da Vinci" find="\bLeonardo\s+(?:D[ea] ?[Vv]|de [Vv]|da[Vv]|da v)inci\b" replace="Leonardo da Vinci"/>
<Typo word="well received" find="\b([Ww])ell-received\b(?=\.| by\b| in\b| at\b)" replace="$1ell received"/>
<Typo word="Apostles' Creed" find="\bApostle(?:[’']s[’']?|s[’]?) Creed\b" replace="Apostles' Creed"/>
<Typo word="Peasants' Revolt" find="\bPeasant(?:[’']s[’']?|s[’]?) Revolt\b" replace="Peasants' Revolt"/>
<Typo word="Years' War" find="\b(Seven|Nine|Ten|Thirteen|Thirty|Sixty|Eighty|Hundred) (?:year[’']?s[’']? [Ww]|Year[’']s[’']? [Ww]|Years[’]? [Ww]|Years' w)ar\b" replace="$1 Years' War"/>
<Typo word="sneak peek" find="\b([Ss])neak\s+peak\b" replace="$1neak peek"/>
<Typo word="Twitter" find="\btwitter(?=\s+(accounts?|feeds?|hashtags?|pages?|profiles?|sites?|that)\b)" replace="Twitter"/>
<Typo word="Prize" find="\b(Peace|Pulitzer)\s[Pp]rice\b" replace="$1 Prize"/><!--don't match Sesame Street character Dr. Nobel Price-->
<Typo word="Volume" find="\b([Vv])olum?ne(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1olume$2"/>
<Typo word="Scarlett Johansson" find="\bScarlet(?:\s+Johann?ss?[oe]|t\s+Johannss?[oe]|t\s+Johans(?:[oe]|se))n\b" replace="Scarlett Johansson"/>
<Typo word="Terence Stamp" find="\bTerrence\s+Stamp\b" replace="Terence Stamp"/>
<Typo word="Wavelength(s)" find="\b([Ww])ave[-\s]+length(s?)\b" replace="$1avelength$2"/>
<Typo word="Stoke-on-Trent" find="\bStoke(?:\s+[Oo]n[- ]|-On[- ]|-on\s+)Trent\b" replace="Stoke-on-Trent"/>
<Typo word="Dom DeLuise" find="\bDom\s+(?:de\s?[Ll]|De\s[Ll]|Del)o?uise\b" replace="Dom DeLuise"/>
<Typo word="Cecil B. DeMille" find="\bCecil B\.\s+(?:de\s?[Mm]|De\s+[Mm]|Dem)ille\b" replace="Cecil B. DeMille"/>
<Typo word="Ellen DeGeneres" find="\bEllen\s+[Dd][ei]\s?gener[ei]s\b" replace="Ellen DeGeneres"/>
<Typo word="Leonardo DiCaprio" find="\bLeonardo\s+(?:d[ei] ?[Cc]|De\s?[Cc]|Di\s+[Cc]|Dic)aprio\b" replace="Leonardo DiCaprio"/>
<Typo word="Robert De Niro" find="\bRobert\s+(?:de\s?[Nn]|De[Nn]|De\s+n)iro\b" replace="Robert De Niro"/>
<Typo word="Danny DeVito" find="\bDanny\s+(?:de\s?[Vv]|De\s+[Vv]|Dev)ito\b" replace="Danny DeVito"/>
<Typo word="Wisden Cricketers' Almanack" find="\bWisden\s+Cricketer(?:s’?\s+Almanack?|[’']?s\s+Almanack?|s'\s+Almanac)\b" replace="Wisden Cricketers' Almanack"/>
<Typo word="Duckworth–Lewis method" find="\bDuckworth(?:[-\/\s]Lewis [Mm]|–Lewis M)ethod\b" replace="Duckworth–Lewis method"/>
<Typo word="Day-Lewis" find="\b(Daniel|Cecil|C\.?)\s+Day\s+Lewis\b" replace="$1 Day-Lewis"/>
<Typo word="Billie Holiday" find="\bBill(?:y\s+Hol?|ie\s+Hol)liday\b" replace="Billie Holiday"/>
<Typo word="Ludwig van Beethoven" find="\bLud(?:vig\s+[Vv][ao]|wig\s+V[ao]|wig\s+[Vv]o)n\s+Beethoven\b" replace="Ludwig van Beethoven"/>
<Typo word="fellow_" find="\bfellow\s+((?:band|class|crew|team)\s?mates?|colleagues?|compatriots?|comrades?|co\s?workers?)\b" replace="$1"/>
<Typo word="a cappella" find="\ba-?cap*el*a\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="a cappella"/><!--don't match Acappella (multiple meanings)-->
<Typo word="House fire" find="\b([Hh])ousefire(s?)\b" replace="$1ouse fire$2"/>
<Typo word="Tess of the d'Urbervilles" find="\bTess of the (?:D['`]?[Uu]r?ber?|d['`]?ur?ber?|d['`]?Uber?|d['`]?Urbe)villes\b" replace="Tess of the d'Urbervilles"/>
<Typo word="Thomas De Quincey" find="\bThomas\s+(?:de\s*Quince?|DeQuince?|De\s+Quinc)y\b" replace="Thomas De Quincey"/>
<Typo word="Daphne du Maurier" find="\bDaphne\s+Du\s*Maurier\b" replace="Daphne du Maurier"/>
<Typo word="Barbra Streisand" find="\bBarb[ae]ra Str[ae]?ie?sand\b" replace="Barbra Streisand"/>
<Typo word="U.S. News & World Report" find="\b((?:U\.?\s?S\.?\s?)News and World [Rr]eports?|(?:US |U\. ?S\.)News & World [Rr]eports?|(?:US |U\. ?S\.)News (?:and|&) World [Rr]eports)\b" replace="U.S. News & World Report"/>
<Typo word="Deliver" find="\b([Dd])eli?ever(ing|y|ies|ed|s?|ance)\b" replace="$1eliver$2"/>
<Typo word="Makeshift" find="\b([Mm])ake-shift\b" replace="$1akeshift"/>
<Typo word="-name" find="\b([Mm]is|[Rr]e|[Uu]n)-nam(e[ds]?|ing)\b" replace="$1nam$2"/>
<Typo word="Upcoming" find="\b(an|his|her|its|the|their)\s+up\s+coming\b" replace="$1 upcoming"/><!--do not match end(ed|s)/wound up coming-->
<Typo word="Throughout" find="\b([Tt])hrough[- ]out\b(?!-| of\b)" replace="$1hroughout"/>
<Typo word="Highlight" find="\b([Hh])iglight(s?|ed|ing)\b" replace="$1ighlight$2"/>
<Typo word="Analogous" find="\b([Aa])n(?:(?:n?al|nal?)l[ao]?|ala?)ge?(y|ies|ous)\b" replace="$1nalog$2"/>
<Typo word="-formation" find="\b([DdRr]e|[Ii]n|[Tt]rans)(?:ofra?mati|foramti|formaiti?)(on(al|s?)|ve(ly)?)\b" replace="$1formati$2"/>
<Typo word="Morocco" find="\b([Mm])or(?:roc?|o)c(o|ans?)\b" replace="$1orocc$2"/>
<Typo word="Boyz II Men" find="\bBoy(?:s\s+(?:II|2|to|11)|z\s+(?:2|to|11))\s+Men\b" replace="Boyz II Men"/> 
<Typo word="Bone Thugs-n-Harmony" find="\bBone\s+Thugs(\s+[Nn]\s+|-N-]|\s+and\s+)Harmony\b" replace="Bone Thugs-n-Harmony"/> 
<Typo word="Liza Minnelli" find="\bLiza\s+Minelli\b" replace="Liza Minnelli"/>
<Typo word="Honorary" find="\b([Hh])onar(?:ar)?y\b" replace="$1onorary"/>
<Typo word="Carl Philipp Emanuel Bach" find="\b(Karl\s+Phill?ipp?\s+Emm?ann?uell?|Carl\s+Phillipp?\s+Emm?ann?uell?|Carl\s+Phill?ip\s+Emm?ann?uell?|Carl\s+Phill?ipp?\s+Emmann?uell?|Carl\s+Phill?ipp?\s+Emm?annuell?|Carl\s+Phill?ipp?\s+Emm?ann?uell)\s+Bach\b" replace="Carl Philipp Emanuel Bach"/>
<Typo word="-ency" find="\b([Aa]g|[Tt]end)anc(y|ies)\b" replace="$1enc$2"/>
<Typo word="Yiddish" find="\byiddish\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Yiddish"/>
<Typo word="Postpone" find="\b([Pp])ost[-\s][Pp]on(e[ds]?|ing)\b" replace="$1ostpon$2"/>
<Typo word="Huguenot" find="\bHugenot(s?)\b" replace="Huguenot$1"/>
<Typo word="Usage" find="\b([Uu])seage(s?)\b" replace="$1sage$2"/>
<Typo word="Congregate" find="\b([Cc])ongregat(e[ds]?|ing)\s+together\b" replace="$1ongregat$2"/>
<Typo word="-cycle (2)" find="\b([Bb]|tr|[Uu]n|[Ee]p)yc[iy]cl(e(?:d|s|rs?|like|)|i(?:c|ng|sts?))\b" replace="$1icycl$2"/><!--excludes Trycycle musician-->
<Typo word="Anniversary" find="\b([Aa])n(?:(?:ive|nnive|niva)rsa|n?iverse|nive[rs]a)r(y|ies)\b" replace="$1nniversar$2"/>
<Typo word="Collaborate" find="\b([Cc])ol(?:(?:abor+|l?aber+|labo)at([a-z]+)(?:\stogether)?|laborat([a-z]+)\stogether)\b" replace="$1ollaborat$2$3"/>
<Typo word="People en Español" find="\bPeople\s+(?:[Ee]n\s+[Ee]span|En\s+[Ee]spañ|en\s+españ)ol\b" replace="People en Español"/>
<Typo word="Mombasa" find="\bMombassa\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mombasa"/>
<Typo word="Dar es Salaam" find="\bDar(?:[- ]+Es[- ]+|-es-)[Ss]alaa?m\b" replace="Dar es Salaam"/>
<Typo word="Kingdom" find="\b([Kk])indgom(s)?\b" replace="$1ingdom$2"/>
<Typo word="Mediterranean" find="\b([Mm])ed(?:[eai]t+er?)ra(?:i?n[iea]{1,2})n\b(?<!iterranean)" replace="$1editerranean"/>
<Typo word="Kingston upon Thames" find="\bKingston(?:[- ]+(?:Upon|[Oo]n)[- ]+|-upon-)Thames\b" replace="Kingston upon Thames"/>
<Typo word="Newcastle upon Tyne" find="\bNewcastle(?:[- ]+(?:Upon|[Oo]n)[- ]+|-upon-)Tyne\b" replace="Newcastle upon Tyne"/>
<Typo word="Renaissance" find="\b([Rr])en(nais|n?ai)sance\b" replace="$1enaissance"/>
<Typo word="(De/Pre)scri(be/ption)" find="\b([Dd]|[Pp]r)(?:es[cr]|escri|ecr|iscr)i(be[ds]?|bing|ptions?)\b" replace="$1escri$2"/>
<Typo word="Family" find="\b([Ff])(?:imily|amilly|amiliy)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1amily"/>
<Typo word="Families" find="\b([Ff])(amilesl|imilies|amillies)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1amilies"/>
<Typo word="Straightforward" find="\b([Ss])traight-forward(ly)?\b" replace="$1traightforward$2"/>
<Typo word="VHS" find="\b[Vv]hs\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="VHS"/>
<Typo word="Citizen" find="\b([Cc])it(?:ze|izie|iza)n(ship|ry|s?)\b" replace="$1itizen$2"/>
<Typo word="Tagalog" find="\btagalog\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tagalog"/>
<Typo word="Franco" find="\bfranco\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Franco"/>
<Typo word="Their own" find="\b([Tt])here\sown\b" replace="$1heir own"/>
<Typo word="Procter & Gamble" find="\bProctor\s?(:?\&|and)\s?Gamble\b" replace="Procter & Gamble"/>
<Typo word="Tuareg" find="\bTaureg\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tuareg"/>
<Typo word="filmmak(er/ing)" find="\bfilmak(ers?|ing)\b" replace="filmmak$1"/><!--did not include "Filmaker", which could be "Filemaker"-->
<Typo word="(best/well) known" find="\b([Bb]est|[Ww]ell)-known(?<!the (?:best|well)-known)(?= for\b| as\b| by\b| in\b)" replace="$1 known"/>
<Typo word="_(forced/used) to" find="\b((?:am|are|is|was|were)(?:\s+not|n['’′]t)?)\s+(force|use)\s+to\b" replace="$1 $2d to"/>
<Typo word="_(ex/op/pro)posed to" find="\b((?:am|are|is|was|were)(?:\s+not|n['’′]t)?)\s+(ex|op|pro)pose\s+to\b" replace="$1 $2posed to"/>
<Typo word="Istanbul" find="\bInstan?bul\b" replace="Istanbul"/>
<Typo word="X-Men" find="\b[Xx]-?men\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="X-Men"/>
<Typo word="Walgreens" find="\bWalgreen[’′']s\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Walgreens"/>
<Typo word="Port-au-Prince" find="\bPort(?: [aA]u[ -]|-Au[ -])Prince\b" replace="Port-au-Prince"/>
<Typo word="(Dis/Re)Organi(s/z)e" find="\b([Oo]|[Dd]iso|[Rr]eo)(?:rgan|rgi?ni|grani)([sz])(e[ds]?|ing|ation(s?|al))\b" replace="$1rgani$2$3"/>
<Typo word="Respectively" find="\b([Rr])espectivley\b" replace="$1espectively"/>
<Typo word="-par(ed/ing)" find="\b([Cc]om|[Pp]re)pair(ed|ing)\b" replace="$1par$2"/><!--don't match Compair, proper name-->
<Typo word="-pares" find="\b([Cc]om|[Pp]re)pairs\b" replace="$1pares"/><!--don't match Compair, proper name-->
<Typo word="-cipality" find="\b([Mm]uni|[Pp]rin)ci?pal[aei]?t(?:i?t?(ies)|(e)(i)(s)|[ei]?t?(y))(?<!cipalit(?:ies|y))\b" replace="$1cipalit$2$4$3$5$6"/>
<Typo word="Commun-" find="\b(?!Comunal\b)([Cc])om(?:un|m?unn|m?unn?t)(al(?:ly|)|i(?:ons?|s[mt]s?|t(?:y|ies)))\b" replace="$1ommun$2"/><!--don't match Comunal, place name-->
<Typo word="-unity" find="\b([Cc]omm|[Dd]is|[Ii]m[mp])untiy\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1unity"/>
<Typo word="Stonemason" find="\b([Ss])tone[-\s]mason(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1tonemason$2"/>
<Typo word="Improve" find="\b([Ii])mporv(e[ds]?|ing)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1mprov$2"/>
<Typo word="Modifie(d/r/s)" find="\b([Mm])odife([ds]|rs?)\b" replace="$1odifie$2"/>
<Typo word="Inheritance" find="\b([Ii]nher)[aei]te(nces?)\b" replace="$1ita$2"/>
<Typo word="Inherit(s/ance/ed)" find="\b([Ii]nher)et(s?|ances?|ed|ing)\b" replace="$1it$2"/>
<Typo word="Still lifes" find="\b([Ss])till-lifes\b" replace="$1till lifes"/><!--don't match "still life" (e.g. "still-life artist")-->
<Typo word="Colleg-" find="\b([Cc])oleg(es?|iate)\b" replace="$1olleg$2"/>
<Typo word="DVD" find="\b[Dd]vd(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="DVD$1"/>
<Typo word="Minister" find="\b((?:[Pp]rime|[Cc](?:abinet|hief)|[Dd]efen[cs]e|[Ff](?:oreign|inance))\s+[Mm])inster(s?)\b" replace="$1inister$2"/>
<Typo word="(O)possum" find="\b([Oo]?p|P)(?:p?oss?o|poss?u|p?osu)m(|u?s|woods?|ons?)\b" replace="$1ossum$2"/>
<Typo word="Aborigine" find="\b([Aa])bor(?:gi|ig)ni?(al|es?)\b" replace="$1borigin$2"/>
<Typo word="Appeared" find="\b([Aa]|[Dd]isa|[Rr]ea)ppeard\b" replace="$1ppeared"/>
<Typo word="-tain" find="\b([Aa]bs|[Bb]ri|[Cc](?:ap|hief|on)|(?:[Aa][ps]|[Uu]n)?[CcPp][eu]r|[FfMm]oun|[Mm]ain)t(?:ain[ai]|ian[ai]?)(s?|ed|ing|[clt]y|ties|ous)\b" replace="$1tain$2"/><!--don't find proper name Detian-->
<Typo word="United States" find="\bUnited\s+Stated\b" replace="United States"/>
<Typo word="Hillary Clinton" find="\bHilary(\s+Rodham)?\s+Clinton\b" replace="Hillary$1 Clinton"/>
<Typo word="Supposed to" find="\b((?:am|are|is|was|were)(?:\s+not|n['’′]t)?)\s+suppose\s+to\b" replace="$1 supposed to"/>
<Typo word="Stalwart" find="\b([Ss])tal(?:lwa|we)rt(s?)\b" replace="$1talwart$2"/>
<Typo word="Corporal" find="\b([Cc])orpral(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1orporal$2"/>
<Typo word="Savvy" find="\b([Ss])aavy\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1avvy"/>
<Typo word="tambourine" find="\btamborine\b" replace="tambourine"/><!--don't find Queensland place "Tamborine"-->
<Typo word="Contiguous" find="\b([Cc])ontingu([a-z]+)\b" replace="$1ontigu$2"/>
<Typo word="Broccoli" find="\b([Bb]ro)(col+|c+oll)i\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1ccoli"/>
<Typo word="Prevail" find="\b([Pp]reva)(?:ill|l)(ed|ing(ly)?)\b" replace="$1il$2"/><!--don't find "Prevale"-->
<Typo word="Melbourne" find="\b[Mm]el+bou(nr?|r)e\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Melbourne"/>
<Typo word="Headquarters" find="\b([Hh])(?:a?ed|ea|ead)[- ]?[Qq]ua(?:rt|tr?)e?r?(?<!eadquarter)(ed|s?)\b" replace="$1eadquarter$2"/>
<Typo word="Invasion" find="\b([Ii])nvassio(ns?)\b" replace="$1nvasio$2"/>
<Typo word="exactly the same" find="\bth(e|is|at|ose)\s+exact\s+same\b" replace="exactly the same"/>
<Typo word="Golem" find="\b([Gg])olle(ms?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1ole$2"/>
<Typo word="Cancel" find="\b([Cc])ancl(l?ed|l?ations?|l?ing)\b" replace="$1ancel$2"/><!--Replace Cancellation below? It seems one or two l's are acceptable-->
<Typo word="A lot" find="\b([Aa])lot\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1 lot"/>
<Typo word="Public (domain/library)" find="\b([Pp])ubic\s*(domain|librar(?:y|ies))\b" replace="$1ublic $2"/>
<Typo word="Herzegovina" find="\b[Hh]erz(?:egovi?ni|agovin)a\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Herzegovina"/>
<Typo word="Landmark" find="\b([Ll])and\s+mar(ks?)\b" replace="$1andmar$2"/>
<Typo word="Nickname" find="\b([Nn])ick[\s\-]+nam(e[ds]?|ing)\b" replace="$1icknam$2"/>
<Typo word="Since then" find="\b([Ss]ince)\s+than\b" replace="$1 then"/>
<Typo word="Aero-" find="\b([Aa])reo(bics?|dromes?|(dynam|mechan|naut)ic(s?|al[a-z]*)|planes?|sols?|space)\b" replace="$1ero$2"/>
<Typo word="Opioid" find="\b([Oo]pi)o(ds?)\b" replace="$1oi$2"/>
<Typo word="Johns Hopkins University" find="\b[Jj]ohn(['′]s)?\s+[Hh]opkins?\s+[Uu]niversity\b" replace="Johns Hopkins University"/>
<Typo word="Recipient" find="\b([Rr]ec)(?:ie|ei?)pien(ts?)\b" replace="$1ipien$2"/>
<Typo word="Annually" find="\b([Aa])n(naull|n?ual+)y\b(?<!nnually)" replace="$1nnually"/>
<Typo word="Centenary" find="\b([Cc])enten(?:e|na)r(y|ies|ians?)\b" replace="$1entenar$2"/>
<Typo word="Commemorate" find="\b([Cc])ome?merat(es?|ed|ing|ions?|ive)\b" replace="$1ommemorat$2"/>
<Typo word="Vice versa" find="\b([Vv])is(?:e|-?a)[\s\-]*versa\b" replace="$1ice versa"/>
<Typo word="Of...descent" find="\b([Oo]f\s+[A-Z][a-z]+(an|ese|ic|ish)\s+de)cs?ent\b" replace="$1scent"/>
<Typo word="Public school" find="\b([Pp])ubic\s*([Ss])[ch]{1,2}o+l\b" replace="$1ublic $2chool"/>
<Typo word="Publication" find="\b([Pp])ubica([a-z]+)\b" replace="$1ublica$2"/>
<Typo word="(In)Conspicuous" find="\b([Ii]nc|C|c)onspici?ous([a-z]*)\b" replace="$1onspicuous$2"/>
<Typo word="Genius" find="\b([Gg])en[io]{2}us\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1enius"/>
<Typo word="Men's" find="\b([Mm])ens'?s?\s+([Bb]as(?:e|ket)ball|[Cc](?:lothing|rew)|[Gg]olf|[Ff]itness|[Hh]ealth|[Jj]ournal|[Ll]acrosse|[Mm]agazine|[Rr]ooms?|[Ss]ports?|[Tt]e(?:ams?|nnis)|and\s+[Ww]omen'?s)\b" replace="$1en's $2"/>
<Typo word="Men's" find="\b([Mm])ens['′’]s?\s+" replace="$1en's "/><!--don't find "mens" without apostrophe (L.); see also "-men's"-->
<Typo word="Jersey" find="\b([Jj])ersy\b" replace="$1ersey"/>
<Typo word="Strasbourg" find="\b([Ss])trassbourg\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1trasbourg"/>
<Typo word="NF-κB" find="\b[Nn][Ff]-?[Kk][Bb]\b" replace="NF-κB"/>
<Typo word="Dairy..." find="\b([Dd])iary\s+(allerg(y|ies)|cattle|council|farm[a-z]*|foods?|milk|products?|Queen)\b" replace="$1airy $2"/>
<Typo word="(In)Different" find="\b(D|d|[Ii]nd)if(?:er?|f[ai]?|ef)rene?([a-z]+)\b" replace="$1ifferen$2"/>
<Typo word="Stomach" find="\b([Ss])t(?:omache|omoch|umach)(s?)\b" replace="$1tomach$2"/>
<Typo word="Qualify" find="\b([Dd]isq|[Uu]nq|Q|q)uai?l+[ia]?f(?<!alif)(y|ies|ied|ying|ications?)\b" replace="$1ualif$2"/>
<Typo word="Qua-...-y" find="\b([Dd]is|E|e|[Uu]n)?([Qq])au(l|nt)[ai]([ft]y|[ft]ies|fied|fying|fications?)\b" replace="$1$2ua$3i$4"/>
<Typo word="Inspection" find="\b([Ii])npect(ors?|ions?)\b" replace="$1nspect$2"/>
<Typo word="Re(tro)spective" find="\b([Rr])e(tro|)pective(ly|s?)\b" replace="$1e$2spective$3"/>
<Typo word="Identi-" find="\b([Ii])ndenti(cal[a-z]*|fy[a-z]*|fi[a-z]+|ty|ties)\b" replace="$1denti$2"/>
<Typo word="Incorporate" find="\b([Ii])ncor(?:o?porta|o?prat|oporat)(e[ds]?|ing|ion)\b" replace="$1ncorporat$2"/>
<Typo word="Etc." find="\b(?:and\s+|)([Ee])(?:tc\b(?<!/etc)([^\.\w])|ct\b\.*)" replace="$1tc.$2"/><!--avoid /etc the Unix file directory-->
<Typo word="Establishment" find="\b(E|e|[Dd]ise)stablishement([a-z]*)\b" replace="$1stablishment$2"/>
<Typo word="Release" find="\b([Rr])el[ae]se([ds])?\b" replace="$1elease$2"/>
<Typo word="Genghis Khan" find="\bGh?[ei]ngh?i[sz]?\s+[Kk]h?ah?n?(?<!Genghis Khan)\b" replace="Genghis Khan"/>
<Typo word="Qur'an" find="\bQ(?:(?:u?[o]r['’`]?a?['’`]?|u['’`]ra?['’`]|u[’`]?ra['’`]|u[’`]?ra?[’`])(?:â|á|ā|aa?)|ur'(?:â|á|ā|aa))n(ic)?\b" replace="Qur'an$1"/><!--not Qaran-->
<Typo word="Guns N' Roses" find="\bGuns(?:[\s-]?['´’]?n['´’]?|[\s-]?['´’]?N[\s-]| ?&|[\s-]?['´’]?N[´’])[\s-]?Roses\b" replace="Guns N' Roses"/>
<Typo word="(S/T)old" find="\b([SsTt])elled\b" replace="$1old"/>
<Typo word="Commedia dell'arte" find="\b([Cc])om+edia\s*[Dd]el+['`′\s]*\s*?[Aa]rte?\b(?<![Cc]ommedia dell'arte)" replace="$1ommedia dell'arte"/>
<Typo word="i.e." find="\bi(?:\.?e|e\.)(['\s,:;\)&-])(?<!\.ie.|'ie')" replace="i.e.$1"/><!--don't generalize to capital Ie; avoid matching website.ie; avoid matching 'ie' used as syllable-->
<Typo word="(1911|Edinburgh) Encyclopædia" find="\b(1911|Edinburgh)\s+[Ee]ncyclop(?:a?e)?dia\b" replace="$1 Encyclopædia"/>
<Typo word="Britannica Online" find="\b[Bb]ri(?:ttan+ic*|t+anic*|t+an+ic)ca+\s+[Oo]nline\b" replace="Britannica Online"/>
<Typo word="Platform" find="\b([Pp])lataform(s?)\b" replace="$1latform$2"/>
<Typo word="Vitamin" find="\b([vV])iramin(s)?\b" replace="$1itamin$2"/>
<Typo word="Website" find="\b([Ww])e(?:b-?(\s*)is|sbi)te(s|)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1eb$2site$3"/>
<Typo word="(Over/Under)Achievement" find="\b(A|a|[Oo]vera|[Uu]ndera)ch(?:e?ie?)v(d|ments?)\b" replace="$1chieve$2"/>
<Typo word="Elliptic(al/ally)" find="\b([Ee])liptic(al(ly)?)?\b" replace="$1lliptic$2"/>
<Typo word="Irreparable" find="\b([Ii])rrep(?:e|ai)rabl([ey])\b" replace="$1rreparabl$2"/>
<Typo word="While" find="\b([Ww])hi(?:el|lle)\b" replace="$1hile"/>
<Typo word="Lantern" find="\b([Ll])atern(s(?<!Laterns))?\b" replace="$1antern$2"/><!--Avoid place name Laterns-->
<Typo word="Newspaper" find="\b([Nn])e[ws]paper(s?|m[ae]n)\b" replace="$1ewspaper$2"/>
<Typo word="In(evi/fla/imi/jec)table" find="\b([Ii])n(evi|fla|imi|jec)tibl(es?|y)\b" replace="$1n$2tabl$3"/>
<Typo word="Of(f) course" find="\b([Oo]f+)course\b" replace="$1 course"/>
<Typo word="(Min/Max/Opt)imum" find="\b([Mm](?:in|ax)|[Oo]pt)i(?:miu?|nu)m(s?)\b" replace="$1imum$2"/>
<!--word="The Earth's" find="\b([Tt])he\s+earth's\b" replace="$1he Earth's"/>  disabled for now-->
<Typo word="Veteran" find="\b([Vv])et(?:a?ra|erea?)n(s?)\b" replace="$1eteran$2"/>
<Typo word="Parishioner" find="\b([Pp]ar)ish[io]ne(rs?)\b" replace="$1ishione$2"/>
<Typo word="Impress" find="\b([Ii])m(?:mpres?|m?pers?|pre)s(e[ds]|i[a-z]+)?\b" replace="$1mpress$2"/><!--avoid impresión etc.--> 
<Typo word="A ... church" find="\b([Aa]n?)\s+(Christian|Protestant|(Roman\s+)?[Cc]atholic|Lutheran|Baptist|Anglican|Methodist|Mormon)\s+Church\b" replace="$1 $2 church"/>
<Typo word="George" find="\bGoerg(e|ian?s?|etown)\b" replace="Georg$1"/><!--don't match "Goerges"-->
<Typo word="The" find="\b[Tt]He([ny]?|irs?|[rs]e|refore)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="The$1"/>
</source>

====New contractions====
:''Per [[WP:CONTRACTION]], the use of contractions is informal and should be avoided.''
<source lang="xml">
<Typo word="-n't" find="\b(([CcWw]|[Ss]h)ould|[Dd](id|o|oes)|[Hh]a(s|d|ve)|[Ww](as|ere))nt\b" replace="$1n't"/><!--don't change cant or wont-->
<!--Typo word="cannot" find="\bcan[’'`]t\b" replace="cannot"/><!--don't change uppercase titles-->
<!--Typo word="will not" find="\bwon[’'`]t\b" replace="will not"/><!--don't change uppercase titles-->
<!--Typo word=" not" find="\b(are|(c|sh|w)ould|d(id|o|oes)|ha([ds]|ve)|is|m(igh|us)t|w(as|ere))n[’'`]t\b" replace="$1 not"/><!--don't change uppercase titles, can't and won't have separate rules-->
<!--Typo word=" are" find="\b(they|w(e|hat|ho)|you)[’'`]re\b" replace="$1 are"/><!--don't change uppercase titles-->
<!--Typo word=" have" find="\b((c|sh|w)ould|they|wh(at|o)|you)[’'`]ve\b" replace="$1 have"/><!--don't change uppercase titles-->
<!--Typo word=" will" find="\b(s?he|they|wh(at|o)|you)[’'`]ll\b" replace="$1 will"/><!--don't change uppercase titles-->
</source>

====New capitalisation====
<source lang="xml">
<Typo word="LP" find="\b(\d{1,2})\s?[Ll][Pp]s?\s((box\s?)?sets?|album)\b" replace="$1-LP $2"/>
<Typo word="USB" find="\busb\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="USB"/>
<Typo word="eBay" find="\b[Ee]bay\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="eBay"/>
<Typo word="PlayStation" find="\b[Pp]laystation(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="PlayStation$1"/>
<Typo word="Islam(ic)" find="\bislam(ics?|is[mt]s?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Islam$1"/><!--No domains or URLs-->
<Typo word="Tamil Nadu" find="\b[Tt]amil\s*[Nn]adu\b(?<!Tamil Nadu)" replace="Tamil Nadu"/>
<Typo word="Indore" find="\bindor(e|eans?|ites?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Indor$1"/>
<Typo word="_Thanksgiving Day" find="\bThanks?giving\s+day\b" replace="Thanksgiving Day"/>
<Typo word="PayPal" find="\b([Pp])ay([Pp])al\b(?<!PayPal)" replace="PayPal"/>
<Typo word="Sufi(sm)" find="\bsufi(s?m?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Sufi$1"/>
<Typo word="Europe" find="\beurope(a(ns?|ni[sz]e[ds]?|ni[sz]ation))?\b" replace="Europe$1"/>
<Typo word="CD" find="\b(\d{1,2})\s?[Cc][Dd]s?\s(([Bb]ox\s?)?[Ss]ets?|album)\b" replace="$1-CD $2"/><!-- don't match cd when it is an abbreviation for candela -->
<Typo word="Sikh(s)" find="\bsikh('?s?'?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Sikh$1"/>
<Typo word="Celtic" find="\bceltic\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Celtic"/><!--Celtic not Celt because of [[Celt (tool)]]-->
<Typo word="Mumbai" find="\bmumbai\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mumbai"/>
<Typo word="MasterCard" find="\b[Mm]aster(?:\s+C|c)ard\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="MasterCard"/>
<Typo word="Anglo" find="\banglo\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Anglo"/>
<Typo word="Swahili" find="\bswahili\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Swahili"/>
<Typo word="Hollywood" find="\bhollywood\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Hollywood"/>
<Typo word="Kannada" find="\bkannada(n?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kannada$1"/>
<Typo word="Allah" find="\ballah\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Allah"/>
<Typo word="Bengal(is)" find="\bbengal(i?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Bengal$1"/>
<Typo word="Bollywood" find="\bbollywood\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Bollywood"/>
<Typo word="Brahmin" find="\bb(rahmins?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="B$1"/>
<Typo word="April Fool('s/s') Day" find="\b[Aa]pril\s+[Ff]ool('s|s')\s+day\b" replace="April Fool$1 Day"/>
<Typo word="April Fools' Day" find="\b[Aa]pril\s+[Ff]ools\s+[Dd]ay\b" replace="April Fools' Day"/>
<Typo word="Fourth of July" find="\b(?:[Ff]o|fou)rth\s+[Oo]f\s+[Jj]uly\b" replace="Fourth of July"/>
<Typo word="Thanksgiving" find="\b([Tt])hans?kgs?iving(s?)\b" replace="$1hanksgiving$2"/>
<Typo word="New Year's Day_" find="\b[Nn]ew\s+[Yy]ear('?s\s+d|s's?\s+[Dd])ay\b" replace="New Year's Day"/><!--avoid band name New Years Day-->
<Typo word="New Year's Eve" find="\b[Nn]ew\s+[Yy]ear('s\s+e|s'?s?\s+[Ee])ve\b" replace="New Year's Eve"/>
<Typo word="Valentine's Day" find="\b[Vv]alentine((s?|s's?)\s+[Dd]|'s\s+d)ay\b" replace="Valentine's Day"/>
<Typo word="Catholic_" find="\bcatholic(s|ism)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Catholic$1"/><!--exclude potential FP catholic-->
<Typo word="Christian" find="\bchristian(s?|i[stz][a-ln-z]+)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Christian$1"/>
<Typo word="Christmas Day" find="\b[Cc]hristmas\s+day\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Christmas Day"/>
<Typo word="Christmas Eve" find="\b[Cc]hristmas\s+eve\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Christmas Eve"/>
<Typo word="Roman Catholic" find="\b(?:Roman(?:-\s*[Cc]|\s*c|[Cc])|roman-?\s*[Cc])at(?:holi?|oli)c([a-z]*)\b" replace="Roman Catholic$1"/>
</source>

====New accents and diacritical marks====
<source lang="xml">
<Typo word="Noël Coward" find="\bNoel Coward\b" replace="Noël Coward"/>
<Typo disabled="Guaraní" find="\bGuarani\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Guaraní"/>
<Typo word="Courage Compétition" find="\bCourage\s+Competition\b" replace="Courage Compétition"/>
<Typo disabled="à la" find="\b(?!ala)(?:[aáa]\s*|à)l[àáa]\b" replace="à la"/><!--disabled, many false positives-->
<Typo word="Janelle Monáe" find="\bJanelle\s+Monae\b" replace="Janelle Monáe"/>
<Typo word="École nationale supérieure des Beaux-Arts" find="\b(?:Ecole [Nn]ationale [Ss]up[eé]rieure des [Bb]eaux[- ][Aa]|École Nationale [Ss]up[eé]rieure des [Bb]eaux[- ][Aa]|École nationale Sup[eé]rieure des [Bb]eaux[- ][Aa]|École nationale superieure des [Bb]eaux[- ][Aa]|École nationale supérieure des beaux[- ][Aa]|École nationale supérieure des Beaux [Aa]|École nationale supérieure des Beaux-a)rts?\b" replace="École nationale supérieure des Beaux-Arts"/>
<Typo word="Roman à clef" find="\b(R|r)oman(s?)[- ]+[aàáAÁÀ][- ]+[Cc]l[eé]f?\b(?<!omans? à clef)" replace="$1oman$2 à clef"/>
<Typo word="Ürümqi" find="\bUrumqi\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ürümqi"/>
<Typo word="Jägermeister" find="\bJae?germeister\b" replace="Jägermeister"/>
<Typo word="Porfirio Díaz" find="\bPorfirio Diaz\b" replace="Porfirio Díaz"/>
<Typo word="Pokémon" find="\b[Pp]ok[eèẽē]'?mon\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Pokémon"/>
<Typo word="Musée" find="\bMusee\s+(de (Cluny|l'Homme)|du L(uxembourg|ouvre)|d'Orsay|Guimet)\b" replace="Musée $1"/>
<Typo disabled="Brasília" find="\bBrasilia\b(?<!(Embraer|EMB 120|Volkswagen|Wésley)\sBrasilia)" replace="Brasília"/>
<Typo word="Luiz Inácio Lula da Silva" find="\bLuiz Inacio Lula da Silva\b" replace="Luiz Inácio Lula da Silva"/>
<Typo word="Hugo Chávez" find="\bHugo\s+Chavez\b" replace="Hugo Chávez"/>
<Typo word="Tabaré Vázquez" find="\bTabare\s+Vazquez\b" replace="Tabaré Vázquez"/>
<Typo word="Perón" find="\b(Juan|Juan Domingo|Isabel|Eva)\s+Peron\b" replace="$1 Perón"/>
<Typo word="Académie française" find="\bAcad(?:[eé]mie\s+[Ff]rancaise?|[eé]mie\s+Fran[cç]aise?|emie\s+[Ff]ran[cç]aise?|[eé]mie\s+[Ff]ran[cç]ais)\b" replace="Académie française"/>
<Typo word="Alain Juppé" find="\bAlain\s+Juppe\b" replace="Alain Juppé"/>
<Typo word="Ancien Régime" find="\bAncien(?:t\s+[Rr][ée]|\s+r[ée]|\s+Re)gime\b" replace="Ancien Régime"/>
<Typo word="Angoulême" find="\bAngouleme\b" replace="Angoulême"/>
<Typo word="Āniwaniwa" find="\bAniwaniwa\b" replace="Āniwaniwa"/>
<Typo word="Bézier" find="\bB[eè]zier(s?)\b" replace="Bézier$1"/>
<Typo word="Brontë(1)" find="\b(Anne|Branwell|Charlotte|Emily|Patrick)\s+Bronte\b" replace="$1 Brontë"/>
<Typo word="Brontë(2)" find="\bBronte\s+([Ss]isters|[Ff]amily)\b" replace="Brontë $1"/>
<Typo word="Chambéry" find="\bChambery\b" replace="Chambéry"/>
<Typo word="Côte ..." find="\bCote\s+(de\s+(?:Beaune|Brouilly|Granit|Nuits)|d['`’](?:Argent|Azur|Opale|Or)|des Landes|Chalonnaise|Fleurie|Saint-Luc|Vermeille)\b" replace="Côte $1"/>
<Typo word="Côte-" find="\bCote-(de-Beaupré|des-Neiges|d['`’](?:Aime|Or)|du-Poivre|Nord|Rôtie|Saint-(?:André|Paul)|Vertu)\b" replace="Côte-$1"/>
<Typo word="Côtes" find="\bCotes\s+(de\s+(?:Bourg|Duras|Gascogne|Toul)|du\s+(?:Rh[ôo]ne|Marmandais|Ventoux))\b" replace="Côtes $1"/>
<Typo word="Côte d'Ivoire" find="\bC(?:ote\s+[Dd]['`’][Ii]|ôte\s+(?:D['`’][Ii]|[Dd][`’][Ii]|[Dd]['`’]i))voire\b" replace="Côte d'Ivoire"/>
<Typo word="Der Freischütz" find="\bDer\s+Freischutz\b" replace="Der Freischütz"/>
<Typo word="Dürrenmatt" find="\bD(?:üren?|ürren|ue?rr?en?)nmatt?\b" replace="Dürrenmatt"/>
<Typo word="Düssel-" find="\b[Dd]ussel(dorf[a-z]*|tal)\b" replace="Düssel$1"/>
<Typo word="É-" find="\bE(c(?:harcon|ollemont|riennes|ueil|ury)|gly|pense|pern(ay|on)|pinay|poye|tampes|tiolles|toges|tréchy|trepy|vreux|vry)\b" replace="É$1"/>
<Typo word="Eugène ..." find="\bEugene\s+(Delacroix|Ionesco|(Marin\s+)?Labiche)\b" replace="Eugène $1"/>
<Typo word="Ferenc Molnár" find="\bFerenc\s+Molnar\b" replace="Ferenc Molnár"/>
<Typo word="Franche-Comté" find="\bFranche(?:\s+Comté|[-\s]+Comte)\b" replace="Franche-Comté"/>
<Typo word="Göttingen" find="\bGottingen\b" replace="Göttingen"/>
<Typo word="Köppen climate classification" find="\b[Kk]oppen\s+climate\s+classification\b" replace="Köppen climate classification"/>
<Typo word="Květa Peschke" find="\bKveta\s+Peschke\b" replace="Květa Peschke"/>
<Typo word="León" find="\b(Castile(-|\s+and\s+)|(Kingdom|Province|Alfonso\s+(III|I?V|IX))\s+of\s+|Juan Ponce de\s+)Leon\b" replace="$1León"/>
<Typo word="Leoš Janáček" find="\bLeos\s+Jan[aàäãǎāăá][cč]ek\b" replace="Leoš Janáček"/>  
<Typo word="Médaille militaire" find="\b(?:M[eèê]dail+e\s+[Mm]|Médail+e\s+M)il+itaire\b" replace="Médaille militaire"/>
<Typo word="Mel Tormé" find="\bMel\s+Torme\b" replace="Mel Tormé"/>
<Typo word="Mérida" find="\bMerida\b" replace="Mérida"/>
<Typo word="Müllerian" find="\b[Mm]ullerian\s+(agene[a-z]*|[Dd]ucts?|hormones?|[Ii]nhib[a-z]+|mimic[a-z]*|tumors?)\b" replace="Müllerian $1"/>
<Typo word="-nçon" find="\b(Ale|Besa)ncon\b" replace="$1nçon"/>
<Typo word="Neue Zürcher Zeitung" find="\bNeue\s+Zurcher\s+Zeitung\b" replace="Neue Zürcher Zeitung"/>
<Typo word="Nîmes" find="\bNimes\b" replace="Nîmes"/>
<Typo word="Nuevo León" find="\bNuevo\s+Leon\b" replace="Nuevo León"/>
<Typo word="Ōkārito" find="\bOkarito\b" replace="Ōkārito"/>
<Typo word="Pâté" find="\bpaté(s?)\b" replace="pâté$1"/><!-- do not change surname Pate or Paté -->
<Typo word="Périg(ord/(u)eux)" find="\bPerig(ord|u?eux)\b" replace="Périg$1"/>
<Typo word="Provençal" find="\bProvencal\b" replace="Provençal"/>
<Typo word="Querétaro" find="\bQueretaro\b" replace="Querétaro"/>
<Typo word="Saarbrücken" find="\bSaarbrucken\b" replace="Saarbrücken"/>
<Typo word="San Luis Potosí" find="\bSan\s+Luis\s+Potosi\b" replace="San Luis Potosí"/>
<Typo word="Saône" find="\bSaone\b" replace="Saône"/>
<Typo word="Sèvres" find="\bS[ée]vres\b" replace="Sèvres"/>
<Typo word="Süddeutsche Zeitung" find="\bSuddeutsche\s+Zeitung\b" replace="Süddeutsche Zeitung"/>
<Typo word="Teatro Colón" find="\b[Tt]eatro\s+[Cc]olon\b" replace="Teatro Colón"/>
<Typo word="Telefónica" find="\bTelefonica\b" replace="Telefónica"/>
<Typo word="Tübingen" find="\bTubingen\b" replace="Tübingen"/>
<Typo word="Yucatán" find="\bYucatan\b" replace="Yucatán"/>
</source>

===A===
<source lang="xml">
<Typo word="Abandon" find="\b([Aa])(?:dba|bo)ndon+([a-z]*)\b" replace="$1bandon$2"/>
<Typo word="Abbreviate" find="\b([Aa])(?:b+ri|bre)viat([a-z]+)\b" replace="$1bbreviat$2"/>
<Typo word="Aberrant/Aberration" find="\b([Aa])b(?:ber?|e)ra([nt][a-z]+)(?<!Aberangell)\b" replace="$1berra$2"/>
<Typo word="Absence" find="\b([Aa])bs(?:cen[sc]|ens)(es?)\b" replace="$1bsenc$2"/>
<Typo word="Absorb" find="\b([Aa])sb?orb([a-z]*)\b" replace="$1bsorb$2"/>
<Typo word="Absorption" find="\b([Aa])bsorb[st]i(on|ve)\b" replace="$1bsorpti$2"/>
<Typo word="Abyssinia" find="\b[Aa]b(?:ysin?|yssin|bys+in?)nia(ns?)?\b" replace="Abyssinia$1"/>
<Typo word="Academy" find="\b([Aa])c(?:edd?e|cadd?e|c?ada|ad|ada(?=me))m+e?(i[ce]s?|ically|y)\b" replace="$1cadem$2"/>
<Typo word="(Ac/De)celerate" find="\b([Aa]c|[Dd]e)(?:c?el|e)lerat([a-z]+)\b" replace="$1celerat$2"/>
<Typo word="Access_" find="(?!\b[Aa]ces\b)\b(A|a|[Ii]na)(?:ces+|cces(?:ss+)?)([ao]r[a-z]+|e[ds]|ib[a-z]+|ing|ion[a-z]*|ive)?\b" replace="$1ccess$2"/><!--avoid matching aces-->
<Typo word="(In)Accessible" find="\b(A|a|[Ii]na)c+es+ab(l[ey]|ilit(y|ies))\b" replace="$1ccessib$2"/>
<Typo word="Acclaim" find="\b([Aa])claim(ed)?\b" replace="$1cclaim$2"/>
<Typo word="(Un)Acceptable" find="\b(A|a|[Uu]na)c(?:ept?[ai]|c?ept?i|c?epa)bl([ey])\b" replace="$1cceptabl$2"/>
<Typo word="Accession" find="\b([Aa])sc+es+[io]{2}n\b" replace="$1ccession"/>
<Typo word="Acclimatise" find="\b([Aa])c+limiti([sz])(e[ds]?|ing|ation)\b" replace="$1cclimati$2$3"/>
<Typo word="Accommodate" find="\b([Aa])c(?:com[aeo]?|om+[aeo]?|comm[ae]?)dat([a-z]+)\b" replace="$1ccommodat$2"/>
<Typo word="Accompanied" find="\b([Aa])c+ompa(?:i?nn|in+)[iy]?e?([ds])\b" replace="$1ccompanie$2"/>
<Typo word="According" find="\b([Aa])ccorin(g|gly)\b" replace="$1ccordin$2"/>
<Typo word="Accordion" find="\b([Aa])c+ord(?:eo|ia)(ns?)\b" replace="$1ccordio$2"/>
<Typo word="(Un)Account" find="\b(A|a|[Uu]na)cco[un]t(s?|ed|an(ts?|cy)|ing|abl[ey])\b" replace="$1ccount$2"/> 
<Typo word="Accus(e/tom)" find="\b([Aa])c(?:c*us|u)s(e[sdr]?|ing|al|able|ati(on|ve)s?|ator[a-z]*|tom(s?|ed))\b" replace="$1ccus$2"/>
<Typo word="(Over/Under)Achieve" find="\b(A|a|[Oo]vera|[Uu]ndera)ch(?:e?i|eie|iei)v(e[a-z]*|ing|abl[ey])\b" replace="$1chiev$2"/>
<Typo word="Acquire" find="\b([Aa])cq[iu](re[ds]?|ring|siti(ons?|ve(ly)?))\b" replace="$1cqui$2"/>
<Typo word="Acquit" find="\b([Aa])c?quitt+(s?)\b" replace="$1cquit$2"/>
<Typo word="Acquittal" find="\b([Aa])c?qui(?:tt)?t(ed|ing|a(l|nce)s?)\b" replace="$1cquitt$2"/>
<Typo word="Across" find="\b([Aa])c(?:cro|c?or)s[st]\b" replace="$1cross"/>
<Typo word="Actual" find="\b([Aa])cut?al([a-z]*)\b" replace="$1ctual$2"/>
<Typo word="Adaptation" find="\b([Aa])dapa(?:ta)?tion([a-z]*)\b" replace="$1daptation$2"/>
<Typo word="Address" find="\b([Aa])d+res(e[ds]|ing|e[er]s?|ab[il][a-z]+)?\b" replace="$1ddress$2"/>
<Typo word="(In)Adequate" find="\b([Ii]na|A|a)d[ai]?quate(ly)?\b" replace="$1dequate$2"/>
<Typo word="Administer" find="\b([Aa])dmin(?:in?str|ster|inster)(s?|ed|ing)\b" replace="$1dminister$2"/>
<Typo word="Administrate" find="\b([Aa])(?:dmin?s|dminini?s|minis|dmini)trat([a-z]+)\b" replace="$1dministrat$2"/>
<Typo word="Admission" find="\b([Aa])ddmiss?i(ons?|ble|bility)\b" replace="$1dmissi$2"/>
<Typo word="Adopt" find="\b([Aa])(?:ddopt|dop)(s?|ed|i(?:ng|ve|ons?))\b" replace="$1dopt$2"/>
<Typo word="Adultery" find="\b([Aa])dultr(y|ate[ds]?|ati(ng|on)|er|ous)\b" replace="$1dulter$2"/>
<Typo word="Advance" find="\b([Aa])davanc(e[ds]?|ing|ements?)\b" replace="$1dvanc$2"/>
<Typo word="Adventurous" find="\b([Aa])dventrous\b" replace="$1dventurous"/>
<Typo word="Advertise" find="\b([Aa])dvertie?s(r?s?|d|ments?)\b" replace="$1dvertise$2"/>
<Typo word="Advertising" find="\b([Aa])dvertsing\b" replace="$1dvertising"/>
<Typo word="Advocate" find="\b([Aa])dovc?at(e[ds]?|ing|ion|ory?)\b" replace="$1dvocat$2"/>
<Typo word="Aerial" find="\b([Aa])eriel(s?|ly)\b" replace="$1erial$2"/>
<Typo word="Aesthetic" find="\b([Aa])(?:stheti|e?sthetia|e?stheci)c(s?|al|al+y)\b" replace="$1esthetic$2"/>
<Typo word="Affidavit" find="\b([Aa])ffadavit(s?)\b" replace="$1ffidavit$2"/>
<Typo word="Affiliate" find="\b([Aa])f(?:f?ill?|f?illi|ill?i|f?ll?i|f?lili?)at(e[ds]?|ing|ions?)\b" replace="$1ffiliat$2"/>
<Typo word="Afghani" find="\b[Aa]f(?:f?gah?|fgh?a)ni(s?|stan)\b" replace="Afghani$1"/><!--cap. of correct spelling is handled under "Afghanistan"-->
<Typo word="Aficionado" find="\b([Aa])ffici[oa]nad(os?)\b" replace="$1ficionad$2"/>
<Typo word="Aforementioned" find="\b([Aa])for(?:men|e?mem|eme)tioned\b" replace="$1forementioned"/>
<Typo word="Afrikaner" find="\b([Aa])fri[ck]aane(rs?)\b" replace="$1frikane$2"/>
<Typo word="After" find="\b([Aa])f[ft]ter\b" replace="$1fter"/>
<Typo word="Against" find="\b([Aa])g(?:aisn?t|ainnst|ia?nst|aints?)\b" replace="$1gainst"/>
<Typo word="Aggravate" find="\b([Aa])g(?:g?[ae]?re|r[aei])vat([a-z]+)\b" replace="$1ggravat$2"/>
<Typo word="Aggregate" find="\b([Aa])g(?:reg?|g?reg)gat(e[ds]?|ely|ing|ive|or)\b" replace="$1ggregat$2"/>
<!--avoid false positive agregation (professional exam/degree in the French system)-->
<Typo word="Aggression" find="\b([Aa])g(?:g?re|res?)s(ions?|ive[a-z]*|ors?)\b" replace="$1ggress$2"/>
<Typo word="Aggrieve" find="\b([Aa])g(?:rie|g?rei)v(e[ds]?|ing)\b" replace="$1ggriev$2"/>
<Typo word="(Dis)Agree" find="\b(A(?!gre\b)|a|[Dd]isa)g(?:gre+|re|reee)(s?|d|ing|ments?|abl[ey])\b" replace="$1gree$2"/><!--don't fix Agre-->
<Typo word="Air-" find="\b([Aa])r?i(craft|liner?s?|planes?|ports?|space)\b" replace="$1ir$2"/>
<Typo word="Airborne" find="\bairbourne?\b" replace="airborne"/><!--don't fix Airbourne, a band-->
<Typo word="Aircraft" find="\b([Aa])i(?:rc|rrcr)ar?(fts?)\b" replace="$1ircra$2"/>
<Typo word="Albeit" find="\b([Aa])l(?:l?bie|lbei)t\b" replace="$1lbeit"/>
<Typo word="Alcohol" find="\b([Aa])l(?:o?cho|choho|ch?oha|ch?aho)l(s?|ics?|ism)\b" replace="$1lcohol$2"/>
<Typo word="Algorithm" find="\b([Aa])lgorh?itm(s?|ic)\b" replace="$1lgorithm$2"/>
<Typo word="Alienate" find="\b([Aa])lientat(e[ds]?|ing|ion)\b" replace="$1lienat$2"/>
<Typo word="(Mis/Re)Align" find="\b(A|a|[Mm]isa|[Rr]ea)llign(s?|ed|ing|ments?)\b" replace="$1lign$2"/>
<Typo word="All intents and purposes" find="\b([Aa])ll\s+intensive\s+purposes\b" replace="$1ll intents and purposes"/>
<Typo word="Allege" find="\b([Aa])l+edg(e[ds]?|ing|edly)\b" replace="$1lleg$2"/>
<Typo word="Allegedly" find="\b([Aa])l+ed?ge?[ld]e?y\b" replace="$1llegedly"/>
<Typo word="Alleviate" find="\b([Aa])l+iviat(e[ds]?|ing|ion|or)\b" replace="$1lleviat$2"/>
<Typo word="Almost" find="\b([Aa])l(?:mso|oms)t\b" replace="$1lmost"/>
<Typo word="Along with" find="\b([Aa])longwith\b" replace="$1long with"/>
<Typo word="Alpha" find="\b([Aa])plha([a-z]*)\b" replace="$1lpha$2"/>
<Typo word="Already" find="\b([Aa])(?:l+reayd|ready|l+red+y)\b" replace="$1lready"/>
<Typo word="Also_" find="\baslo\b" replace="also"/>
<Typo word="Alternative" find="\b([Aa])lternitive([sly]*)\b" replace="$1lternative$2"/>
<Typo word="Although" find="\b([Aa])l(?:[ht]ought?|thought)\b" replace="$1lthough"/>
<Typo word="Alumni" find="\b([Aa])lumi?nis\b" replace="$1lumni"/> 
<Typo word="Alumnus" find="\b([Aa])lmun(us|ae?|i)\b" replace="$1lumn$2"/>
<Typo word="Alumnus_" find="\b([Aa])lumin(us|ae|i)\b" replace="$1lumn$2"/>
<Typo word="An alumnus of" find="\b([Aa])n?\s+[Aa]lumi?ni\s+of\b" replace="$1n alumnus of"/> 
<Typo word="Always" find="\b([Aa])l+w(?:asy|yas)\b" replace="$1lways"/>
<Typo word="Amalgam" find="\b([Aa])malg[ou]m(s?|at(e[ds]?|ing|ion))\b" replace="$1malgam$2"/>
<Typo word="Amateur" find="\b([Aa])m+(?:[aeiou]tuer|[aeiou]ture|[eiou]teur)([a-z]*)\b" replace="$1mateur$2"/>
<Typo word="Ambidextrous" find="\b([Aa])mbi?dextero?us(ly)?\b" replace="$1mbidextrous$2"/>
<Typo word="Ambiguous" find="\b(A|a|[Uu]na)mbigi?ous(ly|ness)?\b" replace="$1mbiguous$2"/> 
<Typo word="(Ambi/Pre)valent" find="\b([Pp]re|[Aa]mbi)v(?:ela|[ae]la)n([ct][a-z]*)\b" replace="$1valen$2"/>
<Typo word="Amend" find="\b([Aa])dmend(s?|ed|ments?|ing|able|atory)\b" replace="$1mend$2"/>
<Typo word="America" find="\b[Aa]merc?ia(n[as]?|nism)?\b" replace="America$1"/>
<Typo word="Ammunition" find="\b([Aa])m+untio(ns?)\b" replace="$1mmunitio$2"/>
<Typo word="Amock" find="\b([Aa])mock\b" replace="$1mok"/>
<Typo word="Among" find="\b([Aa])mo?un(g|gst)\b" replace="$1mon$2"/>
<Typo word="Amongst" find="\b([Aa])mon(?:ge)?st\b" replace="$1mongst"/>
<Typo word="Amount" find="\b([Aa])mout(s?|ed|ing)\b" replace="$1mount$2"/>
<Typo word="(A/Be)musement" find="\b(A|a|[Bb]e)mus(?:em|me)(nts?)\b" replace="$1museme$2"/>
<Typo word="Anaerobic" find="\b([Aa])nerob(es?|ic[a-z]*)\b" replace="$1naerob$2"/>
<Typo word="Ancestor" find="\b([Aa])nsest[oe](rs?)\b" replace="$1ncesto$2"/>
<Typo word="Ancestry" find="\b([Aa])ncest(?:[oe]r|ri)(y|ies|al)\b" replace="$1ncestr$2"/>
<Typo word="Ancient" find="\b([Aa])(?:cie|ncei)nt(s)?\b" replace="$1ncient$2"/>
<Typo word="Ancillary" find="\b([Aa])ncill?iary\b" replace="$1ncillary"/>
<Typo word="Anemone" find="\b([Aa])nenom(es?)\b" replace="$1nemon$2"/>
<Typo word="Annihilate" find="\b([Aa])n(?:n?i?hili|nhil+)at([a-z]+)\b" replace="$1nnihilat$2"/>
<Typo word="Announcement" find="\b([Aa])n+oun?cmen(ts?)\b" replace="$1nnouncemen$2"/>
<Typo word="Annul" find="\b([Aa])n+ull(s?|ments?|ar)\b" replace="$1nnul$2"/>
<Typo word="Annulled" find="\b([Aa])n(?:nu|ul)l(ed|ing)\b" replace="$1nnull$2"/>
<Typo word="Anoint" find="\b([Aa])nnoint(s?|ed|ings?|ments?)\b" replace="$1noint$2"/>
<Typo word="Anomaly" find="\b([Aa])nom(?:o|al)l(y|ies|ous[a-z]*)\b" replace="$1nomal$2"/>
<Typo word="Antarctic_" find="\b([Aa])ntarti(ca?)\b(?<![Ss]infonia\s{1,9})([Aa])ntarti(ca?)" replace="$1ntarcti$2"/><!--avoid 'Sinfonia antartica'-->
<Typo word="Anthropomorphic" find="\b([Aa])nthromorphi([a-z]+)\b" replace="$1nthropomorphi$2"/>
<Typo word="(Anti/Hypo/Paren)thesis" find="\b([Aa]nti|[Hh]ypo|[Pp]aren)th[ai]s([ie]s|i[sz]e[sdr]?)\b" replace="$1thes$2"/>
<Typo word="Antonín Dvořák" find="\bAnton[ií]n\s+Dvo(?:ra|rá|řa)k\b" replace="Antonín Dvořák"/>
<Typo word="Anything" find="\b([Aa])n(?:yty|tyth)ing\b" replace="$1nything"/>
<Typo word="Apart/aside from" find="\b([Aa])(part|side)\s+form\b" replace="$1$2 from"/>
<Typo word="Apartheid" find="\b([Aa])parteid\b" replace="$1partheid"/>
<Typo word="Apennine" find="\b[Aa]p(?:e|pen?)nin(es?|us)\b" replace="Apennin$1"/>
<Typo word="Apocalypse" find="\b([Aa])pocolyp(ses?|tic[a-z]*)\b" replace="$1pocalyp$2"/>
<Typo word="(Un)Apolog(y/etic)" find="\b(A|a|[Uu]na)p(?:p?ol[ae]|polo)g(y|ies|ize[ds]?|(etic|ist|ia|ue)s?)\b" replace="$1polog$2"/>
<Typo word="Apparel" find="\b([Aa])p(?:p?arr[ae]|arr?[ae]|p?ara)l(s?|l?ing|l?ed)\b" replace="$1pparel$2"/>
<Typo word="Apparent" find="\b([Aa])p(?:p*ea?r[aei]|(?:pp+|)ea?r[aei]|p*arr+[aei]|p*ar+[ai])nt(ly)?\b" replace="$1pparent$2"/>
<Typo word="(Un)Appealing" find="\b([Uu]na|A|a)p+ealling\b" replace="$1ppealing"/>
<Typo word="(Dis/Re)Appearance" find="\b(A|a|[Dd]isa|[Rr]ea)p(?:p?earea?|p?era|p?reara)nc(es?)\b" replace="$1ppearanc$2"/>
<Typo word="Appellate" find="\b([Aa])ppelat(e|i[a-z]+)\b" replace="$1ppellat$2"/>
<Typo word="Application" find="\b([Aa])pplicaito(ns?)\b" replace="$1pplicatio$2"/>
<Typo word="(Dis)Appoint" find="\b([Dd]is)?s?([Aa])(?:sp*|)point([a-z]*)\b" replace="$1$2ppoint$3"/>
<Typo word="(Ap/De)preciate" find="\b([Aa]p|[Dd]e)pr(?:[ei]cai|ie?cia|eacia)([a-z]+)\b" replace="$1precia$2"/>
<Typo word="Approaches" find="\b([Aa])p+roach([ds])\b" replace="$1pproache$2"/>
<Typo word="(In)Appropriate" find="\b(A|a|[Ii]na)p(?:propropia|ropri?a|proprai?|propia)t([a-z]+)\b" replace="$1ppropriat$2"/>
<Typo word="Approximate" find="\b([Aa])p+rox(?:i?[ao]m[ai]|imi|imm|ia(?:tema)?)t([a-z]+)\b" replace="$1pproximat$2"/>
<Typo word="Approximately" find="\b([Aa])p+[ro]+x+[aei]*m+[aitel]{2,7}y(?<![Aa]pproximately)\b" replace="$1pproximately"/>
<Typo word="Aqueduct_" find="\b([Aa])quaduct(s?)(?<!Mental\s{1,9}([Aa])quaduct(s?))\b" replace="$1queduct$2"/>
<Typo word="Arabia" find="\b[Aa]raibi?(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Arabi$1"/>
<Typo word="Arbitrary" find="\b([Aa])r?b(?:ritr?a|r?ita|rbitr?e)r((il)?y|iness)\b" replace="$1rbitrar$2"/>
<Typo word="Arboretum" find="\b([Aa])rbo(?:ure|ri)tum\b" replace="$1rboretum"/>
<Typo word="Archetype" find="\b([Aa])rchi?typ(es?|al|ic[a-z]*)\b" replace="$1rchetyp$2"/>
<Typo word="Archimedean" find="\b[Aa]rchimedian\b" replace="Archimedean"/>
<Typo word="Architect" find="\b([Aa])(?:rch(?:[eo]c?|ic)te(?:c?t|cht?)|chitect)(s?|ur[a-z]+)\b" replace="$1rchitect$2"/>
<Typo word="Architectural" find="\b([Aa])rchitectual(ly)?\b" replace="$1rchitectural$2"/>
<Typo word="Architecture" find="\b([Aa])rch[ie](?:ctect|c?techt?|tet|tec)ur([a-z]+)\b" replace="$1rchitectur$2"/>
<Typo word="Argument" find="\b([Aa])rguement([as]?|ive|ative(ly)?|ation|um)\b" replace="$1rgument$2"/>
<Typo word="Armistice" find="\b([Aa])rm(?:[ia]sta|asti)[cs](es?)\b" replace="$1rmistic$2"/>
<Typo word="Arose" find="\b([Aa])rised\b(?<!\bha(?:s|ve|d) +[Aa]rised)" replace="$1rose"/>
<Typo word="Arose" find="\b([Aa])rised\b(?<=\bha(?:s|ve|d) +[Aa]rised)" replace="$1risen"/>
<Typo word="Around_" find="(?!\bAroud\b)\b([Aa])r(?:r?o[nu]d|round|und|ounf)\b" replace="$1round"/><!--ignore name/city Aroud-->
<Typo word="Article" find="\b([Aa])rtic[ae]l?(s?)\b" replace="$1rticle$2"/>
<Typo word="Artillery" find="\b([Aa])rti(?:lla|la|le)r+y\b" replace="$1rtillery"/>
<Typo word="Artist" find="\b([Aa])r(?:itis|tsi)t(s?|ic(ally)?)\b" replace="$1rtist$2"/> 
<Typo word="Ascend" find="\b([Aa])(?:cce|sece)n(sions?|d(?:ed|ing|s)?)\b" replace="$1scen$2"/>
<Typo word="Ascetic" find="\b([Aa])setic(s?|ally|ism)\b" replace="$1scetic$2"/>
<Typo word="Aside" find="\b([Aa])sside\b" replace="$1side"/>
<Typo word="Asphyxiate" find="\b([Aa])sphyxai?t(e[ds]?|ing|ion)\b" replace="$1sphyxiat$2"/>
<Typo word="Assassin" find="\b([Aa])s+assa(ns?)\b" replace="$1ssassi$2"/>
<Typo word="Assassin" find="\b([Aa])ssas[ia]n(s|ate[ds]?|ations?)?\b" replace="$1ssassin$2"/>
<Typo word="Assassinate" find="\b([Aa])ss(?:asi|is)nat(e[ds]?|ions?)\b" replace="$1ssassinat$2"/>
<Typo word="Assassinated" find="\b([Aa])ssasined\b" replace="$1ssassinated"/>
<Typo word="Assassination" find="\b([Aa])ssassintation\b" replace="$1ssassination"/>
<Typo word="Assault" find="\b([Aa])s(?:s[us]a?|au)l(ts?|ted|ting)\b" replace="$1ssaul$2"/>
<Typo word="(Dis/Re)Assemble" find="\b(A|a|[Dd]isa|[Rr]ea)s(?:semp|embe?)l([a-z]+)\b" replace="$1ssembl$2"/>
<Typo word="(As/Re/Reas)sembly" find="\b([Rr]e|[Aa]s|[Rr]eas)sembel(y|ing|ance|ed)\b" replace="$1sembl$2"/>
<Typo word="Assertion" find="\b([Aa])ssertati(ons?|ve[a-z]*)\b" replace="$1sserti$2"/>
<Typo word="Assessment" find="\b([Aa])ssesment\b" replace="$1ssessment"/>
<Typo word="Assign" find="\b([Aa])sign(s?|ed|ing|ments?)\b" replace="$1ssign$2"/>
<Typo word="Assign_" find="\b([Aa])ss(?:s+ign|ing)(s|ing|ed|ments?)\b" replace="$1ssign$2"/><!--don't fix Assing-->
<Typo word="Assist" find="\b([Aa])s(?:si|is+|siss)t(s?|ed|ing|ants?|ance)\b" replace="$1ssist$2"/>
<Typo word="(As/Re)sistant" find="\b(As|as|[Rr]e)s?i(?:t[ae]|s+te)n(ces?|t[a-z]*)\b" replace="$1sistan$2"/>
<Typo word="Associate" find="\b([Aa])s(?:oci|soi?c)ai?t(e[ds]?|ing|ions?)\b" replace="$1ssociat$2"/>
<Typo word="(Un)Assume" find="\b([Uu]na|A|a)s(?:um|s+umm)(e[ds]?|ing(ly)?|ptions?)\b" replace="$1ssum$2"/>
<Typo word="Astronomy" find="\b([Aa])stonom(y|ers?|ic[a-z]*)\b" replace="$1stronom$2"/>
<Typo word="Asymmetric" find="\b([Aa])s(?:s?y)metr(y|ic[a-z]*)\b" replace="$1symmetr$2"/>
<Typo word="Atatürk" find="\bAtaturk\b" replace="Atatürk"/>
<Typo word="Atheist" find="\b([Aa])thies(ts?|m|tic)\b" replace="$1theis$2"/>
<Typo word="Atheistic" find="\b([Aa])theistical\b" replace="$1theistic"/>
<Typo word="Athenian" find="\b([Aa])thenea(ns?)\b" replace="$1thenia$2"/>
<Typo word="Athlete" find="\b([Aa])thelet(es?|ic[a-z]*)\b" replace="$1thlet$2"/>
<Typo word="Atlantic" find="\bAltantic\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Atlantic"/>
<Typo word="Atrocity" find="\b([Aa])ttroci(ty|ties|ous[a-z]*)\b" replace="$1troci$2"/>
<Typo word="Attaché" find="\b([Aa])ttachee(s?)\b" replace="$1ttaché$2"/>
<Typo word="Attach" find="\b([Aa])tt?atch(e[ds]|ing|able|ments?)?\b" replace="$1ttach$2"/>
<Typo word="Attempt" find="\b([Aa])t(?:empt|tem[pt])(s?|ed|ing|able)\b" replace="$1ttempt$2"/>
<Typo word="Attendant" find="\b([Aa])t(?:tende|end[ae])n(ts?|ces?)\b" replace="$1ttendan$2"/>
<Typo word="(Un)Attend(ed/ing)" find="\b(A|a|[Uu]na)(?:t+en|tend?)(ed|ing)\b" replace="$1ttend$2"/>
<Typo word="(In)Attention" find="\b(A|a|[Ii]na)t(?:tens|ent)i(ons?|ve(ness)?)\b" replace="$1ttenti$2"/>
<Typo word="Attitude" find="\b([Aa])t(?:titi|it+u|tittu)d(e?s|inal[a-z]*)\b" replace="$1ttitud$2"/>
<Typo word="(Un)Attractive" find="\b(A|a|[Uu]na)ttrative(ly|ness)?\b" replace="$1ttractive$2"/>
<Typo word="Audience" find="\b([Aa])ude?ia?nc(es?)\b" replace="$1udienc$2"/>
<Typo word="Australia" find="\b[Aa]ustr(?:la?|a?il|ial)i?(a|ans?)\b" replace="Australi$1"/>
<Typo word="Australasia" find="\b[Aa]ustra(?:il|li)(asian?s?)\b" replace="Austral$1"/>
<Typo word="Author" find="\b([Aa])uto(rs?)\b" replace="$1utho$2"/>
<Typo word="Author" find="\bauthe(rs?)\b" replace="autho$1"/><!--Don't match names Auther/Authers-->
<Typo word="(A/Ina/S)uspicious" find="\b([AaSs]|[Ii]na)uspi[st]io(ns?|us(ly)?)\b" replace="$1uspicio$2"/>
<Typo word="Authoritative" find="\b([Aa])(?:uthr|ut|th)or(?:a|i|[ai]t[ai])tive([a-z]*)\b" replace="$1uthoritative$2"/>
<Typo word="Authoritative" find="\b([Aa])uthor[ai]tive\b" replace="$1uthoritative"/>
<Typo word="Authorities" find="\b([Aa])(?:(?:uthr|ut|th)orit(?:i?e|ier|hie)|uthorit(?:e|ier|hie))s\b" replace="$1uthorities"/>
<Typo word="Authority" find="\b([Aa])(?:(?:uthr|ut|th)orith?|uthorith)([a-z]+)\b(?<!\bAutoritratto)" replace="$1uthorit$2"/>
<Typo word="Auto-da-fé" find="\b([Aa])uto-da-fe\b" replace="$1uto-da-fé"/>
<Typo word="Autobiography" find="\b([Aa])uthobiograph(y|ies|ic[a-z]*)\b" replace="$1utobiograph$2"/>
<Typo word="Autochthonous" find="\b([Aa])utoc(?:h?t|th)on(ous(ly)?|[sy]?|es|ism)\b" replace="$1utochthon$2"/>
<Typo word="Automobile" find="\b([Aa])utomibil(es?|ing)\b" replace="$1utomobil$2"/>
<Typo word="Autonomous" find="\b([Aa])uto(?:monom|[mn]on|mom)ou(s[a-z]*)\b" replace="$1utonomou$2"/>
<Typo word="Auxiliary" find="\b([Aa])uxil(?:li?)?ar(y|ies)\b" replace="$1uxiliar$2"/>
<Typo word="Available" find="\b(A|a|[Uu]na)vailalbe\b" replace="$1vailable"/>
<Typo word="(Un)Available" find="\b(A|a|[Uu]na)v(?:ai|a|i)(?:l?ai|lai|l?ia?|l)b([a-z]+)\b" replace="$1vailab$2"/>
<Typo word="Avalanche" find="\b([Aa])valanc(es?)\b" replace="$1valanch$2"/>
<Typo word="Average" find="\b([Aa])v(?:a?ra?|er)g(es?|ed|ing)\b" replace="$1verag$2"/>
<Typo word="Averaged" find="\b([Aa])veragee([ds])\b" replace="$1verage$2"/>
<Typo word="Aviation" find="\b([Aa])vai?t(ion|ors?)\b" replace="$1viat$2"/>
<Typo word="Await" find="\b([Aa])wat(ed|ing|s)\b" replace="$1wait$2"/>
<Typo word="Award" find="\b([Aa])war(ed|ing|s)\b" replace="$1ward$2"/>
<Typo word="Awareness" find="\b([Aa])war(?:ne|enes)ss+\b" replace="$1wareness"/>
<Typo word="Away" find="\b([Aa])(?:wy|yw)a\b" replace="$1way"/>
<Typo word="Awkward" find="\b([Aa])(?:c?kw|wk)ard(ly|ness)?\b" replace="$1wkward$2"/>
</source>

===B===
<source lang="xml">
<Typo word="Back" find="\b([Bb])(?:akc|cak)(s?|ed|ing|ers?|(?:bo|w|y)ards?|hand[a-z]*|hoe?|dat[a-z]*|doors?|fir[ei][a-z]*|light[a-z]*|lit|log[a-z]*|bone[a-z]*|[lw]ash|pack[a-z]*|sides?|spin[a-z]*|stage)\b" replace="$1ack$2"/>
<Typo word="(B/M/S)adly" find="\b([BbMmSs]ad)dly\b" replace="$1ly"/>
<Typo word="(Un)Balance" find="\b(B|b|[Uu]nb)al(?:e|la)nc([a-z]+)\b(?<!Bal(?:enciaga|lanc(?:e|ourt))\b)" replace="$1alanc$2"/><!--Not Ballance, Ballancourt, Balenciaga-->
<Typo word="Banana" find="\b([Bb])an(?:an|na)n(as?)\b" replace="$1anan$2"/>
<Typo word="Bankrupt" find="\b([Bb])an(?:krup|rupt)(s?|ed|c[a-z]+)\b" replace="$1ankrupt$2"/>
<Typo word="Barbiturate" find="\b([Bb])arbituate(s?)\b" replace="$1arbiturate$2"/>
<Typo word="Battalion" find="\b([Bb])at(?:tal|al?)(lions?)\b" replace="$1atta$2"/>
<Typo word="Beachhead" find="\b([Bb])eachea(ds?)\b" replace="$1eachhea$2"/>
<Typo word="Beat" find="\b([Bb])eated\b" replace="$1eat"/>
<Typo word="Beautiful" find="\b([Bb])e(?:at[iy]|ua?t[iy]|auty)full?(ly)?\b" replace="$1eautiful$2"/>
<Typo word="Beauty" find="\b([Bb])eua?ty\b" replace="$1eauty"/>
<Typo word="Because" find="\b([Bb])[ae](?:a?cuse|cuase?|couse|casue|c[ce]ause)\b" replace="$1ecause"/>
<Typo word="Become" find="\b([Bb])eco(?:mm|)(es?|ing)\b" replace="$1ecom$2"/>
<Typo word="Beginner" find="\b([Bb])eg(?:gin|g?i)n(ers?|ings?)\b" replace="$1eginn$2"/>
<Typo word="Beginning" find="\b([Bb])egin(?:inin|ni)g(s?)\b" replace="$1eginning$2"/>
<Typo word="Begins" find="\b([Bb])eggin(s|n(?:er|ing)s?)\b" replace="$1egin$2"/>
<Typo word="(Mis)Behavior" find="\b(B|b|[Mm]isb)ehavoi?(u?r[a-z]*)\b" replace="$1ehavio$2"/>
<Typo word="Beijing" find="\b[Bb]ejing\b" replace="Beijing"/>
<Typo word="Being" find="\b([Bb])eeing(s?)\b" replace="$1eing$2"/>
<Typo word="being" find="\bbeng\b" replace="being"/><!--Beng is a surname-->
<Typo word="Beirut" find="\b[Bb]ei?ruit\b" replace="Beirut"/>
<Typo word="Beleaguered" find="\b([Bb])eleag[eu]r(ed)?\b" replace="$1eleaguer$2"/>
<Typo word="Belgium" find="\b[Bb]eligum\b" replace="Belgium"/>
<Typo word="(Dis/Mis/Non/Un)Believ(ing/able)" find="\b(B|b|[DdMm]isb|[Nn]onb|[Uu]nb)ele?ie?ve(ing|abl[ey]|ability)\b" replace="$1eliev$2"/><!--to catch "e" after "v" with these endings-->
<Typo word="Belligerent" find="\b([Bb])el(?:l?igera|igere)n(ts?|tly|ce)\b" replace="$1elligeren$2"/>
<Typo word="Bellwether" find="\b([Bb])ellweathe(rs?)\b" replace="$1ellwethe$2"/>
<Typo word="Beneficial" find="\b([Bb])en(?:[ei]ficai?|[ai]ficia)([lr][aeilrsy]*)\b" replace="$1eneficia$2"/>
<Typo word="Benefit" find="\b([Bb])en[ia]fit(s?|t[ei][a-z]+)\b" replace="$1enefit$2"/>
<Typo word="Benjamin" find="\b[Bb]enajmin\b" replace="Benjamin"/>
<Typo word="Bernoulli" find="\b[Bb]ernou(?:il|)li\b" replace="Bernoulli"/>
<Typo word="Bestiality" find="\b([Bb])eastiali?ty\b" replace="$1estiality"/>
<Typo word="Between" find="\b([Bb])e(?:twen|w?teen|tweem)\b" replace="$1etween"/>
<Typo word="Beyond" find="\b([Bb])eyo(?:ng|und)\b" replace="$1eyond"/>
<Typo word="(B/M/Tr)illionaire" find="\b((?:[Mm]ulti)?[MmBb]|[Tt]r)il+ioni?are([es])*\b" replace="$1illionaire$2"/>
<Typo word="Bizarre" find="\b([Bb])iz(?:zar+|ar)e(ly)?\b(?<!Some Bizzare)" replace="$1izarre$2"/><!--allow [[Some Bizzare]]-->
<Typo word="Blame" find="\b([Bb])laime?\b" replace="$1lame"/>
<Typo word="Blitzkrieg" find="\b([Bb])litzkreig\b" replace="$1litzkrieg"/>
<Typo word="Bombardment" find="(?<!\b[DdLl]es?\s{1,9})\b([Bb])ombar(?:de|)ment(s?)\b(?!\s{1,9}[Dd]es?\b)" replace="$1ombardment$2"/><!--avoid French word bombardement by use of lookaround for French articles-->
<Typo word="Bombardement (French)" find="\b([Bb])om[bd]ard?ment(s?)\b(?:(?=(\s+([Dd](u|es?)|e[nt]|qui))\b)|(?<=\b(?:[DdLl]es?\s{1,9}[Bb])om[bd]ard?ment(?:s?)))" replace="$1ombardement$2"/>
<Typo disabled="Bonanno" find="\b([Bb])onnano\b" replace="$1onanno"/>
<Typo word="Botswana" find="\b[Bb]o(?:stwa|tswan)na(n?s?)\b" replace="Botswana$1"/>
<Typo word="Boundary" find="\b([Bb])(?:onda?r|ounder)(y|ies)\b" replace="$1oundar$2"/>
<Typo word="Boxes" find="\b([Bb])ox([ds])\b" replace="$1oxe$2"/>
<Typo word="Brazilian" find="\b([Bb])ra(?:sil?|[sz]il)li(ans?)\b" replace="Brazili$2"/>
<Typo word="Breakthrough" find="\b([Bb])reakt(?:t?[hr]ough|hrought)(s?)\b" replace="$1reakthrough$2"/>
<Typo word="Brethren" find="\b([Bb])rethe(?:re?)?n\b(?<!(G.A.|H.|Arthur)\sBrethen)(?!\sColiseum)" replace="$1rethren"/>
<Typo word="Brief" find="\b([Bb])reif(s?|ly|ings?|ed|er|est)\b" replace="$1rief$2"/>
<Typo word="Brillian(t/ce)" find="(?!\bBrillant\b)\b([Bb])ril[il]an(t(ly)?|c[ey])\b" replace="$1rillian$2"/><!--avoid surname Brillant-->
<Typo word="Brimstone" find="\b([Bb])rime(stones?)\b" replace="$1rim$2"/>
<Typo word="British" find="\b[Bb]ritt+(ish|anni[ac])\b" replace="Brit$1"/>
<Typo word="Brittany" find="\bBrit+anny\b" replace="Brittany"/>
<Typo word="Broadcast" find="\b([Bb])r(?:ad|a?od|oa|oada)cast([a-z]*)\b" replace="$1roadcast$2"/>
<Typo word="Broadly" find="\b([Bb])roadyl?\b(?<!\bBroady\b)" replace="$1roadly"/><!--don't match name Broady-->
<Typo word="Broke" find="\bbork(e[nr]?)\b" replace="brok$1"/><!--Borken = place name, Borke = surname-->
<Typo word="Buñuel" find="\bBunuel\b" replace="Buñuel"/>
<Typo word="(Re)Build" find="\b(B|b|[Rr]eb)ui([dt])l?((ing)?s?)\b" replace="$1uil$2$3"/>
<Typo word="(Re)Build" find="(?!\b(?:Bild|der Bilt)\b)\b(B|b|[Rr]eb)(?:iul|[iu]li?)(ds?|t|dings?)\b(?<!van der Bilt)" replace="$1uil$2"/><!--Don't match surnames Bild, van der Bilt-->
<Typo word="(Re/In/Pre/Up/Un/Over/Jerry)Built" find="\b(B|b|[Rr]eb|[Ii]nb|[Pp]reb|[Uu][pn]b|[Oo]verb|[Jj]erryb)uildt\b" replace="$1uilt"/>
<Typo word="Buoy" find="\b(B(?!ouy\b)|b)ouy(s?|ed|ant|ancy)\b" replace="$1uoy$2"/><!--Bouy is a place name-->
<Typo word="Buoyant" find="\b([Bb])(?:ou?y|uo)an(t(ly)?|cy)\b" replace="$1uoyan$2"/>
<Typo word="Bureaucrat" find="\b([Bb])(?:eaur[ao]|ure?u?)cra([a-z]+)\b" replace="$1ureaucra$2"/>
<Typo word="Burglar" find="\b([Bb])urg(?:u?le|ula)r([a-z]*)\b" replace="$1urglar$2"/>
<Typo word="Burial" find="\b([Bb])urri(als?|ed)\b" replace="$1uri$2"/>
</source>

===C===
<source lang="xml">
<Typo word="Caesar" find="\b[Cc]easar(ean?)?(s?)\b" replace="Caesar$1$2"/>
<Typo word="Cafeteria" find="\b([Cc])af[ai]teri(as?)\b" replace="$1afeteri$2"/>
<Typo word="Caisson" find="\b([Cc])as+io(ns?)\b" replace="$1aisso$2"/>
<Typo word="(Mis/Re)Calculate" find="\b([Cc]|[Mm]isc|[Rr]ec)a[lcu]+u?[al]+t(?<!alculat)(e[ds]?|ors?|ions?|ing)\b" replace="$1alculat$2"/>
<Typo word="Calendar" find="\b([Cc])alander(s?)\b" replace="$1alendar$2"/>
<Typo word="Caliber" find="\b([Cc])al(?:a|li)b(ers?|res?|rat(e[ds]?|ing|ion))\b(?<!Quintus Calaber)" replace="$1alib$2"/><!--Not Quintus Calaber-->
<Typo word="California" find="\b[Cc]al(?:for?n?|i?fo[nr]r?|ifron)i(an?s?)\b" replace="Californi$1"/>
<Typo word="Call(ed/ing)" find="\b([Cc])al(ed|ing)\b" replace="$1all$2"/>
<Typo word="Calligraphy" find="\b([Cc])aligraph(y|ers?|ists?|ic)\b" replace="$1alligraph$2"/>
<Typo word="Calvinism" find="\b[Cc]alvanis(m|ts?)\b" replace="Calvinis$1"/>
<Typo word="Cambridge" find="\b[Cc]ambrigd?e\b" replace="Cambridge"/>
<Typo word="Camouflage" find="\b([Cc])am[ao]fla[ud]?g(e[ds]?|ing)\b(?<!Camoflauge)" replace="$1amouflag$2"/><!--Not Camoflauge (rapper)-->
<Typo word="Campaign" find="\b([Cc])ampa(?:g?in|a?ig|ing)(s?|ed|ers?|ing)\b" replace="$1ampaign$2"/>
<Typo word="Can" find="\b([Cc])na\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1an"/><!--Avoid domains and URLs-->
<Typo word="Candidate" find="\b([Cc])and(?:adat|i(?:di)?at|idta)((ur)?es?)\b" replace="$1andidat$2"/>
<Typo word="Candidate" find="\b([Cc]an)[ai]da(te(?:s|\b(?<!Canidate))|c(?:y|ies)|tures?)\b" replace="$1dida$2"/><!--allow rapper Canidate-->
<Typo word="Canister" find="\b([Cc])anniste(rs?)\b" replace="$1aniste$2"/>
<Typo word="Cannot" find="\b([Cc])a(?:|nn)not\b" replace="$1annot"/>
<Typo word="Cantaloupe" find="\b([Cc])antalope(s?)\b" replace="$1antaloupe$2"/>
<Typo word="Capital" find="\b([Cc])aptial(s?|is[mt][a-z]*)\b" replace="$1apital$2"/>
<Typo word="Capitalize" find="\b([Cc])apitiliz([aei][a-z]*)\b" replace="$1apitaliz$2"/>
<Typo word="Captured" find="\b([Cc])aptu[er]d\b" replace="$1aptured"/>
<Typo word="Carcass" find="\b([Cc])arcas\b" replace="$1arcass"/>
<Typo word="Career" find="\b([Cc])arree?r(\b(?<!Carrer)|s)\b" replace="$1areer$2"/><!--Don't fix name Carrer-->
<Typo word="Caribbean" find="\b([Cc])ar(?:r?ab?|rib|r?i)bean\b" replace="Caribbean"/>
<Typo word="Carmelite" find="\b[Cc]armalit(es?)\b" replace="Carmelit$1"/>
<Typo word="Carthaginian" find="\b([Cc])arthagia(ns?)\b" replace="Carthaginia$2"/>
<Typo word="Cartilage" find="\b([Cc])artil+(?:[ie]d?|ad)g(e|inous)\b" replace="$1artilag$2"/>
<Typo word="Cartography" find="\b([Cc])art(?:ho|a)graph(y|ers?|ic)\b" replace="$1artograph$2"/>
<Typo word="Cartridge" find="\b([Cc])art(?:drid?|ri)g(es?)\b" replace="$1artridg$2"/>
<Typo word="Cassette" find="\b([Cc])as(?:et?|s?e)t(es?)\b" replace="$1assett$2"/>
<Typo word="Cassowary" find="\b([Cc])as(?:s?aw[ao]|s?owar|owa)r(y|ies)\b" replace="$1assowar$2"/>
<Typo word="Catapult" find="\b([Cc])atapault(s?|ed|ing)\b" replace="$1atapult$2"/>
<Typo word="Catastrophes" find="\b([Cc])atastrophies\b" replace="$1atastrophes"/>
<Typo word="Catechism" find="\b([Cc])ath[ae]ch?is([mt]s?|tic)\b" replace="$1atechis$2"/>
<Typo word="Category" find="\b([Ss]ubc|C|c)(?:atag|ategi|taeg)or([a-z]+)\b" replace="$1ategor$2"/>
<Typo word="Caterpillar" find="\b([Cc])at(?:ter?pil?|epil|t?erpi)l(ars?)\b" replace="$1aterpill$2"/>
<Typo word="Catholic" find="\b([Cc])ath(?:[eo]?lo|eli)c(s?|ism)\b" replace="$1atholic$2"/>
<Typo word="Caucasian" find="\b([Cc])aucasio(ns?)\b" replace="$1aucasia$2"/>
<Typo word="Caucuses" find="\b([Cc])u?acuse([ds])\b" replace="$1aucuse$2"/>
<Typo word="Ceiling" find="\b([Cc])i?eling(s?|ed)\b" replace="$1eiling$2"/>
<Typo word="Celebrity" find="\b([Cc])eleb[ei]rt(y|ies)\b" replace="$1elebrit$2"/> 
<Typo word="Celebr-" find="\b([Cc])eleber(at(?:e[ds]?|ions?|ing|ory)|it(?:y/ies))\b" replace="$1elebr$2"/>
<Typo word="Cellpadding" find="\b([Cc])el(?:lpa|pad)ding\b" replace="$1ellpadding"/>
<Typo word="Celsius" find="\b([Cc]elc|cels)ius\b" replace="Celsius"/>
<Typo word="Cemetery" find="\b([Cc])emen?ta?re?(y|ies)\b" replace="$1emeter$2"/>
<Typo word="Censor" find="\b([Cc])ensu(rs?)\b" replace="$1enso$2"/>
<Typo word="Census" find="\b([Cc])encus\b" replace="$1ensus"/><!--don't match latin word sensus-->
<Typo word="(Cent|Mill)ipede" find="\b([Cc]ent|[Mm]ill)[ae]pede(s)?\b" replace="$1ipede$2"/>
<Typo word="Central" find="\b([Cc])enteral(ly|is[mt]s?|i[sz][aei][a-z]*)?\b" replace="$1entral$2"/>
<Typo word="Century" find="\b([Cc])ent(?:ru|ua)r?(y|ies|ions?)\b" replace="$1entur$2"/>
<Typo word="Ceremony" find="\b([Cc])era?mon(y|ies|ial[a-z]*|ious[a-z]*)\b" replace="$1eremon$2"/>
<Typo word="(Un)Ceremonious" find="\b(C|c|[Uu]nc)er[io]mon(y|ies|i(al|ous)(ly)?)\b" replace="$1eremon$2"/>
<Typo word="César Franck" find="\bCesar\s+Franc?k\b" replace="César Franck"/>
<Typo word="Cézanne" find="\b[Cc]ezanne\b" replace="Cézanne"/>
<Typo word="Challenge" find="\b([Cc])hal(?:en|lan|le)g(e[ds]?|ers?|ing|eable)\b" replace="$1halleng$2"/>
<Typo word="Champagne" find="\b([Cc])hampange\b" replace="$1hampagne"/>
<Typo word="Champion" find="\b([Cc])hampoin([a-z]*)\b" replace="$1hampion$2"/>
<Typo word="Champs-Élysées" find="\b[Cc]hamps-[Ee]lysees\b" replace="Champs-Élysées"/>
<Typo word="Chancellor" find="\b([Cc])hancel(?:o|l?e)r(s?|ship|sville)\b" replace="$1hancellor$2"/>
<Typo word="(Inter/Un)Change" find="\b(C|c|[Ii]nterc|[Uu]nc)h(?:aneg|nage|ang)(s?\b(?<![Cc]hangs?)|d|able)\b" replace="$1hange$2"/><!--don't match name Chang(s), chang-->
<Typo word="(Inter/Un/Ex/Re/Dis)Cha(n/r)geable" find="\b(C|c|[Ii]nterc|[Uu]nc|[Ee]xc|[Rr]ec|[Dd]isc)ha([nr])g[aei](bl[ey][a-z]*|bility)\b" replace="$1ha$2gea$3"/>
<Typo word="Character" find="\b([Cc])(?:(?:a?h(?:ra|are?)c|arach?)t[aeo]|ha?r(?:achte|a?ct[ao]|e?cte|ate))r([a-z]*)\b(?<![Cc]haracter)" replace="$1haracter$2"/>
<Typo word="(Un)Characteristic(s/ally)" find="\b(C|c|[Uu]nc)hara?(?:l?i|c?t[eo]r)s?i?s?i?ti?c(s?|all?y)\b(?<!(C|c|[Uu]nc)haracteristic(s?|all?y))" replace="$1haracteristic$2"/> 
<Typo word="Chargé d'affaires" find="\b([Cc])harg(?:e\s+d['’]|é\s+D['’]|é\s+d’)([Aa])ffaires\b" replace="$1hargé d'$2ffaires"/>
<Typo word="Charisma" find="\b([Cc])h?ar[ai]sma(\b|tic(?:s?|ally))\b(?<!Carisma\b|Carasmatic\b)(?<![Cc]harisma(\b|tic(?:s?|ally)))" replace="$1harisma$2"/><!--don't fix Carisma or Carasmatic-->
<Typo word="Charitable" find="\b([Cc])hartiable\b" replace="$1haritable"/>
<Typo word="Charles(ton)" find="\bChalres(ton)?\b" replace="Charles$1"/>
<Typo word="Chaser" find="\b([Cc])has(rs?)\b" replace="$1hase$2"/>
<Typo word="Chat" find="\b([Cc])aht(s?)\b" replace="$1hat$2"/>
<Typo word="Check" find="\b([Cc])hekc(s|ing)?\b" replace="$1heck$2"/>
<Typo word="Chemical" find="\b([Cc])hemcial(s?|ly)\b" replace="$1hemical$2"/>
<Typo word="Chemist" find="\b([Cc])hemest(ry|s)?\b" replace="$1hemist$2"/>
<Typo word="Chief" find="\b([Cc])heif(s?|ly|doms?|ship|tains?)\b" replace="$1hief$2"/>
<Typo word="Childbirth" find="\b([Cc])hildbird\b" replace="$1hildbirth"/>
<Typo word="Children" find="\b(C|c|[Gg]randc|[Ss]tepc)hil(?:dere?|re)n\b" replace="$1hildren"/>
<Typo word="Children's" find="\b(C|c|[Gg]randc|[Ss]tepc)hild(?:re|er)ns(?:['′’]s?(\s)|(\b))" replace="$1hildren's$2$3"/>
<Typo word="Choreograph" find="\b([Cc])horo?egraph(s?|y|ies|ers?|ed|ing)\b" replace="$1horeograph$2"/>
<Typo word="Chorus" find="\b([Cc])hrous(es|ing)?\b" replace="$1horus$2"/>
<Typo word="(Mis)Chosen" find="\b(C|c|[Mm]isc)hoosen\b" replace="$1hosen"/>
<Typo word="Chronicle" find="\b([Cc])hor?nicl(e[ds]?|ers?|ing)\b" replace="$1hronicl$2"/>
<Typo word="Church" find="\b([Cc])(?:hu|ur|hru)ch(es)?\b" replace="$1hurch$2"/>
<Typo word="Churches" find="\b([Cc])hurchs\b" replace="$1hurches"/>
<Typo word="Cigarette" find="\b([Cc])ig(?:garet|g?are|g?arret?)te(s)?\b" replace="$1igarette$2"/>
<Typo word="Circuit" find="\b([Cc])(?:ircu|iricui?|urcui)t([a-z]*)\b" replace="$1ircuit$2"/>
<Typo word="(Re)Circulation" find="\b(C|c|[Rr]ec)irculato(ns?)\b" replace="$1irculatio$2"/>
<Typo word="Circumcision" find="\b([Cc])ircum(?:sc?i[cs]|[cs]+ic)io(ns?)\b" replace="$1ircumcisio$2"/>
<Typo word="Citrus" find="\b([Cc])irtus\b" replace="$1itrus"/>
<Typo word="Civilian" find="\b([Cc])ivillian(s?|iz(e[ds]?|ing|ation))\b" replace="$1ivilian$2"/>
<Typo word="(Re)Claims" find="\b(C|c|[Rr]ec)laimes\b" replace="$1laims"/>
<Typo word="Clarinet" find="\b([Cc])larinette?(s?)\b" replace="$1larinet$2"/>
<Typo word="Class" find="\b([Cc])las(e[ds]|ing|if(y[a-z]*|i[ce][a-z]*))\b(?<![Cc]las(?:|e|es))\b" replace="$1lass$2"/><!--don't match (C\c)las(e/es)-->
<Typo word="Classic" find="\b([Cc])lasic(s?|al[a-z]*|is[tm]s?|iz[ei][a-z]*)\b" replace="$1lassic$2"/>
<Typo word="Clear_" find="\b([Cc])laer(e[rd]|est|ly)\b" replace="$1lear$2"/>
<Typo word="(Un)Clear" find="\b(C|c|[Uu]nc)lera\b" replace="$1lear"/>
<Typo word="Coast" find="\b([Cc])aost(s?|ed|ing)\b" replace="$1oast$2"/>
<Typo word="Cocktail" find="\b([Cc])o[ck]tail(\b|s\b(?<!Coctails))" replace="$1ocktail$2"/><!--Avoid false positive "Coctails" (band)-->
<Typo word="Coffee" find="\b([Cc])of[ef]e(house|pot|shop)?(s?)\b" replace="$1offee$2$3"/>
<Typo word="Coincide" find="\b([Cc])o-incid(e[ds]?|ent(al(ly)?)?)\b" replace="$1oincid$2"/>
<Typo word="Collapse" find="\b([Cc])ollasp(e[ds]?|ing|ible)\b" replace="$1ollaps$2"/>
<Typo word="Collateral" find="\b([Cc])olateral(ly|ize[ds]?|izing)?\b" replace="$1ollateral$2"/>
<Typo word="Colleague" find="\b([Cc])ol(?:le|ea)gu(es?)\b" replace="$1olleagu$2"/>
<Typo word="(Re)Collection" find="\b(C|c|[Rr]ec)ol(?:el?ct[aei]|lect[ae]?)(ons?|ve(s?|ly))\b" replace="$1ollecti$2"/>
<Typo word="Colonizer" find="\b([Cc])oloni[sz]ator(s)?\b" replace="$1olonizer$2"/>
<Typo word="Colonnade" find="\b([Cc])ol+onad(es?)\b" replace="$1olonnad$2"/>
<Typo word="Colony" find="\b([Cc])ollon(y|ies|ize[ds]?|izations?)\b" replace="$1olon$2"/>
<Typo word="Colorado" find="\b[Cc]ola?rad(o|ans?)\b" replace="Colorad$1"/>
<Typo word="Colossal" find="\b([Cc])ol(?:los?|l?o)s(al(ly)?|us)\b" replace="$1oloss$2"/>
<Typo word="Column" find="\b([Cc])olun?m+(\b(?<!Colum)|s\b)" replace="$1olumn$2"/><!--don't match name Colum-->
<Typo word="Contemp-" find="\b([Cc])om(temp[a-z]+)\b" replace="$1on$2"/>
<Typo word="Combination" find="\b([Cc])omb(?:[ao]natio|intatio|inati)(ns?)\b" replace="$1ombinatio$2"/>
<Typo word="Combustion" find="\b([Cc])ombusi(on|ve(ly)?)\b" replace="$1ombusti$2"/>
<Typo word="Comeback" find="\b([Cc])ombac(ks?)\b" replace="$1omebac$2"/>
<Typo word="Comedic" find="\b([Cc])ommedi(c|ans?)\b" replace="$1omedi$2"/>
<Typo word="(Un)Comfortable" find="\b(C|c|[Uu]nc)o(?:nforta|mforti)bl([ey])\b" replace="$1omfortabl$2"/>
<Typo word="(-)Coming" find="\b([A-Za-z]*[Cc])om[em]ing(s?)\b(?<!Commings)" replace="$1oming$2"/><!--don't match surname Commings-->
<Typo word="Command(eer/o/ment)" find="\b([Cc])om(?:madn|and)(ee?rs?|ed|eer(?:ed|ing)|oe?s?\b(?<![Cc]omandos?)|ments?)?\b" replace="$1ommand$2"/>
<!--exclude Spanish title C/omandos-->
<Typo word="Commemorate" find="\b([Cc])om(?:(?:(?:m?em+|me)r|em+)[oe]r[ai]t|memorit|memer[ai]t)([a-z]+)\b" replace="$1ommemorat$2"/>
<Typo word="Commemorate" find="\b([Cc])om+em+(?:er[ai]|ori)t(e[ds]?|ing|ions?|ives?)\b" replace="$1ommemorat$2"/>
<Typo word="Commercial" find="\b([Cc])om(?:m?eri|er)ci?al(\b(?<!Comercial)|s|ly|i[sz](?:e[ds]?|ing|ation)|is[mt]s?)\b" replace="$1ommercial$2"/><!--Don't fix Comercial, common Spanish/Portuguese word-->
<Typo word="(De)Commission" find="\b(C|c|[Dd]ec)om(?:is|mi|ms?|m?s)sion(s?|ing|ed|ers?)\b" replace="$1ommission$2"/>
<Typo word="Commitment" find="\b([Cc])om(?:it?|m?it)tmen(ts?)\b" replace="$1ommitmen$2"/>
<Typo word="Committ(ed/al)" find="\b([Cc])o(?:mitt?|mmit)(ees?|ed|ing|al\b(?<![Cc]omital))\b" replace="$1ommitt$2"/><!--don't fix "comital"-->
<Typo word="Committee" find="\b([Cc])om(?:m[ei]t(?:ee?|te)|it[te]ee?|mitty)(s?|m[ae]n)\b" replace="$1ommittee$2"/>
<Typo word="Commodity" find="\b([Cc])omod+it(y|ies)\b" replace="$1ommodit$2"/>
<Typo word="(Un)Common" find="\b(C|c|[Uu]nc)omm(?:en|ong)(s?|ers?|ly|ali?t(y|ies))\b(?<!Commens)" replace="$1ommon$2"/>
<Typo word="Commonwealth" find="\b([Cc])om+onweath\b" replace="$1ommonwealth"/>
<Typo word="(Tele)communicate" find="\b([Tt]elec|C|c)om(?:unic|minic|muin?c|mui?ni|munc?i)at(e[ds]?|ors?|ions?|ive(ly)?)\b" replace="$1ommunicat$2"/>
<Typo word="Communities" find="\b([Cc])omm?un?it[ei]+s\b(?<!ommunities)" replace="$1ommunities"/>
<Typo word="Company" find="\b([Cc])om(?:apan|ap?n|pna)(y|ies|ions?)\b" replace="$1ompan$2"/>
<Typo word="Comparative" find="\b([Cc])omp(?:ar[ei]?|era)tiv(es?|ely|ist|eness)\b" replace="$1omparativ$2"/>
<Typo word="Comparison" find="\b([Cc])omparisio(ns?)\b" replace="$1ompariso$2"/>
<Typo word="(In)Compatible" find="\b(C|c|[Ii]nc)ompa?ti?abl([ey])\b" replace="$1ompatibl$2"/>
<Typo word="(In/Histo)Compatibility" find="\b(C|c|[Ii]nc|[Hh]istoc)ompa(?:ti?[ai]b|ti?abi|bi)lit(y|ies)\b" replace="$1ompatibilit$2"/>
<Typo word="(In)Competent" find="\b(C|c|[Ii]nc)omp(?:et[ai]|[ai]t[ea]|tete)n(ce|t(ly)?)\b" replace="$1ompeten$2"/>
<Typo word="Competition" find="\b([Cc])o(?:mpetitit?|mpet[ae]t|pmetit)(ions?|ive(?:ly|ness)?|ors?)\b" replace="$1ompetit$2"/><!--see also "-petiti(on/ve)"-->
<Typo word="Compilation" find="\b([Cc])om(?:ilati?|pi?liati?|plilati?|pilli?ati?|pilat)on(s?)\b" replace="$1ompilation$2"/>
<Typo word="(In)Complete" find="\b(C|c|[Ii]nc)ompl(?:eate?\b(?<!Compleat)|eete|ate)(s?|d|ly|ness)\b" replace="$1omplete$2"/>
<!--Don't fix Compleat, (in)complet-->
<Typo word="(In)Completely" find="\b(C|c|[Ii]nc)omplet(?:elyl|le?y)\b" replace="$1ompletely"/>
<Typo word="Comp(l)eting" find="\b([Cc]ompl?et)et?i(ng|on?)\b" replace="$1i$2"/>
<Typo word="Composite" find="\b([Cc])omposate(s)?\b" replace="$1omposite$2"/>
<Typo word="Compound" find="\b([Cc])omp[ou]nd([a-z]*)\b" replace="$1ompound$2"/>
<Typo word="Comprehensive" find="\b([Cc])omphrehensi(ve(ly)?|on|bl[ey])\b" replace="$1omprehensi$2"/>
<Typo word="Comprise" find="\b([Cc])onpris(e[ds]?|ing)\b" replace="$1ompris$2"/>
<Typo word="Compromise" find="\b([Cc])ompr(?:imis|[io]miz)(e[ds]?|ing)\b" replace="$1ompromis$2"/>
<Typo word="(Com/Pro)pulsory" find="\b([Cc]om|[Pp]ro)puls[ae]r(y|ies)\b" replace="$1pulsor$2"/>
<Typo word="Compute" find="\b([Cc])m?opute(r?s?|d|ri[sz]e[ds]?)\b" replace="$1ompute$2"/>
<Typo word="Concentrate" find="\b([Cc])onsentrat(e[ds]?|ing|ions?)\b" replace="$1oncentrat$2"/>
<Typo word="Concept" find="\b([Cc])on(?:sept|cep([abd-su-z]))([a-z]*)\b" replace="$1oncept$2$3"/>
<Typo word="(Un)Concern" find="\b(C|c|[Uu]nc)onsern(s?|ing|ed)\b" replace="$1oncern$2"/>
<Typo word="Condemned" find="\b([Cc])ond(?:em+|amn)e([dr])\b" replace="$1ondemne$2"/>
<Typo word="Condominium" find="\b([Cc])ondominum(s?)\b" replace="$1ondominium$2"/>
<Typo word="Confides" find="\b([Cc])onfids\b" replace="$1onfides"/>
<Typo word="Confirmation" find="\b([Cc])onfirmmation\b" replace="$1onfirmation"/>
<Typo word="Conform" find="\b([Cc])oform(ers?|ed|ing|ance)\b" replace="$1onform$2"/>
<Typo word="Confront" find="\b([Cc])onfont(s?|ing|ation(al|ists?)?|ers?|ed)\b" replace="$1onfront$2"/>
<Typo word="Congratulate" find="\b([Cc])ongradulat(e[ds]?|ing|ions|ory)\b" replace="$1ongratulat$2"/>
<Typo word="Congressional" find="\b([Cc])ongres[is]ona(l(ly)?)\b" replace="$1ongressiona$2"/>
<Typo word="Conjecture" find="\b([Cc])onjecutr(e[ds]?|ing)\b" replace="$1onjectur$2"/>
<Typo word="(Dis/Un)Connect" find="\b(C|c|[Dd]isc|[Uu]nc)onect(s?|ions?|ed|ing|ives?|ors?)\b" replace="$1onnect$2"/>
<Typo word="Connecticut" find="\b[Cc]on(?:(?:nn+|)ec?t?icut*|n*et?c?icut*|n*ec?t?c?icut+)t\b" replace="Connecticut"/>
<Typo word="Connive" find="\b([Cc])oniv(e[drs]?|ing)\b" replace="$1onniv$2"/>
<Typo word="Connotation" find="\b([Cc])(?:o|an)notati(ons?|ve(ly)?)\b" replace="$1onnotati$2"/>
<Typo word="Conquered" find="\b([Cc])onqu(?:er|re|erre)d\b" replace="$1onquered"/>
<Typo word="Conqueror" find="\b([Cc])onquere(rs?)\b" replace="$1onquero$2"/>
<Typo word="(Sub/Un/Semi/Pre)Conscious" find="\b(C|c|[Ss]ubc|[Pp]rec|[Ss]emic|[Uu]nc)on[cs]io(us(ly)?|usness|nabl[ey])\b" replace="$1onscio$2"/>
<Typo word="(Sub/Un/Semi/Pre)Consciousness" find="\b(C|c|[Ss]ubc|[Pp]rec|[Ss]emic|[Uu]nc)ons(?:ciou|ici?ous?)ness(es)?\b" replace="$1onsciousness$2"/>
<Typo word="Consecutive" find="\b([Cc])onsectut?ive(ly)?\b" replace="$1onsecutive$2"/>
<Typo word="Consensus" find="\b([Cc])on(?:s?cens|e?senc)us\b" replace="$1onsensus"/>
<Typo word="Consent" find="\b([Cc])onscent(ed|ing)\b" replace="$1onsent$2"/>
<Typo word="Conservative" find="\b([Cc])onservitiv(es?|ely|ism)\b" replace="$1onservativ$2"/>
<Typo word="(Re)Consider" find="\b([Rr]ec|C|c)on(?:cid|sdid?)er(s?|ed|ing|abl[ey])\b" replace="$1onsider$2"/>
<Typo word="(In)Considerate" find="\b(C|c|[Ii]nc)onsiderite?(ly)\b" replace="$1onsiderate$2"/>
<Typo word="(Re)Considered" find="\b([Rr]ec|C|c)onsider(?:d|es)\b" replace="$1onsidered"/>
<Typo word="Consolidate" find="\b([Cc])onsol[ao]dat(e[ds]?|ing|ions?)\b" replace="$1onsolidat$2"/>
<Typo word="Consommé" find="\b([Cc])onsomme(s)?\b" replace="$1onsommé$2"/>
<Typo word="Conspiracy" find="\b([Cc])onspiri(cy|cies|tor[a-z]*)\b" replace="$1onspira$2"/>
<Typo word="(In)Constantly" find="\b(C|c|[Ii]nc)onstanly\b" replace="$1onstantly"/>
<Typo word="Consternation" find="\b([Cc])onstarnatio(ns?)\b" replace="$1onsternatio$2"/>
<Typo word="Constituent" find="\b([Cc])o(?:n?stis?tu|n[st]itu|nstutu|nstitute|nstis?tua|n[st]itea|n[st]itee)(?:en|ne|n)(?<!onstituen)(ts?|cy|cies)\b" replace="$1onstituen$2"/>
<Typo word="(Re/Un)Constitute" find="\b(C|c|[Rr]ec|[Uu]nc)onsitut([a-z]+)\b" replace="$1onstitut$2"/>
<Typo word="(Un)Constitution" find="\b(C|c|[Uu]nc)o(?:nstitu|[ns]titut)ion([a-z]*)\b" replace="$1onstitution$2"/>
<Typo word="(Un)Constrain" find="\b(C|c|[Uu]nc)onstain(t?s?|ed|ing)\b" replace="$1onstrain$2"/>
<Typo word="Consultant" find="\b([Cc])onsul(?:te|a)n(ts?)\b" replace="$1onsultan$2"/>
<Typo word="Consum(ption/ptive/e/mate)" find="\b([Cc])omsum(pti(ons?|ve)|er?s?|ed|ing|erism|mat(e[ds]?|ion))\b" replace="$1onsum$2"/>
<Typo word="Consumer" find="\b([Cc])onsumber(s?|ism)\b" replace="$1onsumer$2"/>
<Typo word="Consummate" find="\b([Cc])onsumat(e[ds]?|ing|ions?)\b" replace="$1onsummat$2"/>
<Typo word="Contain" find="\b([Cc])o[mu]n?tain(s?|e[dr]s?|ing)\b" replace="$1ontain$2"/>
<Typo word="Contains" find="\b([Cc])ontai?nes\b" replace="$1ontains"/>
<Typo word="(De)Contaminate" find="\b(C|c|[Dd]ec)ontaiminat(e[ds]?|ing|ions?)\b" replace="$1ontaminat$2"/>
<Typo word="(Con/Ex)temporaneous" find="\b([Cc]on|[Ee]x)temporan(?:[eou]{1,2})s(ly)?\b" replace="$1temporaneous$2"/>
<Typo word="(Con/Pre)tender" find="\b([Cc]on|[Pp]re)tendo(rs?)\b" replace="$1tende$2"/>
<Typo word="(Inter/Trans)Continental" find="\b([Ii]nterc|C|c|[Tt]ransc)ontine(?:tal|ntial)\b" replace="$1ontinental"/>
<Typo word="(Dis)Continue" find="\b(C|c|[Dd]isc)o(?:(?:ns|un)ti|nt)(?:in|nu)(e[ds]?|ing|ity|ations?|(?:al|ous)(?:ly)?)\b" replace="$1ontinu$2"/>
<Typo word="(Dis)Continue" find="\b(C|c|[Dd]isc)ontiu(e[ds]?|ing|al(ly)?)\b" replace="$1ontinu$2"/>
<Typo word="(Dis)Continuous" find="\b(C|c|[Dd]isc)onti(?:[nu]ou|nuo)s(ly)?\b" replace="$1ontinuous$2"/>
<Typo word="Contrary" find="\b([Cc])ontary\b" replace="$1ontrary"/>
<Typo word="Contrast" find="\b([Cc])on(?:stra|tar)st(s?|ing(ly)?|ed|able)?\b" replace="$1ontrast$2"/>
<Typo word="Control" find="\b([Cc])ontrol(ls?)\b" replace="$1ontro$2"/>
<Typo word="(Un)Controlled" find="\b(C|c|[Uu]nc)ontrol(e[dr]|ing)\b" replace="$1ontroll$2"/>
<Typo word="Controversial" find="\b([Cc])ontroversal(ly)?\b" replace="$1ontroversial$2"/>
<Typo word="Controversy" find="\b([Cc])ontr(?:[oa]ver?[ct]?|avers|[oa]ves)(y|ies|ial(ly)?)\b" replace="$1ontrovers$2"/>
<Typo word="(In)Convenient" find="\b(C|c|[Ii]nc)onv(?:eine|v?ienie|enia)n(t(ly)?|ces?)\b" replace="$1onvenien$2"/>
<Typo word="(Un)Conventional" find="\b(C|c|[Uu]nc)onve(?:tion|nti)al(ly|is[mt]|ize[ds]?)?\b" replace="$1onventional$2"/>
<Typo word="Converter" find="\b([Cc])onverto(rs?)\b" replace="$1onverte$2"/>
<Typo word="Conveyor" find="\b([Cc])onveye(rs?)\b" replace="$1onveyo$2"/>
<Typo word="(Un)Convince" find="\b(C|c|[Uu]nc)onvic(e[ds]?|ing(ly)?)\b" replace="$1onvinc$2"/>
<Typo word="(Un)Cooperate" find="\b(C|c|[Uu]nc)oop[ao]rat(e[ds]?|ing|ion|ive(ly)?)\b" replace="$1ooperat$2"/>
<Typo word="(Un)Coordinate" find="\b([Cc]|[Uu]nc)oordian?t([a-z]+)\b" replace="$1oordinat$2"/>
<Typo word="Copenhagen" find="\b[Cc]openhagan\b" replace="Copenhagen"/>
<Typo word="Copied" find="\b([Cc])oppied\b" replace="$1opied"/>
<Typo word="Copy" find="\b([Cc])poy(ing)?\b" replace="$1opy$2"/>
<Typo word="Copyright" find="\b([Cc])opywrite\b" replace="$1opyright"/>
<Typo word="Cordial" find="\b([Cc])oridal(s?|ity|ly)\b" replace="$1ordial$2"/>
<Typo word="(In/Disin)Corporate" find="\b(C|c|[Ii]nc|[Dd]isinc)orp(?:[ae]rt?|ort|ro)at(e[ds]?|ions?|ing)\b" replace="$1orporat$2"/>
<Typo word="(In)Correct" find="\b(C|c|[Ii]nc)(?:r+ect|or(?:rr+|)ec?tc?|or+etc?)(s?|ed|(ing)?(ly)?|ions?|[ai]b(le|ility)|or|ness)\b" replace="$1orrect$2"/>
<Typo word="Correspond" find="\b([Cc]orr|[Rr])(?:is|e)(?:po[ns]d|spon)(|s\b(?<!\b[Rr]espons)|ed|ing(ly)?|ents?|enc(?:es?|y|ies))\b" replace="$1espond$2"/>
<Typo word="Corresponde(nt/ce)" find="\b([Cc])orr[ei]spondan(ts?|ces?|cy)\b(?!\s+[Dd]es?\b)(?<!\b(?:[Ll]a|[Ll]es|des?|et)\s+\b([Cc])orr[ei]spondan(ts?|ces?|cy)\b(?!\s+[Dd]es?\b))" replace="$1orresponden$2"/>
<!--avoid French word correspondance(s) via lookaround for French articles-->
<Typo word="Corridor" find="\b([Cc])o(?:r[aei]do|rr?[aei]doo|c?o?rr[ae]do)(rs?)\b(?<![Cc]orredor)" replace="$1orrido$2"/>
<Typo word="Cotton_" find="\bcotten\b" replace="cotton"/><!--Don't match surname Cotten-->
<Typo word="Could" find="\b([Cc])oudl\b" replace="$1ould"/>
<Typo word="(C/W/Sh)ould have" find="\b([CcWw]|[Ss]h)ould\s+of\b(\S|\s+(?:been|[dg]one|had|said))\b" replace="$1ould have$2"/> 
<Typo word="Couldn't" find="\b([Cc])oudl?n't\b" replace="$1ouldn't"/>
<Typo word="Council" find="\b([Cc])ouci(ls?|llors?)\b" replace="$1ounci$2"/>
<Typo word="Countries" find="\b([Cc])oun(?:t?ir|ri)es\b" replace="$1ountries"/>
<Typo word="Country" find="\b([Cc])ontr(ies|y(sides?)?|m[ae]n|[iy]e?fied)\b" replace="$1ountr$2"/>  
<Typo word="Coup d'État" find="\b([Cc])oup(s?)\s+([Dd])['`]Etat\b" replace="$1oup$2 $3'État"/>
<Typo word="Coup d'état" find="\b([Cc])oup(s?)\s+([Dd])['`]?\s?[eê]tat?\b" replace="$1oup$2 $3'état"/>
<Typo word="Courier" find="\b([Cc])oururie(rs?)\b" replace="$1ourie$2"/>
<Typo word="Covenant" find="\b([Cc])onvenant([a-z]*)\b" replace="$1ovenant$2"/>
<Typo word="Creüsa" find="\bcreusa\b" replace="Creüsa"/>
<Typo word="Create" find="\b([Cc])reaete(s?|d)\b" replace="$1reate$2"/>
<Typo word="credence" find="\bcreedence\b" replace="credence"/><!--Don't match to Creedence, which usually refers to the band Creedence Clearwater Revival-->
<Typo word="(In)Credible" find="\b(C|c|[Ii]nc)read[ia]b(l[ey]|ility)\b" replace="$1redib$2"/>
<Typo word="Criteria" find="\b([Cc])riteri(?:a|on)s\b(?<![Tt]he Criterions)" replace="$1riteria"/><!--The Criterions are a group-->
<Typo word="Criterion" find="\b([Cc])ritereon\b" replace="$1riterion"/>
<Typo word="Critical" find="\b([Cc])r(?:tic|itc?|itis|ittic)(al(ly)?|i[sz](e[ds]?|ing)|isms?)\b" replace="$1ritic$2"/>
<Typo word="Critics" find="\b([Cc])riticists\b" replace="$1ritics"/>
<Typo word="Crocodile" find="\b([Cc])rockodil(es?)\b" replace="$1rocodil$2"/>
<Typo word="Crucifixion" find="\b([Cc])rucifiction\b" replace="$1rucifixion"/>
<Typo word="Crudités" find="\b([Cc])rudite(s?)\b" replace="$1rudité$2"/>
<Typo word="Cruise" find="\b([Cc])rusi?(e[ds]?|ers?|ing)\b(?<!Cruser?)" replace="$1ruis$2"/><!--Cruse & Cruser are surnames-->
<Typo word="Crystalli(s/z)ation_" find="\b([Cc])rystal([io][a-z]+)\b" replace="$1rystall$2"/>
<Typo word="Cuisine" find="\b([Cc])usin(es?)\b" replace="$1uisin$2"/>
<Typo word="Culinary" find="\b([Cc])ul(?:lina|iner?|inar)ry\b" replace="$1ulinary"/>
<Typo word="(C/F)ulminate" find="\b([CcFf])uliminat(e[ds]?|ing|ions?)\b" replace="$1ulminat$2"/>
<Typo word="(Agri/Horti/Multi)Cultural" find="\b(C|c|[Aa]gric|[Hh]ortic|[Mm]ultic)ult(ral[a-z]*)\b" replace="$1ultu$2"/>
<Typo word="Cumulative" find="\b([Cc])umulatative(ly)?\b" replace="$1umulative$2"/>
<Typo word="Curaçao" find="\bCuracao\b" replace="Curaçao"/>
<Typo word="Curiosity" find="\b([Cc])uriousit(y|ies)\b" replace="$1uriosit$2"/>
<Typo word="Currently" find="\b([Cc])ur(?:r?entel|r?en[lt]|ente?l|rente?le)e?y\b" replace="$1urrently"/>
<Typo word="Curriculum" find="\b([Cc])(?:iriculu|urricule)m\b" replace="$1urriculum"/>
<Typo word="Customer" find="\b([Cc])u(?:tso|sot)mer(s)?\b" replace="$1ustomer$2"/>
<Typo word="Cylinder" find="\b([Cc])(?:yc|i)lind(ers?|rical(ly)?)\b" replace="$1ylind$2"/>
<Typo word="Cylindrical" find="\b([Cc])ylinderical(ly)?\b" replace="$1ylindrical$2"/>
</source>

===D===
<source lang="xml">
<Typo word="Dardanelles" find="\b(?:[Dd]arde|darda)nelles\b" replace="Dardanelles"/>
<Typo word="Dante Alighieri" find="\bDante\s+Aligh(?:ei?ri|irei?)\b" replace="Dante Alighieri"/>
<Typo word="Daughter" find="\b([Dd])au(?:gt?h|gt|hg?t)er(s?)\b" replace="$1aughter$2"/>
<Typo word="Deal" find="\bdael(s?)\b" replace="deal$1"/><!--don't match the surnames Dael or Daels-->
<Typo word="Deal" find="\b([Dd])ael(t|ings?)\b" replace="$1eal$2"/>
<Typo word="(De)Caffeinate" find="\b([Dd]ec|C|c)af(?:fi?e?|ei)nat(e[ds]?|ing|ion)\b" replace="$1affeinat$2"/>
<Typo word="Decide" find="\b([Dd])esi(de[ds]?|ding|sions?|dedly)\b" replace="$1eci$2"/>
<Typo word="(Un)Decidedly" find="\b(D|d|[Uu]nd)ecidely\b" replace="$1ecidedly"/>
<Typo word="(In)Decision" find="\b(D|d|[Ii]nd)e(?:cis|sc?isi|sici)(ons?|ve(ly)?)\b" replace="$1ecisi$2"/>
<Typo word="Decrees" find="\b([Dd])ecress\b" replace="$1ecrees"/>
<Typo word="Defensive" find="\b([Dd])efencive([a-z]*)\b" replace="$1efensive$2"/>
<Typo word="Deficit" find="\b([Dd])efict(s?)\b" replace="$1eficit$2"/>
<Typo word="(Re/Un)Define" find="\b(D|d|[Rr]ed|[Uu]nd)ef(?:fn?in|f?inin)(e[ds]?|ing|itions?)\b" replace="$1efin$2"/>
<Typo word="(In)Definition" find="\b(D|d|[Ii]nd)ef(?:f?inet|ninit|f+inite?|inti|nint?i?)(ons?|ve(s?|ly|ness))\b" replace="$1efiniti$2"/>
<Typo word="Degradation" find="\b([Dd])egredation\b" replace="$1egradation"/>
<Typo word="Degrade" find="\b([Dd])egrat(e[ds]?|ing)\b" replace="$1egrad$2"/>
<Typo word="Deity" find="\b([Dd])iet(y|ies)\b" replace="$1eit$2"/>
<Typo word="Déjà Vu" find="\b([Dd])(?:éja|ejà)\s+([Vv])u\b" replace="$1éjà $2u"/><!--"deja vu" should not be replaced, see [[wikt:deja vu]]-->
<Typo word="(D/R)elegate" find="\b([DdRr])elagat(e[ds]?|ing|ions?)\b" replace="$1elegat$2"/>
<Typo word="Delineate" find="\b([Dd])eliniat([a-z]+)\b" replace="$1elineat$2"/>
<Typo word="Delirious" find="\b([Dd])elerious(ly)?\b" replace="$1elirious$2"/>
<Typo word="Delusively" find="\b([Dd])elusionally\b" replace="$1elusively"/>
<Typo word="(Mis)Demeanor" find="\b(D|d|[Mm]isd)(?:amenou?|eme(?:no|a?ne))(rs?)\b" replace="$1emeano$2"/>
<Typo word="(Un)Democrat" find="\b(D|d|[Uu]nd)e(?:o?m|mor)cra([ct][a-z]*)\b" replace="$1emocra$2"/>
<Typo word="Demographic" find="\b([Dd])emographical\b" replace="$1emographic"/>
<Typo word="Demolition" find="\b([Dd])emolisio(ns?)\b" replace="$1emolitio$2"/>
<Typo word="(D/R)emonstrate" find="\b([DdRr])emo(?:str|n[st]r)at(e[ds]?|ing|ions?|ive(s?|ly)|ors?)\b" replace="$1emonstrat$2"/>
<Typo word="Denigrate" find="\b([Dd])enegrat(e[ds]?|ing|ors?|ions?)\b" replace="$1enigrat$2"/>
<Typo word="Dénouement" find="\b([Dd][eé])noument\b" replace="$1nouement"/><!--"denouement" should not be replaced, see [[wikt:denouement]]-->
<Typo word="Department" find="\b([Dd])e(?:par|ptart?|aprt)me?nt(al(ly)?|s)?\b" replace="$1epartment$2"/>
<Typo disabled="Département(al)" find="\b([Dd])epartement(ale?)?\b" replace="$1épartement$2"/><!--disabled per talk, departement is often department instead-->
<Typo word="(In)Dependent" find="\b([Ii]nd|[Dd])(?:(?:en|i)?pen?d[ae]n|en?pen?dan|ependende|ndepeden)(t|tly|ce)\b(?<!\b[Dd]ependants?)(?<![Ll]'independance)" replace="$1ependen$2"/><!--don't match dependant, (L/l)'independance-->
<Typo word="Depict" find="\b([Dd])espict(s?|ions?)\b" replace="$1epict$2"/>
<Typo word="Derivative" find="\b([Dd])erivia?ti(ves?|ons?)\b" replace="$1erivati$2"/>
<Typo word="Derive" find="\b([Dd])(?:iriv|eriviat)(e[ds]?|ing|ations?)\b" replace="$1eriv$2"/>
<Typo word="Derogatory" find="\b([Dd])erog[io]tory\b" replace="$1erogatory"/>
<Typo word="Derrière" find="\b([Dd])er+ier+e(s?)\b" replace="$1errière$2"/>
<Typo word="Descendant" find="\b([Dd])e(?:scendand|[cs]end[ae]nt)(s?)\b" replace="$1escendant$2"/>
<Typo word="Descriptor" find="\b([Dd])e(?:scr?|s?cri?)ipte(rs?)\b" replace="$1escripto$2"/>
<Typo word="Desiccate" find="\b([Dd])es+[aei]cat(e[ds]?|ions?)\b" replace="$1esiccat$2"/>
<Typo word="Design" find="\b([Dd])(?:[ei]s(?:sigi?n|gin|ing)|isign)(s?|ed|ers?|ing)\b" replace="$1esign$2"/>
<Typo word="Desktop" find="\b([Dd])esktiop(s)?\b" replace="$1esktop$2"/>
<Typo word="Desperate" find="\b([Dd])esp[ai]rat(e(ly)?|ion)\b" replace="$1esperat$2"/>
<Typo word="Destroy" find="\b([Dd])est(?:ory|roi)(s?|ed|ers?|ing)\b" replace="$1estroy$2"/>
<Typo word="(Non/In)Destruct" find="\b([Dd](?!istructs?\b)|[Ii]nd|[Nn]ond)ist?ruct([a-z]*)\b" replace="$1estruct$2"/><!--avoid "distruct" (district?)-->
<Typo word="Detach" find="\b([Dd])etatch(e[ds]|ing|ments?|able)?\b" replace="$1etach$2"/>
<Typo word="Detail" find="\b([Dd])e(?:tail|ati)l(s?|ed|ing)\b" replace="$1etail$2"/>
<Typo word="(In)Detect" find="\b(D|d|[Ii]nd)ectect([a-z]*)\b" replace="$1etect$2"/>
<Typo word="(Un)Detectable" find="\b([Uu]n|D|d)etecabl([ey])\b" replace="$1etectabl$2"/>
<Typo word="Détente" find="\b([Dd])etente\b" replace="$1étente"/>
<Typo word="Deterrent" find="\b([Dd])eter(?:e|r?a)n(ts?|ce)\b" replace="$1eterren$2"/>
<Typo word="Deteriorate" find="\b([Dd]et)e(?:o?r|rior)iat(e[ds]?|ing|ion)\b" replace="$1eriorat$2"/>
<Typo word="Determine" find="\b([Dd])et(?:ermin|[er]m)in(e[ds]?|ing|ate|ations?)\b" replace="$1etermin$2"/>
<Typo word="(De/Nu)triment" find="\b([Dd]e|nu)tr[ea]men(ts?|tal)\b" replace="$1trimen$2"/>
<Typo word="Devastate" find="\b([Dd]ev)(?:[ei]sta|asa?)t(e[ds]?|ing|ion)\b" replace="$1astat$2"/>
<Typo word="Develop" find="\b([Dd]ev)(?:el+[aeiu]?|[aiou]?l+.?|ell.?)p(s?|e[dr]|ing|ment(s?|al(ly)?))\b" replace="$1elop$2"/>
<Typo word="Developer" find="\b([Dd])evel(?:opo|eop)r(s)?\b" replace="$1eveloper$2"/>
<Typo word="Development" find="\b([Dd])e(?:(?:vol[oe]|levo|vel)p[oe]?men|velope?mn)(ts?|tal)\b" replace="$1evelopmen$2"/>
<Typo word="Devastate" find="\b([Dd])ev(?:[ei]st?|as)at(es?|ed|ing|ion)\b" replace="$1evastat$2"/>
<Typo word="Device" find="\b([Dd])ivice(s)?\b" replace="$1evice$2"/>
<Typo word="Diabolical" find="\b([Dd])i(?:ab|bo)lica(l(ly)?)\b" replace="$1iabolica$2"/>
<Typo word="Diameter" find="\b([Dd])iamate(rs?)\b" replace="$1iamete$2"/>
<Typo word="Diamonds" find="\b([Dd])iamons\b" replace="$1iamonds"/>
<Typo word="Diarrhea" find="\b([Dd])iar[hr]ea\b" replace="$1iarrhea"/>
<Typo word="Dichotomy" find="\b([Dd])ichtom(y|ies)\b" replace="$1ichotom$2"/>
<Typo word="Didn't" find="\b([Dd])idint\b" replace="$1idn't"/>
<Typo word="Differentiate" find="\b([Dd])iff?[aie]?ren(?:tiatiat|[cs]iat)(e[ds]?|ing|ions?)\b" replace="$1ifferentiat$2"/>
<Typo word="Difficult" find="\b([Dd])if(?:f?iculi|icul|f?cul|f?i?cuil)t(l?y|ies)?\b" replace="$1ifficult$2"/>
<Typo word="Diffuse" find="\b([Dd])ifus(er?[ds]?|ing|ely|eness|ion|ive)\b" replace="$1iffus$2"/>
<Typo word="Dilapidate" find="\b([Dd])(?:e|il)lapidat(e[ds]?|ion)\b" replace="$1ilapidat$2"/>
<Typo word="Dilemma" find="\b([Dd]il)l?e(?:nm|mn|mmm+)a(s)?\b" replace="$1emma$2"/>
<Typo word="_Dilemma" find="\bdil(?:e|lem?)ma(s?)\b" replace="dilemma$1"/>
<Typo word="Dimension" find="\b([Dd])ime(?:nt?|sn)ion(s?|al(ly|ity)?)\b" replace="$1imension$2"/>
<Typo word="Diminish" find="\b([Dd])em+inish(e[ds]|ing|ments?|abl[ey])?\b" replace="$1iminish$2"/>
<Typo word="Diminutive" find="\b([Dd])iminuiti([a-z]+)\b" replace="$1iminuti$2"/>
<Typo word="Dining" find="\b([Dd])inning\s+([Aa]rea|[Cc]ar|[Cc]lub|[Hh]all|[Rr]oom|[Tt]able)(s?)\b" replace="$1ining $2$3"/>
<Typo word="Diocese" find="\b([Dd])ioses(es?|an)\b" replace="$1ioces$2"/>
<Typo word="Diplomacy" find="\b([Dd])iplomancy\b" replace="$1iplomacy"/>
<Typo word="(In)Directly" find="\b(D|d|[Ii]nd)(?:riectl|irect)y\b" replace="$1irectly"/>
<Typo word="Disability" find="\b([Dd])isibilit(y|ies)\b" replace="$1isabilit$2"/>
<Typo word="Disappear" find="\b([Dd])is+ap+ear+(?<!isappear)(s?|ed|ing|ances?)\b" replace="$1isappear$2"/>
<Typo word="Disaster" find="\b([Dd])iaste(rs?)\b" replace="$1isaste$2"/>
<Typo word="Disastrous" find="\b([Dd])isa(?:ste|t)rous(ly)?\b" replace="$1isastrous$2"/>
<Typo word="Disciple" find="\b([Dd])i[cs]ipl(es?|in[ei][a-z]*)\b" replace="$1iscipl$2"/>
<Typo word="(Un)Discipline 1" find="\b(D|d|[Uu]nd)i(?:scpline?|s?ciplin)([ds])?\b" replace="$1iscipline$2"/>
<Typo word="(Un)Discipline 2" find="\b(D|d|[Uu]nd)i[sc]ic?(plin[a-z]+)\b" replace="$1isci$2"/>
<Typo word="Discography" find="\b([Dd])is(?:ograph|cograp)(y|ies)?\b" replace="$1iscograph$2"/>
<Typo word="(Re)Discover" find="\b(D|d|[Rr]ed)i[cs]over([sy]?|e[dr]|ing|ies)\b" replace="$1iscover$2"/>
<Typo word="Discrepancy" find="\b([Dd])iscrepen[cs](y|ies)\b" replace="$1iscrepanc$2"/>
<Typo word="Discuss" find="\b([Dd])(?:i|es)cs?uss(e[ds]|ing|ions?)?\b" replace="$1iscuss$2"/>
<Typo word="Disdain" find="\b([Dd])istain(s?|ed|ing|ful(ly|ness)?)\b" replace="$1isdain$2"/>
<Typo word="(Dis)enchanted" find="\b([Dd]ise|E|e)nchanged\b" replace="$1nchanted"/>
<Typo word="Disguise" find="\b([Dd])i(?:sq|g)uis(e[ds]?|ing)\b" replace="$1isguis$2"/>
<Typo word="Disparagingly" find="\b([Dd])isparingly\b" replace="$1isparagingly"/>
<Typo word="Display" find="\b([Dd])i(?:apla|spal)y(s?|ed)\b" replace="$1isplay$2"/>
<Typo word="displease" find="\bunplease([ds])?\b" replace="displease$1"/>
<Typo word="Displease" find="\bUnplease([ds])?\b" replace="Displease$1"/>
<Typo word="Dissident" find="\b([Dd])is(?:(?:|ss+)[aeio]d[ae]|s+[aeo]d[ae]|s+[aeio]da)n(ts?|ce)\b" replace="$1issiden$2"/>
<Typo word="(In)Distinct_" find="\b(D|d|[Ii]nd)is(?:ctinc|tic|inc|t[ai]n(?=ti))t(i(ve(ly)?|on)|ly)?\b" replace="$1istinct$2"/><!--Distin is a name-->
<Typo word="(Un)Distort" find="\b(D|d|[Uu]nd)is(ort[a-z]+)\b" replace="$1ist$2"/>
<Typo word="Distribute" find="\b([Dd])i(?:si)?tribut(e[ds]?|ing|ors?|ions?)\b" replace="$1istribut$2"/>
<Typo word="Distribution" find="\b([Dd])istribusion\b" replace="$1istribution"/>
<Typo word="District" find="\b([Rr]ed|D|d)is(?:rt?ic?t|t?ri[ct]|itrict)(s?|ed|ing)\b" replace="$1istrict$2"/>
<Typo word="Divide_" find="\bdevi(de[drs]?|ding|sions?)\b" replace="divi$1"/><!--Do not match surname Devide-->
<Typo word="Division" find="\b([Dd])iv(?:is|si)(ons?)\b" replace="$1ivisi$2"/>
<Typo word="Doctrines" find="\b([Dd])oc[rt]ine(s)?\b" replace="$1octrine$2"/>
<Typo word="(Un)Document" find="\b(D|d|[Uu]nd)(?:occ?u(?:eme?nt|mnet|metn|mant)|(?:oc|c*)cument)([a-z]*)\b" replace="$1ocument$2"/>
<Typo word="Does" find="\b([Dd])oe(?:ns|se)\b" replace="$1oes"/>
<Typo word="Doesn't" find="\b([Dd])o(?:ens|se?n)'?t\b(?<!Wilma Doesnt)" replace="$1oesn't"/><!--Do not match name Wilma Doesnt-->
<Typo word="Doing" find="\b([Dd])o(?:ign|img|ind|nig)\b" replace="$1oing"/>
<Typo word="Dollar" find="\b([Dd])oller(s)?\b(?<!Mikhail Doller)" replace="$1ollar$2"/><!--Not [[Mikhail Doller]]-->
<Typo word="Don't" find="\b([Dd])ont\b'?(?!\s+(ils?|elles?|les?|la|des?|une?)\b)" replace="$1on't"/>
<!--avoid correct French by use of lookahead for French words-->
<Typo word="Double" find="\b([Dd])oulbe(d?|s)\b" replace="$1ouble$2"/>
<Typo word="Dramatic" find="\b([Dd])ramtic(ally|s?)\b" replace="$1ramatic$2"/>
<Typo word="Draughtsman" find="\b([Dd])ra(f|ugh)t(m[ae]n[a-z]*|wom[ae]n)\b" replace="$1ra$2ts$3"/>
<Typo word="Dravidian" find="\b([Dd])ravadian\b" replace="$1ravidian"/>
<Typo word="Dream" find="(?!\bDeram\b)\b([Dd])eram(s?|ing|ers?)\b" replace="$1ream$2"/><!--don't fix Deram (Records)-->
<Typo word="Dreams" find="\b([Dd])(?:erams|reasm)\b" replace="$1reams"/>
<Typo word="Drink" find="\b([Dd])rnik(s?|ers?|ing)\b" replace="$1rink$2"/>
<Typo word="Drummer" find="\b([Dd])rum(ers?|ing)\b" replace="$1rumm$2"/>
<Typo word="Dumbbell" find="\b([Dd])umbell(s)?\b" replace="$1umbbell$2"/>
<Typo word="Duplicate" find="\b([Dd])upil?cat([a-z]+)\b" replace="$1uplicat$2"/>
<Typo word="du Pré" find="\b(Jacqueline|Hil+ary|Iris)\s+[dD]u\s*[pP]r(?:é?eé?|e?èe?)\b" replace="$1 du Pré"/>
<Typo word="During" find="\b([Dd])u(?:ri|rrin|t?in)g\b" replace="$1uring"/>
<Typo word="Durrës" find="\bDurres\b" replace="Durrës"/>
<Typo word="(D/L/T)ying" find="\b([DdLlTt])ieing\b" replace="$1ying"/>
</source>

===E===
<source lang="xml">
<Typo word="(En/De)cipher" find="\b([Ee]n|[Dd]e)cy(phers?)\b" replace="$1ci$2"/>
<Typo word="(Endo/Mega/Mono)liths" find="\b([Ee]ndo|[Mm](ega|ono))lithes\b" replace="$1liths"/>
<Typo word="(Ex/In/Pro)hibition" find="\b([Ee]x|[Ii]n|[Pp]ro)(?:hib|ibi)tion((is[mt])?s?)\b" replace="$1hibition$2"/>
<Typo word="Each other" find="\b([Ee])achother\b" replace="$1ach other"/>
<Typo word="Each" find="\b([Ee])ahc\b" replace="$1ach"/>
<Typo word="Earlier" find="\b([Ee])alie(r|st)\b" replace="$1arlie$2"/>
<Typo word="Early" find="(?!\bEraly\b)\b([Ee])(?:ear|ra)l(y|ier|iest)\b" replace="$1arl$2"/>
<Typo word="(L/Y)Earning" find="\b([LlYy]e|E|e|[Uu]nle|[Rr]ele)arnign(s)?\b" replace="$1arning$2"/>
<Typo word="Ecc-" find="\b([Ee]c)(lesiast[a-z]*|entric[a-z]*)\b" replace="$1c$2"/>
<Typo word="écla(t/ir)" find="\becla(t|irs?)\b" replace="écla$1"/>
<Typo word="Eclectic" find="\b([Ee])(?:cc|g)lectic(s?|ally|ism)\b" replace="$1clectic$2"/>
<Typo word="Eclipse" find="\b([Ee])clisps?(e[ds]?|ing)\b" replace="$1clips$2"/>
<Typo word="(Un)Economic" find="\b(E|e|[Uu]ne)comonic(al(ly)?|s)?\b" replace="$1conomic$2"/>
<Typo word="Economy" find="\b([Ee])c[ce]onom([a-z]+)\b" replace="$1conom$2"/>
<Typo word="Ecstasy" find="\b([Ee])sctasy\b" replace="$1cstasy"/>
<Typo word="Edit" find="\b([Ee])ditt(ed|ing|or(ial)?s?)\b" replace="$1dit$2"/>
<Typo word="Education" find="\b([Ee])duac?t(e[ds]?|ing|ors?|ion(al(ly)?)?)\b" replace="$1ducat$2"/>
<Typo word="Education" find="\b([Ee])duction\b(?<=(?:[Bb]oards?\s{1,9}of|[Cc]o(?:mmunity|llege)|[Dd]epartment\s{1,9}of|[Ee](?:arl|lementar)y|[Ff](?:ormal|urther)|[Hh]igher|[Mm]inist(?:ers?|ry)\s{1,9}(?:of|for)|[Pp](?:hysical|rimary)|[Ss](?:econdary|pecial|ex|chools?\s{1,9}of)|[Tt]ertiary)\s{1,9}[Ee]duction)\b" replace="$1ducation"/>
<Typo disabled="Eels" find="\b([Ee])les\b" replace="$1els"/>
<Typo word="(In)Efficient" find="\b(E|e|[Ii]ne)ff(?:eci?|ic)en([a-z]+)\b" replace="$1fficien$2"/>
<Typo word="Eighteen" find="\b([Ee])ight-?teen((th)?s?)\b" replace="$1ighteen$2"/>
<Typo word="Eighth" find="\b([Ee])igth\b" replace="$1ighth"/>
<Typo word="Eighty" find="\b([Ee])igt?h(y|ies)\b" replace="$1ight$2"/>
<Typo word="Either" find="\b([Ee])iter\b" replace="$1ither"/>
<Typo word="(S)Elect" find="\b([Ss]?e|E)llect([a-z]*)\b" replace="$1lect$2"/>
<Typo word="Electric" find="\b([Ee])let+ri(c[a-z]*)\b" replace="$1lectri$2"/>
<Typo word="Electricity" find="\b([Ee])le(?:ctric|trici)(ty|ans?)\b" replace="$1lectrici$2"/>
<Typo word="Elemental" find="\b([Ee])limenta(l|ry)\b" replace="$1lementa$2"/>
<Typo word="Elephant" find="\b([Ee])lphan(ts?)\b" replace="$1lephan$2"/>
<Typo word="Eleventh" find="\b([Ee])levn?eth\b" replace="$1leventh"/>
<Typo word="(In)Eligible" find="\b(E|e|[Ii]ne)l(?:lig[ai]|iga?)b(le|ility)\b" replace="$1ligib$2"/>
<Typo word="Eliminate" find="\b([Ee])l(?:emin|imi)at(e[ds]?|ing|ions?)\b" replace="$1liminat$2"/>
<Typo word="Else(where)" find="\b([Ee])sle(where)?\b" replace="$1lse$2"/>
<Typo word="Emanate" find="\b([Ee])minat(e[ds]?|ations?)\b" replace="$1manat$2"/>
<Typo word="Embarrass" find="\b([Ee])mbar(?:as|ra)s(e[ds]|ing(ly)?|ments?)?(?!\s+River\b)\b" replace="$1mbarrass$2"/><!--avoid Embarras River-->
<Typo word="Embarrassment" find="\b([Ee])mbar(?:ra|as?)se?(ments?|ing|ed)\b" replace="$1mbarrass$2"/>
<Typo word="Embezzle" find="\b([Ee])mbezz?ell(e[drs]?|ing|ment)\b" replace="$1mbezzl$2"/>
<Typo word="Emblematic" find="\b([Ee])mblamatic(ally)?\b" replace="$1mblematic$2"/>
<Typo word="Émigré" find="\bEmigr[éè](e?s?)\b" replace="Émigré$1"/>
<Typo word="émigré" find="\bemigr[éè](e?s?)\b" replace="émigré$1"/><!--"emigre" should not be replaced, see [[wikt:emigre]]-->
<Typo word="Émile Zola" find="\bEmile\s+Zola\b" replace="Émile Zola"/>
<Typo word="(E/Pro/Im/Pree)minent" find="\b([Pp]ro|[Ii]m|[Pp]ree|E|e)minan(ces?|cy|t(ly)?)\b" replace="$1minen$2"/>
<Typo word="Emissary" find="\b([Ee])m(?:m?isar?|m?is+ar)r(y|ies)\b" replace="$1missar$2"/>
<Typo word="(E/O)mission" find="\b([EeOo])(?:m+i[cst]|mmi[cst]+)io(ns?)\b" replace="$1missio$2"/>
<Typo word="(E/O)mitted" find="\b([EeOo])m(?:m?i|mit?)t(e[dr]|ing)\b" replace="$1mitt$2"/>
<Typo word="Emphasi(s/z)e" find="\b([Ee])mphai([sz]ed?)\b" replace="$1mphasi$2"/>
<Typo word="Emphasis" find="\b([Ee])mph[as]is(ed?|ing)?\b" replace="$1mphasis$2"/>
<Typo word="Emperor" find="\b([Ee])mp(?:ere|o?r[eo])r(s?|ship)\b" replace="$1mperor$2"/>
<Typo word="Emphysema" find="\b([Ee])mphys[iy]ma\b" replace="$1mphysema"/>
<Typo word="Empirical" find="\b([Ee])mperic(al(ly)?|is[mt])\b" replace="$1mpiric$2"/>
<Typo word="(Un)Employ" find="\b([Uu]ne|E|e)mply(s?|e[edr]?s?|ing|ment|ab[a-z]*)\b" replace="$1mploy$2"/>
<Typo word="Employ" find="\bImploy(ers?|ed|ing|s?|ments?)\b" replace="Employ$1"/>
<Typo word="employ" find="\bimploy(ers?|ed|ing|s?|ments?)\b" replace="employ$1"/>
<Typo word="Encyclopedia" find="\b([Ee])ncylc?opedi(as?|c)\b" replace="$1ncyclopedi$2"/>
<Typo word="Encyclopedia(1)" find="\b([Ee]nc)(?:lyclop|ylc?op|ycolp|ycopl?|yclo)(a?e|æ)di(as?|c)\b" replace="$1yclop$2di$3"/>
<Typo word="Encyclopedia(2)" find="\b([Ee]ncyclop)(?:e?a)?di(as?|c)\b" replace="$1edi$2"/>
<Typo word="Encyclopædia (Iranica|Metropolitana)" find="\bEncyclopa?edia\s+(Iranica|Metropolitana)\b" replace="Encyclopædia $1"/>
<Typo word="Encyclopaedia Judaica" find="\bEncyclop([eæ])?dia\s+Judaica\b" replace="Encyclopaedia Judaica"/>
<Typo word="Encyclopædia Britannica(1)" find="\b[Ee]ncyclo?p(?:a?e?|æ)dia\s+Bri(?:ttan+ic+|t+anic+|t+an+icc|t+an+i)a+\b" replace="Encyclopædia Britannica"/><!--correct "Britannica"-->
<Typo word="Encyclopædia Britannica(2)" find="\b[Ee]ncycl(?:op|o?pa?e)dia\s+[Bb]rit+an+ic*a+\b" replace="Encyclopædia Britannica"/><!--correct "Encyclopædia"-->
<Typo word="Endeavo(u)r" find="\b([Ee])ndev(ou?r)(s?|ed|ing)\b" replace="$1ndeav$2$3"/>
<Typo word="Ending" find="\b([Ee])ndig\b" replace="$1nding"/>
<Typo word="(Arch)Enemy" find="\b([Aa]rche|E|e)(?:[nm]i|me|nen)m(y|ies)\b" replace="$1nem$2"/><!--don't find "Archey"-->
<Typo word="(Arch)Enemy" find="\b([Aa]rche|E|e)nemie\b" replace="$1nemy"/>
<Typo word="Engineer" find="\b([Ee])ng(?:i?ene|n?e|in)er(s?|ed|ing)\b" replace="$1ngineer$2"/>
<Typo word="Enhancement" find="\b([Ee])nchance(ments?)\b" replace="$1nhance$2"/>
<Typo word="Enlightenment" find="\b([Ee])n(?:glighte?n?|g?lightn?)(ments?)\b" replace="$1nlighten$2"/>
<Typo word="Enmity" find="\b([Ee])(?:mn|nem)ity\b" replace="$1nmity"/>
<Typo word="Ennoble" find="\b([Ee])nobl(ed?|ing)\b" replace="$1nnobl$2"/>
<Typo word="Enormous" find="\b([Ee])nourmous(ly)?\b" replace="$1normous$2"/>
<Typo word="Enough" find="\b([Ee])nou(?:pht?|ght)\b" replace="$1nough"/>
<Typo word="Ensconced" find="\b([Ee])nsconsed\b" replace="$1nsconced"/>
<Typo word="(Dis)Entangle" find="\b(E|e|[Dd]ise)ntagle([ds]?|ments?)\b" replace="$1ntangle$2"/>
<Typo word="Enthusiasm" find="\b([Ee])nt(?:husia|usias)([mt]s?|tic\w?)\b" replace="$1nthusias$2"/>
<Typo word="Entire" find="\b([Ee])n(?:itr|tri)e([lt]y)?\b" replace="$1ntire$2"/>
<Typo word="Entire(l/t)y" find="\b([Ee])ntie?ri?([lt]y|ties)" replace="$1ntire$2"/>
<Typo word="(Non)Entity" find="\b(E|e|[Nn]one)ntitit(y|ies)\b" replace="$1ntit$2"/>
<Typo word="Entrepreneur" find="\b([Ee])ntrep(?:er?neu|r?enue?)r([a-z]*)\b" replace="$1ntrepreneur$2"/>
<Typo word="entrusted" find="\bIntrust(ed|s?|ing)\b" replace="Entrust$1"/>
<Typo word="entrusted" find="\bintrust(ed|s?|ing)\b" replace="entrust$1"/>
<Typo word="Envelop" find="\benvelope(s?\s+(?:me|him|us|them))\b" replace="envelop$1"/>
<Typo word="Environment" find="\b([Ee])nvi?(?:rion?|ro|orn?)men(t[a-z]+)\b" replace="$1nvironmen$2"/>
<Typo word="Épée" find="\bEp[eéè]e(s?)\b" replace="Épée$1"/>
<Typo word="épée" find="\bep[eéè]e(s?)\b" replace="épée$1"/>
<Typo word="Episode" find="\b([Ee])p(?:idsod|i?siod|isoid|ispod|sisod|osid|isdo)(es?|ic(al(ly)?)?)\b" replace="$1pisod$2"/> 
<Typo word="Eponymous" find="\b([Ee])p(?:nymo|onym)us(ly)?\b" replace="$1ponymous$2"/>
<Typo word="Equator" find="\b([Ee])quitor(ial(?:ly)?)\b" replace="$1quator$2"/>
<Typo word="Equilibrium" find="\b([Ee])quilibrum\b" replace="$1quilibrium"/>
<Typo word="(Non)Equilibrium" find="\b(E|e|[Nn]one)quil(?:l?ib|libr)(iums?|ia|ate[ds]?|ating)\b" replace="$1quilibr$2"/>
<Typo word="Equipment" find="\b([Ee])q(?:u?ip|iu?p?|ui?)(?:pi?|)(?<![Ee]quip)ment\b" replace="$1quipment"/>
<Typo word="Equipped" find="\b([Ee])(?:quip|qupp|qupi|quppi)(ed|ing)\b" replace="$1quipp$2"/>
<Typo word="Equivalen(ce/t)" find="\b([Ee])qui(?:ale|v[aei]la|le|vlal[ea]|v[ei]le)n(ts?|tly|ces?)\b" replace="$1quivalen$2"/>
<Typo word="Eradicate" find="\b([Ee])rradica([bnt][a-z]+)\b" replace="$1radica$2"/>
<Typo word="Erect" find="\b([Ee])rrect(s?|ing|ed|ions?|ly)\b" replace="$1rect$2"/>
<Typo word="Erratically" find="\b([Ee])ratica?ly\b" replace="$1rratically"/>
<Typo word="Erroneous" find="\b([Ee])r(?:oni?|roni?)ous(ly)?\b" replace="$1rroneous$2"/>
<Typo word="Erupt" find="\b([Ee])rrupt(s?|ed|ing|ions?)\b" replace="$1rupt$2"/>
<Typo word="Especially" find="\b([Ee])(?:(?:xpeci|spe(?:c|si))al?|specia|cspec(?:ai|ia)l)ly\b" replace="$1specially"/>
<Typo word="espresso" find="\bexpresso\b" replace="espresso"/><!--don't match [[Expresso]]-->
<Typo word="Essence" find="\b([Ee])ssens(es?)\b" replace="$1ssenc$2"/>
<Typo word="(Non/Quint)Essential" find="\b(E|e|[Nn]one|[Qq]uinte)s(?:sentai|sentua|sesita|sencia|en[tc]ia)l([a-z]*)\b" replace="$1ssential$2"/>
<Typo word="Essentially" find="\b([Ee])s+en[tc]ialy\b" replace="$1ssentially"/>
<Typo word="Establishes" find="\b([Ee])a?stabi?l?ish?(?<![Ee]stablish)(e[ds]?|ing|ments?|)\b" replace="$1stablish$2"/>
<Typo word="Estimate" find="\b([Ee])sitmat(es?|ed|ing|ions?)\b" replace="$1stimat$2"/>
<Typo word="Ethnic" find="\b([Ee])(?:nthn?|tn)ic(ity|ities)?\b" replace="$1thnic$2"/><!--don't match Ethenic-->
<Typo word="European" find="\b[Ee]ur(?:opia|po?ea|opeo)(ns?|ni[sz]e[ds]?|ni[sz]ation)\b" replace="Europea$1"/>
<Typo word="Evaluate" find="\b([Ee])val[au]t(e[ds]?|ing|ion|ive|ors?)\b" replace="$1valuat$2"/>
<Typo word="Eventual" find="\b([Ee])ven(?:htu|ti?)al(ly|it(y|ies))?\b" replace="$1ventual$2"/>
<Typo word="Every" find="\b([Ee])veyr\b" replace="$1very"/>
<Typo word="Every-" find="\b([Ee])ver(body|one|thing|where)\b" replace="$1very$2"/>
<Typo word="Evidently" find="\b([Ee])videntally\b" replace="$1vidently"/>
<Typo word="Evil" find="\b([Ee])fel\b" replace="$1vil"/>
<Typo word="Evolution" find="\b([Ee])nvolution([a-z]*)\b" replace="$1volution$2"/>
<Typo word="Exacerbate" find="\b([Ee])xerbat(e[ds]?|ing|ions?)\b" replace="$1xacerbat$2"/>
<Typo word="(In)Exact" find="\b(E|e|[Ii]ne)xcac?t(ly)?\b" replace="$1xact$2"/>
<Typo word="Exaggerate" find="\b([Ee])xag(?:er?|ger)rat([a-z]+)\b" replace="$1xaggerat$2"/>
<Typo word="Exalted" find="\b([Ee])xhalted\b" replace="$1xalted"/>
<Typo word="(Un)Examined" find="\b(E|e|[Uu]ne)xaminated\b" replace="$1xamined"/>
<Typo word="Example" find="\b([Ee])x(?:em|ma)pl(es?)\b" replace="$1xampl$2"/>
<Typo word="Excavate" find="\b([Ee])xacavat(e[ds]?|ing|ions?|ors?)\b" replace="$1xcavat$2"/>
<Typo word="Exceeded" find="\b([Ee])xced(ed|ing(ly)?)\b" replace="$1xceed$2"/>
<Typo word="Excel" find="\b(?!\bExcell\b)([Ee])xcel(ls?)\b" replace="$1xce$2"/><!--Don't fix Excell-->
<Typo word="Excellent" find="\b([Ee])x(?:el+a|c?el[ae])n(t(ly)?|c[ey])\b" replace="$1xcellen$2"/>
<Typo word="Except" find="\b([Ee])xept(s?|ed|ing|able|ive[a-z]*|ion(s?|less|al[a-z]*|abl[a-z]+))\b" replace="$1xcept$2"/>
<Typo word="Exchange" find="\b([Ee])xc(?:hanch|ang|hagn)(e[ds]?|ing)\b" replace="$1xchang$2"/>
<Typo word="Excitement" find="\b([Ee])xcitment\b" replace="$1xcitement"/>
<Typo word="Exciting" find="\b([Ee])xict(e[ds]|ing)\b" replace="$1xcit$2"/>
<Typo word="Execute" find="\b([Ee])x(?:cecut|ectu?t?)(e[ds]?|ing|i(?:on|ve)s?)\b" replace="$1xecut$2"/>
<Typo word="Exempt" find="\b([Ee])x(?:ce|a)mpt(s?|ed|ing|ions?)\b" replace="$1xempt$2"/>
<Typo word="Exercise" find="\b([Ee])x(?:cercis|ercies|ersi[sz]|ecis)(e[sdr]?|ing)\b" replace="$1xercis$2"/>
<Typo word="Exerted" find="\b([Ee])xtered\b" replace="$1xerted"/>
<Typo word="Exhaust" find="\b([Ee])x(?:au|hua)st(s?|ed|ing|ion|ive[a-z]*)\b" replace="$1xhaust$2"/>
<Typo word="Exhibit" find="\b([Ee])x[hib]{2,5}t(?<!xhibit)(s?|t?ed|ing|ors?|ion(ist)?s?)\b(?<!xbibits?)" replace="$1xhibit$2"/>
<Typo word="Exile" find="\b([Ee])xlile(d)?\b" replace="$1xile$2"/>
<Typo word="Exist" find="\b([Ee])x(?:isi|[cs]is)t(s?|ing|ed|ence)\b" replace="$1xist$2"/>
<Typo word="(Non/Pre/Co)Existence" find="\b(E|e|[Nn]one|[Pp]ree|[Cc]oe)xist[aei]nse\b" replace="$1xistence"/>
<Typo word="Exonerate" find="\b([Ee])xonorate(s?|d)\b" replace="$1xonerate$2"/>
<Typo word="Expand" find="\b([Ee])xpan(s|ed|ing|able)\b" replace="$1xpand$2"/>
<Typo word="Expansion" find="\b([Ee])xapansi(ons?|ve(ly)?)\b" replace="$1xpansi$2"/>
<Typo word="(Un)Expectant" find="\b(E|e|[Uu]ne)xpectand(ly)?\b" replace="$1xpectant$2"/>
<Typo word="(Un)Expected" find="\b(E|e|[Uu]ne)xpeced\b" replace="$1xpected"/>
<Typo word="Expedition" find="\b([Ee])xpiditio(ns?|nary)\b" replace="$1xpeditio$2"/>
<Typo word="(In)Experience" find="\b(E|e|[Ii]ne)[sx]p(?:eria|iere|erei)nc(e[ds]?|ing)\b" replace="$1xperienc$2"/>
<Typo word="Experience" find="\b([Ee])(?:[sx]p(?:rience|erienc)|sperience)([ds])?\b" replace="$1xperience$2"/>
<Typo word="Experiment" find="\b([Ee])xpeiment(s?|al(ly)?)\b" replace="$1xperiment$2"/>
<Typo word="Explain" find="\b([Ee])xp(?:ali|la)(ns?|ning)\b" replace="$1xplai$2"/>
<Typo word="Explanation" find="\b([Ee])xpla?inat(ions?|ory)\b" replace="$1xplanat$2"/>
<Typo word="(Ex/Im)plicitly" find="\b([Ee]x|[Ii]m)plic(?:il?t|tl)y\b" replace="$1plicitly"/>
<Typo word="Exploitation" find="\b([Ee])xplo(?:ta|iti)ti(ons?|ve(ly)?)\b" replace="$1xploitati$2"/>
<Typo word="Express" find="\b([Ee])xress(ing|ed|ions?|ive)?\b" replace="$1xpress$2"/>
<Typo word="Expropriate" find="\b([Ee])xpropiat(e[ds]?|ing|ions?)\b" replace="$1xpropriat$2"/>
<Typo word="(Over)Extension" find="\b(E|e|[Ov]vere)xtens?tio(ns?)\b" replace="$1xtensio$2"/>
<Typo word="External" find="\b([Ee])x(?:ertern|trn|te[rn])al(ly)?\b" replace="$1xternal$2"/>
<Typo word="Extinct" find="\b([Ee])x(?:inct|tint)(ions?)?\b" replace="$1xtinct$2"/>
<Typo word="Extra- (no hyphen)" find="\b([Ee])xtra-(judicial(ly)?|mundane|murals?|ordinar(il)?y|posable|provincial|terr(itorial(ity)?|estrials?))\b" replace="$1xtra$2"/> 
<Typo word="Extradition" find="\b([Ee])xtradic(iotns?)\b" replace="$1xtradi$2"/>
<Typo word="Extraordinary" find="\b([Ee])xtr-?ordinar((il)?y)\b" replace="$1xtraordinar$2"/>
<Typo word="Extravagant" find="\b([Ee])xtrav(?:en?g[ae]|an?ge)n(t(ly)?|ces?)\b" replace="$1xtravagan$2"/>
<Typo word="Extremely" find="\b([Ee])xt(?:eme|remem)le?y\b" replace="$1xtremely"/>
<Typo word="Extremist" find="\b([Ee])xtermist(s)?\b" replace="$1xtremist$2"/>
<Typo word="Extremophile" find="\b([Ee])xtremeophile(s)?\b" replace="$1xtremophile$2"/>
</source>

===F===
<source lang="xml">
<Typo word="Facilitate" find="\b([Ff])acil(?:[it][ae]|ite|lita)t(e[ds]?|ing|ions?)\b" replace="$1acilitat$2"/>
<Typo word="Factor_" find="\b([Ff])acter(s|ed|ing|ize[ds]?|y|ies)\b" replace="$1actor$2"/><!--Don't fix "Facter": name of software-->
<Typo word="Fahrenheit" find="\b([Ff]arh?|fahr)enheit\b" replace="Fahrenheit"/>
<Typo word="(In)Fallible" find="\b(F|f|[Ii]nf)al+ab(le|ility)\b" replace="$1allib$2"/>
<Typo word="(Un)Familiar" find="\b(F|f|[Uu]nf)am(?:illia|ilai?|milia)(r(ly|ity)?|l)\b" replace="$1amilia$2"/>
<Typo word="Families" find="\b([Ff])(?:amil|imili)es\b" replace="$1amilies"/>
<Typo word="(In)Famous" find="\b([Ii]nf|F|f)am(?:eous|ous[et])(ly)?\b" replace="$1amous$2"/> 
<Typo word="Fanaticism" find="\b([Ff])anatism\b" replace="$1anaticism"/>
<Typo word="Fasci(nate/st)" find="\b([Ff])aci(nat(?:e[ds]?|ing(?:ly)?)|s(?:m|ts?|tic))\b" replace="$1asci$2"/>
<Typo word="Fasciitis" find="\b([Ff])ascitis\b" replace="$1asciitis"/>
<Typo word="favo(u)rite" find="\bfav(ou?r)it(s?)\b" replace="fav$1ite$2"/>
<Typo word="Feature" find="\b([Ff])(?:aetu|eautu?)r(es?|ed|ing)\b" replace="$1eatur$2"/>
<Typo word="(Con/Non)Federal" find="\b(F|f|[CcNn]onf)ed(?:re|ar)a(l(ly)?|lis[mt]s?|cy|cies|te[ds]?|tions?)\b" replace="$1edera$2"/>
<Typo word="Feud" find="\b([Ff])ued(s?|ing|ed|al[a-z]*)\b" replace="$1eud$2"/>
<Typo word="Fictitious" find="\b([Ff])ictious(ly)?\b" replace="$1ictitious$2"/>
<Typo word="Field_" find="\b([Ff])eild(\b(?<!Feild)|s|y|ed|ing\b(?<!Feilding)|ers?|able)\b" replace="$1ield$2"/><!--Don't match surnames Feild, Feilding-->
<Typo word="Fierce" find="\b([Ff])eirce(r?|st|ly|ness)\b" replace="$1ierce$2"/>
<Typo word="Fiery" find="\bfire?y\b" replace="fiery"/>
<Typo word="Fifteen" find="\b([Ff])i(?:f|fet|fth|t|ve?t)een((th)?s?)\b" replace="$1ifteen$2"/>
<Typo word="Fight" find="\b(F|f|[Ff]iref)igt?h(s?|ing|ers?)\b" replace="$1ight$2"/>
<Typo word="Finally" find="\b([Ff])i[an]n[al]l?y\b(?<!Finaly)" replace="$1inally"/><!--Don't match surname Finaly-->
<Typo word="Find" find="\b([Ff])idn\b" replace="$1ind"/>
<Typo word="Finite" find="\b([Ff])i(?:n[ae]te|nit|anite)(s?|ly|ness)\b" replace="$1inite$2"/><!--see also "-finite" & "-finit(iv)e"; don't find "Finet"-->
<Typo word="First" find="\b([Ff])i(rts|srt|rsr)\b" replace="$1irst"/>
<Typo word="First" find="\b([Ff])rst(s?|ly)\b" replace="$1irst$2"/>
<Typo word="First" find="\b([Ff])r?ist\s*(-|\s)\s*(aid|base|born|class|floors?|hand|lady|ly|persons?|places?|rater?|round|sergeants?|string|time|water|year)\b" replace="$1irst$2$3"/>
<Typo word="Flamboyant" find="\b([Ff])lamb[ou][ou]y[ae]n(t(ly)?|ce)\b" replace="$1lamboyan$2"/>
<Typo word="(In)Flammable" find="\b(F|f|inf)lamable\b" replace="$1lammable"/>
<Typo word="Fledge" find="\b([Ff])leg(ed|e?l?ing)\b" replace="$1ledg$2"/>
<Typo word="Flemish" find="\bflem+ish\b" replace="Flemish"/>
<Typo word="Florida" find="\b[Ff]lordi?a(n?s?)\b" replace="Florida$1"/>
<Typo word="Flourish" find="\b([Ff])lu?orish(e[ds]|ing)?\b" replace="$1lourish$2"/>
<Typo word="Fluoresce" find="\b([Ff])l(?:uorosc?|o?u?r[eo]sc?)(e[ds]?|en(?:t|ce)s?\b(?<!lorescen(?:t|ce)s?)|ing)\b" replace="$1luoresc$2"/><!--allow Florescent and Florescence-->
<Typo word="Fluorine" find="\b(F|f|[Hh](?:exa|ydro)f|[Dd]if|[Tt](?:ri|etra)f|[Pp]entaf)lour(o|esc(e[ds]?|ing|en(t|ce))|i(c|[dn]es?|dat(e[ds]?|ing|ion)))\b" replace="$1luor$2"/>
<Typo word="Foie gras" find="\b([Ff])ois?(?:\s|-)+([Gg]ras)\b" replace="$1oie $2"/>
<Typo word="Follow" find="\b([Ff])ol[ol]w(s?|ing|ed|ers?)\b" replace="$1ollow$2"/>
<Typo word="Fomalhaut" find="\b[Ff]ormalhaut\b" replace="Fomalhaut"/>
<Typo word="Forbidden" find="\b([Ff])orbid(en|ing)\b" replace="$1orbidd$2"/>
<Typo word="Foreign" find="\b([Ff])or(?:iegn|eing)(ers?|isms?)?\b" replace="$1oreign$2"/>
<Typo word="Forerunner" find="\b([Ff])or+(unners?)\b" replace="$1orer$2"/>
<Typo word="Foreword" find="\b([Ff])or(?:ewa|wo)rd\b" replace="$1oreword"/>
<Typo word="Forfeit" find="\b([Ff])ore?fie?t+(s?|ed|ing|ers?|ures?)\b" replace="$1orfeit$2"/>
<Typo word="(Un)Forgettable" find="\b(F|f|[Uu]nf)orget[ai]bl([ey])\b" replace="$1orgettabl$2"/>
<Typo word="Formalise" find="\b([Ff])ormalli([sz]ed?)\b" replace="$1ormali$2"/>
<Typo word="((D/M)is)In/De/Re/…)Formation" find="\b(F|f|[Ii]nf|[DdMm]isinf|[Pp]?[DdRr]ef|[Cc]onf|[Mm]alf|[Tt]ransf)o(?:m+ati|rmat|rmti)(on|ve(ly)?)\b" replace="$1ormati$2"/>
<Typo word="Formed" find="\b([Ff])r?omed\b" replace="$1ormed"/>
<Typo word="Formerly" find="\b([Ff])o(?:rmer?l|mer|rme?)le?y\b" replace="$1ormerly"/>
<Typo word="(Mis/Un)Fortunate" find="\b([Uu]nf|F|f|[Mm]isf)or(?:etun[ai]te|tunite|tuante|tun[aei]t)(ly|s?|ness)\b(?<!Fortunat)" replace="$1ortunate$2"/><!--Don't match surname Fortunat-->
<Typo word="(Mis/Un)Fortunately" find="\b([Uu]nf|F|f|[Mm]isf)ortunetle?y\b" replace="$1ortunately"/>
<Typo word="(Mis/Un)Fortune" find="\b([Mm]isf|[Uu]nf|F|f)ourtun([a-z]+)\b(?<!Fourtune)" replace="$1ortun$2"/><!-- Avoid the wrestling team previously known as [[Fourtune]] -->
<Typo word="Forty" find="\b([Ff])ourt(y|ieths?|ies)\b" replace="$1ort$2"/>
<Typo word="Forward" find="\b([Ff])o(?:rw|wa)rd(s?|ed|ing|ers?)\b" replace="$1orward$2"/>
<Typo word="Foundation" find="\b([Ff])o(?:ud?n|nd)ation(s?|al(ly)?|less)\b(?<!Fondation)" replace="$1oundation$2"/><!--Avoid Fondation, french-->
<Typo word="Foundry" find="\b([Ff])oundar(y|ies)\b" replace="$1oundr$2"/>
<Typo word="Fourth" find="\b([Ff])or?uth\b" replace="$1ourth"/>
<Typo word="Franchise_" find="\b([Ff])ranchiz(e[ders]?|ing)(?!\s+[Bb]oy[sz])\b" replace="$1ranchis$2"/>
<Typo word="Franciscan" find="\b[Ff]ransiscan(s?)\b" replace="Franciscan$1"/>
<Typo word="Franz Lehár" find="\bFranz\s+Lehar\b" replace="Franz Lehár"/>
<Typo word="(Un)Friend_" find="\b(F|f|[Uu]nf)(?:ire|re?i)nd([a-z]*)\b(?<!Fr(ind(all|le|sbury)|eind(lich)?))" replace="$1riend$2"/><!--Avoid Frindall, Frindle, Frindsbury, Freind and Freindlich-->
<Typo word="From" find="\b([Ff])rmo\b" replace="$1rom"/>
<Typo word="from_" find="\bfrome\b" replace="from"/>
<Typo word="Frontier" find="\b([Ff])roniter(s)?\b" replace="$1rontier$2"/>
<Typo word="Fuchsia" find="\b([Ff])uschi(as?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1uchsi$2"/>
<Typo word="Frustum" find="\b([Ff])rustr(ums?|a)\b" replace="$1rust$2"/>
<Typo word="Fulfill" find="\b(F|f|[Uu]nf)u(?:lfill+|fil?)l(s?|ed|ing|ment)\b" replace="$1ulfill$2"/>
<Typo word="Fulfilled" find="\b([Ff])ulfiled\b" replace="$1ulfilled"/>
<Typo word="(Dis/Dys/Mal/Co)Function" find="\b(F|f|[Dd][yi]sf|[Mm]alf|[Cc]of)u[cn]tion([a-z]*)\b" replace="$1unction$2"/>
<Typo word="Fundamental" find="\b([Ff])und[^a\s-]?men?t([a-z]*)\b" replace="$1undament$2"/>
<Typo word="Funeral" find="\b([Ff])urneral(s)?\b" replace="$1uneral$2"/>
<Typo word="Further" find="\b([Ff])u(?:rthu|the|ruthe)r(s?|ed|ing|ances?|more|most)\b(?<!Furthur)" replace="$1urther$2"/><!--don't match Furthur, name of a bus-->
</source>

===G===
<source lang="xml">
<Typo word="(Inter)Galactic" find="\b(G|g|[Ii]nterg)alatic\b" replace="$1alactic"/>
<Typo word="Galaxy" find="\b([Gg])allax(y|ies)\b" replace="$1alax$2"/>
<Typo word="Galvanize" find="\b([Gg])alvini[sz](e[drs]?|ing|ation)\b" replace="$1alvaniz$2"/>
<Typo word="Games" find="\b([Gg])anes\b" replace="$1ames"/>
<Typo word="Gandhi" find="\b(Mahatma|Mohandas(\s+K\.)?|Indira|Sonia|Rahul)\s+[Gg](?:ha|ah)ndi\b" replace="$1 Gandhi"/>
<Typo word="Gandhi" find="\bghandi\b" replace="Gandhi"/>
<Typo word="Gangster" find="\b([Gg])anster(s)?\b" replace="$1angster$2"/>
<Typo word="garrison_" find="\bgariss?on(s?|ed)\b" replace="garrison$1"/>
<Typo word="Gauge" find="\b([Gg])uag(e[ds]?|ing)\b" replace="$1aug$2"/>
<Typo word="Genealogy" find="\b([Gg])enea?olog([a-z]+)\b" replace="$1enealog$2"/>
<Typo word="General" find="\b([Gg])e(?:mer|nre|nar)al([a-z]*)\b" replace="$1eneral$2"/>
<Typo word="(Re/De)Generate" find="\b([RrDd]eg|G|g)en(?:ra|erat)t([a-z]+)\b" replace="$1enerat$2"/>
<Typo word="(Gen/Nem)esis" find="\b([Gg]en|[Nn]em)[ai](s[ie]s)\b" replace="$1e$2"/>
<Typo word="Genital" find="\b([Gg])enetal(s?|ia|ly)\b" replace="$1enital$2"/>
<Typo word="General Motors'" find="\bGeneral Motor's\s+" replace="General Motors' "/>
<Typo word="Georg(e/ia/etown)" find="\bGe(?:ogr?|rog)(e|ian?s?|etown)\b" replace="Georg$1"/>
<Typo word="Georgia" find="\b[Gg]eoriga(n?s?)\b" replace="Georgia$1"/>
<Typo word="Gérard Depardieu" find="\bGerard\s+Depardieu\b" replace="Gérard Depardieu"/>
<Typo word="Gewürztraminer" find="\b[Gg]ewurt?ztraminer\b" replace="Gewürztraminer"/>
<Typo word="Ghanaian" find="\b[Gg]hanian(s?)\b" replace="Ghanaian$1"/>
<Typo word="Girlfriend" find="\b([Gg])irfr(?:ie|ei)nd(s?)\b" replace="$1irlfriend$2"/>
<Typo word="Given" find="\b([Gg])ievn\b" replace="$1iven"/>
<Typo word="Gjirokastër" find="\bGjirokaster\b" replace="Gjirokastër"/>
<Typo word="(Eye/Sun)Glasses" find="\b([Ee]yeg|[Ss]ung|G|g)lases\b" replace="$1lasses"/>
<Typo word="Glögg" find="\b([Gg])logg\b" replace="$1lögg"/>
<Typo word="Goddess" find="\b([Gg])odess(es)?\b" replace="$1oddess$2"/>
<Typo word="Godunov" find="\b([Gg])odounov\b" replace="$1odunov"/>
<Typo word="(On/Fore/Out)Going" find="\b(G|g|[Oo]ng|[Ff]oreg|[Oo]utg)o(ign|nig)\b" replace="$1oing"/>
<Typo word="Götterdämmerung" find="\b[Gg]ot+erdam+erung\b" replace="Götterdämmerung"/>
<Typo word="Gottlieb" find="\b([Gg])ottleib\b" replace="Gottlieb"/>
<Typo word="Governance" find="\b([Gg])over(?:a|ne)nce\b" replace="$1overnance"/>
<Typo word="Government" find="\b([Gg])ov(?:orn?m|en?r?m|ermn?|ernmn|ernem)en?t(s?|al(ly)?)\b" replace="$1overnment$2"/>
<Typo word="Governor" find="\b([Gg])(?:uver?n[eo]|overne|venro|ou?vene)r(s?|ships?)\b" replace="$1overnor$2"/>
<Typo word="Graduate" find="\b([Uu]nderg|[Pp]ostg|G|g)(?:adua?|ardua|radu|rauda)t(es?|ed|ing|ions?)\b" replace="$1raduat$2"/>
<Typo word="Graffiti" find="\b([Gg])raf(?:it?|fit)t(i|o|ists?)(?<!Porno Graffitti)\b" replace="$1raffit$2"/><!--Don't match Porno Graffitti-->
<Typo word="gramophone_" find="\bgramaphone(s?)\b" replace="gramophone$1"/>
<Typo word="grammar_" find="\bgrammer(s?|ians?)\b" replace="grammar$1"/>
<Typo word="(Un)Grammatical" find="\b([Uu]ng|G|g)ramati(cal[a-z]*)\b" replace="$1rammati$2"/>
<Typo word="Grandfather/mother/..." find="\b([Gg])ra(?:n|nd-)((?:fa|mo)ther|parent|daughter|child(?:ren)?|aunt|nephew|niece|stand|uncle|son)(?<!rand-(?:aunt|uncle|nephew|niece)|Granson)(s)?\b" replace="$1rand$2$3"/>
<Typo word="grandson_" find="\bgranson(s)?\b" replace="grandson$1"/>
<Typo word="-Graph-" find="\b([A-Za-z]*[Gg])rpah([a-z]*)\b" replace="$1raph$2"/>
<Typo word="(Un)Grateful" find="\b(G|g|[Uu]ng)re?at(ful[a-z]*)\b" replace="$1rate$2"/>
<Typo word="_Great" find="(?!\bGerat\b)\b([Gg])(?:erat|rae?t)(est|ly)?\b" replace="$1reat$2"/>
<!--Don't match grater or proper noun Gerat-->
<Typo word="grief_" find="\bgreif\b" replace="grief"/><!--Greif is a surname-->
<Typo word="Grievous" find="\b([Gg])r(?:ievi|eiv)(ous[a-z]*)\b" replace="$1riev$2"/>
<Typo word="(Re/Un)Group" find="\b(G|g|[Rr]eg|[Uu]ng)r(?:opu|uop)(s?|ed|ing)\b" replace="$1roup$2"/>
<Typo word="Grow" find="\b([Gg])rwo(s?|n)\b" replace="$1row$2"/>
<Typo word="Guadalupe" find="\b[Gg]uadulupe\b" replace="Guadalupe"/>
<Typo word="Guanine" find="\b([Gg])(?:una|au)nine\b" replace="$1uanine"/>
<Typo word="Guarana" find="\b([Gg])auarana\b" replace="$1uarana"/>
<Typo word="Guarantee" find="(?!\bGarante\b)\b([Gg])(?:[au]r[ae]|aur[ae]|uare)nte+([ds]?|ing)\b" replace="$1uarantee$2"/><!--Garante is a surname-->
<Typo word="(Body/Un)Guard" find="\b([Bb]odyg|[Uu]ng|G|g)aurd(s?|ed|ing|edly|ians?)\b" replace="$1uard$2"/>
<Typo word="Guatemala" find="\b([Gg])uatamala(ns?)?\b" replace="Guatemala$2"/>
<Typo word="(Mis)Guidance" find="\b(G|g|[Mm]isg)uidence\b" replace="$1uidance"/>
<Typo word="Guideline" find="\b([Gg])uidline(s)?\b" replace="$1uideline$2"/>
<Typo word="Guinness" find="\b[Gg]uin(?:es|n?e)s\b" replace="Guinness"/>
<Typo word="Guttural" find="\b([Gg])ut(?:u|t?a|t?e)ral(s?|ism|ness|ly)\b" replace="$1uttural$2"/>
</source>

===H===
<source lang="xml">
<Typo word="Habeas" find="\b([Hh])aba?eus\b" replace="$1abeas"/>
<Typo word="Habitué" find="\b([Hh])abitue(e?s?)\b" replace="$1abitué$2"/>
<Typo word="Ha(d/s/t)" find="\b([Hh])([dst])a\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1a$2"/>
<Typo word="Halloween" find="\b[Hh]al(?:l?owea|owe[ea]?)n\b" replace="Halloween"/>
<Typo word="Happen" find="\b([Hh])apen(ing|s?|ed)\b" replace="$1appen$2"/>
<Typo word="Happened" find="\b([Hh])ap(?:p?en[dn]e|pen)d\b" replace="$1appened"/>
<Typo word="Harass" find="\b([Hh])ar(?:ras+|r?as|r+as+e)(e[ds]|ing(?:s?|ly)|ments?)\b" replace="$1arass$2"/><!--don't match name Haras-->
<Typo word="Harassment" find="\b([Hh])arassement\b" replace="$1arassment"/>
<Typo word="Hardware" find="\b([Hh])arware\b" replace="$1ardware"/>
<Typo word="Harold(son)" find="\bHarlod(son)?\b" replace="Harold$1"/>
<Typo word="Have" find="\b([Hh])(?:aev|vae)\b" replace="$1ave"/>
<Typo word="(S)Having" find="\b(H|[Ss]?h)(?:ave|va)ing\b" replace="$1aving"/>
<Typo word="He" find="\b([Hh])ge\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1e"/>
<Typo word="Heard" find="\b([Hh])eared\b" replace="$1eard"/>
<Typo word="Heart" find="(?!\bHerat\b)\b([Hh])erat(s)?\b" replace="$1eart$2"/><!--Don't match city Herat-->
<Typo word="Height" find="\b([Hh])(?:e?ighth|ieght)(s?|en(?:s?|ed|ing|ers?))\b" replace="$1eight$2"/>
<Typo word="Heirs" find="\b([Hh])ier(s|ess(?:es)?)(?<!Hiers)\b" replace="$1eir$2"/><!--don't match hier, French/German word or surname Hiers-->
<Typo word="Helicopter" find="\b([Hh])e(?:licopto|li?[eo]copte|ilocopte)r(s?)\b" replace="$1elicopter$2"/>
<Typo word="Helmet" find="\b([Hh])elment(s)?\b" replace="$1elmet$2"/>
<Typo word="Help" find="(?:\bHalper\b)\b([Hh])(?:al|le|elp)p([a-z]*)\b" replace="$1elp$2"/><!--Don't match surname Halper-->
<Typo word="Hemorrhage" find="\b([Hh])(?:em(?:mor?|o)rh?ag|aemorrag)(e[ds]?|ing|ic)\b" replace="$1emorrhag$2"/>
<Typo word="Heredity" find="\b([Hh])eridit(ar)?y\b" replace="$1eredit$2y"/>
<Typo word="Hergé" find="\bHerge\b" replace="Hergé"/>
<Typo word="Heritage" find="\b([Hh])er(?:ri|r?[ae])tage?(s?)\b" replace="$1eritage$2"/>
<Typo word="_heroes" find="\bheros\b" replace="heroes"/><!--Don't match proper noun Heros-->
<Typo word="(Kilo/Mega/Giga)Hertz" find="\b(H|h|[Kk]ilo[Hh]|(?:[Mm]e|[Gg]i)ga[Hh])ertzs\b" replace="$1ertz"/>
<Typo word="Hesitant" find="\b([Hh])esist[ae]n(t|tly|cy)\b" replace="$1esitan$2"/>
<Typo word="Heyday" find="\b([Hh])eyd([ae])ys\b" replace="$1eyd$2y"/>
<Typo word="Hiatus" find="\b([Hh])aitus\b" replace="$1iatus"/>
<Typo word="Hierarchy" find="\b([Hh])(?:ie|ei)ra(?:ch|rc)(y?|ies|(?:ic)?(?:al[a-z]*)?)\b" replace="$1ierarch$2"/>
<Typo word="Hieroglyph" find="\b([Hh])(?:ierogl|eirogly)ph(s?|ic(?:s?|al[a-z]*))\b" replace="$1ieroglyph$2"/>
<Typo word="High" find="\b([Hh])(?:eigh|ig)(er|est|ness|way(?:s|\b(?<!Heighway)))\b" replace="$1igh$2"/><!--Don't match surname Heighway-->
<Typo word="Hilarity" find="\b([Hh])illari(ty|ous[a-z]*)\b" replace="$1ilari$2"/>
<Typo word="Hindrance" find="\b([Hh])ind(?:er[ea]|ren?)nce(s?)\b" replace="$1indrance$2"/>
<Typo word="Hippopotamus" find="\b([Hh])ip(?:o|p?op)potamus(es)?\b" replace="$1ippopotamus$2"/>
<Typo word="Hirsute" find="\b([Hh])[ei]rsuit\b" replace="$1irsute"/>
<Typo word="(Pre)Historic" find="\b(H|h|[Pp]reh)(?:istoric|sitor)i(c[a-z]*|ans?)\b" replace="$1istori$2"/>
<Typo word="History" find="\b([Hh])(?:st|is)or(ies|y|ic[a-z]*)\b" replace="$1istor$2"/>
<Typo word="Homepage" find="\b([Hh])ompage(s)?\b" replace="$1omepage$2"/>
<Typo word="(Dis)Hono(u)r" find="\b(H|h|[Dd]ish)ouno(u?r)(s|e[de]|ing|ifics?|abl[ey])?\b" replace="$1ono$2$3"/>
<Typo word="Horrify" find="\b([Hh])or(?:rifi?|iff?y?)(ing)?\b" replace="$1orrify$2"/>
<Typo word="However" find="\b([Hh])(?:ow|woe)ver\b" replace="$1owever"/>
<Typo word="http:" find="\b([Hh])t(?:p[L:]|t(?:pL|tp[L:]))" replace="$1ttp:"/>
<Typo word="http://" find="\b([Hh])ttp:\\\\" replace="$1ttp://"/>
<Typo word="Humanities" find="\b([Hh])uman(?:it|ti)es\b" replace="$1umanities"/>
<Typo word="Humiliate" find="\b([Hh])umilat(e[ds]?|i(ng|ve|on)|or[sy]?)\b" replace="$1umiliat$2"/>
<Typo word="Humor" find="\b([Hh])umer\b" replace="$1umor"/>
<Typo word="Humoral" find="\b([Hh])umoural\b" replace="$1umoral"/>
<Typo word="Humorous" find="\b([Hh])um(?!erous\b)[eu]rous(ly|ness)?\b" replace="$1umorous$2"/>
<Typo word="Hundred" find="\b([Hh])undere?d(s?|ths?)\b" replace="$1undred$2"/>
<Typo word="Husband" find="\b([Hh])usban(s?|ry)\b" replace="$1usband$2"/>
<Typo word="Hydrogen" find="\b([Hh])ydogen\b" replace="$1ydrogen"/>
<Typo word="Hydrophile/phobe" find="\b([Hh])ydr[oa]p(il|ob)(es?|i[ac]|icity)\b" replace="$1ydroph$2$3"/>
<Typo word="Hygiene" find="\b([Hh])ygein(e|i(c|st)s?)\b" replace="$1ygien$2"/>
<Typo word="Hypocrisy" find="\b([Hh])ypocr(?:a[cs]|ic)(y|ies)\b" replace="$1ypocris$2"/>
<Typo word="Hypocrite" find="\b([Hh])ypocrit(s)?\b" replace="$1ypocrite$2"/>
</source>

===I===
<!--Some "In-" words appear under their roots: "(In)Root"-->
<source lang="xml">
<Typo word="Iconoclast" find="\b([Ii])conclast(s?|ic)\b" replace="$1conoclast$2"/>
<Typo word="Idea" find="\b([Ii])dae(s?)\b(?!'')" replace="$1dea$2"/><!--don't match scientific names-->
<Typo word="Identifier" find="\b([Ii])dentife(rs?|d)\b" replace="$1dentifie$2"/>
<Typo word="Identi(f/t)y" find="\b([Ii])denti([tf])iy\b" replace="$1denti$2y"/>
<Typo word="Idiosyncra(c/s)y" find="\b([Ii])d(?:eosynch?|iosynch)ra([cst][ei-y]+)\b" replace="$1diosyncra$2"/>
<Typo word="Illegal" find="\b([Ii])(?:l+[ie]{2,}|l[ie])gal(ly)?\b(?<!\bEl Ilegal)" replace="$1llegal$2"/>
<Typo word="Illinois" find="\b(?:[Ii]l(?:[li]a?noi|ll+[ai]noi?|l+[ai]ni?o|l+ioni)s|illinois)\b" replace="Illinois"/>
<Typo word="Illness" find="\b([Ii])lless(es)?\b" replace="$1llness$2"/>
<Typo word="Illusion" find="\b([Ii])llution(s)?\b" replace="$1llusion$2"/>
<Typo word="Illustrate" find="\b([Ii])ll?[iu](?:str|st|tr|sr)(?<!llustr|llitr)(at[a-z]+|ious[a-z]*)\b" replace="$1llustr$2"/>
<Typo word="Imagine" find="\b([Ii])magen(e[ds]?|ary|ation)\b" replace="$1magin$2"/>
<Typo word="Imagined" find="\b([Ii])magin([ds])\b" replace="$1magine$2"/><!--don't find "Imagin"-->
<Typo word="Immediate" find="\b([Ii])m(?:m+idi?|(?:mm+)?ea?di?|m+ea?d|m+eadi?)ate?(ly)?\b" replace="$1mmediate$2"/>
<Typo word="Immediately" find="\b([Ii])m+ediate?ley\b" replace="$1mmediately"/>
<Typo word="Imminent" find="\b([Ii])manent(ly)?\b" replace="$1mminent$2"/>
<Typo word="Impedance" find="\b([Ii])mpedenc(es?)\b" replace="$1mpedanc$2"/>
<Typo word="Implement" find="\b([Ii])mpl[ia]ment(s?|e[dr]?|al|ing|ations?)\b" replace="$1mplement$2"/>
<Typo word="Important" find="\b([Ii])mport(?:na|am)(t|tly|ce)\b" replace="$1mportan$2"/>
<Typo word="Imprison" find="\b([Ii])mpri(?:sonn|on|so(?:ne)?)(ed|ment|ing|s)?\b" replace="$1mprison$2"/>
<Typo word="Imprison" find="\bempris+on(s?|ed|ing|ment)\b" replace="imprison$1"/>
<Typo word="Improv(e/ise)" find="\b([Ii])mp(?:re|or)v([a-z]+)\b" replace="$1mprov$2"/>
<Typo word="Inaccurate" find="\b([Ii])n(?:nac?|a)cura(c[a-z]+|te[a-z]*)\b" replace="$1naccura$2"/>
<Typo word="Inaugurates" find="\b([Ii])naugure([ds])\b" replace="$1naugurate$2"/>
<Typo word="Incinerate" find="\b([Ii])(?:cin[ea]|n?[cs]ina|nsin[ea])rat([a-z]+)\b" replace="$1ncinerat$2"/>
<Typo word="Include" find="\b([Ii])nclud(s?)\b" replace="$1nclude$2"/>
<Typo word="Including" find="\b([Ii])n(?:l?cudi|clud)ng\b" replace="$1ncluding"/>
<Typo word="Increase" find="\b([Ii]n)craes(e[ds]|ing(?:ly)?)\b" replace="$1creas$2"/>
<Typo word="Increment" find="\b([Ii])ncr[ai]ment(s?|al(ly)?)\b" replace="$1ncrement$2"/>
<Typo word="Incunabula" find="\b([Ii])ncunabla\b" replace="$1ncunabula"/>
<Typo word="India(na)" find="\b[Ii]ndai(ns?|ni?an?s?)?\b" replace="India$1"/>
<Typo word="Indiana University" find="\b[Uu]niversity\s+of\s+[Ii]ndiana\b" replace="Indiana University"/>
<Typo word="Indicate" find="\b([Ii]n)decat(e[ds]?|ing|ors?)\b" replace="$1dicat$2"/>
<Typo word="Indict" find="\b([Ii])ndite\b" replace="$1ndict"/>
<Typo word="Indictment" find="\b([Ii])ndic?tement(s)?\b" replace="$1ndictment$2"/>
<Typo word="Indigenous" find="\b([Ii])ndig(?:ine?|eni)ous(ly)?\b" replace="$1ndigenous$2"/>
<Typo word="Indiscernible" find="\b([Ii])ndis[cs]ernabl([a-z]+)\b" replace="$1ndiscernibl$2"/>
<Typo word="Individual" find="\b([Ii])(?:ndv|div)ia?dual(ly|s)?\b" replace="$1ndividual$2"/>
<Typo word="Indulge" find="\b([Ii])ndulgue(d?|s|nces?)\b" replace="$1ndulge$2"/>
<Typo word="Industry" find="\b([Ii])n(?:ds?utr|udstr|dusr?t|distr)(y|ies|ial[a-z]*)\b" replace="$1ndustr$2"/>
<Typo word="Ine(…)ible" find="\bune(d|lig|xhaust|xpress)[ia]b(l[ey]|ility)\b" replace="ine$1ib$2"/>
<Typo word="Inevitable" find="\b([Ii])nev(?:[ai]ti|itita)bl([ey])\b" replace="$1nevitabl$2"/>
<Typo word="Infantry" find="\b([Ii])nf(?:ant|rantr)y(m[ae]n)?\b" replace="$1nfantry$2"/>
<Typo word="(Non)Infectious" find="\b(I|i|[Nn]oni)nfectu(ous[a-z]*)\b" replace="$1nfecti$2"/>
<Typo word="Infiltrate" find="\b([Ii])nfilitrat(es?|ed|ions?|ing|ors?)\b" replace="$1nfiltrat$2"/>
<Typo word="Inflammation" find="\b([Ii])[nm]flama(tions?|tory|bl[ey]|bility)\b" replace="$1nflamma$2"/>
<Typo word="Influence" find="\b([Ii])nfluent(e[ds]?)\b" replace="$1nfluenc$2"/>
<Typo word="Influential" find="\b([Ii])nf(?:luenc[iu]|uen[tc][iu]|luentu)al(ly)?\b" replace="$1nfluential$2"/>
<Typo word="Infringement" find="\b([Ii])nfrigement(s?)\b" replace="$1nfringement$2"/>
<Typo word="Inhabitants" find="\b([Ii])nhabitans\b" replace="$1nhabitants"/>
<Typo word="Initial" find="\b([Ii])(?:nnit[it]?|nti|nit|n?titi?)a(?:l|(?=ly\b))(s?|ly|l?(?:ed|ing)|ers?|isms?|i[sz](?:e[ds]?|ing|ations?)|it(?:y|ies)|ness)\b" replace="$1nitial$2"/>
<Typo word="Initiative/Initiation" find="\b([Ii])ni(?:ti(?:ai)?|cia|ta)ti(ves?|ons?)\b" replace="$1nitiati$2"/>
<Typo word="Injured" find="\b([Ii])njur[ir]ed\b" replace="$1njured"/>
<Typo word="Innocence" find="(?!\bInnosense\b)\b([Ii])n(?:osenc|no[cs]ens)e\b" replace="$1nnocence"/><!--don't match group Innosense-->
<Typo word="Inoculate" find="\b([Ii])n(?:noc?|oc)cula([a-z]+)\b" replace="$1nocula$2"/>
<Typo word="Input" find="\b([Ii])mput(s?|ting|ted)\b" replace="$1nput$2"/> 
<Typo word="Insofar" find="\b([Ii])n(?:so\s+|\s+so)far\b" replace="$1nsofar"/><!--"insofar" is proper American English, "in so far" proper British; thus correct only mixed usage-->
<Typo word="Inspire" find="\b([Ii])[mn]ps?ir(ed?|es|ing|ation[a-z]*)\b" replace="$1nspir$2"/>
<Typo word="Instead" find="\b([Ii])nst(?:ade|ed)\b" replace="$1nstead"/>
<Typo word="Instrument" find="\b([Ii])n(?:stur?|tru|sru|tst?ru)ment(s|ally|ality|alities|als?|alis[tm]s?|ation)?\b" replace="$1nstrument$2"/>
<Typo word="Integer" find="\b([Ii])nterg(ers?|rity|ra(ls?|n[dt]s?|ble|bility|te[ds]?|tors?|ti(ve|ng|on[a-z]*)))\b" replace="$1nteg$2"/>
<Typo word="Intellectual" find="\b([Ii])ntelectual(ly|s)?\b" replace="$1ntellectual$2"/>
<Typo word="Intelligence" find="\b([Ii])ntel(?:[eil]|l[ae])gen(cer?s?|t|tly|tsia)\b" replace="$1ntelligen$2"/>
<Typo word="(Dis)Interest" find="\b(I|i|[Dd]isi)(?:nt(?:re|er)|tnere)st(s?|ing(ly)?|ed)\b" replace="$1nterest$2"/>
<Typo word="Interim" find="\b([Ii])nter(?:u|ri)?m\b" replace="$1nterim"/>
<Typo word="International" find="\b([Ii])nte(?:rnati|[nr]atio?)(nal[a-z]*)\b" replace="$1nternatio$2"/>
<Typo word="(Mis/Re)Interpret" find="\b(I|i|[Mm]isi|[Rr]ei)nterper?e?t([a-z]*)\b(?<![Ii]nterpetiolar|[Ii]nterpetaloids?)" replace="$1nterpret$2"/>
<Typo word="Interpreter" find="\b([Ii])ntepretator(s)?\b" replace="$1nterpreter$2"/>
<Typo word="(Un)Interrupt" find="\b((?<!Lemon\s{1,9})I|i|[Uu]ni)nterr?uppt(s?|ed|ing|ions?)\b" replace="$1nterrupt$2"/>
<Typo word="(Un)Interrupted" find="\b([Uu]ni|I|i)nter+uped\b" replace="$1nterrupted"/>
<Typo word="Intervenes" find="\b([Ii])ntervine([ds])?\b" replace="$1ntervene$2"/>
<Typo word="Into" find="\b([Ii])not\b" replace="$1nto"/>
<Typo word="Intra- (no hyphen)" find="\b([Ii])ntra-(murals?|state|uterine|venous(ly)?)\b" replace="$1ntra$2"/>
<Typo word="(Re)Introduce" find="\b(I|i|[Rr]ei)(?:tnro|ntru?|nctr[ou]?|nt[aeo]r?)duc?(e[ds]?|ing|tions?|tory)\b" replace="$1ntroduc$2"/>
<Typo word="Intuition" find="\b([Ii])nti?uti(ons?|ve(ly)?)\b" replace="$1ntuiti$2"/> 
<Typo word="Investigate" find="\b([Ii])nv(?:estiaga?t|estingat|estigait|estiga|estigt|estiat|esta?gat?|esigat|stigat)(ions?|or[sy]?|e[ds]?|ing|ive)\b" replace="$1nvestigat$2"/>
<Typo word="Investment" find="\b([Ii])nvesment(s?)\b" replace="$1nvestment$2"/>
<Typo word="Invincible" find="\b([Ii])nvinc(?:e[ia]?|a)b(l[ey]|ility|leness)\b" replace="$1nvincib$2"/>
<Typo word="Iridescent" find="\b([Ii])rridescen(t(ly)?|ce)\b" replace="$1ridescen$2"/>
<Typo word="Irritate" find="\b([Ii])r(?:ra|i)ta(te[ds]?|ti(ng(ly)?|on)|bl[ey])\b" replace="$1rrita$2"/>
<Typo word="Isn't" find="\b([Ii])snt\b" replace="$1sn't"/>
<Typo word="Israel" find="\b(?:[Ii]srea|israe)l(is?|ites?)?\b" replace="Israel$1"/>
</source>

===J===
<source lang="xml">
<Typo word="Jalapeño" find="\b([Jj])alape[nńň]o(s)?\b(?!\s[Rr]ecords?)\b" replace="$1alapeño$2"/><!--Not Jalapeno Records-->
<Typo word="Janáček" find="\bJan(?:[aàäãǎāăá]c|[aàäãǎāă]č)ek\b" replace="Janáček"/>   
<Typo word="Japanese" find="\b[Jj]ap(?:anes|enese)\b" replace="Japanese"/>
<Typo word="Jardinière" find="\b([Jj])ardiniere\b" replace="$1ardinière"/>
<Typo word="Jeopardy" find="\b([Jj])eapardy\b" replace="$1eopardy"/>
<Typo disabled="Jewel(le)ry" find="\b([Jj])ewl(le)?e?ry\b" replace="$1ewel$2ry"/>
<Typo disabled="Jewellery" find="\b([Jj])ewe(?:le|lla)ry\b" replace="$1ewellery"/>
<Typo word="Joan Miró" find="\bJoan\s+Miro\b" replace="Joan Miró"/>
<Typo word="Johnnie" find="\bjohn+ie\b" replace="Johnnie"/>
<Typo word="José Ferrer" find="\bJos[eè]\s+Ferrer\b" replace="José Ferrer"/>
<Typo word="Joseph" find="\b[Jj]o(?:spe|esp)h\b" replace="Joseph"/>
<Typo word="Journ(al/ey)" find="\b([Jj])ounr?(al(s?|is[mt]s?|l?ing)|ey(s?|ed|ing|m[ae]n))\b" replace="$1ourn$2"/>
<Typo word="Journeyed" find="\b([Jj])our?nie?(ed|s)\b" replace="$1ourney$2"/>
<Typo word="Judaism" find="\b(?:[Jj]uada?ism|[Jj]ewism)\b" replace="Judaism"/>
<Typo word="Judg(e)ment" find="\b([Jj])ugd?(e)?ment(s?|al(ly)?)\b(?<!\b[Ll]e\s{1,9}[Jj]ugement\b)" replace="$1udg$2ment$3"/><!--Not Le jugement-->
<Typo word="Judicial" find="\b([Jj])ud(?:uci|ic|isu)a(l|ry)\b" replace="$1udicia$2"/>
<Typo word="(Jun/Sen)ior" find="\b([Jj]u|[Ss]e)(?:ino|noi)r(s?|ity)\b" replace="$1nior$2"/>
<Typo word="Jurisdiction" find="\b([Jj])uri(?:d|st)iction(s|ally|al)?\b" replace="$1urisdiction$2"/>
<Typo word="Just(ify)" find="\b([Jj])s(?:ut|tu)(ice|ly|if(?:i[ace][a-z]+|y))?\b" replace="$1ust$2"/>
<Typo word="Juvenile" find="\b([Jj])uv[ai]nil(e[a-z]*|ity|ia)\b" replace="$1uvenil$2"/>
</source>

===K===
<source lang="xml">
<Typo word="Kåldolmar" find="\b([Kk])aldolmar\b" replace="$1åldolmar"/>
<Typo word="Kazakhstan" find="\b[Kk]azah?kstan(is?)?\b" replace="Kazakhstan$1"/>
<Typo word="Kindergarten" find="\b([Kk])in[dt]erga(?:t|rd)(ens?)\b" replace="$1indergart$2"/>
<Typo word="Knife" find="\b([Kk])nive\b" replace="$1nife"/>
<Typo word="(Ac)Knowledge" find="\b(K|k|[Aa]ck)nowl(?:d?eg|ed|egd?)(e[ds]?|ing|ements?|eab[a-z]+)\b" replace="$1nowledg$2"/>
<Typo word="Kraków" find="\b([Kk])rakow\b(?<!(Jonah|Kenneth|Kenneth K.) Krakow)(?!\s[Tt]ownship)" replace="$1raków"/><!--not Jonah Krakow, Kenneth (K.) Krakow or Krakow Township-->
<Typo word="Kroužek" find="\b([Kk])rouzek\b" replace="$1roužek"/>
<Typo disabled="Kümmel" find="\b([Kk])ummel\b" replace="$1ümmel"/><!--False positive Bernhard Kummel i.e (Kummel 1964)-->
</source>

===L===
<source lang="xml">
<Typo word="La bohème" find="\bLa\s+([Bb])oheme\b" replace="La $1ohème"/>
<Typo word="Labelled" find="\b([Ll])abl(ed|ing)\b" replace="$1abell$2"/>
<Typo word="Laboratory" find="\b([Ll])ab(?:r?a|or)tor(y|ies)\b" replace="$1aborator$2"/>
<Typo word="Laborious" find="\b([Ll])abo(?:r[iou]{1,2}|uriou)(s[a-z]*)\b(?<!aborista)" replace="$1aboriou$2"/>
<Typo word="Lacquer" find="\b([Ll])aquer(s?|ed|ing|ers?)\b" replace="$1acquer$2"/>
<Typo word="L'Âge d'or" find="\bL'(?:[ÂAa]ge\s+(?:D['`’][Oo]|[Dd][`’][Oo]|[Dd]['`’]O)|[aA]ge\s+[dD]['`’][Oo])r\b" replace="L'Âge d'or"/>
<Typo word="Laid" find="\b([Ll])ayed\b" replace="$1aid"/>
<Typo word="Ländler" find="\b([Ll])andler\b" replace="$1ändler"/>
<Typo word="Language" find="\b([Ll])a(?:ngaua?|ngu|nguan|gua|ngu?a)gu?e(?<!anguage)(s?)\b" replace="$1anguage$2"/>
<Typo word="Large" find="\b([Ll])arg(ly|st)?\b" replace="$1arge$2"/>
<Typo word="Largely" find="\b([Ll])arg(elle?|e?le)y\b" replace="$1argely"/>
<Typo word="Larvae" find="\b([Ll])avr?ae\b" replace="$1arvae"/>
<Typo word="Laser" find="\blazer(s)?\b" replace="laser$1"/>
<Typo word="Lasso" find="\b([Ll])as+oo\b" replace="$1asso"/>
<Typo word="Last" find="\b([Ll])(?:astr|sat)(ly)?\b" replace="$1ast$2"/>
<Typo word="Late" find="\b([Ll])aste(r(?<!Laster)|st)\b" replace="$1ate$2"/><!--Laster is a surname & a Transformer-->
<Typo word="Latitude" find="\b([Ll])attitud(es?|inal)\b" replace="$1atitud$2"/>
<Typo word="(Col)League" find="\b(L|l|[Cc]oll)ea(?:ugu?|g)e(r?s?|d)\b" replace="$1eague$2"/>
<Typo word="(Un/Re)Learn" find="\b(L|l|[Uu]nl|[Rr]el)eran(s?|t|ed|ing)\b" replace="$1earn$2"/>
<Typo word="least" find="\belast\b" replace="least"/>
<Typo word="Left" find="\b([Ll])efted\b" replace="$1eft"/>
<Typo word="(L/R)egion" find="\b([LlRr])eagion(s?|al(s?|ly|ism|i[sz]e[ds]?)|ary|aries)\b" replace="$1egion$2"/>
<Typo word="Légion d'honneur" find="\b[Ll]egion\s+[dD]['`][Hh]onneur\b" replace="Légion d'honneur"/>
<Typo word="Legionnaire" find="(?!\bLegionaires\b)\b([Ll])egionaire?(s?)\b" replace="$1egionnaire$2"/><!--don't match Oshawa Legionaires-->
<Typo word="(Il)Legitimate" find="\b([Ii]ll|L|l)(?:igit[ai]?m[ai]|egit[ae]?m[ai]|[ei]git[ai]?mi)(t[eio][a-z]*|c[iy][a-z]*)\b" replace="$1egitima$2"/>
<Typo word="(Il)Legitima(cy/te)" find="\b(L|l|[Ii]ll)egit?ma(cy|te(?:ly)?)\b" replace="$1egitima$2"/>
<Typo disabled="Leibniz" find="\b[Ll]eibnitz\b" replace="Leibniz"/><!--Leibnitz is a town and district in Austria and a parish in Australia-->
<Typo word="Leisure" find="\b([Ll])iesure(ly)?\b" replace="$1eisure$2"/>
<Typo word="(Wave)Length" find="\b(L|l|[Ww]avel)en(?:ght|th)(s?|y|en(s?|e[dr]|ing)|ways|wise|ily|iness)\b" replace="$1ength$2"/>
<Typo word="Les Misérables" find="\bLes\s+Miserables\b" replace="Les Misérables"/>
<Typo word="Lethal" find="\b([Ll])eathal(ly|ity)?\b" replace="$1ethal$2"/>
<Typo word="Levitate" find="\b([Ll])ev[ae]tat(e[ds]?|ing|ions?|ors?)\b" replace="$1evitat$2"/>
<Typo word="Li(k/v)elihood" find="\b([Ll]i[vk]el)yho+(ds?)\b" replace="$1ihoo$2"/>
<Typo word="Liaison" find="\b([Ll])iasi?o(ns?)\b" replace="$1iaiso$2"/>
<Typo word="Libel" find="\b([Ll])ibell(s?)\b" replace="$1ibel$2"/>
<Typo word="Library" find="\b([Ll])ib(?:r(?:ar|e)r|ar)(y|ies|ians?)\b" replace="$1ibrar$2"/>
<Typo word="Libya" find="\b[Ll]ybia(ns?)?\b" replace="Libya$1"/>
<Typo word="Licen(s/c)e" find="\b([Ll])isc?en([cs])(ed?|ing|(e+|ure|or)s?)\b" replace="$1icen$2$3"/>
<Typo word="Lieutenant" find="\b([Ll])[ieu]{2,3}t[ae]{1,2}nt?[ae]{1,2}(?<![Ll]ieutena)n(ts?|cy)\b" replace="$1ieutenan$2"/>
<Typo word="Lifetime" find="\b([Ll])iftime(s?)\b" replace="$1ifetime$2"/>
<Typo word="Liked" find="\b([Ll])i(?:ek|uke)([ds])?\b" replace="$1ike$2"/>
<Typo word="Limit" find="\b([Ll])mit([a-z]*)\b" replace="$1imit$2"/>
<Typo word="Lipizzaner" find="\b[Ll]ip(?:piz?|i)zaner(s?)\b" replace="Lipizzaner$1"/>
<Typo word="Liquor" find="\b([Ll])iqour(s?|ed|ices?)\b" replace="$1iquor$2"/>
<Typo word="Listen/Glisten/Moisten" find="\b(L|[Gg]?l|[Uu]nl|[Mm]o)istn(s?|ed|er(?:ship)?s?|ing|able)\b" replace="$1isten$2"/>
<Typo word="(Il)Literate" find="(?!\bLitteral\b)\b(L|l|[Ii]ll)it(?:ara|eri?|tera)(tes?|ture|cy|l|lly|tim?|ry|lis[mt]s?)\b" replace="$1itera$2"/><!--don't fix surname Litteral-->
<Typo word="Literature" find="\b([Ll])itr?[ai]ture\b" replace="$1iterature"/>
<Typo word="Littérateur" find="\b([Ll])it[eéè]rateur(s)?\b" replace="$1ittérateur$2"/>
<Typo word="Little" find="(?!\bLittel\b)\b([Ll])itt(?:tle|el)\b" replace="$1ittle"/><!--avoid Littel (surname)-->
<Typo word="Live" find="(?!\bLiev Schreiber\b)\b([Ll])iev(ly)?\b" replace="$1ive$2"/><!--avoid actor Liev Schreiber-->
<Typo word="Lived" find="\b([Ll])ieved\b" replace="$1ived"/>
<Typo word="(Long/Short)-lived" find="\b([Ll]ong|[Ss]hort)lived\b" replace="$1-lived"/>
<Typo word="Lo(ne/rd/ve/w)liness" find="(?!\bLovelines\b)\b([Ll])o([nv]e|rd|w)l(?:ynes?|ine)s\b" replace="$1o$2liness"/>
<Typo word="Loosely" find="\b([Ll])osely\b" replace="$1oosely"/>
<Typo word="Los Angeles" find="\b[Ll](?:as\s*[Aa]nge?le?|[ao]s\s*[Aa]ng(?:le|el))a?s\b" replace="Los Angeles"/>
<Typo word="Louisiana" find="\b[Ll]ou(?:siani?|isiani|isiann)(a|ians?)\b" replace="Louisian$1"/>
<Typo word="Love" find="\b([Ll])(?:voe|veo|oev)\b" replace="$1ove"/>
</source>

===M===
<source lang="xml">
<Typo word="Mackerel" find="\b([Mm])ackeral\b" replace="$1ackerel"/>
<Typo word="Macramé" find="\b([Mm])acrame\b" replace="$1acramé"/>
<Typo word="Ma(d/k)e" find="\bAm([dk])(es?|ing)\b(?<!\bAmde)" replace="Ma$1$2"/><!--don't match Amde-->
<Typo word="ma(d/k)e" find="\bam([dk])(es?|ing)\b" replace="ma$1$2"/>
<Typo word="Magazine" find="\b([Mm])agasine(s)?\b" replace="$1agazine$2"/>
<Typo word="Mainly" find="\b([Mm])ailny\b" replace="$1ainly"/>
<Typo word="Maintain" find="\b([Mm])ant(?:ia|ai)n(s?|e[dr]|ing|ab[a-z]+)\b" replace="$1aintain$2"/>
<Typo word="Maintenance" find="\b([Mm])a(?:i?nt(?:[ae]in[ae]|ian[ae]|[ae]|[ae]ne|an[ae])|ntena)nce\b" replace="$1aintenance"/>
<Typo word="Majority" find="\b([Mm])a(?:joro|rjori)ty\b" replace="$1ajority"/>
<Typo word="Make" find="\b([Mm])k(?:ae|ea)(s?)\b" replace="$1ake$2"/>
<Typo word="Makes" find="\b([Mm])akse\b" replace="$1akes"/>
<Typo word="Mammal" find="\b([Mm])amal(s?|ian)\b" replace="$1ammal$2"/>
<Typo word="(Mis)Manage_" find="\b(M|m|[Mm]ism)an(?:ag|ge|ege?)(d|ments?|ab(l[ey]|leness|ility))\b" replace="$1anage$2"/>
<Typo word="Manager" find="\b([Mm])anger(s?|es?|ess?ess?)(?<=([Aa]ccount(?:ing)|[Aa]ss(?:istan|e)t|[Bb]an[dk]|[Bb]usiness|[Cc](?:lien|os)t|[Ee]ngineering|[Ff]o{1,9}tbal{1,9}|[Ff]ormer|[Gg]eneral|[Hh]otel|[Ll]and|[Mm](?:arketing|aterials|iddle|oney)|[Oo]ffice|[Pp](?:eople|ersonnel|ro(?:cess|duct[a-z]{0,99}|gram{1,9}e?|ject))|[Rr]isk|[Ss](?:ales|enior|tress|ystems?)|[Tt](?:ime|eam)|[Uu]pper|[Ww]aste)\s{1,9}[Mm]anger(?:s?|es?|ess?ess?))\b" replace="$1anager$2"/>
<Typo word="(Mis)Managing" find="\b([Mm]|[Mm]ism)an(?:g|age)ing\b" replace="$1anaging"/>
<Typo word="(Out)Maneuver" find="\b(M|m|[Oo]utm)an(o?)(?:u|ue|e)ver(ed|s?|ing)\b" replace="$1an$2euver$3"/>
<Typo word="(Un)Manoeuvrable" find="\b([Uu]nm|M|m)anouverable\b" replace="$1anoeuvrable"/>
<Typo word="Manifestation" find="\b([Mm])ani(?:fes|sfesta)tio(ns?)\b" replace="$1anifestatio$2"/>
<Typo word="(Re/Un)Manufacture" find="\b(M|m|[Rr]em|[Uu]nm)(?!anufactur)[au]n(?:[aiou]{0,2}fr?ac?|[ua]fa|[au]fa)[ct]ur(e[ds]?|ers?|ing|e?able|e?ability)\b" replace="$1anufactur$2"/>
<Typo word="Manufactures" find="\b([Mm])anufact?ur(s?|d)\b" replace="$1anufacture$2"/>
<Typo word="Mark" find="(?!\bMarkes\b)\b([Mm])(?:rak|arke(s))\b" replace="$1ark$2"/><!--don't match surname Markes-->
<Typo word="Marked" find="\b([Mm])aked(ly)?\b" replace="$1arked$2"/>
<Typo word="Marriage" find="\b([Mm])ar(?:rai|ia|r*[aie])ge(s?|able)\b(?!\s+(?:[Dd]e|[Bb]lanc|[Dd]')\b)(?<!\b(?:[Uu]n|[LlDd]es?|[Dd]u)\s+\b([Mm])ar(?:rai|ia|r*[aie])ge(s?|able)\b(?!\s+(?:[Dd]e|[Bb]lanc|[Dd]')\b))" replace="$1arriage$2"/><!--avoid valid French term thru use of lookaround to find French articles-->
<Typo word="Mariage (French) (1)" find="\b([Mm])arriage(s?)\b(?<=\b(?:[Uu]n|[LlDd]es?|[Dd]u)\s+\b([Mm])arriage(s?)\b)" replace="$1ariage$2"/>
<Typo word="Mariage (French) (2)" find="\b([Mm])arriage(s?)\b(?=\s+(?:[Dd][e']|[Bb]lanc)\b)" replace="$1ariage$2"/>
<Typo word="Married" find="\b([Mm])arryi?ed\b" replace="$1arried"/>
<Typo word="Masquerade" find="\b([Mm])asquarad([a-z]+)\b" replace="$1asquerad$2"/>
<Typo word="Massachusetts" find="\b[Mm]as(?:(?:ss+|)[aeu]ch?u?s+et*|s*[eu]ch?u?s+et*|s*[aeu]cu?s+et*|s*[aeu]ch?s+et*|s*[aeu]ch?u?ss+et*|s*[aeu]ch?u?s+e(?:tt|))ts\b" replace="Massachusetts"/>
<Typo word="Masturbate" find="\b([Mm])asterbat([ei][a-z]*)\b" replace="$1asturbat$2"/>
<Typo word="Material" find="\b([Mm](?:etam)?ater)ai?l(is(?:m|ts?)|s?)\b" replace="$1ial$2"/>
<Typo word="Mathematician" find="\b([Mm])athe(?:matic|m?tici)an(s)?\b" replace="$1athematician$2"/>
<Typo word="Mathematics" find="(?!\bMathematica\b)\b([Mm])ath(?:a?matic|ematica)(s?|ians?|al[a-z]*)\b" replace="$1athematic$2"/>
<Typo word="Mayonnaise" find="\b([Mm])ayon(?:n?ais|ais?)s(es?)\b" replace="$1ayonnais$2"/>
<Typo word="Mayoral" find="\b([Mm])ayoria(l|lty)\b" replace="$1ayora$2"/>
<Typo word="Meant" find="\bmenat\b" replace="meant"/><!--don't replace Egyptian goddess Menat-->
<Typo word="Medi(a)eval" find="\b([Mm])ed(?:e(ia?)e?v[aei]|(ia)e?v[ei])l(ly|is[mt]s?)?\b" replace="$1ed$2$3eval$4"/>
<Typo word="Medicine" find="\b([Mm])ed(?:acine|iciney)\b" replace="$1edicine"/>
<Typo word="Medieval" find="\b([Mm])(idie|[ie]de)vi?al\b" replace="$1edieval"/>
<Typo word="(Re/Dis)Member" find="\b([Rr]em|[Dd]ism|M|m)emeber(s?|ed|ing)\b" replace="$1ember$2"/>
<Typo word="Memoir" find="\b([Mm])emio(rs?|rists?)\b" replace="$1emoi$2"/>
<Typo word="memorable" find="\brememberable\b" replace="memorable"/>
<Typo word="Memorable" find="\bRememberable\b" replace="Memorable"/>
<Typo word="Ménage à trois" find="\b([Mm])(?:énage\s+[áa]|enage\s+[aáà])\s+trois\b" replace="$1énage à trois"/>
<Typo word="Mental" find="\b([Mm])enal(ly)\b" replace="$1ental$2"/>
<Typo word="Mention" find="\b([Mm])aintion(ed|s|ing)\b" replace="$1ention$2"/>
<Typo word="Mercantile" find="\b([Mm])ercentile\b" replace="$1ercantile"/>
<Typo word="Merchandise" find="\b([Mm])e(?:rche|cha)ndi([sz])(e[drs]?|ers|ing[s]?)\b" replace="$1erchandi$2$3"/>
<Typo word="Mérimée" find="\bM(?:er+im+[ée]|érr?imm?e)e?\b" replace="Mérimée"/>
<Typo word="Message" find="\b([Mm])es(?:se|a)g(e[rds]?|ing)\b" replace="$1essag$2"/>
<Typo word="Messaging" find="\b([Mm])ess[ae]nging\b" replace="$1essaging"/>
<Typo word="Messenger" find="\b([Mm])essanger(s?)\b" replace="$1essenger$2"/>
<Typo word="Metallic" find="\b(M|m|[Bb]im|[Nn]onm)et(?:tal?|a)l(ic(?:a|ally)?|iferous|ograph[a-z]+|oid[a-z]*|urg[iy][a-z]*)\b(?<!Metaloids?)" replace="$1etall$2"/><!--Not Metaloid(s) see [[Vaglass]]-->
<Typo word="Metaphor" find="\b([Mm])ethaphor(s?|ical[a-z]*)\b" replace="$1etaphor$2"/>
<Typo word="Meteorite" find="\b([Mm])eterorite(s?)\b" replace="$1eteorite$2"/>
<Typo word="Meteorology" find="\b([Mm])eto?erolog(y|ists?|ic[a-z]*)\b" replace="$1eteorolog$2"/>
<Typo word="Metropolitan" find="\b([Mm])etr(?:(?:op|po)lit|(?:opo?|po)lti|o?po?liti)(ans?|ical|ic)\b" replace="$1etropolit$2"/>
<Typo word="Michigan" find="\b[Mm]ichagan\b" replace="Michigan"/>
<Typo word="Microscope" find="\b([Mm])icoscop(es?|y|ic(ally)?)\b" replace="$1icroscop$2"/>
<Typo word="Milieu" find="\b([Mm])(?:ilea?u|elieu)(x)?\b" replace="$1ilieu$2"/>
<Typo word="Military" find="\b(M|m|[Dd]em|[Nn]onm|[Pp]aram)il(?:lit[ae]r|iter|a?tar|irat|iatr|l?itra?)(y|ies|ily|is[tm]s?|istic|i[sz][a-z]+)\b" replace="$1ilitar$2"/>
<Typo word="Millennium_" find="\bmil(?:en?|le)ni(um|a|al[a-z]*)\b" replace="millenni$1"/>
<Typo word="Million" find="(?!\bMillon\b)\b([Mm])il[il]on(aires?|s)\b" replace="$1illion$2"/><!--Millon is a surname-->
<Typo word="Mimicking" find="\b([Mm])imic(ing|ed)\b" replace="$1imick$2"/>
<Typo word="Mineral" find="\b([Mm])in(?:eri|ir)al(s?)\b" replace="$1ineral$2"/>
<Typo word="Miniature" find="\b([Mm])in[ai]tur(es?|iz[a-z]+)\b" replace="$1iniatur$2"/>
<Typo word="Minimum" find="\b([Mm])inum(a|um)\b(?<!Minuma)(?!-ku)\b" replace="$1inim$2"/><!--Not [[Minuma]], [[Minuma-ku, Saitama]]-->
<Typo word="Minion" find="\b([Mm])(?:yni[oa]|inia)n(s)?\b" replace="$1inion$2"/>
<Typo word="Minister" find="\b([Mm])in(?:si?|en?s|ins)t(er(?:ed|ing|s?\b(?<![Mm]insters?)))\b" replace="$1inist$2"/>
<Typo word="Ministry" find="\b([Mm])in(?:iste|si?t|inst|en?st)r(y|ies)\b" replace="$1inistr$2"/>
<Typo word="Minnesota" find="\b[Mm]in(?:nn+e|e|ni)sot(a|ans?)\b" replace="Minnesot$1"/>
<Typo word="Mirror" find="\b([Mm])irr?orr(ed|ing|s)?\b" replace="$1irror$2"/>
<Typo word="Miscellaneous" find="\b([Mm])iscel(?:lani?|ane)ous\b" replace="$1iscellaneous"/>
<Typo word="Mischief" find="\b([Mm])ischei(f|vous[a-z]*)\b" replace="$1ischie$2"/>
<Typo word="Mischievous" find="\b([Mm])isch(?:ei?v[ei]?|iev[ei]|)ou(s[a-z]*)\b" replace="$1ischievou$2"/>
<Typo word="Misogyny" find="\b([Mm])ysogyn(y|ist)\b" replace="$1isogyn$2"/>
<Typo word="Missile" find="\b([Mm])is[is]le(s)?\b" replace="$1issile$2"/>
<Typo word="(Ad/E/Inter/O/…)Mission" find="\b([Ii]nter|[Pp]er|[Rr]e|[EeOo]|(?:[DdRr]e)?(?:[Aa]d|[Cc]om|[Ss]ub|[Tt]rans))mis[si](ons?|onar(y|ies)|ve(ly)?|bl[ey])\b" replace="$1missi$2"/>
<Typo word="Mississippi" find="\b[Mm]i(?:s(?:ss+|)is+ip+|s+is(?:ss+|)ip+|s+is+ip(?:pp+|))i(ans?)?\b" replace="Mississippi$1"/>
<Typo word="Missouri" find="\bmisouri\b" replace="Missouri"/>
<Typo word="Misspell" find="\b([Mm])is(?:-s)?pell(s?|ings?|ed)\b" replace="$1isspell$2"/>
<Typo word="Mithraic" find="\bmythraic\b" replace="Mithraic"/>
<Typo word="Mizzen" find="\bmissen\b" replace="mizzen"/><!-- Don't match surname Missen -->
<Typo word="Model" find="\b([Mm])odle(s)?\b" replace="$1odel$2"/>
<Typo word="Modem" find="\b([Mm])oderm(s)?\b" replace="$1odem$2"/>
<Typo word="Moisture" find="\b([Mm])osture\b" replace="$1oisture"/>
<Typo word="Molecule" find="\b([Mm])oleclu(es|ar)?\b" replace="$1olecul$2"/>
<Typo word="Molière" find="\bMoliere\b" replace="Molière"/>
<Typo word="Moment" find="\b([Mm])o(?:mmen|mem)t(ar(?:y|ily)|s)?\b" replace="$1oment$2"/>
<Typo word="Monastery" find="\b([Mm])on(?:est[ae]?|asta?)r(y|ies|ial)\b" replace="$1onaster$2"/>
<Typo word="Money" find="\b([Mm])oeny(ed)?\b" replace="$1oney$2"/>
<Typo word="Moniker" find="\b([Mm])onicker(s?)\b" replace="$1oniker$2"/>
<Typo word="Monkeys" find="\b([Mm])onkies\b(?<!Funkie Monkies)" replace="$1onkeys"/><!--not Funkie Monkies-->
<Typo word="Monotype" find="\b([Mm])ona?typ(es?|ic)\b" replace="$1onotyp$2"/>
<Typo word="_month" find="\bmounth(ly|s?)\b" replace="month$1"/><!--don't match Mounth-->
<Typo word="More" find="\b([Mm])roe(over)?\b" replace="$1ore$2"/>
<Typo word="More" find="\bomre\b" replace="more"/>
<Typo word="Alanis Morissette" find="\b[Aa]lan+is\s+[Mm]or+isette\b" replace="Alanis Morissette"/><!--don't match Bill Morrisette-->
<Typo word="Mortar" find="\b([Mm])orter(s|ed|ing)\b" replace="$1ortar$2"/><!--Avoid surname Morter-->
<Typo word="Mortgage" find="\b([Mm])orgag(e[eds]?|ing)\b" replace="$1ortgag$2"/>
<Typo word="Motivate" find="\b([Mm])otiviat(e[ds]?|ing|ion)\b" replace="$1otivat$2"/>
<Typo word="Mountain" find="\b([Mm])o(?:utain|untai?ni|ntai?n)(ee?r(?:s|ed|ing|(?<!Montaner))|ous[a-z]*|s?|sides?|tops?|y)(?!\s(Berton|wax))(?<!((Nils|Patrick|La)\s|Saint-)Montan)\b" replace="$1ountain$2"/><!--Not Nils Montan, Saint-Montan, Patrick Montan, Montan Berton, Montan wax, La Montan-->
<Typo word="Movie" find="\b([Mm])ovei(s)?\b" replace="$1ovie$2"/>
<Typo word="Mucous" find="\b([Mm])ucuou?s\b" replace="$1ucous"/>
<Typo word="Multiple" find="\b([Mm])ut?lipl(e[stx]?|y|ie[srd]|ying|ica(ti[a-z]*|nds?)|iable|icity)\b" replace="$1ultipl$2"/>
<Typo word="Multiplier" find="\b([Mm])ultiple(d|rs?)\b" replace="$1ultiplie$2"/>
<Typo word="Municipal" find="\b([Mm])un(?:in?c?pi?|icipi|cip|nicip)a(l[a-z]*)\b" replace="$1unicipa$2"/>
<Typo word="Murder" find="\b([Mm])uder(s?|ing|ed|ers?)\b" replace="$1urder$2"/>
<Typo word="Museum" find="\b([Mm])usu?em(s?)\b" replace="$1useum$2"/>
<Typo word="Musical" find="\b([Mm])usci?al([se]?|ly|ity)\b(?<!Musial)" replace="$1usical$2"/><!--Musial is a surname-->
<Typo word="Musician" find="\b([Mm])uscician(s?)\b" replace="$1usician$2"/>
<Typo word="Mutilate" find="\b([Mm])util[li]at(e[ds]?|ing|ions?)\b" replace="$1utilat$2"/>
<Typo word="Myriad" find="\b([Mm])yraid\b" replace="$1yriad"/>
<Typo word="Myself" find="\b([Mm])ysefl?\b" replace="$1yself"/>
<Typo word="Mysterious" find="\b([Mm])(?:yster|ister[iy])ou(s[a-z]*)\b" replace="$1ysteriou$2"/>
<Typo word="Mystery" find="\b([Mm])ister(ies|y(?<!Mistery))\b" replace="$1yster$2"/>
</source>

===N===
<source lang="xml">
<Typo word="Name" find="\b([Nn])mae(s?|ly|d)\b" replace="$1ame$2"/>
<Typo word="Napoleonic" find="\b[Nn]apoleonian\b" replace="Napoleonic"/>
<Typo word="National" find="\b(N|n|[Ii]ntern)ato?in(al[a-z]*)\b" replace="$1ation$2"/>
<Typo word="(Un)Natural" find="\b(N|n|[Uu]nn)aturual(s?|ly)\b" replace="$1atural$2"/>
<Typo word="(Un)Naturally" find="\b(N|n|[Uu]nn)atur(?:el?|a|uru?al?)ly\b" replace="$1aturally"/>
<Typo word="Nazareth" find="\b[Nn]azere(th|nes?)\b" replace="Nazare$1"/>
<Typo word="(Un)Necessary" find="\b(N|n|[Uu]nn)e(?:cassa|s+[ae]s+a|ces+e)r(y|ily)\b" replace="$1ecessar$2"/>
<Typo word="Necessity" find="\b([Nn])ec(?:ces?|e)sit(y|ies|ate[ds]?|ating)\b" replace="$1ecessit$2"/>
<Typo word="Née" find="([ (])n[eè][eèé]\b" replace="$1née"/>
<Typo word="Négligée" find="\b([Nn])(?:églige|egligé)e?(s?)\b" replace="$1égligée$2"/><!--"negligee" should not be replaced, see [[wikt:negligee]]-->
<Typo word="Negligible" find="\b([Nn])egli(?:ga|)bl([ey])\b" replace="$1egligibl$2"/>
<Typo word="(Re)Negotiate" find="\b(N|n|[Rr]en)ego(?:cia|ta)(ted?|ting|t(e|ion|or)s?|bl[ey]|bility|nt(?<!ciant)s?)\b" replace="$1egotia$2"/>
<Typo word="Neighbo(u)r" find="\b([Nn])[ei]+[gh]*bh?(?:o?(u?)[oe]?r|ro?(u?)o?)(?<![Nn]eighbou?r)(s?|ed|ing|hoods?|ly|liness)\b(?<!Nigh?bor|Nebr|Nieboer|Niebh?ur)" replace="$1eighbo$2$3r$4"/>
<Typo word="Nevada" find="\b[Nn]eveda(n?s?)\b" replace="Nevada$1"/>
<Typo word="Never" find="\b([Nn])ver\b" replace="$1ever"/>
<Typo word="(Never/None)theless" find="\b([Nn])(ever|one)(?:the\s+|\s+the|th)\s?less\b" replace="$1$2theless"/>
<Typo word="New Delhi" find="\bNew\s*[Dd]ehli\b" replace="New Delhi"/>
<Typo word="New" find="\b([Nn])we(s?)\b(?!-|\s(?:Nwe|[Oo]rie|[Nn]kwo)\b)(?<!Nwe)" replace="$1ew$2"/><!--not Nwe Nwe and Nwe- etc 'Nwe' is a name-->
<Typo word="Newsletter" find="\b([Nn])ew[ls]etter(s?)\b" replace="$1ewsletter$2"/>
<Typo word="Newsstand" find="\b([Nn])ewstand(s?)\b" replace="$1ewsstand$2"/>
<Typo word="Niccolò Machiavelli" find="\bNic+ol+o\s+Mac+hi?avel+i\b" replace="Niccolò Machiavelli"/>
<Typo word="Nickel_" find="(?:\bNickle\b)\b([Nn])ickle(ic|ous|iferous|odeons?)?\b" replace="$1ickel$2"/><!--Don't correct surname Nickle-->
<Typo word="Niece" find="\b([Nn])eice(s?)\b" replace="$1iece$2"/>
<Typo word="Nighttime" find="\b([Nn])ightime\b" replace="$1ighttime"/>
<Typo word="Nineteen" find="\b([Nn])inteen(s?|ths?)\b" replace="$1ineteen$2"/>
<Typo word="Ninety" find="\b([Nn])int(y|ies|ieths?|een(th)?)\b" replace="$1inet$2"/>
<Typo word="Ninth" find="\b([Nn])inet(hs?)\b" replace="$1int$2"/>
<Typo word="Nonetheless" find="\b([Nn])ontheless\b" replace="$1onetheless"/>
<Typo word="Nonoperational" find="\bunoperational\b" replace="nonoperational"/>
<Typo word="Nonoperational" find="\bUnoperational\b" replace="Nonoperational"/>
<Typo word="Nonsense" find="\b([Nn])onsenc(e|ical[a-z]*)\b" replace="$1onsens$2"/>
<Typo word="North" find="\b([Nn])oth(ern[a-z]*|erly)?\b(?<!Noth)" replace="$1orth$2"/><!--Allow surname Noth-->
<Typo word="North(ea/we)stern" find="\b([Nn])orth[er]+(ea|we)st(ern[a-z]*)\b" replace="$1orth$2st$3"/>
<Typo word="Northern" find="\b([Nn])o(?:r?her|r?the|ther?)(n|ners?|nmost|ly)\b(?<!Northen)" replace="$1orther$2"/><!--Not surname Northen-->
<Typo word="Notably" find="\b([Nn])ota(?:ble|bil|l)y\b" replace="$1otably"/>
<Typo word="Notice" find="\b([Nn])otive([ds])?\b" replace="$1otice$2"/>
<Typo word="Notoriety" find="\b([Nn])oteriety\b" replace="$1otoriety"/>
<Typo word="(Not)withstand" find="\b([N|n]otw|[Ww])hithstand([a-z]*)\b" replace="$1ithstand$2"/>
<Typo word="Nouméa" find="\b[Nn]oumea\b" replace="Nouméa"/>
<Typo word="Nouveau" find="\b([Nn])oveau(x?)\b" replace="$1ouveau$2"/>
<Typo word="Now" find="\b([Nn])(?:owe?s|wo)\b" replace="$1ow"/>
<Typo word="Nowadays" find="\b([Nn])ow\s?(a\s)?days\b" replace="$1owadays"/>
<Typo word="Nuclear" find="\b([Nn])ucule?ar\b" replace="$1uclear"/>
<Typo word="Nuisance" find="\b([Nn])u(?:isans|sanc)(es?)\b" replace="$1uisanc$2"/>
<Typo word="Nullarbor" find="\b[Nn]ullabour\b" replace="Nullarbor"/>
<Typo word="Numerical" find="\b([Nn])umber[ai]ca(l|lly)\b" replace="$1umerica$2"/>
<Typo word="Numerous" find="\b([Nn])um(?:eri|ber)ou(s[a-z]*)\b" replace="$1umerou$2"/>
<Typo word="Nuptial" find="\b([Nn])uptual(s?)\b" replace="$1uptial$2"/>
<Typo word="Nurturing" find="\b([Nn])utur(e[ds]?|ing)\b" replace="$1urtur$2"/>
</source>

===O===
<source lang="xml">
<Typo word="(Dis)Obedient" find="\b([Dd]iso|O|o)bedian(t(ly)?|ce)\b" replace="$1bedien$2"/>
<Typo word="Obituary" find="\b([Oo])bit(?:i?a|a?u)r(y|ies)\b" replace="$1bituar$2"/>
<Typo word="Obsess" find="\b([Oo])b(?:sses?|se|es)s(e[ds]|i(ng|ve|ons?)(ly)?|ors?)?\b" replace="$1bsess$2"/>
<Typo word="Obsolete" find="\b([Oo])bselete([ds]?|ly)\b" replace="$1bsolete$2"/>
<Typo word="Obstacle" find="\b([Oo])bsta(?:cal|ncle)(s?)\b" replace="$1bstacle$2"/>
<Typo word="Obstacle" find="\b([Oo])b(?:s?tica?le?|s?tacal|tacle)(s?)\b" replace="$1bstacle$2"/> 
<Typo word="Occasion" find="\b([Oo])c(?:as+|cai?ss+|c?ais+|c?as[st]|c?at)i?on+(s?|al[a-z]*|ed|ing)\b" replace="$1ccasion$2"/>
<Typo word="Occupied" find="\b([Oo])ccupate([ds])\b" replace="$1ccupie$2"/>
<Typo word="Occupy" find="\b([Oo])ccupate?(ing)?\b" replace="$1ccupy$2"/>
<Typo word="(Un)Occupy" find="\b(O|o|[Uu]no)c(?:u|c?up)p(y(ing)?|ie[ds]|ants?|ation[a-z]*)\b" replace="$1ccup$2"/>
<Typo word="Occur" find="\b([Oo])c(?:ur?|co?ur)r(s?)\b" replace="$1ccur$2"/>
<Typo word="(Re)Occurred/ing/ence" find="\b([Rr]eo|O|o)c(?:ur+|c?ur)(ing|ed|ences?|ent)\b" replace="$1ccurr$2"/>
<Typo word="Occurrence" find="\b([Oo])c(?:c?urr?a|ur+e)n(ces?|t)\b" replace="$1ccurren$2"/>
<Typo word="Octahedron" find="\b([Oo])ctohedr(ons?|al?(ly)?)\b" replace="$1ctahedr$2"/>
<Typo word="Octave" find="\b([Oo])ctiv(es?|al)\b" replace="$1ctav$2"/>
<Typo word="Oeuvre" find="\b([Oo])uevr(es?)\b" replace="$1euvr$2"/>
<Typo word="Officer" find="\b([Oo])ffcer(s?)\b" replace="$1fficer$2"/>
<Typo word="(Un)Official" find="\b(O|o|[Uu]no)ffic(?:ai?|cia)l(s?|ly|dom|ism)\b" replace="$1fficial$2"/><!--avoid foreign word oficial-->
<Typo word="(Un)Officially" find="\b(O|o|[Uu]no)f+(?:ica|cial)ly\b" replace="$1fficially"/>
<Typo word="Oft(en)times" find="\b([Oo])ft(en)?[-\s]+times\b" replace="$1ft$2times"/>
<Typo word="Often" find="\b([Oo])ftenly\b" replace="$1ften"/>
<Typo word="Olympic" find="\b([Oo])l(?:my?p|ypm?|ym)ic(s?)\b" replace="$1lympic$2"/>
<Typo word="Omelette" find="\b([Oo])mlette(s?)\b" replace="$1melette$2"/>
<Typo word="Ominous" find="\b([Oo])m(?:ni|en|min)ous(ly)?\b" replace="$1minous$2"/>
<Typo word="Once/Twice" find="\b([Oo]n|[Tt]wi)ced\b" replace="$1ce"/>
<Typo word="Only" find="\b([Oo])nyl\b" replace="$1nly"/>
<Typo word="Onomatopoeia" find="\b([Oo])nomatopeo?i(a|c[a-z]*)\b" replace="$1nomatopoei$2"/>
<Typo word="Opening" find="\b([Oo])p+enn(ings?|ed)\b" replace="$1pen$2"/>
<Typo word="Operate" find="\b([Oo])perrat([a-z]+)\b" replace="$1perat$2"/>
<Typo word="Ophthalmology" find="\b([Oo])pthal?m(olog(?:y|ists?)|ic)\b" replace="$1phthalm$2"/>
<Typo word="Oppo(nent/site)" find="\b([Oo])ppe(nents?|se[ds]?|sing|sites?)\b" replace="$1ppo$2"/>
<Typo word="Opponent" find="\b([Oo])ppono?nent(s)?\b" replace="$1pponent$2"/>
<Typo word="Opportunity" find="\b([Oo])p+(?:r?or?|[eu]r)t?uni(?<![Oo]pportuni)(ty|ties|s[tm]s?|stic[a-z]*)\b" replace="$1pportuni$2"/>
<Typo word="(Un)Oppose" find="\b(O|o|[Uu]no)p+oss(e[ds]?|ing)\b" replace="$1ppos$2"/>
<Typo word="(O/Su/Presu)ppose" find="\b(O|o|[Ss]u|[Pp]resu)pos([a-z]+)\b(?<!Reta Oposta)(?<![Oo]possums?)(?<!Oposura)" replace="$1ppos$2"/>
<Typo word="Opposite" find="\b([Oo])pp(?:osit|osate|asite)(s?|ly)\b" replace="$1pposite$2"/>
<Typo word="Opposition" find="\b([Oo])pp?ositition\b" replace="$1pposition"/>
<Typo word="Optimism" find="\b([Oo])pto?mi(sm|st[a-z]*|[sz](e[ds]?|ing|ations?))\b" replace="$1ptimi$2"/>
<Typo word="Orchestra" find="\b([Oo])rch[aiou]?stra([i-sy]*)\b" replace="$1rchestra$2"/>
<Typo word="(Un)Ordered" find="\b(O|o|[Uu]no)rded\b" replace="$1rdered"/>
<Typo word="Ordinary" find="\b([Oo])ridinar(y|ily)\b" replace="$1rdinar$2"/>
<Typo word="Ordnance (Survey/…)" find="\bOrdinance\s+(Board|Corps|Department|Group|Museum|Squadron|Survey|Testing)\b" replace="Ordnance $1"/>
<Typo word="Origin" find="\b([Oo])rgin(s)?\b" replace="$1rigin$2"/>
<Typo word="(Un)Original" find="\b(O|o|[Uu]no)r(?:n?gini?|igni?|ingini?|i?n?gi?ni|igion)a(l(ly)?|te[ds]?|ting|t(ion|or)s?)\b" replace="$1rigina$2"/>
<Typo word="Originally" find="\b([Oo])rig(?:[aie]nn?a|in[in]al?|i?onal?)ly\b" replace="$1riginally"/>
<Typo word="Orphanage" find="\b([Oo])rphan(ges?)\b" replace="$1rphana$2"/>
<Typo word="Orthogonal" find="\b([Oo])rthagonal(ly|s?)\b" replace="$1rthogonal$2"/>
<Typo word="Other" find="\b([Oo])(?:teh|hte)r(s?)\b" replace="$1ther$2"/>
<Typo word="Others" find="\b([Oo])therw\b" replace="$1thers"/>
<Typo word="Out" find="\botu\b\s" replace="out"/><!--Allow surname and place name Otu but not Ma'afu'otu'itonga-->
<Typo word="Outer" find="\b([Oo])utter(most|wear)?\b" replace="$1uter$2"/>
<Typo word="Output" find="\b([Oo])uput(ted|s?|ting)\b" replace="$1utput$2"/>
<Typo word="Overridden" find="\b([Oo])ver(?:id|r?i)den\b" replace="$1verridden"/>
<Typo word="Override" find="\b([Oo])ver(id(es?|den|ing)|ode)\b" replace="$1verr$2"/>
<Typo word="(Over/Under)whelm" find="\b([Oo]v|[Uu]nd)erw(?:ea?l|heli)m(s?|ed|ing)\b" replace="$1erwhelm$2"/>
<Typo word="Oxymoron/Oxygen" find="\b([Oo])xi(moro|ge)n\b" replace="$1xy$2n"/>
</source>

===P===
<source lang="xml">
<Typo word="Palme d'Or" find="\b[Pp]alme\s+(?:D['`’][Oo]|[Dd][`’][Oo]|[Dd]['`’]o)r\b" replace="Palme d'Or"/>
<Typo word="Palme d'Or" find="\b[Pp]alm\s+[dD]['`’][Oo]r\b" replace="Palme d'Or"/>
<Typo word="Pamphlet" find="\b([Pp])am[fp]let(s|ing)?\b" replace="$1amphlet$2"/>
<Typo word="Pantomime" find="\b([Pp])antomine(s)?\b" replace="$1antomime$2"/>
<Typo word="Paper" find="\b([Pp])apaer(s|ing|ed)?\b" replace="$1aper$2"/>
<Typo word="Papier-mâché" find="\b([Pp])ap(?:i?er[-\s]+[Mm]ach[é]|ier mâché)\b" replace="$1apier-mâché"/><!--"papier-mache" should not be replaced, see [[wikt:papier-mache]]-->
<Typo word="Parade" find="\b([Pp])erade([ds])\b" replace="$1arade$2"/>
<Typo word="(Un)Parallel" find="\b(P|p|[Uu]np)ar(?:rall?e|r?alel?|r+alle|el+e)l(s?|i[sz]e[ds]?|isms?|epipeds?|ograms?|ed)\b" replace="$1arallel$2"/>
<Typo word="Parallelly" find="\b([Pp])arr?al(?:ell|lel)?y\b" replace="$1arallelly"/>
<Typo word="Paraphernalia" find="\b([Pp])araphr?enalia\b" replace="$1araphernalia"/>
<Typo word="Parenthesis" find="\b([Pp])aranthe(s[ei]s|tic[a-z]+)\b" replace="$1arenthe$2"/>
<Typo word="Parishioner" find="\b([Pp])ar(?:r+is+h?i?|is+i?|is+h)oner(s?|ship)\b" replace="$1arishioner$2"/>
<Typo word="Parliament" find="(?!\bParlament\b)\b([Pp])ar?l[ai]i?ment(s?|ar[a-z]+)\b" replace="$1arliament$2"/><!--avoid common proper name for foreign parliament "Parlament-->
<Typo word="Parmesan" find="\bparmesan\b" replace="Parmesan"/>
<Typo word="Participate" find="\b([Pp])a[rt]+[ei]?c[aei]*pa?(?<!articipa)(nts?|te[ds]?|ting|tion|tor[sy]?|nc[ey])\b" replace="$1articipa$2"/>
<Typo word="Particular" find="\b([Pp])a(?:rticlu?|ticul)a([a-z]+)\b" replace="$1articula$2"/>
<Typo word="Particular" find="\b([Pp])ar(?:itucla|ticual)(r[a-z]*)\b" replace="$1articula$2"/>
<Typo word="Particularly" find="\b([Pp])articu(?:l+al?r|all?|ari?l|l+ar[ei]l+|alr|llarl)y\b" replace="$1articularly"/>
<Typo word="Party" find="\b([Pp])ary\b" replace="$1arty"/>
<Typo word="(Sur)pass" find="\b(p|[Ss]urp)as(e[ds]|ing)\b" replace="$1ass$2"/><!--avoid Pasing a place in Germany-->
<Typo word="Passenger" find="\b([Pp])a(?:sen|sse)ger(s?)\b" replace="$1assenger$2"/>
<Typo word="Passer-by" find="\b([Pp])asser\s+bye?r?(s?)\b" replace="$1asser$2-by"/> 
<Typo word="Passers(-)by" find="\b([Pp])asser(-?)bye?r?s\b" replace="$1assers$2by"/> 
<Typo word="Pastime" find="\b([Pp])as[st]tim(es?)\b" replace="$1astim$2"/>
<Typo word="Pastoral" find="\b([Pp])astural\b" replace="$1astoral"/>
<Typo word="Patent" find="\b([Pp])attent(ed|ing|s?)\b" replace="$1atent$2"/>
<Typo word="(Im)Patience" find="\b(P|p|[Ii]mp)aitien(t|ce)\b" replace="$1atien$2"/>
<Typo word="Patrolling" find="\b([Pp])atrol(ing|e[dr])\b" replace="$1atroll$2"/>
<Typo word="Pavilion" find="\b([Pp])avillion(s?)\b(?!,? [Ww]yoming\b)" replace="$1avilion$2"/><!--Not [[Pavillion, Wyoming]]-->
<Typo word="Pejorative" find="\b([Pp])erjor[ai]ti(ve[a-z]*|ons?)\b" replace="$1ejorati$2"/>
<Typo word="Peloton" find="\b([Pp])eleton\b" replace="$1eloton"/>
<Typo word="Penélope Cruz" find="\bPenelope\s+Cruz\b" replace="Penélope Cruz"/>
<Typo word="Peninsula" find="\b([Pp])en(?:n?is|nins|sin)ul(ar?)\b" replace="$1eninsul$2"/>
<Typo word="Pennsylvania" find="\b[Pp]en(?:sylva|n?sylvan)nia(ns?)?\b" replace="Pennsylvania$1"/>
<Typo word="People" find="\b([Pp])(?:eop[el]|oeple)(d?|s)\b" replace="$1eople$2"/>
<Typo word="People" find="\b([Pp])o?eo(?:lpe|pel)(s?)\b" replace="$1eople$2"/>
<Typo word="(Un/Mis/Ap)Perceive" find="\b(P|p|[Uu]np|[Mm]isp|[Aa]pp)(?:rec[ei]+|ercie)v(e[ds]?|ing|abl[ey])\b" replace="$1erceiv$2"/>
<Typo word="Percent" find="\b([Pp])recent(ages?)?\b" replace="$1ercent$2"/>
<Typo word="Perform" find="\b([Pp])e(?:for|rfo(?:re)?)m(s?|ed|ers?|ing|able|ances?)\b" replace="$1erform$2"/>
<Typo word="(Non)Performance" find="\b(P|p|[Nn]onp)(?:er?|re)form(?:en|n?a)(ces?)\b" replace="$1erforman$2"/>
<Typo word="Performs" find="\b([Pp])erfore?mes\b" replace="$1erforms"/>
<Typo word="Perhaps" find="\b([Pp])er(?:hasp|heaps|hpas|phas)\b" replace="$1erhaps"/>
<Typo word="Perimeter" find="\b([Pp])erimite(rs?)\b" replace="$1erimete$2"/>
<Typo word="Period" find="\b([Pp])rer?iod(s?|ic|ical(s?|ly))\b" replace="$1eriod$2"/>
<Typo word="Peripatetic" find="\b([Pp])eripathetic\b" replace="$1eripatetic"/>
<Typo word="Peripheral" find="\b([Pp])eripherial(s?|ly)\b" replace="$1eripheral$2"/>
<Typo word="Perjury" find="\b([Pp])erjery\b" replace="$1erjury"/>
<Typo word="(Im)Permanent" find="\b(P|p|[Ii]mp)er(?:man[ai]|m[ei]n[aei]|n[aei]m[aei])n(t[a-z]*|c[ey])\b" replace="$1ermanen$2"/>
<Typo word="Perpendicular" find="\b([Pp])erpindicular(ly)?\b" replace="$1erpendicular$2"/>
<Typo word="Perseverance" find="\b([Pp])erserver[ae]n(ce|t|tly)\b" replace="$1erseveran$2"/>
<Typo word="Persevere" find="\b([Pp]erse)rver(e[ds]?|ing)\b" replace="$1ver$2"/>
<Typo word="Persistent" find="\b([Pp])er(?:iste)n(t|tly|c[ey])\b" replace="$1ersisten$2"/><!--Don't fix persistant, a concept in ontology-->
<Typo word="Personage" find="\b([Pp])erson(nages?)\b" replace="$1erso$2"/>
<Typo word="Personal" find="\b([Pp])eros?nal(ity|ly)?\b" replace="$1ersonal$2"/>
<Typo word="Personnel" find="\b([Pp])ersonn?ell\b" replace="$1ersonnel"/>
<Typo word="Persuade" find="\b([Pp])(?:ursua|ersu|ususa)(de[ds]?|ding|si[a-z]+)\b" replace="$1ersua$2"/>
<Typo word="Perturbation" find="\b([Pp])ertub(ed|ations?)\b" replace="$1erturb$2"/>
<Typo word="Pessary" find="\b([Pp])essiary\b" replace="$1essary"/>
<Typo word="(Com)Petition" find="\b(P|p|[Cc]omp)etetion(ed|ing|s)?\b" replace="$1etition$2"/>
<Typo word="Pharaoh" find="\b([Pp])haroah(s?)\b(?!\sSanders)(?<!(American|Ashley|Jay)\sPharoah|illage\sof\sthe\sPharoahs)" replace="$1haraoh$2"/>
<Typo word="Phenomenal" find="\b([Pp])heno(?:nmen|menon|nem)a(l|lly)?\b" replace="$1henomena$2"/>
<Typo word="Phenomenally" find="\b([Pp])henomenonly\b" replace="$1henomenally"/>
<Typo word="Phenomenon" find="\b([Pp])heno(?:m(?:on)?(?:enom|onon)|n[eo]mon)\b" replace="$1henomenon"/>
<Typo word="Philanthropy" find="\b([Pp])hila(?:n?thr|ntr|nth)oph?(?<!lanthrop)(y|ies|ists?|ically|ical|ic|e)\b" replace="$1hilanthrop$2"/>
<Typo word="Philosophical" find="\b([Pp])h(?:ill?i|yll?o)sophical(ly)?\b" replace="$1hilosophical$2"/>
<Typo word="Philosophy" find="\b([Pp])hil(?:osa?|[ai]?so)ph(ers?|ic[a-z]*|y|ies|i[sz][a-z]+)\b" replace="$1hilosoph$2"/>
<Typo word="Pho(n/t)ograph" find="\b([Pp])ho([nt])a?graph(s?|y|ic[a-z]*|ers?)\b" replace="$1ho$2ograph$3"/>
<Typo word="Phoenician" find="\b[Pp]honecian(s?)\b" replace="Phoenician$1"/>
<Typo word="Physics" find="\b([Pp])hisic(s?|ists?|al(s?|ly|ity|is[mt]s?)|ize[ds]?|ians?)\b" replace="$1hysic$2"/>
<Typo word="Piña Colada" find="\bPina\s+[Cc]olada(s)?\b" replace="Piña Colada$1"/>
<Typo word="Picture" find="\b([Pp])citur(es?|ed|ing)\b" replace="$1ictur$2"/>
<Typo word="Piece" find="\b([Pp])eic(e[ds]?|ing|emeal|ework)\b" replace="$1iec$2"/>
<Typo word="Pilgrimage" find="\b([Pp])ilgr(?:im|a)mage(s?)\b" replace="$1ilgrimage$2"/>
<Typo word="Pineapple" find="\b([Pp])inn?app?le(s)?\b" replace="$1ineapple$2"/>
<Typo word="Pinocchio" find="\bPin(?:noc?|o)chio\b" replace="Pinocchio"/>
<Typo word="Pioneer" find="\b([Pp])i(?:on(?:n|n?ee)|non)e+r(s|ed|ing)?\b" replace="$1ioneer$2"/>
<Typo word="Place" find="\b([Pp])alce([a-z]*)\b" replace="$1lace$2"/>
<Typo word="(Dis/Em/Mis/Re)Placement" find="\b([Rr]ep|[DdMm]isp|[Ee]mp|P|p)lacment(s?)\b" replace="$1lacement$2"/>
<Typo word="Plácido Domingo" find="\bPlacido\s+Domingo\b" replace="Plácido Domingo"/>
<Typo word="Plagiarism" find="\b([Pp])lagarism\b" replace="$1lagiarism"/>
<Typo word="Plague" find="\b([Pp])laug(e[ds]?|ing)\b" replace="$1lagu$2"/>
<Typo word="Plaintiff" find="\b([Pp])lantiff(s?)\b" replace="$1laintiff$2"/>
<Typo word="_plant life" find="(?!\bPlantlife\b)\b([Pp])lant-?life\b" replace="$1lant life"/><!--ignore proper n. Plantlife-->
<Typo word="Plantation" find="\b([Pp])la[nt]ation(s?)\b" replace="$1lantation$2"/>
<Typo disable="Plaque" find="\b([Pp])lacque(s?)\b" replace="$1laque$2"/><!--not placque http://www.merriam-webster.com/medical/placque-->
<Typo word="Plateau" find="\b([Pp])late(us?)\b" replace="$1latea$2"/>
<Typo word="Platinum" find="\b([Pp])lat(?:ni?|ini)um(s?)\b" replace="$1latinum$2"/>
<Typo word="Playwright" find="\b([Pp])lay(?:right|writer?)(s?)\b" replace="$1laywright$2"/>
<Typo word="(Un)Pleasant" find="\b(P|p|[Uu]np)l(?:a?esa|ease)nt(ly|ness)?\b" replace="$1leasant$2"/>
<Typo word="Plebiscite" find="\b([Pp])leb[ei][cs]ite(s?)\b" replace="$1lebiscite$2"/>
<Typo word="Plummet" find="\b([Pp])lum(?:met|et?)t(s?|ing|ed)(?<!Rue Plumet)\b" replace="$1lummet$2"/>
<Typo word="Poem" find="\b([Pp])eom(s)?\b" replace="$1oem$2"/>
<Typo word="Poetry" find="\b([Pp])(?:eotr|oet)y\b" replace="$1oetry"/>
<Typo word="Point" find="\b(P|p|[Dd]isapp|[Aa]pp)iont(s?|ers?|ed|ing|ments?)\b" replace="$1oint$2"/>
<Typo word="Poison" find="\b([Pp])o(?:isi|sio)n(s?|ed|ous|ing)\b" replace="$1oison$2"/>
<Typo word="Political" find="\b([Pp])ol(?:itc|t?ic|iti)al(ly)?\b" replace="$1olitical$2"/>
<Typo word="Politician" find="\b([Pp])oliti(?:ti|c)an(s?)\b" replace="$1olitician$2"/>
<Typo word="Pollinate" find="\b([Pp])olinat([a-z]+)\b" replace="$1ollinat$2"/>
<Typo word="Pollute" find="\b([Pp])olut(e[ds]?|ing|ion)\b" replace="$1ollut$2"/>
<Typo word="Pölsa" find="\b([Pp])olsa\b" replace="$1ölsa"/>
<Typo word="Polyphonic" find="\b([Pp])olyphonyic\b" replace="$1olyphonic"/>
<Typo word="Polysaccharide" find="\b([Pp])olysacc?(?:aride|charid)(s)?\b" replace="$1olysaccharide$2"/>
<Typo word="Pomegranate" find="\b([Pp])omegranite(s?)\b" replace="$1omegranate$2"/>
<Typo word="Popular" find="\b([Pp])opulare\b" replace="$1opular"/>
<Typo word="(Pop/Reg)ularity" find="\b([Pp]op|Rrr]eg)ularaty\b" replace="$1ularity"/>
<Typo word="Popularly" find="\b(P|p)opular([ia]l)?y\b" replace="$1opularly"/>
<Typo word="Population" find="\b([Pp])op(?:ulati|luatio|oulatio)(ns?)\b" replace="$1opulatio$2"/>
<Typo word="Portrait" find="\b([Pp])r?o(?:tr|rt)a(y(?:s?|als?|ed|ing)|it(?:ure)?s?)\b" replace="$1ortra$2"/>
<Typo word="Portraying" find="\b([Pp])ortraing\b" replace="$1ortraying"/>
<Typo word="Portugal" find="\b[Pp]ortugual\b" replace="Portugal"/>
<Typo word="Portuguese" find="\b[Pp]ortug(?:u?e+u|e*)se\b" replace="Portuguese"/>
<Typo word="Position" find="\b([Pp])(?:soi|os[st]i)tion(s?|ed|al(ly)?)\b" replace="$1osition$2"/>
<Typo word="(Dis/Im/Re/Com/Sup)Position" find="\b(P|p|[Dd]isp|[Ii]mp|[Rr]ep|[Cc]omp|[Ss]upp)os(?:ititi?|[io]sti|ti)(on(s?|ed|ing|al(ly)?)|ve(s?|ly))\b" replace="$1ositi$2"/>
<Typo word="(Dis/Re)Possess" find="\b(P|p|[Dd]isp|[Rr]ep)os(?:es?|se)s(e[ds]|ing|ions?|ive(s?|ly|ness)|ors?)\b" replace="$1ossess$2"/>
<Typo word="Possesses" find="\b([Pp])ossessess\b" replace="$1ossesses"/>
<Typo word="(Im)Possibility" find="\b(P|p|[Ii]mp)os(?:s?ibli|ibili)t(y|ies)\b" replace="$1ossibilit$2"/>
<Typo word="(Im)Possible" find="(?<!\bè\s{0,9})\b(P|p|[Ii]mp)os(?:ib|sab|sibi)l([ey])\b" replace="$1ossibl$2"/>
<Typo word="Posthumous" find="\b([Pp])ost(?:h?umos|humousl|homous)(ly)?\b" replace="$1osthumous$2"/>
<Typo word="Potato" find="\b([Pp])otatoe\b" replace="$1otato"/>
<Typo word="Potsdam" find="\bpostdam\b" replace="Potsdam"/>
<Typo word="Power" find="\b([Pp])woer(ed|ful(?:ly)?)\b" replace="$1ower$2"/>
<Typo word="Powerful" find="\b([Pp])o(?:ver|we)ful\b" replace="$1owerful"/>
<Typo word="Practical" find="\b([Pa])racticle\b" replace="$1ractical"/>
<Typo word="Practice" find="\b([Pp])ratic(e[ds]?|ing|al(ly)?)\b" replace="$1ractic$2"/>
<Typo word="Practitioner" find="\b([Pp])racti(?:ci)?on(ers?)\b" replace="$1ractition$2"/>
<Typo word="Prairie" find="\b([Pp])ra(?:iry|rie)(s)?\b" replace="$1rairie$2"/>
<Typo word="Pre-Columbian" find="\b([Pp])re-Colombian\b" replace="$1re-Columbian"/>
<Typo word="Precursor" find="\b([Pp])recu(?:rse|so)r(s)?\b" replace="$1recursor$2"/>
<Typo word="Predecessor" find="\b([Pp])recedessor(s)?\b" replace="$1redecessor$2"/>
<Typo word="Predecessor" find="\b([Pp])red(?:[ai][cs]+es+[eo]|[aie](?:s|[cs]{2,})es+[eo]|[aie][cs]+es[eo]|[aie][cs]+es+e)r(s?)\b" replace="$1redecessor$2"/>
<Typo word="Predictable" find="\b([Pp])redicatbl([ey])\b" replace="$1redictabl$2"/>
<Typo word="Prediction" find="\b([Pp])rediciton(s)?\b" replace="$1rediction$2"/>
<Typo word="Predominately" find="\b([Pp])redomiantly\b" replace="$1redominately"/>
<Typo word="Preeminent" find="\b([Pp])reminen(t|ce)\b" replace="$1reeminen$2"/>
<Typo word="Preferably" find="\b([Pp])referrabl([ey])\b" replace="$1referabl$2"/>
<Typo word="Pregnant" find="\b([Pp])reg(?:a|ne|ana)n(t|cy|cies)\b" replace="$1regnan$2"/>
<Typo word="Premier(e)" find="\b([Pp])r(?:imie|eme?i)r(s?|e[ds]?|ing)\b" replace="$1remier$2"/>
<Typo word="Premillennial" find="\b([Pp])remillenial\b" replace="$1remillennial"/>
<Typo word="Preoccupy" find="\b([Pp])reocup(y|ie[ds]|ations?)\b" replace="$1reoccup$2"/>
<Typo word="Prerogative" find="\b([Pp])erogative(s?)\b" replace="$1rerogative$2"/>
<Typo word="Presence" find="\b([Pp])res(?:(?:a|ce)nc|ens)e\b" replace="$1resence"/>
<Typo word="Presidential" find="\b([Pp])res(?:edenti|idenit)al\b" replace="$1residential"/>
<Typo word="Prestigious" find="\b([Pp]res)(?:itig[ie]|i?teg[ie]|i?t[ie]ge|itgi|tig)ous(ly)?\b" replace="$1tigious$2"/>
<Typo word="Presumably" find="\b([Pp])resum(?:abe|ib)ly\b" replace="$1resumably"/>
<Typo word="Priest" find="\b([Pp])reist(s?|ly|hoods?)\b" replace="$1riest$2"/>
<Typo word="Priesthood" find="\b([Pp])riestood\b" replace="$1riesthood"/>
<Typo word="Primitive" find="\b([Pp])rimative(s?|ly)\b" replace="$1rimitive$2"/>
<Typo word="Primordial" find="\b([Pp])rimordal\b" replace="$1rimordial"/>
<Typo word="Princip(al/le)" find="\b([Pp])ri(?:ci|nc|nici)p(al(s?|ly)|le[ds]?)\b" replace="$1rincip$2"/>
<Typo word="(Im)Prison" find="\b(P|p|[Ii]mp)rision(s?|ers?|ed|ing|ment)\b" replace="$1rison$2"/> 
<Typo word="Private" find="\b([Pp])rivi?t(ely|es?|i[sz](e[ds]?|ing|ations?))\b" replace="$1rivat$2"/>
<Typo word="Privilege" find="\b(P|p|[Uu]nderp)riv(?:i?led|[ae]l[ei]d?|il[ai]|elle)g(e[dsr]?|ing)\b" replace="$1rivileg$2"/>
<Typo word="Probabilistic" find="\b([Pp])robablistic\b" replace="$1robabilistic"/>
<Typo word="Probability" find="\b([Pp])roba(?:bila|libi)ty\b" replace="$1robability"/>
<Typo word="(Im)Probably" find="\b([Pp]|[Ii]mp)ro(?:bal?|b|pab)l([ey])\b" replace="$1robabl$2"/>
<Typo word="Problem" find="\b([Pp])(?:orble|robel)m(s?)\b" replace="$1roblem$2"/>
<Typo word="Procedure" find="\b([Pp])roce(?:edure|dger)(s?)\b" replace="$1rocedure$2"/>
<Typo word="Proceed" find="\b([Pp])rocede?(ed|ings?|s)?\b" replace="$1roceed$2"/> 
<Typo word="Process" find="\b([Pp])ro(?:cces*|ce|es?)s(e[ds]|ing|ors?|ions?)?\b" replace="$1rocess$2"/>
<Typo word="Processor" find="\b([Pp])rocesser(s)?\b" replace="$1rocessor$2"/>
<Typo word="Proclaim" find="\b([Pp])roclam(e[dr]|ing)\b" replace="$1roclaim$2"/>
<Typo word="Profess_" find="\b([Pp])rof(?:es{2,}|fes?)s(e[ds]|ing)?\b" replace="$1rofess$2"/>
<Typo word="Profession" find="\b([Pp])roff?esion(s?)\b" replace="$1rofession$2"/>
<Typo word="(Non/Semi/Un)Professional" find="\b([Nn]onp|[Uu]np|[Se]mip|[Pp])rof(?:fes+ion+al?|esion+al?|essionnal?|essional)l(s?|ly|i[sz][a-z]+)\b(?<!ofesional\b)" replace="$1rofessional$2"/><!--Don't match Spanish word profesional-->
<Typo word="Professor" find="\b([Pp])rof(?:f?es[oe]|f?esse|fess[oe])r(s)?\b(?!\s+de\b)(?<!\b(?:[Dd]el|[AaEe]l|[EeUu]n)\s+\b([Pp])rof(?:f?es[oe]|f?esse|fess[oe])r(s)?\b(?!\s+de\b))" replace="$1rofessor$2"/><!--Avoid matching foreign "profesor" thru use of lookaround for various articles-->
<Typo word="Profesor (Spanish)" find="\b([Pp])rofessor(s)?\b(?<=\b(?:[Dd]el|[Ee]l)\s+\b([Pp])rofessor(s)?\b)" replace="$1rofesor$2"/>
<Typo word="Proficient" find="\b([Pp])rof(?:fi[stc]i[ea]|i[stc]ia)n(t|cy|tly)\b" replace="$1roficien$2"/>
<Typo word="Programmable" find="\b([Pp])rogramable\b" replace="$1rogrammable"/>
<Typo word="Progress" find="\b([Pp])(?:rog|togr)ess(ed|ing|ive[a-z]*|ions?)\b" replace="$1rogress$2"/>
<Typo word="Proliferation" find="\b([Pp])reliferat([a-z]+)\b" replace="$1roliferat$2"/>
<Typo word="pro-life" find="\bpro\s*life(rs?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="pro-life$1"/><!--exclude cap. form due to various proper nouns-->
<Typo word="Prolific" find="\b([Pp])rofilic(ly)?\b" replace="$1rolific$2"/>
<Typo word="Promiscuous" find="\b([Pp])romiscous(ly)?\b" replace="$1romiscuous$2"/>
<Typo word="Promote" find="\b([Pp])(?:romot|omo)t(ions?|e[ds]|ing)\b" replace="$1romot$2"/>
<Typo word="Prompt" find="\b([Pp])ropmt(s|ed|ing)\b" replace="$1rompt$2"/>
<Typo disabled="Pronominal" find="\b([Pp])ronomial\b" replace="$1ronominal"/><!--see http://en.wiktionary.org/wiki/pronomial-->
<Typo word="Pronounced" find="\b([Pp])rou?nou[nc]+h?(?<!ronounc)(e[ds]?|ing|ments?)\b" replace="$1ronounc$2"/>
<Typo word="Pronouncement" find="\b([Pp])rouncement(s)?\b" replace="$1ronouncement$2"/>
<Typo word="Pronunciation" find="\b([Pp])ron(?:ou?nci?ation|uncation|unciaton|uciation|o?unici?ati?on)(s?)\b" replace="$1ronunciation$2"/>
<Typo word="Propaganda" find="\b([Pp])r(?:opo|apa)gand(as?|i[sz]e[ds]?|ists?)\b" replace="$1ropagand$2"/>
<Typo word="Propaganda" find="\b([Pp])ropogand([a-z]+)\b" replace="$1ropagand$2"/>
<Typo word="Propagate" find="\b([Pp])ropogat(e[ds]?|ing|ion)\b" replace="$1ropagat$2"/>
<Typo word="proper" find="\bpropper(ly)?\b" replace="proper$1"/><!--avoid surname Propper-->
<Typo word="Prophecy" find="\b([Pp])rophac(ies|y)\b" replace="$1rophec$2"/>
<Typo word="Prophesied_" find="\b([Pp]rophe)c(ied|iers?|ying)\b" replace="$1s$2"/>
<Typo word="(Dis)Proportion" find="\b(P|p|[Dd]isp)(?:opor|ropo)tion(ate(?:ly)?|al(ly)?|s)?\b" replace="$1roportion$2"/>
<Typo word="(Dis)Proportionate" find="\b(P|p|[Dd]isp)roportiat(e|ely)\b" replace="$1roportionat$2"/>
<Typo word="Proposition" find="\b([Pp])ropostion(s?|ed)\b" replace="$1roposition$2"/>
<Typo word="Proprietary" find="\b([Pp])ropietar(y|ily|ies)\b" replace="$1roprietar$2"/>
<Typo word="Proselytizing" find="\b([Pp])roseletyzing\b" replace="$1roselytizing"/>
<Typo word="Protagonist" find="\b([Pp])rot[ao]ganis(ts?)\b" replace="$1rotagonis$2"/>
<Typo word="Protect" find="\b([Pp])retect([a-z]*)\b(?<!tect(o|al|um))" replace="$1rotect$2"/><!--don't match pretecto, pretectal or pretectum--> 
<Typo word="Protein" find="\b([Pp])rotie(n(ase|oid|uria)?s?|ds?)\b" replace="$1rotei$2"/>
<Typo word="Protestant" find="\bprotest[ae]nt(s?|ism)\b" replace="Protestant$1"/>
<Typo word="Protocol" find="\b([Pp])rotocal(s)?\b" replace="$1rotocol$2"/>
<Typo word="Protuberance" find="\b([Pp])rot(?:rubera|r?ubere)n(ces?|t|tly)\b" replace="$1rotuberan$2"/>
<Typo word="(Ap/Im/Dis/Disap/Re)Prove" find="\b(P|p|[Aa]pp|[Ii]mp|[Dd]isp|[Dd]isapp|[Rr]ep)roov(e[dnrs]?|ing[a-z]*|abl[ey]|al)\b" replace="$1rov$2"/>
<Typo word="Provide" find="\b([Pp])(?:orvid|rovd)(e(?:d|rs?)|ing)\b" replace="$1rovid$2"/>
<Typo word="Provincial" find="\b([Pp])rov(?:i?ni?ci?|ici)(?<!vinci)al(ly)?\b" replace="$1rovincial$2"/>
<Typo word="Provisional" find="\b([Pp])rovisonal(ly)?\b" replace="$1rovisional$2"/>
<Typo word="Provocative" find="\b([Pp])rovacative(ly)?\b" replace="$1rovocative$2"/>
<Typo word="Proximity" find="\b([Pp])roximty\b" replace="$1roximity"/>
<Typo word="Psyche" find="\b([Pp])(?:hych|sy[ch]|ysc)(es?|(edel|ot)?ics?|iatr[a-z]+|olog[a-z]+)\b" replace="$1sych$2"/>
<Typo word="(Un)Published" find="\b(P|p|[Uu]np)ub(?:ish|lis)(ed|ing|er?s?|able)?\b" replace="$1ublish$2"/>
<Typo word="Puccini" find="\bpucini\b" replace="Puccini"/>
<Typo word="Pumpkin" find="\b([Pp])umkin\b" replace="$1umpkin"/>
<Typo word="Purchase" find="\b([Pp])uchas(e[ds]?|ing)\b" replace="$1urchas$2"/>
<Typo word="Purport" find="\b([Pp])(?:urpo|erpor?)t([a-qt-z]*)\b" replace="$1urport$2"/><!--avoid -rated suffix-->
<Typo word="Purpose" find="\b([Pp])(?:r?up|upr)os(e([ds]?|ful|less)(ly)?|ing)\b" replace="$1urpos$2"/>
<Typo word="Purposely" find="\b([Pp])urposedly\b" replace="$1urposely"/>
<Typo word="Pursue" find="\b([Pp])ersu(e[ds]?|ers?|ing|its?|able|ant|ance)\b" replace="$1ursu$2"/>
</source>

===Q===
<source lang="xml">
<Typo word="(Ac)Quaint" find="\b([Aa]cq|Q|q)uiant(s?|(ed)?(ly)?|est|ing|ance[a-z]*)\b" replace="$1uaint$2"/>
<Typo word="Quantity" find="\b([Qq])uan(?:it(?:it)?|tat|titi)(y|ies)\b" replace="$1uantit$2"/>
<Typo word="Quarantine" find="\b([Qq])uar(?:anta|ent)ine(d?|s)\b" replace="$1uarantine$2"/>
<Typo word="Quarter_" find="\b([Qq])uater(?!cent|n|ma(?:in|ss))([a-z]*)\b" replace="$1uarter$2"/>
<Typo disabled="Québécois" find="\bQu(?:ebé|[éeè]be)cois(es?)?\b" replace="Québécois$1"/>
<Typo word="Question" find="\b([Qq])ue(?:[st]ion|stoin|stiom|siton)(s?|ed|ing|ers?)\b" replace="$1uestion$2"/>
<Typo word="Questionable" find="\b([Qq])uest(?:ionn|on)a(b[il][a-z]+)\b" replace="$1uestiona$2"/>
<Typo word="Questionnaire" find="\b([Qq])uestion+air(s)?\b" replace="$1uestionnaire$2"/>
<Typo word="Quintessential" find="\b([Qq])uinessential(ly)?\b" replace="$1uintessential$2"/>
<Typo word="Quizzes" find="\b([Qq])uize([ds])\b" replace="$1uizze$2"/>
</source>

===R===
<source lang="xml">
<Typo word="Rabbinical" find="\b([Rr])abin+ical(ly)?\b" replace="$1abbinical$2"/>
<Typo word="Radioactive" find="\b([Rr])adiactiv([a-z]+)\b" replace="$1adioactiv$2"/>
<Typo word="Railroad" find="\b([Rr])ail(?:rao|oa)d(s?|ing|ed|ers?)\b" replace="$1ailroad$2"/>
<Typo word="Rapid" find="\b([Rr])epid(s)?\b" replace="$1apid$2"/>
<Typo word="Raspberry" find="\b([Rr])as(?:[pb]er+|[pb]+er)(y|ies)\b" replace="$1aspberr$2"/>
<Typo word="Ratify" find="\b([Rr])adif(y|ied|ication)\b" replace="$1atif$2"/>
<Typo word="Raucous" find="\b([Rr])a(?:ca|uc)us(ly)?\b" replace="$1aucous$2"/>
<Typo word="Reach" find="\b([Rr])e(?:ac|ch)(e[ds]|ing)\b" replace="$1each$2"/>
<Typo word="real" find="\brela\b" replace="real"/><!--Don't match surname Rela-->
<Typo word="Realistic" find="\b([Rr])ealsit(ic[a-z]*|s)?\b" replace="$1ealist$2"/>
<Typo word="Realized" find="\b([Rr])eliz(e[ds]?|ation|ing)\b" replace="$1ealiz$2"/>
<Typo word="Really" find="\b([Rr])(?:el?a|ael)ly\b" replace="$1eally"/>
<Typo word="Rebell(ed|ing|ion)" find="(?<!\b[Ll]a\s{1,9})\b([Rr])eb(?:bel?|e|l)l(ed|ing|ion(?!\s+(?:del?\b|en\b|a\b))s?|ious[a-z]*)\b" replace="$1ebell$2"/><!--avoid Spanish word rebelion(sic) by looking for Spanish articles-->
<Typo word="Rebelión" find="(?<=\b[Ll]a\s{1,9})\b([Rr])ebelion\b" replace="$1ebelión"/>
<Typo word="Rebelión" find="\b([Rr])ebelion(?=\s+(?:del?\b|en\b|a\b))\b" replace="$1ebelión"/>
<Typo word="Rebound" find="\b([Rr])ebounce\b" replace="$1ebound"/>
<Typo word="Recall" find="\b([Rr])eacll(s?|ed|ing)\b" replace="$1ecall$2"/>
<Typo word="Recipe" find="\b([Rr])ecipi(es?)\b" replace="$1ecip$2"/>
<Typo word="Recognise" find="\b([Rr])eco[ng]i([sz](e[ds]?|ing|abl[ey])|tions?)\b" replace="$1ecogni$2"/>
<Typo word="Recommend" find="\b([Rr])e(?:cc[ao]m?men|comen|comman|ommen|comm?e)d(s?|ed|ers?|ing|at[a-z]+|able)\b" replace="$1ecommend$2"/>
<Typo word="Reconciliation" find="\b([Rr])econ[cs]il(?:li|)at(ions?|ory)\b" replace="$1econciliat$2"/>
<Typo word="Reconnaissance" find="\b([Rr])ec(?:c+on+[aeiou]+s+[aei]+|c*on(?:nn+|)+[aeiou]+s+[aei]+|c*on+(?:[eiou]?[aeiou]?|[aeiou]?[aeou]?)s+[aei]+|c*on+[aeiou]+s(?:ss+|)[aei]+|c*on+[aeiou]+s+(?:[ei]|ai))nce(s|)\b" replace="$1econnaissance$2"/>
<Typo word="Record" find="\b([Rr])ecrod(s?|ings?|ed|ers?)\b" replace="$1ecord$2"/>
<Typo word="Recreate" find="\b([Rr])ecrat(e[ds]?|ion(al(ly)?)?|ing)\b" replace="$1ecreat$2"/>
<Typo word="Recruit" find="\b([Rr])ec(?:ru|ui)t(s?|ing|ed|ments?|ers?)\b" replace="$1ecruit$2"/>
<Typo word="Recurr(ed/ing)" find="\b([Rr])e[a]?c(?:cur?|u)r(ed|ing|ent(ly)?|ences?)\b" replace="$1ecurr$2"/><!--reoccuring is a legitimate word-->
<Typo word="Redeem" find="\b([Rr])eedem(s|ed|ing)\b" replace="$1edeem$2"/>
<Typo word="Refer" find="\b([Rr])ef[fr]er(s?|ee[ds]?|en[cs](e[ds]?|ing)|ent(s?|ial))\b" replace="$1efer$2"/>
<Typo word="Referendum" find="\b([Rr])efr?edendum\b" replace="$1eferendum"/>
<Typo word="Referred" find="\b([Rr])ef(?:[fr]?e|rer)r(ed|ing|als?)\b" replace="$1eferr$2"/>
<Typo word="Referring" find="\b([Rr])efr?eriang\b" replace="$1eferring"/>
<Typo word="Refers" find="\b([Rr])efr?(?:er|re)rs\b" replace="$1efers"/>
<Typo word="Refrigerate" find="\b([Rr])efridgerat(ion|ing|ed|es?|ors?)\b" replace="$1efrigerat$2"/>
<Typo word="Refusal" find="\b([Rr])efusla(s)?\b" replace="$1efusal$2"/>
<Typo word="Regard" find="\b([Rr])eguard(ing|less|s)\b" replace="$1egard$2"/>
<Typo word="Regardless" find="\birr?egu?ardless\b" replace="regardless"/>
<Typo word="Regardless" find="\bIrr?egu?ardless\b" replace="Regardless"/>
<Typo word="Regards" find="\b([Rr])e(garde|agrd)s\b" replace="$1egards"/>
<Typo word="Regular" find="\b([Rr])egluar(ity|ly)?\b" replace="$1egular$2"/>
<Typo word="(Ir)Regularly" find="\b(R|r|[Ii]rr)egu(?:lar(?:il)?y|arly)\b" replace="$1egularly"/>
<Typo word="Regulation" find="\b([Rr])egulaion(s)?\b" replace="$1egulation$2"/>
<Typo word="Regulator" find="\b([Rr])egulaotr(s)?\b" replace="$1egulator$2"/>
<Typo word="Rehearse" find="\b([Rr])ehers(als?|e[ds]?|ing)\b" replace="$1ehears$2"/>
<Typo word="Reign" find="\b([Rr])eigin(ed|ing|s)?\b" replace="$1eign$2"/>
<Typo word="Reincarnation" find="\b([Rr])eicarnat(ion|ing|e[ds]?)\b" replace="$1eincarnat$2"/>
<Typo word="Reinforce" find="\b([Rr])eenforc(e[ds]|ments?|ing)\b" replace="$1einforc$2"/>
<Typo word="(Re)iterate" find="\b([Rr]ei|I|i)tterat(ed?|es|ing|ions?|ive(ly)?|or)\b" replace="$1terat$2"/>
<Typo word="Rejuvenate" find="\b([Rr])ejuv[ai]nat(e[ds]?|ing|ion|ors?)\b" replace="$1ejuvenat$2"/>
<Typo word="Relate" find="\b([Rr])eala?t(e[ds]?|ion(s?|al|ships?)|iv[ei][a-z]*)\b" replace="$1elat$2"/>
<Typo word="Relation" find="\b([Rr])elatiopn(s?|ships?)\b" replace="$1elation$2"/>
<Typo word="Relatively" find="\b([Rr])ea?lita?ve(ly|s)?\b" replace="$1elative$2"/>
<Typo word="Release" find="\b([Rr])e(?:al[ae]a?|la?e)s(e[ds]?|ing)\b" replace="$1eleas$2"/>
<Typo word="(Ir)Relevant" find="\b(R|r|[Ii]rr)el(?:l+[ae]v[ae]|av[ae]|evea?)n(c[ey]|t|tly)\b" replace="$1elevan$2"/>
<Typo word="(Un)Reliability" find="\b(R|r|[Uu]nr)e(?:liabli|alibil)ty\b" replace="$1eliability"/>
<Typo word="Relief" find="\b([Rr])elei(fs?|ve(r?s?|d)|ving)\b" replace="$1elie$2"/>
<Typo word="Religion" find="\b([Rr])el(?:ige?o|gio|igioi)(ns?|nless|us[a-z]*|se|sity|nis[tm])\b" replace="$1eligio$2"/>
<Typo word="Religious" find="\b([Rr])eligios(ly|ness)?\b" replace="$1eligious$2"/>
<Typo word="Relinquish" find="\b([Rr])el(?:enqui|iqui|inque?)sh(e[ds]|ment|ing)?\b" replace="$1elinquish$2"/>
<Typo word="Remain" find="(?!\bRemian\b)\b([Rr])e(?:mia|ama?i|mai)nd?(?<![Rr]emain)(s?|ed|ders?|ing)\b" replace="$1emain$2"/><!--avoid proper noun Remian-->
<Typo word="Remaining" find="\b([Rr])ema(ing(ing)?|ning)\b" replace="$1emaining"/>
<Typo word="Remember" find="\b([Rr])emeber(s?|ed|ing)\b" replace="$1emember$2"/>
<Typo word="Reminisce" find="\b([Rr])em(?:ines?|enis?|ini|insi?)c(e[ds]?|ing|en[ct][a-z]*)\b" replace="$1eminisc$2"/>
<Typo word="Remnant" find="\b([Rr])em[ei]n[ae]nt(s)?\b" replace="$1emnant$2"/>
<Typo word="René Descartes" find="\bRene\s+Descartes\b" replace="René Descartes"/>
<Typo word="Rendezvous" find="\b([Rr])ende[vz]ous\b" replace="$1endezvous"/>
<Typo word="Renewal" find="\b([Rr])enewl(s)?\b" replace="$1enewal$2"/>
<Typo word="Renown" find="\b([Rr])eknown(|ed)\b" replace="$1enown$2"/>
<Typo word="Renters" find="\b([Rr])entor(s)?\b" replace="$1enter$2"/>
<Typo word="Reorganization" find="\b([Rr])eorganision\b" replace="$1eorganization"/>
<Typo word="Repeated" find="\b([Rr])epetead(ly)?\b" replace="$1epeated$2"/>
<Typo word="(Un)Repentant" find="\b(R|r|[Uu]nr)epe(?:nte|t[ae])n(t|tly|ce)\b" replace="$1epentan$2"/>
<Typo word="Repertoire" find="\b([Rr])ep[eir]to(ires?|ry|ries|rial)\b" replace="$1eperto$2"/>
<Typo word="Replacement" find="\b([Rr])elpacement(s)?\b" replace="$1eplacement$2"/>
<Typo word="Reported" find="\b([Rr])eportad(ly)?\b" replace="$1eported$2"/>
<Typo word="Represent" find="\b([Rr])e(?:[pr]+es+[ea]?[nte]+|prsent)(?<!epresent|epresse)(s?|ed|ing|atives?|ation(?:al|s)?)\b" replace="$1epresent$2"/>
<Typo word="Representation" find="\b([Rr])epres(?:anta|en)ti(on|ves?)\b" replace="$1epresentati$2"/>
<Typo word="Representative" find="\b([Rr])eprese?[nt][ntaei]*ve?(?<!entative)(s?)\b" replace="$1epresentative$2"/>
<Typo word="Reprimand" find="\b([Rr])epr[ae]mand(s?|ed|ings?)\b" replace="$1eprimand$2"/>
<Typo word="Require" find="\b([Rr])(?:ecqui?re?|equre?|quire?|equie?r)([ds]?|ments?)\b" replace="$1equire$2"/>
<Typo word="Requiring" find="\b([Rr])(?:ecqui?|equ|qui)re?ing\b" replace="$1equiring"/>
<Typo word="Rescind" find="\b([Rr])e[sc]ind(s?|ed|ing)" replace="$1escind$2"/>
<Typo word="Resemble" find="\b([Rr])es(?:sembl|emb)(e[ds]?|ing|[ae]nces?)\b" replace="$1esembl$2"/>
<Typo word="Reservoir" find="\b([Rr])esevoir(s)?\b" replace="$1eservoir$2"/>
<Typo word="Reside" find="\b([Rr])ecid(e[ds]?|ents?|ing)\b" replace="$1esid$2"/>
<Typo word="Resolute" find="\b([Rr])esollut([a-z]+)\b" replace="$1esolut$2"/>
<Typo word="Respect" find="\b([Rr])epsect([a-z]*)\b" replace="$1espect$2"/>
<Typo word="Response" find="\b([Rr])e(?:pons|sponc|spoms)(es?|ive(ly)?|ib[a-z]+)\b" replace="$1espons$2"/>
<Typo word="Response" find="\b([Rr])e(?:pons|sponc|spo[mn]s)\b" replace="$1esponse"/>
<Typo word="(Ir)Responsibility" find="\b(R|r|[Ii]rr)espon(?:s[ae]?bili|sibli|sibil|is?bili|nsibili)t(?:i?t?(ies)|(e)(i)(s)|[ei]?t?(y))\b" replace="$1esponsibilit$2$4$3$5$6"/>
<Typo word="(Ir)Responsible" find="\b(R|r|[Ii]rr)espon(?:s[ae]b|sibi|isb)(l[ey])\b" replace="$1esponsib$2"/>
<Typo word="Restaurant" find="\b([Rr])e(?:[st]au|stu?[aeu][ua]?|st)(?:ru?a?e?u?n?)(ts?)(?<!estaurants?)(?<=\b[Ra-z]{1,10}[nu][a-z]{1,10})\b" replace="$1estauran$2"/>
<Typo word="Restaurateur" find="\b([Rr])est(?:[ae]ra|arau)nt[eo]u?(rs?)\b" replace="$1estaurateu$2"/><!--[[wikt:restauranteur]] is acceptable-->
<Typo word="Result" find="\b([Rr])eult(ed|s|ing|ant)?\b" replace="$1esult$2"/>
<Typo word="Résumé" find="\b([Rr])(?:esumé|ésume)(s?)\b" replace="$1ésumé$2"/><!--don't replace "resume"-->
<Typo word="Resurgence" find="\b([Rr])esurgan(ce|t)\b" replace="$1esurgen$2"/>
<Typo word="Resurrect" find="\b([Rr])esss?urect(s|ed|ing|ion)?\b" replace="$1esurrect$2"/>
<Typo word="Resuscitate" find="\b([Rr])es(?:[cs]usc?|[cs]?us+|[cs]?uc[cs]?)ita(t(e[ds]?|ors?|ing|ive|ions?)|ble|nts?)\b" replace="$1esuscita$2"/>
<Typo word="Retaliate" find="\b([Rr])etalitate([ds])\b" replace="$1etaliate$2"/>
<Typo word="Retaliation" find="\b([Rr])etalitation\b" replace="$1etaliation"/>
<Typo word="Retrieve" find="\b([Rr])et(?:rei|ire)v(e[ds]|ing|als?)\b" replace="$1etriev$2"/>
<Typo word="Returned" find="\b([Rr])etu(?:rn|nre)d\b" replace="$1eturned"/>
<Typo word="Reversal" find="\b([Rr])everal(s)?\b" replace="$1eversal$2"/>
<Typo word="(R)Evolutionary" find="\b([Rr]?[Ee])volutiona[ry]\b" replace="$1volutionary"/>
<Typo word="Rewrite" find="\b([Rr])ewriet(s)?\b" replace="$1ewrite$2"/>
<Typo word="Rewritten" find="\b([Rr])ewitten\b" replace="$1ewritten"/>
<Typo word="Reykjavik" find="\b[Rr]e(?:kj|jkj?)avik\b" replace="Reykjavik"/>
<Typo word="Rhinoceros" find="\b([Rr])hinocerous(es)?\b" replace="$1hinoceros$2"/>
<Typo word="Rhythm" find="\b([Rr])(?:yth[iey]?|hyth[iey]|htyh|hyt)m(s?|ic[a-z]*|ists?)\b" replace="$1hythm$2"/>
<Typo word="Rhythmic" find="\b([Rr])hytmic(al(ly)?)?\b" replace="$1hythmic$2"/>
<Typo word="Ricochet" find="\b([Rr])ichochet(s?|ed)\b" replace="$1icochet$2"/>
<Typo word="Ridiculous" find="\b([Rr])edic+ulou(s[a-z]*)\b" replace="$1idiculou$2"/>
<Typo word="Rigueur" find="\b([Rr])igeur\b" replace="$1igueur"/>
<Typo word="Rockefeller" find="\b[Rr]ockerfeller\b" replace="Rockefeller"/>
<Typo word="Rococo" find="\b([Rr])ococco\b" replace="$1ococo"/>
<Typo word="Roommate" find="\b([Rr])oomate(s?)\b" replace="$1oommate$2"/>
<Typo word="Rose" find="\b([Rr])ised\b" replace="$1ose"/>
<Typo word="Rudimentary" find="\b([Rr])ud(?:[ae]menta|imentat)r(y|i[a-z]+)\b" replace="$1udimentar$2"/>
<Typo word="Rule" find="\b([Rr])ulle([ds])\b" replace="$1ule$2"/>
<Typo word="Rumors" find="\b([Rr])umer(ed|s)\b" replace="$1umor$2"/>
<Typo word="Running" find="\b([Rr])un(?:nun|in)g\b" replace="$1unning"/>
<Typo word="Russian" find="\b([Rr])ussi(?:on|na)(s)?\b" replace="$1ussian$2"/>
</source>

===S===
<source lang="xml">
<Typo word="Sabotage" find="\b([Ss])abat[ao]g(e[ds]?|ing)\b" replace="$1abotag$2"/>
<Typo word="Sacrifice" find="\b([Ss])acr[ae]fic(e[ds]?|ing|ial(ly)?)\b" replace="$1acrific$2"/>
<Typo word="Sadducee" find="\b[Ss]ad(?:uc?|d?uc)ce(es?|an|eism)\b" replace="Sadduce$1"/>
<Typo word="Safety" find="\bsafte?y\b" replace="safety"/><!--don't match last name Safty-->
<Typo word="Salvador Dalí" find="\bSalvador\s+Dali\b" replace="Salvador Dalí"/>
<Typo word="Same" find="\b([Ss])mae\b" replace="$1ame"/>
<Typo word="Sanction" find="\b([Ss])an(?:tio|c?tion)n(s?|ed|ing)\b" replace="$1anction$2"/>
<Typo word="Sandwich" find="\b([Ss])andw(?:hi|it)ch(e[ds]|ing)?\b" replace="$1andwich$2"/>
<Typo word="Satellite" find="\b([Ss])at(?:e|tel?|t?[ai]l?)lite(s?)\b" replace="$1atellite$2"/>
<Typo word="Satirical" find="\b([Ss])atric(al(ly)?)?\b" replace="satiric$2"/>
<Typo word="Satisfy" find="\b(S|s|[Dd]iss|[Uu]ns)at(?:i?si|i)f(y|ying|ie[ds]|act(ion|ory|orily|oriness))\b" replace="$1atisf$2"/>
<Typo word="Saudi Arabia" find="\b[Ss](?:uadi+|audia)\s*[Aa]rabia(n?)\b" replace="Saudi Arabia$1"/>
<Typo word="Sauté" find="\b([Ss])autt([eé])(s?|ed)\b" replace="$1aut$2$3"/><!--don't replace "saute", see [[wikt:saute]]-->
<Typo word="Saxon" find="\bsaxon(s?|y|ism)\b" replace="Saxon$1"/>
<Typo word="Saxophone" find="\b([Ss])axaphon(es?|ists?)\b" replace="$1axophon$2"/>
<Typo word="Says" find="\b([Ss])(?:asy|yas)\b" replace="$1ays"/>
<Typo word="Scenario" find="\b(?!Senario\b)([Ss])(?:ena|c?ene)rio(s?)\b" replace="$1cenario$2"/><!--avoid proper noun "Senario"-->
<Typo word="Schedule" find="\b([Ss])(?:chedu[ae]|[ch]edu[ae]?)l(es?|ed|ing)\b" replace="$1chedul$2"/>
<Typo word="Scholarship" find="\b([Ss])cho(?:lar|olars)hip(s)?\b" replace="$1cholarship$2"/>
<Typo word="Scholastic" find="\b([Ss])choolastic(s?|ally)\b" replace="$1cholastic$2"/>
<Typo word="Schrödinger" find="\b[Ss]chrodinge(r[a-z]*)\b" replace="Schrödinge$1"/>
<Typo word="Science" find="\b([Ss])cine?ce\b" replace="$1cience"/>
<Typo word="Scientific" find="\b([Ss])cient(?:if|fi)c(ally)?\b" replace="$1cientific$2"/>
<Typo word="(Un)Screen" find="\b(S|s|[Uu]ns)cren([a-z]*)\b" replace="$1creen$2"/>
<Typo word="(Screen/Song)writer" find="\b([Ss])(creen|ong)(?:wrigh|nwri|(?:\s+|\-)wri)ter(s?)\b" replace="$1$2writer$3"/>
<Typo word="Script" find="\b([Ss])cirpt([a-z]*)\b" replace="$1cript$2"/>
<Typo word="Scroll" find="\b([Ss])coll(s?)\b" replace="$1croll$2"/>
<Typo word="(Re)Search" find="\b(S|s|[Rr]es)each(ed|er?s?|ing)?\b" replace="$1earch$2"/>
<Typo word="Second" find="\b([Ss])eco(?:dn?|nt)(s?|ary|ly)\b" replace="$1econd$2"/>
<Typo word="Secretary" find="\b([Ss])ecretart(y|ies|ia[lt]e?s?)\b" replace="$1ecretar$2"/><!--see also "-etary"-->
<Typo word="(In)Security" find="\b(S|s|[Ii]ns)ec(?:rui|ui?re?)t(y|ies)\b" replace="$1ecurit$2"/>
<Typo word="Seeing" find="\b([Ss])eing\b" replace="$1eeing"/>
<Typo word="Segment" find="\b([Ss])egement(s?|ed|ing|ations?)\b" replace="$1egment$2"/>
<Typo word="Sei(z/n)e" find="\b([Ss])ie([zn](e[ds]?|ing)|zures?|ners?)\b" replace="$1ei$2"/>
<Typo word="-self" find="\b([Ii]t|[Mm]y|[Hh](?:i[ms]|er)|[Oo]ne|[Yy]?[Oo]ur|[Tt]he(?:y|m|ir))(?:sle?|esl)(f|ves)\b" replace="$1sel$2"/>
<Typo word="(Re)Semblance" find="\b([Rr]es|[Ss])emb(?:e?le|ela)nc(es?)\b" replace="$1emblanc$2"/>
<Typo word="Sense_" find="\b([Ss])en[cs]e?(?<!ense)(s|d|less(ly|ness)?)\b" replace="$1ense$2"/>
<Typo word="(In/…)Sensitive" find="\b(S|s|(?:[Hh]yp|[Oo]v|[Ss]up)ers|[IiUu]ns|[Nn]ons|[Pp]hotos)ensa?tiv(e|ely|ity)\b" replace="$1ensitiv$2"/>
<Typo word="Sentence" find="(?!\bSentance\b)\b([Ss])entanc(e[ds]?|ings?|ers?)\b" replace="$1entenc$2"/><!--don't fix surname Sentance-->
<Typo word="(In)Separable" find="\b(S|s|[Ii]ns)ep(?:e?ra|area?|ere)(bl[ey]|te[ds]?|tely|ti(on|s[mt]|ng)s?)\b" replace="$1epara$2"/>
<Typo word="Sepulcher" find="\b([Ss])epulchure\b" replace="$1epulcher"/>
<Typo word="Sergeant" find="\bsarg(e?a|e)nt\b" replace="sergeant"/><!--Don't fix surname Sargeant-->
<Typo word="Service" find="\b([Ss])evic(e[ds]?|ing)\b" replace="$1ervic$2"/>
<Typo word="Settle" find="\b([Rr]es|[Uu]ns|S|s)etl(ed?|ers?|ements?|ing)\b" replace="$1ettl$2"/>
<Typo word="Settlement" find="\b([Ss])ett(?:ele|l)ment(s)?\b" replace="$1ettlement$2"/>
<Typo word="Seventeen" find="\b([Ss])eve(?:te|nt)en(s?|ths?)\b" replace="$1eventeen$2"/>
<Typo word="Sevent(h/y)" find="\b([Ss])evet(hs?|y|ie(th)?s?)\b" replace="$1event$2"/>
<Typo word="Sever(e/ely/ity/al/ance)" find="\b([Ss])erver(e|ely|ity|al[a-z]*|ance)\b" replace="$1ever$2"/>
<Typo word="Several" find="\b([Ss])e(?:rvera|v[aei]r[ei]a?|v[ai]r[aei])l\b" replace="$1everal"/>
<Typo word="(Over)Shadow" find="\b([Ss]|[Oo]vers)haddow(s?|ed|ing)\b(?<!\bShaddow)" replace="$1hadow$2"/><!--avoid surname Shaddow-->
<Typo word="she" find="\bseh\b(?<!-seh)" replace="she"/><!-- Not with dash before-->
<Typo word="Shepherd" find="(?!\bSheperd\b)\b([Ss])heperd(s?|ed|ing)\b" replace="$1hepherd$2"/><!--Don't fix surname Sheperd-->
<Typo word="Sheriff" find="\b([Ss])herr?if(s)?\b(?<!\bSherif)" replace="$1heriff$2"/><!--Don't fix surname Sherif-->
<Typo word="Shield_" find="\bsheild(s?|ed|ing)\b" replace="shield$1"/><!-- Don't fix surname Sheilds -->
<Typo word="Shipped" find="\b(?!Shiping)([Ss])hip(ed|ing)\b" replace="$1hipp$2"/>
<Typo word="Shkodër" find="\bShkoder\b" replace="Shkodër"/>
<Typo word="Shortly" find="\b([Ss])horly\b" replace="$1hortly"/>
<Typo word="Should" find="\b([Ss])houdl\b" replace="$1hould"/>
<Typo word="Shouldn't" find="\b([Ss])hou(?:dln'|den)t\b" replace="$1houldn't"/>
<Typo word="Shrewd" find="\b([Ss])hrewed(ly)?\b" replace="$1hrewd$2"/>
<Typo word="Shriek" find="\b([Ss])hre[ai]k(s?|ed|ing)\b" replace="$1hriek$2"/>
<Typo word="Shrunk" find="\b([Ss])hrinked\b" replace="$1hrunk"/>
<Typo word="Sibling" find="\b([Ss])i(?:b[aei]l|lbl?)ing(s?)\b" replace="$1ibling$2"/>
<Typo word="Sidereal" find="\b([Ss])edereal\b" replace="$1idereal"/>
<Typo word="(Be)Sie(g/v)e" find="\b(S|s|[Bb]es)ei([gv]e[ds]?|[gv]ing)\b(?<!David\sSeiving|(Leander|Pierre)\sSeige)(?!\sMonstracity)" replace="$1ie$2"/>
<Typo word="Signat(ure/ory)" find="\b([Ss])ign[ei]t([ou])r(es?|y|ies)\b" replace="$1ignat$2r$3"/>
<Typo word="(In)Significant" find="\b(S|s|[Ii]ns)ig(?:inifica|nficia|nifac?|ifica|nifiga|nifca|nfica)n(t|ce|tly)\b" replace="$1ignifican$2"/>
<Typo word="(In/Non)Significant" find="\b(S|s|[Ii]ns|[Nn]ons)ign(?:i?fi?gan|(?:i?f|fi?)can|if(?:ac[ae]n|icen|ica))(t|tly|ce)\b" replace="$1ignifican$2"/>
<Typo word="Signify" find="\b([Ss])ignf(y|ie[drs]s?)\b" replace="$1ignif$2"/>
<Typo word="(Dis/Veri)Similar" find="\b(S|s|[Dd]iss|[Vv]eris)im(?:(?:mili?|[ua]l|ili)ari?|ilari)(ly|ity)?\b" replace="$1imilar$2"/>
<Typo word="Simply" find="\b([Ss])imp(?:ley|yl)\b" replace="$1imply"/>
<Typo word="Since" find="\b([Ss])icne\b" replace="$1ince"/>
<Typo word="Singsong" find="\b([Ss])ingsog\b" replace="$1ingsong"/>
<Typo word="Sinn Féin" find="\bSinn\s+F(ei|ie)n\b" replace="Sinn Féin"/>
<Typo word="Sistine" find="\bsixtine?\b" replace="Sistine"/>
<Typo word="Situate" find="\b([Ss])it(?:uta|au)t(e[ds]?|ing|ions?)\b" replace="$1ituat$2"/>
<Typo word="Skagerrak" find="\b[Ss]kagerak\b" replace="Skagerrak"/>
<Typo word="(Endo/Exo)Skeleton" find="\b([Ee](?:nd|x)os|S|s)kelat(ons?|al)\b" replace="$1kelet$2"/>
<Typo word="Slaughter" find="\b([Ss])laugter(s?|ing|ed|houses?)\b" replace="$1laughter$2"/>
<Typo word="Slightly" find="\b([Ss])ligh(?:ltl?|t)y\b" replace="$1lightly"/>
<Typo word="Slowly" find="\b([Ss])lowy\b" replace="$1lowly"/>
<Typo word="Smooth" find="\b([Ss])moothe\b(?!\s[Ss]ylk)\b" replace="$1mooth"/>
<Typo word="Sneak" find="\b([Ss])neek(\b(?<!Sneek)|s|ers?|ed|i[a-z]+|y)\b" replace="$1neak$2"/><!--don't match Sneek-->
<Typo word="Sneeze" find="\b([Ss])ne+s(e[ds]?)\b" replace="$1neez$2"/>
<Typo word="Snorkeled" find="\b([Ss])norkl(ed|ers?|ing)\b" replace="$1norkel$2"/> 
<Typo word="Social" find="\b(?:(S)o(?:ical|cal\B)|(s)o(?:ical|cal))(i[sz](?:e[ds]?|ing|ations?)|ism|ists?|it(?:i?es?|y)|ly)?\b" replace="$1$2ocial$3"/><!--don't match Socal-->
<Typo word="Societies" find="\b([Ss])ocities\b" replace="$1ocieties"/>
<Typo word="Software" find="\b([Ss])of(?:ware|twares\b(?<!\bRJ Softwares))\b" replace="$1oftware"/><!--don't match RJ Softwares-->
<Typo word="Soldier" find="\b([Ss])oilde(rs?|ring)\b" replace="$1oldie$2"/>
<Typo word="Soldiers" find="\b([Ss])oliders\b" replace="$1oldiers"/>
<Typo word="Solely_" find="\b(?<![A-Z][a-z]{0,99}\s{1,9})soley\b" replace="solely"/><!--ignore surname Soley-->
<Typo word="Soliloquy" find="\b([Ss])oliliqu(y|ies|i[sz](e[ds]?|ing)|ists?)\b" replace="$1oliloqu$2"/>
<Typo word="Solitary" find="\b([Ss])olat[ae]ry\b" replace="$1olitary"/>
<Typo word="Soloist" find="\b([Ss])olist(s)?\b" replace="$1oloist$2"/>
<Typo word="(In)Soluble" find="\b(S|s|[Ii]ns)oluab(l[ey]|ility)\b" replace="$1olub$2"/>
<Typo word="Some-" find="\b([Ss])(?:moe|oe?m)(what|where|thing|one|body|[dw]ays?|how|place|times?)\b" replace="$1ome$2"/>
<Typo word="Someone" find="\b([Ss])omene\b" replace="$1omeone"/>
<Typo word="Somewhat" find="\b([Ss])omewaht\b" replace="$1omewhat"/>
<Typo word="Sony" find="\b(?:SONY|sony)\b" replace="Sony"/>
<Typo word="(Un)Sophisticate" find="\b(S|s|[Uu]ns)(?:oph|ofist|uphist)icat(e[ds]?|ing|ion)\b" replace="$1ophisticat$2"/>
<Typo word="Sophomore" find="\b([Ss])o(?:f|ph)mor(es?|ic[a-z]*)\b" replace="$1ophomor$2"/>
<Typo word="Soufflé" find="\b([Ss])oufl([eé])(s?|ed)\b" replace="$1ouffl$2$3"/><!--"souffle" should not be replaced, see [[wikt:souffle]]-->
<Typo word="Sought" find="\b([Ss])eeked\b" replace="$1ought"/>
<Typo word="Sound" find="\b([Ss])oudn(s)?\b" replace="$1ound$2"/>
<Typo word="Soundtrack" find="\b([Ss])ountrack\b" replace="$1oundtrack"/>
<Typo word="Soup" find="\b([Ss])uop\b" replace="$1oup"/>
<Typo word="Southern" find="\b([Ss])ourth(er([ns]?|ly|lies|nmost)|(ea|we)st(er(n?|l[iesy]+))?)?\b" replace="$1outh$2"/>
<Typo word="Souvenir" find="\b([Ss])ouvenier(s?)\b" replace="$1ouvenir$2"/>
<Typo word="Soviets" find="\b([Ss])oveit(s)?\b" replace="$1oviet$2"/>
<Typo word="Space" find="\b(S|s|[Uu]ns)(?:poa|ap)c(e(?:[ds]?|rs?)|ings?)\b" replace="$1pac$2"/>
<Typo word="Spaghetti" find="\b([Ss])pag(?:et?|he)t(i|ini)\b" replace="$1paghett$2"/>
<Typo word="Spanish" find="\b[Ss]painish\b" replace="Spanish"/>
<Typo word="Sparse" find="\b([Ss])parce(r?|st|ly|ness)\b" replace="$1parse$2"/>
<Typo word="Special" find="\b(S|[Ee]?s)pe(?:ica|cai)l(s?|ly|ists?|i?ty)\b" replace="$1pecial$2"/>
<Typo word="Specialise" find="\b([Ss])pecialli([sz](e[ds]?|ing|ations?))\b" replace="$1peciali$2"/>
<Typo word="Species" find="\b([Ss])peices\b" replace="$1pecies"/>
<Typo word="Specific" find="\b([Ss])pec(?:if|fi)c(s?|ity|ally|ations?)\b" replace="$1pecific$2"/>
<Typo word="Specimen" find="\b([Ss])peciman\b" replace="$1pecimen"/>
<Typo word="Spectacular" find="\b([Ss])pectauc?la(rs?|rly)\b" replace="$1pectacula$2"/>
<Typo word="Spectrum" find="\b([Ss])pect(um|al?)\b" replace="$1pectr$2"/>
<Typo word="Speeches" find="\b([Ss])p[pr]ech(es)?\b" replace="$1peech$2"/>
<Typo word="Speech_" find="\b(?<![A-Z][a-z]{0,99}\s{1,9})([Ss])peach(es)?\b" replace="$1peech$2"/>
<Typo word="Spermatozoon" find="\b([Ss])permatozoan\b" replace="$1permatozoon"/>
<Typo word="Spiral" find="\b([Ss])prial(s?|l?ed|l?ing)\b" replace="$1piral$2"/>
<Typo word="Spiritual" find="\b([Ss])p(?:ri(?:t|ri)u|iriti)al(s?|ly|ity|is[mt]s?)\b" replace="$1piritual$2"/>
<Typo word="Splendour" find="\b([Ss])pendour\b" replace="$1plendour"/>
<Typo word="Sponsor" find="\b([Ss])pon(?:se|zo)r(s?|ed|ing|ships?)\b" replace="$1ponsor$2"/>
<Typo word="Spontaneous" find="\b([Ss])pontan(?:[eiou]{1,2})s(ly)?\b" replace="$1pontaneous$2"/>
<Typo word="Spread" find="\b([Ss])pre(?:ade)?d\b(?<!spreaded)" replace="$1pread"/><!--not "with spreaded peanut butter"-->
<Typo word="Square" find="\b([Ss])qaure([ds])?\b" replace="$1quare$2"/>
<Typo word="(De)Stabilize" find="\b(S|s|[Dd]es)tab(?:li)?li([sz](e[drs]?|ing|ation))\b" replace="$1tabili$2"/>
<Typo word="Staff" find="\b([Ss])taf(?!\s(?:de|Van|Coppens|Diecisiete|Dobbelaere)\b)(?<!Kees Staf)(s?|ed)\b" replace="$1taff$2"/><!--not Staf De Clercq, Staf Van Reet, Kees Staf etc.-->
<Typo word="Stainless" find="\b([Ss])tainle+s\b" replace="$1tainless"/>
<Typo word="(B/St/T/W)alked" find="\b([BbTtWw]|[Ss]t)alekd\b" replace="$1alked"/>
<Typo word="(B/St/T/W)alking" find="\b([BbTtWw]|[Ss]t)(?:laking|alkign)\b" replace="$1alking"/>
<Typo word="Stand" find="\b([Ss])tnad([a-z]*)\b" replace="$1tand$2"/>
<Typo word="Standards" find="\b([Ss])tandars\b" replace="$1tandards"/>
<Typo word="Start_" find="(?!\bStrater\b)\b([Ss])trat(ed|ing|ers?)\b" replace="$1tart$2"/><!--don't match strat (guitar), Strater (surname)-->
<Typo word="Statement" find="\b([Ss])tatmen(ts?)\b" replace="$1tatemen$2"/>
<Typo word="Statesman" find="\b([Ss])tatem([ae])n\b" replace="$1tatesm$2n"/>
<Typo word="Status" find="\bstaus\b" replace="status"/><!--avoid the surname Staus-->
<Typo word="Station" find="\b([Ss])taion([a-z]*)\b" replace="$1tation$2"/>
<Typo word="Stereotype" find="\b([Ss])teri?otyp(e[ds]?|ing|ical(ly)?)\b" replace="$1tereotyp$2"/>
<Typo word="Stifle" find="\b([Ss])tiffl(e[ds]?|ing)\b" replace="$1tifl$2"/>
<Typo word="Still" find="\b([Ss])itll(ness)?\b" replace="$1till$2"/>
<Typo word="Stirring" find="\b(s)tir(ed|ing)\b" replace="$1tirr$2"/>
<Typo word="Stirs" find="\b([Ss])tirrs\b" replace="$1tirs"/>
<Typo word="Stockholm" find="\b[Ss]tockhome?\b" replace="Stockholm"/>
<Typo word="Stop" find="\b([Ss])tpo(s)?\b" replace="$1top$2"/>
<Typo word="(Hi)Stories" find="\b(S|s|[Hh]is)tor(?:eis|ise)\b" replace="$1tories"/>
<Typo word="(Hi)Story" find="\b(S|s|[Hh]is)(?:otry|topry|toyr|troy)\b" replace="$1tory"/>
<Typo word="Strand" find="(?!\bStrnad\b)\b([Ss])trnad(ed|ing|s)?\b" replace="$1trand$2"/><!--don't match surname Strnad-->
<Typo word="Strange" find="(?!\bStanger?\b)\b([Ss])tange(ness|ly|rs?|st)?\b" replace="$1trange$2"/><!--don't match surnames Stange, Stanger-->
<Typo word="Strategy" find="\b([Ss])t(?:art[ae]|rat[ai]|rade)g(y|ies|ic[a-z]*|i[sz](e[ds]?|ing))\b" replace="$1trateg$2"/>
<Typo word="Streamline" find="\b([Ss])treemlin([a-z]+)\b" replace="$1treamlin$2"/>
<Typo word="Strength" find="\b([Ss])tre(?:gth|nt?gh|nth|ngh?t|nght?h?)(s?|en(?:ed|ing|s?|ers?))\b" replace="$1trength$2"/>
<Typo word="Strenuous" find="\b([Ss])trenous(ly)?\b" replace="$1trenuous$2"/>
<Typo word="(Re/Con/Di/Redi)Strict" find="\b([Rr]es|S|s|[Cc]ons|[Dd]is|[Rr]edis)tict(s?|e[dr]|ing|or|ness|est|ly|ive[a-z]*)\b" replace="$1trict$2"/>
<Typo word="Strictest" find="\b([Ss])trictist\b" replace="$1trictest"/>
<Typo word="Strikingly" find="\b([Ss])trikely\b" replace="$1trikingly"/>
<Typo word="(A)Stringent" find="\b(S|[Aa]?s)tingen(t|tly|cy)\b" replace="$1tringen$2"/>
<Typo word="Strong" find="(?!\bStong\b)\b([Ss])tor?ng(er|est|ly)?\b" replace="$1trong$2"/><!--don't match surname Stong-->
<Typo word="Stronger" find="\b([Ss])t(?:ro|or)neg(r|st)\b" replace="$1tronge$2"/>
<Typo word="Struggle" find="\b([Ss])t(?:ruggel|rugle|uggle)([ds])?\b" replace="$1truggle$2"/>
<Typo word="Struggling" find="\b([Ss])tugg?ling\b" replace="$1truggling"/>
<Typo word="Stubbornness" find="\b([Ss])tub(?:bor|orn?)nes?s\b" replace="$1tubbornness"/>
<Typo word="Student" find="\b([Ss])tudnet(s)?\b" replace="$1tudent$2"/>
<Typo word="Study" find="\b([Ss])tudd(ie[ds]|y)\b" replace="$1tud$2"/>
<Typo word="Studying" find="\b([Ss])tuding\b" replace="$1tudying"/>
<Typo word="Sturdy" find="\b([Ss])tird(y|i(e[drs]|est|ly|ness))\b" replace="$1turd$2"/>
<Typo word="(Free/Life)Style" find="\b(S|s|[Ff]rees|[Ll]ifes)(?:ytl|tly)((?:|i[sz])(?:e[ds]?|ings?)|is[ht][a-z]*)\b" replace="$1tyl$2"/>
<Typo word="Stylus" find="\b([Ss])tilus\b" replace="$1tylus"/>
<Typo word="(Sub/Un)conscious" find="\b([Ss]ub|[Uu]n)con(?:[cs]ious|science)(ly)?\b" replace="$1conscious$2"/>
<Typo word="Subjugation" find="\b([Ss])ubjudgation\b" replace="$1ubjugation"/>
<Typo word="Submit" find="\b([Ss])umbi(ts?|tted|tting|ssions?)\b" replace="$1ubmi$2"/>
<Typo word="(In)Subordinate" find="\b(S|s|[Ii]ns)ubordin?[ae]nt(e[ds]?|or|ive|ly|ions?)\b" replace="$1ubordinat$2"/>
<Typo word="Subspecies" find="\b([Ss])ubpecies\b" replace="$1ubspecies"/>
<Typo word="Substance" find="\b([Ss])ub(?:sta|tan)ce(s?)\b" replace="$1ubstance$2"/>
<Typo word="(In/Un)Substantial" find="\b(S|s|[IiUu]ns)ubsta(?:nc?|t)ia(l?|lly|lity|te[ds]?|ting)\b" replace="$1ubstantia$2"/>
<Typo word="Subterranean" find="\b([Ss])ubter?ran[ei]a(?<!ubterranea)(n|nly)\b" replace="$1ubterranea$2"/>
<Typo word="Suburb" find="\b([Ss])u(?:rburb|burburb)(s?|an(ism|ites?)?|ed)\b" replace="$1uburb$2"/>
<Typo word="Suburban" find="\b([Ss])ubur(?:bia|burba)n(ites?)?\b" replace="$1uburban$2"/>
<Typo word="Succeed" find="\b([Ss])ucc(?:cee|ed?)d(s?|ed|ing)\b" replace="$1ucceed$2"/>
<Typo word="Succeed" find="\b([Ss])uc(?:c?s|)e(ed(s?|ed|ing)|ss(es|(ful|ive)(ly)?|ions?|ors?)?)\b" replace="$1ucce$2"/>
<Typo word="(Un)Success" find="\b(S|s|[Uu]ns)uc(?:c?s)?ess?(es|ful[a-z]*|ors?)?\b" replace="$1uccess$2"/>
<Typo word="Successfully" find="\b(S|s|[Uu]ns)uccess(?:fulyl|ully)\b" replace="$1uccessfully"/>
<Typo word="Successive" find="\b([Ss])uc(?:ce|es?)si(ve[a-z]*|ons?)\b" replace="$1uccessi$2"/>
<Typo word="Suddenly" find="\b([Ss])udd?ently\b" replace="$1uddenly"/>
<Typo word="(In)Sufficient" find="\b(S|s|[Ii]ns)uf(?:[if]cie|f?icei?|f?icia?)n(t|tly|cy|cies)\b" replace="$1ufficien$2"/>
<Typo word="Succinct" find="\b([Ss])uccint(ly|ness)?\b" replace="$1uccinct$2"/>
<Typo word="Suffrage" find="\b([Ss])uf(?:f?e|e?)rag(e|ett(es?|ism)|is[tm]s?)\b" replace="$1uffrag$2"/>
<Typo word="Suggest" find="\b([Ss])ugest(s?|ed|ing|ive[a-z]*|ions?|ib[a-z]+)\b" replace="$1uggest$2"/>
<Typo word="Suicidal" find="\b([Ss])ucidial\b" replace="$1uicidal"/>
<Typo word="Suicide" find="\b([Ss])ucid(es?|al)\b" replace="$1uicid$2"/>
<Typo word="Summary" find="\b([Ss])um(?:a|e|me(?!ry))r(y|ily|i[sz](ation|e[ds]?|ing))\b" replace="$1ummar$2"/>
<Typo word="Supersede" find="\b([Ss])uperce+(de[ds]?|ding|ssions?)\b" replace="$1uperse$2"/>
<Typo word="Supplant" find="\b([Ss])u(?:r?|rp)plant(s?|ed|ing)\b" replace="$1upplant$2"/>
<Typo word="Supplement" find="\b([Ss])up(?:l[aie]+|pl[ai])ment(al|ary|ed|s|ing)?\b" replace="$1upplement$2"/>
<Typo word="Supply" find="\b([Ss])upp(iers?|y)\b" replace="$1uppl$2"/>
<Typo word="Support" find="\b([Ss])up(?:|pp+)ort(s?|ers?|ed|ing|ive[a-z]*)\b" replace="$1upport$2"/>
<Typo word="supp-" find="\bwupp(ly|orts?|ose[a-z]*)\b" replace="supp$1"/>
<Typo word="Supp-" find="\bWupp(ly|orts?|ose[a-z]*)\b" replace="Supp$1"/>
<Typo word="Supposed" find="\b([Ss])upp?o(?:ss)?(ed|edly|ing)\b" replace="$1uppos$2"/>
<Typo word="Supposedly" find="\b([Ss])uppos(?:ab|ing)ly\b" replace="$1upposedly"/>
<Typo word="(Immunosu/Su/O)ppress" find="\b((?:[Ss]|[Ii]mmunos)u|[Oo])(?:rp+res?|p+re|pres?)s(e[ds]|i[nov][a-z]+|ants?|ible|[eo]rs?)?\b" replace="$1ppress$2"/>
<Typo word="Surface" find="\b([Ss])urf(?:i?c|as)(e[ds]?|ing)\b" replace="$1urfac$2"/>
<Typo word="Surname" find="\b([Ss])irname([ds])?\b" replace="$1urname$2"/>
<Typo word="(Un)Surprise" find="\b(S|s|[Uu]ns)u(?:pri[sz]|rpriz)(e[ds]?|ing(ly)?)\b" replace="$1urpris$2"/>
<Typo word="Surrender" find="\b([Ss])ur(?:r?under|rend)(s?|ed|ing)\b" replace="$1urrender$2"/>
<Typo word="Surreptitious" find="\b([Ss])urr?(?:e?peti|ep)tious(ly)?\b" replace="$1urreptitious$2"/>
<Typo word="Surround" find="\b([Ss])(?:ur(?:ou|ro)[un]|orr?(?:o?u)n)d(s?|ed|ings?)\b" replace="$1urround$2"/>
<Typo word="Surströmming" find="\b([Ss])urstromming\b" replace="$1urströmming"/>
<Typo word="Surveil" find="\b([Ss])urveill\b" replace="$1urveil"/>
<Typo word="Surveillance" find="\b([Ss])urveil(?:l?e|a)nce\b" replace="$1urveillance"/>
<Typo word="Surveyor" find="\b([Ss])urveye(rs?)\b" replace="$1urveyo$2"/>
<Typo word="Surviv(e/al/or)" find="(?!\b[Ss]urvie\b)\b([Ss])u(?:rvivi|[rv]iv|rvi)(ed?|es|ors?(hip)?|al|ing)\b" replace="$1urviv$2"/><!--Don't match French word survie-->
<Typo word="Survivor" find="\b([Ss])ur?viv(?:io|e)(rs?)\b" replace="$1urvivo$2"/>
<Typo word="Susceptible" find="\b([Ss])u(?:c?sept[ai]|sc?epta)((ve|ble)(ness)?|bility|vity)\b" replace="$1uscepti$2"/>
<Typo word="Swea(r/t)" find="\b([Ss])wae([rt](s?|ing)|te[dr]s?)\b" replace="$1wea$2"/>
<Typo word="Swimming" find="\b([Ss])wiming(ly)?\b" replace="$1wimming$2"/>
<Typo word="Switch" find="\b([Ss])wti?ch(e[ds]|ing)?\b" replace="$1witch$2"/>
<Typo word="Symmetric" find="\b([Ss])ym(?:et+ric|metral)\b" replace="$1ymmetric"/>
<Typo word="(A/Anti)Symmetry" find="\b(S|[Aa]?s|[Aa]ntis)ymetr(y|ies|ical(ly)?)\b" replace="$1ymmetr$2"/>
<Typo word="Symphony" find="\b([Ss])ynphon(y|ies|ic)\b" replace="$1ymphon$2"/>
<Typo word="Symptom" find="\b([Ss])y(?:pmtom|mpton)(s?|atic)\b" replace="$1ymptom$2"/>
<Typo word="Synagogue" find="\b([Ss])(?:yno|ina)gog((ue)?s?|(ic)?al)\b" replace="$1ynagog$2"/>
<Typo word="Synchronize" find="\b([Ss])ync[hr]oniz(e[drs]?|ations?|ing)\b" replace="$1ynchroniz$2"/>
<Typo word="Synonymous" find="\b([Ss])inon[oay]mous(ly)?\b" replace="$1ynonymous$2"/>
<Typo word="Synthesis" find="\b([Ss])ynthas(is|i[sz]e[sdr]?)\b" replace="$1ynthes$2"/>
<Typo word="Synthesis" find="\b([Ss])ynthis([ie]s|i[sz]e[sdr]?)\b" replace="$1ynthes$2"/>
<Typo word="Syphilis" find="\b([Ss])[yi]phyl+[iu](s|tic)\b" replace="$1yphili$2"/>
<Typo word="Syrup" find="\b([Ss])yrap\b" replace="$1yrup"/>
<Typo word="System" find="\b([Ss])s?y(?:te|s)m(s|atic(ally)?|ati[sz]ed?)?\b" replace="$1ystem$2"/>
</source>

===T===
<source lang="xml">
<Typo word="(Mis)Take" find="\b(T|t|[Ss]t|[Mm]ist)kae([sn])?\b" replace="$1ake$2"/>
<Typo word="Talent_" find="(?!\bTallents?\b)\b([Tt])allent(s|ed)?\b" replace="$1alent$2"/><!--Tallent is a surname-->
<Typo word="Target" find="\b([Tt])argett(able|ed|ing|s)\b" replace="$1arget$2"/>
<Typo word="Tattoo" find="\b([Tt])a(?:t+ooe|too)(ed|s)?\b" replace="$1attoo$2"/>
<Typo word="Taught" find="\b([Tt])eached\b" replace="$1aught"/>
<Typo word="Taxonomy" find="\b([Tt])axanom(y|ic|ists?)\b" replace="$1axonom$2"/>
<Typo word="(Non)Technical" find="\b(T|t|[Nn]ont)ec(?:i?ni|h?ini?)(cal[a-z]*|ques?|cians?)\b" replace="$1echni$2"/>
<Typo word="Technician" find="\b([Tt])ech(?:ic|nit)(ians?|al[a-z]*)\b" replace="$1echnic$2"/>
<Typo word="Telephony" find="\b([Tt])elphon([a-z]+)\b" replace="$1elephon$2"/>
<Typo word="Televise" find="\b([Tt])el(?:ivi[sz]|eviz)(e[ds]?|i(ng|on)s?|ors?|ual)\b" replace="$1elevis$2"/>
<Typo word="Television" find="\b([Tt])ele(?:vsio|vis?o|levisio)n(s?)\b" replace="$1elevision$2"/>
<Typo word="(In/Sub)Temperate" find="\b(T|t|[Ii]nt|[Ss]ubt)emp(?:a?r[ae]|ere?)?(te|tely|tures?|ment[a-z]*|nce)\b" replace="$1empera$2"/>
<Typo word="Temperature" find="\b([Tt])em(?:pertaur|eratur|pa?re?a?tur|peratu)e(s)?\b" replace="$1emperature$2"/>
<Typo word="(Con)Temporary" find="\b([Cc]ont|[Tt])[ae]?(?:mp?|pm?)(?:r?orar?|[oe]?rar|oa?r|r?oar?)(?<![Tt]emporar)(y|ily|ies)\b" replace="$1emporar$2"/>
<Typo word="Tendency" find="\b([Tt])endan?c(y|ies)\b" replace="$1endenc$2"/>
<Typo word="Tennessee" find="\b[Tt]en(?:(?:nn+|)ess+e*|n+es(?:ss+)?e*|n+ess+(?:ee+|))(e|ans?)\b" replace="Tennesse$1"/>
<Typo word="(Extra)Terrestrial" find="\b(T|t|[Ee]xtrat)er(?:rest|estr?)ial(s?|ly)\b" replace="$1errestrial$2"/>
<Typo word="Territory" find="\b([Tt])er+[iae]t*o+[rt]*(?<!erritor)(y|ies|ially|ial)\b" replace="$1erritor$2"/>
<Typo word="Terrorist" find="\b([Tt])err(?:itor|o)ist(s?|ic)\b" replace="$1errorist$2"/>
<Typo word="Tête-à-tête" find="\b([Tt])ete-a-tete(s)?\b" replace="$1ête-à-tête$2"/>
<Typo word="Thérèse Raquin" find="\bTh[eè]r[eé]se\s+Raquin\b" replace="Thérèse Raquin"/>
<Typo word="Than" find="\b([Tt])ahn\b" replace="$1han"/>
<Typo word="Tha(n/t/w)" find="\b([Tt])h([ntw])a\b" replace="$1ha$2"/>
<Typo word="Thanks" find="\b([Tt])hansk\b" replace="$1hanks"/>
<Typo word="That" find="\b([Tt])(?:(?:yh|h[gy])at|hta|aht)\b" replace="$1hat"/>
<Typo word="That's" find="\b([Tt])ha(?:ts|st)\b" replace="$1hat's"/>
<Typo word="Thaw" find="\bunthaw(s?|ed|ing)\b" replace="thaw$1"/>
<Typo word="Thaw" find="\bUnthaw(s?|ed|ing)\b" replace="Thaw$1"/>
<Typo word="The" find="\b([Tt])(?:heh|hge|hw|je|[jgt]he)\b" replace="$1he"/>
<Typo word="The(space)" find="\b([Tt])he(([Bb]e|[Ff]ir|[Ll]a|[Mm]o)st|[Ss]econd|[Tt]hird)\b" replace="$1he $2"/><!--don't find "Theman", "TheWorld"-->
<Typo word="(space)The" find="\b([Aa](?:fter|nd|s|t)|[Bb]y|[Ff]or|[IiOo][fn]|[Oo]ver|[Tt]o|[Uu](?:nder|ntil|p)[Ww](?:hen|ith))([Tt])he(?!\sInternational)\b" replace="$1 $2he"/><!--don't find "(Be/Go/Or/So)the" or [[Tothe International]]-->
<Typo word="Theatre" find="\b([Tt])heather(s)?\b" replace="$1heatre$2"/>
<Typo word="Theatre" find="\b([Tt])hreatr(es?|ics?|ical(s?|ly))\b" replace="$1heatr$2"/>
<Typo word="Their" find="\bth(?:eri|ier)(s?)\b" replace="their$1"/><!--Thier & Thiers are surnames-->
<Typo word="Themselves" find="\b([Tt])he(?:mself|irselve)s\b" replace="$1hemselves"/>
<Typo word="(T/W)hen" find="\b([TtWw])(?:hne?|ehn)\b" replace="$1hen"/>
<Typo word="Theorem" find="\b([Tt])heoru?m\b" replace="$1heorem"/>
<Typo word="Theoretic" find="\b([tT])heorectic(al[a-z]*|s)?\b" replace="$1heoretic$2"/>
<Typo word="There(after/by/fore)" find="\b([Tt])her(after|by|fore)\b" replace="$1here$2"/>
<Typo word="There (grammar)" find="\b([Tt])heir\s+((?:are|were|is|(?:c|w|sh)ould|[hw]as|have|had|may)(?:n't)?|can(?:not|'t)?|shall|shan't|ain't|might(?=\s+be\b))\b(?!-)" replace="$1here $2"/><!--Don't match 'their would-be'-->
<Typo word="These" find="\b([Tt])heese\b" replace="$1hese"/>
<Typo word="They" find="\b([Tt])(?:yhe|ehy)\b" replace="$1hey"/>
<Typo word="Thief" find="\b([Tt])hei(f|ves|very|ving)\b" replace="$1hie$2"/>
<Typo word="Thing" find="\b([Tt])h(?:ign|nig)(s?)\b" replace="$1hing$2"/>
<Typo word="Things" find="\b([Tt])higsn\b" replace="$1hings"/>
<Typo word="Think" find="\b([Tt])hi(?:kn|unk)(s?|ing)\b" replace="$1hink$2"/>
<Typo word="Thin(g/k)" find="\bHtin([gk])n?(s?|ing)?\b" replace="Thin$2$3"/>
<Typo word="thin(g/k)" find="\bhtin([gk])n?(s?|ing)?\b" replace="thin$2$3"/>
<Typo word="Third" find="\b([Tt])h(?:rid|irth)(s?|ly)\b" replace="$1hird$2"/>
<Typo word="Thirteen" find="\b([Tt])h(?:rit|irth)een(s?|ths?)\b" replace="$1hirteen$2"/>
<Typo word="This" find="\b([Tt])(?:ihs|hsi|ghis)\b" replace="$1his"/>
<Typo word="This/There/Them/They/Then/The" find="\bHt(e[mny]?|is|ere)\b" replace="Th$1"/>
<Typo word="This/there/them/they/then/the" find="\bht(e[mny]?|is|ere)\b" replace="th$1"/>
<Typo word="Thorough_" find="\b([Tt])hro(?:rough(ly|ness)?|ugh(ly))\b" replace="$1horough$2$3"/><!--don't match through(ness)-->
<Typo word="Those" find="\b([Tt])hsoe\b" replace="$1hose"/>
<Typo word="(T/W)hose" find="\b([TtWw]h)oose\b" replace="$1ose"/>
<Typo word="Threaten" find="\b([Tt])(?:hret|h?reath?)e?n(?<!hreaten)(s|ed|ings?)?\b" replace="$1hreaten$2"/>
<Typo word="Threatened" find="\b([Tt])hreatend(?:ed)?\b" replace="$1hreatened"/>
<Typo word="Three" find="\b([Tt])hree(es?)\b" replace="$1hre$2"/>
<Typo word="Threshold" find="\b([Tt])(?:h?res(?:s|hh)|resh)old(s?)\b" replace="$1hreshold$2"/>
<Typo word="T(h)rough" find="\b([Tt]h?)roug\b" replace="$1rough"/>
<Typo word="Through(out)" find="\b([Tt])hrou(?:[gh]|ght|hg)(out)?\b" replace="$1hrough$2"/>
<Typo word="Throughout" find="\b([Tt])houghout\b" replace="$1hroughout"/>
<Typo word="Thus far" find="\b([Tt])husfar\b" replace="$1hus far"/>
<Typo word="Tighten" find="\b([Tt])ightn(ing|ed|s)?\b" replace="$1ighten$2"/>
<Typo word="Time" find="\b([Tt])iem(ly|lines*)?\b" replace="$1ime$2"/>
<Typo word="Time" find="\b([Tt])imn(e[ds]?|ely|ing)\b" replace="$1im$2"/>
<Typo word="Tobacco" find="\b([Tt])(?:|abb?[ao]c?|obbac?|oba)co(s?|nists?)\b(?<!Tabac(co|os?)\b)" replace="$1obacco$2"/><!--Don't correct Tabaco(s) City, surname Tabacco-->
<Typo word="Today" find="\b([Tt])odya\b" replace="$1oday"/>
<Typo word="Today's" find="\b([Tt])oday(?:s's?|s\b)" replace="$1oday's"/>
<Typo word="Together" find="\b([Tt])(?:ogheh?th?|ogehth?|oget|iogeth?)er(ness)?\b" replace="$1ogether$2"/>
<Typo word="(In)Tolerant" find="\b(T|t|[Ii]nt)ol(?:l?ere|lera)n(ces?|t(ly)?)\b" replace="$1oleran$2"/>
<Typo word="Tolkien" find="\b[Tt]olkein\b" replace="Tolkien"/>
<Typo word="Tomorrow" find="\b([Tt])om(?:mor?|o)ro(ws?)\b" replace="$1omorro$2"/>
<Typo word="Tongue" find="\b([Tt])oung(e[ds]?|ing)\b" replace="$1ongu$2"/>
<Typo word="Tonight" find="\b([Tt])on(?:ihg|gih)t\b" replace="$1onight"/>
<Typo word="Torpedoes" find="\b([Tt])orpe(?:adoe?|do)([ds])\b" replace="$1orpedoe$2"/>
<Typo word="_Torsion_" find="\b(?<!X\.\s{1,3})([Tt])ortion(s?|al(ly)?)\b" replace="$1orsion$2"/><!--don't find "X. Tortion World Wide"; beware of "tort" variants-->
<Typo word="Total" find="\b([Tt])ottal(s|ly|l?ed|l?ing)?\b" replace="$1otal$2"/>
<Typo word="Tournament" find="\b([Tt])[ou]+[urna]{2,5}m[en]+t(?<!ournament)(s?)\b" replace="$1ournament$2"/>
<Typo word="(Un)Toward(s)" find="\b(T|t|[Uu]nt)ow(?:ra|or)(ds?)\b" replace="$1owar$2"/>
<Typo word="Town" find="\b([Tt])won(houses?|s|ships?)?\b" replace="$1own$2"/>
<Typo word="(In)Tractable" find="\b(T|t|[Ii]nt)ractibl([ey])\b" replace="$1ractabl$2"/>
<Typo word="(Ex/Non)Tradition" find="\b(T|t|[Ee]xt|[Nn]ont)radi(?:i?t|cti)on(s?|al(ly)?|alis[mt]s?)\b" replace="$1radition$2"/>
<Typo word="Traffic_" find="\b([Tt])raf+ic(ed|ers?|ing)\b" replace="$1raffick$2"/>
<Typo word="Trailer" find="\b([Tt])railor(s?|ed|ing|able)\b" replace="$1railer$2"/>
<Typo word="Transcribing" find="\b([Tt])ranscript(e[ds]?|ing)\b" replace="$1ranscrib$2"/>
<Typo word="Transept" find="\b([Tt])ranscep(ts?)\b" replace="$1ransep$2"/>
<Typo word="Transferred" find="\b([Tt])rans?fe(re[dr]|ring?)\b" replace="$1ransfer$2"/>
<Typo word="Transform" find="\b([Tt])ranform(s?|ed|ers?|ing|ati[a-z]+|able)\b" replace="$1ransform$2"/>
<Typo word="Transition" find="\b([Tt])rans(?:is|iti)?tion(s|al)?\b" replace="$1ransition$2"/>
<Typo word="Translate" find="\b([Tt])ran(?:sa)?lat(e[ds]?|ing|ions?|ors?)?\b" replace="$1ranslat$2"/>
<Typo word="Transparent" find="\b([Tt])ransp(?:[^a]r.|ar[^e])n(t|tly|ce|cy|tness)\b" replace="$1ransparen$2"/>
<Typo word="Transportation" find="\b([Tt])ranspora(tion|ble|bility)\b" replace="$1ransporta$2"/>
<Typo word="Transcontinental" find="\b([Tt])rans(\s|-)continental\b" replace="$1ranscontinental"/>
<Typo word="(Mal/Mis)Treatment" find="\b(T|t|[Mm](?:al|is)t)reateme?n(ts?)\b" replace="$1reatmen$2"/>
<Typo word="Tremolo" find="\b([Tt])remelo(s?)(?<!\bTremelo)\b" replace="$1remolo$2"/><!--don't match place Tremelo-->
<Typo word="Tried" find="\b([Tt])ryed\b" replace="$1ried"/>
<Typo word="Triggered" find="\b([Tt])rig+uered\b" replace="$1riggered"/>
<Typo word="Trilogy" find="\b([Tt])riology\b" replace="$1rilogy"/>
<Typo word="Trolling" find="\b([Tt])roling\b" replace="$1rolling"/>
<Typo word="Troubles" find="\b([Tt])oubles\b" replace="$1roubles"/>
<Typo word="Truly" find="\b([Tt])ru(?:le|el)y\b" replace="$1ruly"/>
<Typo word="Trunk" find="\b([Tt])urnk\b" replace="$1runk"/>
<Typo word="Trust" find="\b([Tt])ust(s?|ing|worthy)\b" replace="$1rust$2"/>
<Typo word="Tübingen" find="\b[Tt]ubingen\b" replace="Tübingen"/>
<Typo word="Turmoil" find="\b([Tt])ermoil\b" replace="$1urmoil"/>
<Typo word="Tutelage" find="\b([Tt])ut(?:[ai]l[aie]|el[ei])ge\b" replace="$1utelage"/>
<Typo word="Twelfth" find="\b([Tt])wel(?:f|th)(s?)\b" replace="$1welfth$2"/>
<Typo word="Twentieth" find="\b([Tt])went(?:e?i|ien)th\b" replace="$1wentieth"/>
<Typo word="(A)Typical" find="\b(T|[Aa]?t)(?:ipic|ypci)al(ly|ity|ness)?\b" replace="$1ypical$2"/>
<Typo word="Tyranny" find="\b([Tt])yr(?:ran?|a)n(y|ic[a-z]*|ous[a-z]*|iz[a-z]*)\b" replace="$1yrann$2"/>
</source>

===U===
<!--Most "Un-" words appear under their roots: "(Un)Root"-->
<source lang="xml">
<Typo word="Übermensch" find="\b[Uu]bermensch(es)?\b" replace="Übermensch$1"/>
<Typo word="Ulterior" find="\balterior\b" replace="ulterior"/>
<Typo word="Ultimate" find="\b([Uu])l(?:i?t|ta)mat(e(ly)?|um)\b" replace="$1ltimat$2"/>
<Typo word="Ultimately" find="\b([Uu])ltimely\b" replace="$1ltimately"/>
<Typo word="Unanimous" find="\b([Uu])na(?:mi|ny)[nm]ous(ly)?\b" replace="$1nanimous$2"/>
<Typo word="Under Milk Wood" find="\bUnder\s+Milkwood\b" replace="Under Milk Wood"/>
<Typo word="Under(ground/stand)" find="\b([Uu])(?:dner|ndre)(grounds?|stand(?:abl[ey]|ing|s?))\b" replace="$1nder$2"/>
<Typo word="(Mis)Understand" find="\b(U|u|[Mm]isu)(?:dn|nd)er(?:stna|tan)d(s?|abl[ey]|ings?)\b" replace="$1nderstand$2"/>
<Typo word="(Mis)Understood" find="\b(U|u|[Mm]isu)nderstoo[^d]\b" replace="$1nderstood"/>
<Typo word="Undoubtedly" find="\b([Uu])ndoubtely\b" replace="$1ndoubtedly"/>
<Typo word="Unilateral" find="\b([Uu])n(?:[ia]latre|alater)a(l|lly)\b" replace="$1nilatera$2"/>
<Typo word="Uninhabited" find="\b([Uu])nihabited\b" replace="$1ninhabited"/>
<Typo word="Universal" find="\b([Uu])niver(?:si)?al(s?|ly|ity|ness|is[tm]s?)\b" replace="$1niversal$2"/>
<Typo word="University" find="\b([Uu])n[ei]?v[erscit]{3,7}(?:(?:(y)|[it]*(ies)|[it]*(i)t(es))|(i)t(es))\b(?<!niversit(?:y|ies))" replace="$1niversit$2$3$4$5$6$7"/>
<Typo word="Unknown" find="\b([Uu])(nkon?|kno)wn\b" replace="$1nknown"/>
<Typo word="Unofficial" find="\binofficial(ly)?\b" replace="unofficial$1"/>
<Typo word="Unofficial" find="\bInofficial(ly)?\b" replace="Unofficial$1"/>
<Typo word="Unwieldy" find="\b([Uu])nw(?:eildl?|ieldl)(y|iness)\b" replace="$1nwield$2"/>
<Typo word="Until" find="\b([Uu])(?:nit|ntil|pti)l\b" replace="$1ntil"/>
<Typo word="Util-" find="\b([Uu])(?:t|lti)li+([stz][a-z]+)\b" replace="$1tili$2"/>
<Typo word="Up to" find="\b([Uu])pto\b" replace="$1p to"/>
<Typo word="(Mis/Dis)Use" find="\b(U|u|[DdMm]isu)is(e[ds]?)\b" replace="$1s$2"/>
<Typo word="(Un)Usual" find="\b(U|u|[Uu]nu)s(?:s+ual?|s*aul?|al|ua|us[au]l)(ly)?\b" replace="$1sual$2"/>
<Typo word="Uzbekistan" find="\b[Uu]zbekystan\b" replace="Uzbekistan"/>
</source>

===V===
<source lang="xml">
<Typo word="Vacuum" find="\b([Vv])ac(?:cuum|c?ume?)(s?|ed|ing)\b" replace="$1acuum$2"/>
<Typo word="Variety" find="\b([Vv])(?:ar[ia]+t|r?iet|ri?eit|arie)(ies|y)\b" replace="$1ariet$2"/>
<Typo word="(Junior/Senior) varsity" find="\b([Jj]u|[Ss]e)niors\s+varsity\b" replace="$1nior varsity"/>  
<Typo word="Vegetable" find="\b([Vv])eg[ai]?tabl(es?)\b" replace="$1egetabl$2"/>
<Typo word="Vegetarian" find="\b([Vv])eg(?:et(?:ter?|er)|ata)rian(s?|ism)\b" replace="$1egetarian$2"/>
<Typo word="Vehicle" find="\b([Vv])ehic[aeu]le?(s)?\b" replace="$1ehicle$2"/>
<Typo word="Vengeance" find="\b([Vv])eng[ea]nce\b" replace="$1engeance"/>
<Typo word="Venomous" find="\b([Vv])en[aei]mous\b" replace="$1enomous"/>
<Typo word="Verify" find="\b([Vv])era?f(y|ie[ds]|ying|ications?)\b" replace="$1erif$2"/>
<Typo word="(Ad/…)Version" find="\b([Aa]d|[Cc]on|[Dd]i|[Ii]n|[Oo]b|[Pp]er|[Rr]e|[Ss]ub)?([Vv])er(?:is|ti)o(ns?)\b" replace="$1$2ersio$3"/>
<Typo word="(In)Vertebrate" find="\b(V|v|[Ii]nv)ertibrate(s?)\b" replace="$1ertebrate$2"/>
<Typo word="Vertical" find="\b([Vv])erticle(s?)\b" replace="$1ertical$2"/>
<Typo word="Very" find="\b([Vv])(?:eyr|rey|yer|yre)\b" replace="$1ery"/>
<Typo word="Veteran" find="\b([Vv])erter(ans?)\b" replace="$1eter$2"/>
<Typo word="Veterinary" find="\b([Vv])er?t(?:[ea]?r[aei]?|[eai])n[ae](?<!eterina)r(y|ians?)\b" replace="$1eterinar$2"/>
<Typo word="Vicinity" find="\b([Vv])(?:(?:a|in)cini|[ai]cin)t(y|ies)\b" replace="$1icinit$2"/>
<Typo word="Victory" find="\b([Vv])itor(y|ies|ious(ly)?)\b" replace="$1ictor$2"/>
<Typo word="View" find="\b(?:Vei|Wie)w(ing|ers?|ed|able)\b(?<!Wiewer)" replace="View$1"/>
<Typo word="View" find="\b(?:vei|wie)w(ing|ers?|ed|able)\b" replace="view$1"/>
<Typo word="Vigilance" find="\b([Vv])ig(?:[ae]?la|[iea]le)n([ct][a-z]*?)\b" replace="$1igilan$2"/>
<Typo word="Vigorous" find="\b([Vv])ig(?:[aei]rou?|oro)s(ly|ness)?\b" replace="$1igorous$2"/>
<Typo word="Vilify" find="\b([Vv])il(?:li|l?a)f(y|ie[ds]|ying|ications?)\b" replace="$1ilif$2"/>
<Typo word="Village" find="\b([Vv])il(?:a|l?i|le?)ge(r?s?)(?<!illigers?|Villeger)\b" replace="$1illage$2"/>
<Typo word="Villain" find="(?!\bVilain\b)\b(V|v|[Ss]uperv)il(?:l?ia|ai)n(s?|y|ous[a-z]*|ess)\b" replace="$1illain$2"/><!--Don't match surname Vilain-->
<Typo word="Violence" find="\b([Vv])iolentce\b" replace="$1iolence"/>
<Typo word="Virtual" find="\b([Vv])irutal(ly)?\b" replace="$1irtual$2"/>
<Typo word="Viscosity" find="\b([Vv])iscocit(y|ies)\b" replace="$1iscosit$2"/>
<Typo word="Visit" find="\b([Vv])is(?:is)?t(ing|ed|ors?)\b" replace="$1isit$2"/><!--don't find "visiter"-->
<Typo word="(Di/Pa/Pro/Reple/Super/Tele)Visor" find="\b([Dd]i|[Pp](?:a|ro)|[Rr]eple|[Ss]uper|[Tt]ele)([Vv])iser([a-z]*)\b" replace="$1$2isor$3"/>
<Typo word="Volcano" find="\b([Vv])ol?lcanoe\b" replace="$1olcano"/>
<Typo word="Volkswagen" find="\b[Vv]olkswagon(s?)\b" replace="Volkswagen$1"/>
<Typo word="Volley(ball)" find="\b([Vv])ol[el]y([ -]?ball)?(ed|ers?|ing|s?)\b(?<!\bVol[le]y\b)" replace="$1olley$2$3"/>
<!--Don't match proper nouns Volly/Voley unless followed by " ball" --->
<Typo word="(In)Voluntary" find="\b(V|v|[Ii]nv)ol[oe]ntary\b" replace="$1oluntary"/>
<Typo word="Volunteer" find="\b([Vv])ol(?:ante?|unt|ou?nte?|l[ou]nte?)er(ed|ing|s?)\b" replace="$1olunteer$2"/>
<Typo word="Vomit" find="\b([Vv])omitt(s?|e[dr]|ing)\b" replace="$1omit$2"/>
</source>

===W===
<source lang="xml">
<Typo word="(Un)Want" find="\b(W|w|[Uu]nw)(?:atn|hant|nat)(s?|ed|ing)\b" replace="$1ant$2"/>
<Typo word="Warfare" find="\b([Ww])arefare\b" replace="$1arfare"/>
<Typo word="(Un)Warrant" find="\b(W|w|[Uu]nw)ar(?:re|a)nt((ee|[eo]r)?s?|ed|ing|y|ies)\b" replace="$1arrant$2"/>
<Typo word="Was" find="(?!\bWass\b)\b([Ww])(?:ea|as)s\b" replace="$1as"/><!--Don't match surname Wass-->
<Typo word="Way" find="\b([Ww])ya(s)?\b" replace="$1ay$2"/>
<Typo word="Weapon" find="\b([Ww])(?:eapon[ae]|[ae]pon)(s?|ry|i[sz]ed?)\b" replace="$1eapon$2"/>
<Typo word="Website" find="\b([Ww])e(?:bstit?e|bsit|biste|sbite)(s)?\b" replace="$1ebsite$2"/>
<Typo word="Weigh" find="\b([Ww])iegh(ed|ing)\b" replace="$1eigh$2"/>
<Typo word="Weight" find="\b([Oo]verw|[Uu]nderw|[Ll]ightw|[Mm]iddlew|[Hh](?:eavy|undred)w|[Ff](?:eather|ly)w|[Cc](?:ount|ruis)erw|[Pp](?:enny|aper)w|[Ww]elterw|W|w)ieght(s?|ed|ing|less)\b" replace="$1eight$2"/>
<Typo word="Weird" find="\b([Ww])ierd(er|est|l?y|ness|o|oes|ies?)?\b(?<!Carissa's Wierd)" replace="$1eird$2"/><!--not Carissa's Wierd-->
<Typo word="well" find="\bvell\b" replace="well"/>
<Typo word="What" find="\b([Ww])(?:aht|hta)\b" replace="$1hat"/>
<Typo word="Where" find="\b([Ww])(?:her|eh)re\b" replace="$1here"/>
<Typo word="Whereabouts" find="\b([Ww])(?:her[ae]|erea)bouts\b" replace="$1hereabouts"/>
<Typo word="Whereas" find="\b([Ww])her(?:as|ease)\b" replace="$1hereas"/>
<Typo word="Whereupon" find="\b([Ww])herupon\b" replace="$1hereupon"/>
<Typo word="Whether" find="\b([Ww])hther\b" replace="$1hether"/>
<Typo word="Which" find="\b([Ww])(?:hihc|hcih|hic|ihch|hlch)\b" replace="$1hich"/>
<Typo word="who" find="\bwoh\b" replace="who"/><!--don't match name Woh-->
<Typo word="Wholly" find="\b([Ww])holel?y\b" replace="$1holly"/>
<Typo word="Widespread" find="\b([Ww])ide(?:-?srea|-sprea|-?spre)d\b" replace="$1idespread"/><!--don't fix "wide-spreading"-->
<Typo word="Wikipedia" find="\b[Ww]h?[Iiî]+[KkCc]+[Iiîaeou]+?[ -]?([MmPp])+[aeiǣæÆé]{0,2}di?e?[îi]?(an?\'?s?|c)\b(?!\.\w|-\w)(?<!Wiki[mp]edi(an?\'?s?|c)\b)" replace="Wiki$1edi$2"/><!--Not URLs's and domains-->
<Typo word="William(s/son/sburg)" find="\bWillaim(s?|sons?|sburg)\b" replace="William$1"/>
<Typo word="(Un)Willingness" find="\b(W|w|[Uu]nw)illingless\b" replace="$1illingness"/>
<Typo word="Windows" find="\b([Ww])indoes\b" replace="$1indows"/>
<Typo word="with" find="\bwithe\b" replace="with"/><!--Don't fix surname Withe-->
<Typo word="With" find="\b([Ww])(?:ih[nt]?|hith|itht|tit?h)\b" replace="$1ith"/>
<Typo word="Withdrawal" find="\b([Ww])ithdrawl(s?)\b" replace="$1ithdrawal$2"/>
<Typo word="Withhold" find="\b([Ww])ith([oe])ld(s?|ing)\b" replace="$1ithh$2ld$3"/>
<Typo word="Within" find="\b([Ww])ithing\b" replace="$1ithin"/>
<Typo word="Wonderful" find="\b([Ww])onerful(ly)?\b" replace="$1onderful$2"/>
<Typo word="Word" find="\b([Ww])rod(ing|ed|s?)\b" replace="$1ord$2"/> 
<Typo word="Wor(d/k)" find="\bOwr([dk])(s?|ers?|ed|ing|y)\b" replace="Wor$1$2"/>
<Typo word="wor(d/k)" find="\bowr([dk])(s?|ers?|ed|ing|y)\b" replace="wor$1$2"/>
<Typo word="(Un)Work" find="\b(W|w|[Uu]nw)(?:rok|okr)(ed|ing|abl[ey]|ability|m[ae]n[a-z]*|ingm[ae]n|bench|fare|(er|shop|room|out|(sp|pl)ace|table|ho[ru]se|book|boat|load|a?day|flow|folk|up|week|aholic|station)?s?)\b" replace="$1ork$2"/>
<Typo word="Workstation" find="\b([Ww])ork(?:sts|\-sta)tion(s)?\b" replace="$1orkstation$2"/> 
<Typo word="World" find="\b([Ww])orls\b" replace="$1orld"/>
<Typo word="World" find="\b(W|w|[Uu]nderw)(?:rol|olr)d(s?|ly|wide)\b" replace="$1orld$2"/>
<Typo word="World Wide Web" find="\b[Ww]orld[-\s]*wide\s+[Ww]eb\b" replace="World Wide Web"/> 
<Typo word="Worldwide" find="\b([Ww])ord?l(-?)wide\b" replace="$1orld$2wide"/>
<Typo word="Worsen" find="\b([Ww])orsten([a-z]*)\b" replace="$1orsen$2"/>
<Typo word="Worthwhile" find="\b([Ww])orthwile(ness)?\b" replace="$1orthwhile$2"/>
<Typo word="Would" find="\b([Ww])(?:uould|oudl)\b" replace="$1ould"/>
<Typo word="Would" find="\bOwu(?:ld|dl)\b" replace="Would"/>
<Typo word="would" find="\bowu(?:ld|dl)\b" replace="would"/>
<Typo word="Wrestler" find="\b([Ww])rester(s)?\b" replace="$1restler$2"/>
<Typo word="Write" find="\b([Ww])(?:irt?|rit|riit?)t(er?s?|ing|ten)\b" replace="$1rit$2"/>
<Typo word="Wr(i/o)te" find="\b([Ww])r([io])et(s)?\b" replace="$1r$2te$3"/>
<Typo word="write" find="\brwite(s)?\b" replace="write$1"/>
<Typo word="Write" find="\bRwite(s)?\b" replace="Write$1"/>
<Typo word="Written" find="\b([Ww])riten\b" replace="$1ritten"/>
</source>

===X===
<source lang="xml">
<Typo word="Xbox" find="\b[Xx][-\s]?[Bb][Oo][Xx]([e\']?s)?\b(?<!Xbox([e\']?s)?)(?!\sbinding)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Xbox$1"/><!--Not false positive X-box binding protein-->
</source>

===Y===
<source lang="xml">
<Typo word="Yacht" find="\b([Yy])at?ch(s?|ing|sm[ae]n)\b" replace="$1acht$2"/>
<Typo word="Year/Near/Clear" find="\b([Yyn]|[Cc]l)(?:era|aer)(s?|ly|ings?|ed)\b" replace="$1ear$2"/>
<Typo word="Ye(ar/t)" find="\bEy(ar(s?|ly)|t)\b" replace="Ye$1"/>
<Typo word="ye(ar/t)" find="\bey(ar(s?|ly)|t)\b" replace="ye$1"/>
<Typo word="Years" find="\b([Yy])(easr|ersa)\b" replace="$1ears"/>
<Typo word="Yellow" find="\b([Yy])elow(s?|ed|ing|er|ish)\b" replace="$1ellow$2"/>
<Typo word="You" find="\b([Yy])(?:tou|uo|oiu)\b(?<!Youd\b)" replace="$1ou"/>
<Typo word="you'(d\ve\re\ll)_" find="\b([Yy])ou;?(d|[rv]e|ll)\b(?<!\bYoud)" replace="$1ou'$2"/><!--avoid false positive Youd-->
<Typo word="Your(s)_" find="(?!\b[Yy]oru\b)\b([Yy])(?:uor|oru)(s?|self|selves)\b" replace="$1our$2"/><!--avoid false positive yoru/Yoru-->
<Typo word="Yourself" find="\b([Yy])ouself\b" replace="$1ourself"/>
</source>

===Z===
<source lang="xml">
<Typo word="Zebra" find="\b([Zz])ee+(bras?)\b" replace="$1e$2"/>
<Typo word="Zionism" find="\bsionis(ts?|m)\b" replace="Zionis$1"/>
</source>

===SI unit symbols===
<source lang="xml">
<Typo word="bit" find="([\d\.]+(?:\s|&nbsp;|-)?[KkMmGgTt]?)(?:bps|(?:bits|b)\/se?c?)\b" replace="$1bit/s"/>
<Typo word="kbit" find="([\d\.]+(?:\s|&nbsp;|-)?)Kbit/s\b" replace="$1kbit/s"/>
<Typo word="Mbit" find="([\d\.]+(?:\s|&nbsp;|-)?)mbit/s\b" replace="$1Mbit/s"/>
<Typo word="Gbit" find="([\d\.]+(?:\s|&nbsp;|-)?)gbit/s\b" replace="$1Gbit/s"/>
<Typo word="F (farad)" find="([\d\.]+(?:\s|&nbsp;|-)?[nµkMT])f\b" replace="$1F"/>
<Typo word="GHz (gigahertz)" find="([\d\.]+(?:\s|&nbsp;|-)?)g[hH][zZ]\b" replace="$1GHz"/>
<Typo word="GPa (gigapascal)" find="([\d\.]+(?:\s|&nbsp;|-)?)gP[Aa]\b" replace="$1GPa"/>
<Typo word="Hz (hertz)" find="\b([µmkMGT\s]|[-\d\.]+(?:&nbsp;|-)?)h[zZ]\b" replace="$1Hz"/>
<Typo word="J (joule)" find="([\d\.]+(?:\s|&nbsp;|-)?[µmkMGT])j\b" replace="$1J"/>
<Typo word="kg (kilogram)" find="([\d\.]+)(?<!\b198[89])(?:\s|&nbsp;)?(?:K[Gg]'?s?|[Kk][Gg]'?s)\b(?<!Co\.\s?KG)" replace="$1&nbsp;kg"/>
<Typo word="km (kilometre)" find="([\d\.]+)(?<!\b(?:1979|1980|1995))(?:\s|&nbsp;)?(?:K[Mm]'?s?|[Kk][Mm]'?s)\b" replace="$1&nbsp;km"/>
<Typo word="-kg (kilogram)" find="([\d\.]+)-(?:K[Gg]'?s?|[Kk][Gg]'?s)\b" replace="$1-kg"/>
<Typo word="-km (kilometre)" find="([\d\.]+)-(?:K[Mm]'?s?|[Kk][Mm]'?s)\b" replace="$1-km"/>
<Typo word="kHz (kilohertz)" find="([\d\.]+)(?:\s|&nbsp;)?(K[hH][zZ]|khz)\b" replace="$1&nbsp;kHz"/>
<Typo word="-kHz (kilohertz)" find="([\d\.]+)-(K[hH][zZ]|khz)\b" replace="$1-kHz"/>
<Typo word="kJ (kilojoule)" find="([\d\.]+(?<!\b(?:1981|199[58]))(?:\s|&nbsp;|-)?)K[jJ]\b" replace="$1kJ"/>
<Typo word="km²" find="\b(?<!\{)[Ss][Qq][-.\s]+[Kk][Mm][Ss]?\b" replace="km<sup>2</sup>"/><!--Look-behind makes sure it's not in a conversion template-->
<Typo word="kPa (kilopascal)" find="([\d\.]+(?:\s|&nbsp;|-)?)K(?:[pP]a|pA)\b" replace="$1kPa"/>
<Typo word="Pa (pascal)" find="([\d\.]+(?:\s|&nbsp;|-)?[µkMGT])p[aA]\b" replace="$1Pa"/>
<Typo word="W (watt)" find="([\d\.]+(?:\s|&nbsp;|-)?[µmkMGT])w\b" replace="$1W"/>
<Typo word="Wb (weber)" find="([\d\.]+(?:\s|&nbsp;|-)?)([µmkMGT])w[bB]\b" replace="$1$2Wb"/>
</source>

===Capitalisation===

====Cultures, languages, and ethnic groups====
<!--See also "Geographical proper names"-->
<source lang="xml">
<Typo word="Ålandish" find="\b[Aa]landish\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ålandish"/>
<Typo word="Algonquian" find="\balgon(qu|k)(ia?ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Algon$1$2"/>
<!--American covered in "America(n)" rule-->
<Typo word="Apache" find="\bapache(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Apache$1"/>
<Typo word="Ara(b/wak/ucan/maic/mean/paho/gonese)" find="\bara(b(i(an|st))?s?|wak(an)?s?|ucan(ian)?s?|maic|ma?eans?|pahoe?s?|gonese)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ara$1"/>
<Typo word="Arabic_" find="\barabic(ize[ds]?|izing)?\b(?<![Gg]um\s{1,9}arabic)" replace="Arabic$1"/>
<Typo word="Atha(b/p)as(c/k)an" find="\batha([bp])as([ck])an(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Atha$1as$2an$3"/>
<Typo word="Breton" find="\bbret+o(ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Breto$1"/>
<Typo word="Catalan" find="\bcatal+a(ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Catala$1"/>
<Typo word="Cherokee" find="\bcher+oke+(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cherokee$1"/>
<Typo word="Cyrillic" find="\bcyr+il+i(cs?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cyrilli$1"/>
<Typo word="Czech" find="\bch?zech(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Czech$1"/>
<Typo word="Dakota" find="\bdakota(n?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Dakota$1"/>
<Typo word="Dutch" find="\bdutch(m[ae]n)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Dutch$1"/>
<!--English- covered in another rule-->
<Typo word="French" find="\bfrench(m[ae]n)*\b(?!\sfr(y|ies))(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="French$1"/><!-- avoid "french fry/fries" -->
<Typo word="Gujarati" find="\bguj[au]rat+(is?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Gujarat$1"/>
<Typo word="Gurkha" find="\bgurkha(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Gurkha$1"/>
<Typo word="Hebrew" find="\bhebr(ews?|aic|ais[tm])\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Hebr$1"/>
<Typo word="Hellenic" find="\bhel+[ae]n((ist)?ic)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Hellen$1"/>
<Typo word="Hind(i/u(stan(i)))" find="\bhind([iu]s?|ustan(is?)?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Hind$1"/>
<Typo word="Hispan-" find="\bhispan(ics?|ici[sz][a-z]+|ia|iola|o)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Hispan$1"/>
<Typo word="Irish" find="\birish(m[ae]n)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Irish$1"/>
<Typo word="Jew" find="\bj(ews?|ewish(ness)?|udaica?|udean?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="J$1"/>
<Typo word="Latin" find="\blatin(?!-?[0-9])([ao]s?|is[mt]s?|i[sz](e[ds]?|ing))?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Latin$1"/>
<Typo word="Navajo" find="\bnava([hj]os?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Nava$1"/>
<Typo word="Ptolem(y|aic)" find="\bptolem(y|aic)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ptolem$1"/>
<Typo word="Sanskrit" find="\b(sanskri|[Ss]anskir?)t\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Sanskrit"/>
<Typo word="Sioux" find="\bsiou(x|an)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Siou$1"/>
<Typo word="Tamil" find="\btamil\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tamil"/>
<Typo word="Urdu" find="\burdu\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Urdu"/>
<Typo word="Viking" find="\bvikin(gs?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Vikin$1"/>
</source>

====Companies and institutions====
<source lang="xml">
<Typo word="Disney World" find="\b[Dd]isney[Ww]orld\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Disney World"/><!--Not domains and URLs-->
<Typo word="Disneyland" find="\b[Dd]isney(\s+[Ll]|L)and\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Disneyland"/><!--Not domains and URLs-->
<Typo word="Harvard" find="\bharvard\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Harvard"/><!--Not domains and URLs-->
<Typo word="IBM" find="\b[Ii]bm\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="IBM"/><!--Not domains and URLs-->
<Typo word="Microsoft" find="\b(?:micros|[Mm]icors|[Mm]icro[S\$])oft\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Microsoft"/><!--Not domains and URLs-->
<Typo word="TiVo" find="\b(?:Tiv|ti[Vv])o('?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="TiVo$1"/><!--Not domains and URLs-->
</source>

====Continents and subcontinents====
<source lang="xml">
<Typo word="(Ant)Arctic Circle" find="\b(A|Anta)rctic\s+circle\b" replace="$1rctic Circle"/>
<Typo word="Antarctic" find="\bantarc?ti(ca?)\b(?!'')(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Antarcti$1"/><!--Arctic dealt with elsewhere, don't match on organism scientific name-->
<Typo word="Africa" find="\bafri(can?s?|ka(n?|ans|ners?|nda))\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Afri$1"/>
<Typo word="America" find="\bameric(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Americ$1"/>
<Typo word="Asia_" find="\bai?si(an?s?|atic)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Asi$1"/><!--Avoid match on .asia (domain name)-->
<Typo word="Austral(as)ia" find="\baustral((as)?ian?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Austral$1"/>
<Typo word="Central America" find="\bcentral\s*[Aa]meric(an?s?)\b" replace="Central Americ$1"/>
<Typo word="Eur(asia/ope)" find="\beur(asia(?:ns?|)|ope(?:ans?|))\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})"replace="Eur$1"/>
<Typo word="North America" find="\bnorth\s*[Aa](merican?s?)\b" replace="North A$1"/>
<Typo word="Panamerica" find="\bpan[Aa]merica(n?s?|nism)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Panamerica$1"/>
<Typo word="Pan-America" find="\bpan-[Aa]merica(n?s?|nism)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Pan-America$1"/>
<Typo word="Polynesia" find="\bpolynes(ian?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Polynes$1"/>
<Typo word="South America" find="\bsouth\s*[Aa](merican?s?)\b" replace="South A$1"/>
</source>

====Geographical proper names====
<source lang="xml">
<!--Geographical names with capital letters-->
<Typo word="Abkhazia" find="\babkha(s|[sz]ian?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Abkha$1"/>
<Typo word="Afghanistan" find="\bafghani(s?|stan)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Afghani$1"/>
<Typo word="Akro(n/tiri)" find="\bakro(n|tiri)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Akro$1"/>
<Typo word="Åland" find="\båland\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Åland"/>
<Typo word="Albania" find="\balbania(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Albania$1"/>
<Typo word="Algeria" find="\balgeri(e|an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Algeri$1"/>
<Typo word="Andorra" find="\bandor+a(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Andorra$1"/>
<Typo word="Angola" find="\bangoli?(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Angol$1"/>
<Typo word="Anguilla" find="\banguil+(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Anguill$1"/>
<Typo word="Anti(gua/lles)" find="\banti(guan?s?|lles)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Anti$1"/>
<Typo word="Greater Antilles" find="\bgreater\s+[Aa]ntilles\b" replace="Greater Antilles"/>
<Typo word="Lesser Antilles" find="\bles+er\s+[Aa]ntilles\b" replace="Lesser Antilles"/>
<Typo word="Arabia" find="\barab(s?|ian?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Arab$1"/>
<Typo word="Argentina" find="\bargentin(a|e(an)?s?)\b(?!\'\')(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Argentin$1"/><!--avoid when part of scientific name-->
<Typo word="Armenia" find="\barmenia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Armenia$1"/>
<Typo word="Aruba" find="\barub(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Arub$1"/>
<Typo word="Ascension Island" find="\bascension island\b" replace="Ascension Island"/>
<Typo word="Austr-" find="\baustr(al|ones)?(ian?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Austr$1$2"/>
<Typo word="Azer-" find="\bazer(baijan)?(is?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Azer$1$2"/>
<Typo word="Babylon(ia)" find="\bbab[yi]lon(ian?s?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Babylon$1"/>
<Typo word="Bahamas" find="\bbaham+(as?|i?ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Baham$1"/>
<Typo word="Bahrain" find="\bbahrain(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Bahrain$1"/>
<Typo word="Bangladesh" find="\bbangl[ae]des(hi?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Banglades$1"/>
<Typo word="Barbados" find="\bbarbad(os|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Barbad$1"/>
<Typo word="Barbuda/Bermuda" find="\bb(arb|erm)ud(i?an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="B$1ud$2"/>
<Typo word="Basutoland" find="\bbasutoland\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Basutoland"/>
<Typo word="Bei(jing/rut)" find="\bbei(jing|rut)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Bei$1"/>
<Typo word="Bel(arus/gium/ize)" find="\bbel(arus(s?ians?)?|gi(um|ans?)|iz(e|ians?))\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Bel$1"/>
<Typo word="Benin" find="\bbenin(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Benin$1"/>
<Typo word="Bhutan" find="\bbhutan(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Bhutan$1"/>
<Typo word="Bolivia/Bosnia" find="\bbo(liv|sn)i(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Bo$1i$2"/>
<Typo word="Botswana" find="\bbotswana(n?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Botswana$1"/>
<Typo word="Brazil" find="\bbrazil?(l|lians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Brazi$1"/>
<Typo word="Brunei" find="\bbrunei\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Brunei"/>
<Typo word="Bulgar(ia)" find="\bbulgar(ian?s?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Bulgar$1"/>
<Typo word="Burkina Faso" find="\b[Bb]urkina\s*(?:fas+|Fass)o\b" replace="Burkina Faso"/>
<Typo word="Bur(kina/ma/undi)" find="\bbur(kina|ma|mese|urundi(ans?)?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Bur$1"/>
<Typo word="Byzantine" find="\bbyzant?ti(nes?|um)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Byzanti$1"/>
<Typo word="Cambodia" find="\bcambodia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cambodia$1"/>
<Typo word="Cameroon" find="\bcameroon\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cameroon"/>
<Typo word="Cameroonian" find="\bcamero+nia(ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cameroonia$1"/>
<Typo word="Canada" find="\bcanad(a|i[ae]n[as]?)\b(?<!canadien)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Canad$1"/>
<Typo word="Cape Verde" find="\b[Cc]ape\s*verde\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cape Verde"/>
<Typo word="Cayman Islands" find="\b[Cc]ayman islands\b" replace="Cayman Islands"/>
<Typo word="Central African Republic" find="\b[Cc]entral\s+[Aa]frican\s+republic\b" replace="Central African Republic"/>
<Typo word="Chadian" find="\bchadia(ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Chadia$1"/>
<Typo word="Chilean" find="\bchil+[ei]a(ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Chilea$1"/>
<Typo word="Chinese" find="\bchin+es+e\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Chinese"/>
<Typo word="Christmas Island" find="\b[Cc]hristmas\s+island\b" replace="Christmas Island"/>
<Typo word="Col(o/u)mbia" find="\bcol([ou])mbia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Col$1mbia$2"/><!--Not domains and URLs-->
<Typo word="Comoros" find="\bcomoros\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Comoros"/>
<Typo word="Congo" find="\bcong(o|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cong$1"/>
<Typo word="Cook Islands" find="\b[Cc]ook\s*islands\b" replace="Cook Islands"/>
<Typo word="Corsica" find="\bcorsica(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Corsica$1"/>
<Typo word="Costa Rica" find="\b[Cc]osta\s*rica(ns?)?\b" replace="Costa Rica$1"/>
<Typo word="Côte d'Ivoire" find="\bc[oô]te\s+d'[Ii]voire\b" replace="Côte d'Ivoire"/>
<Typo word="Crete" find="\bcret(e|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cret$1"/>
<Typo word="Croatia" find="\bcroat(s?|ia|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Croat$1"/>
<Typo word="Cuba_" find="\bcuba(ns?)?(?!\s+prime)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cuba$1"/>
<Typo word="Cyprus" find="\bc[yi]pr(us|iots?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cypr$1"/>
<Typo word="Czech Republic" find="\bczec[hk]\s*[Rr]epublic\b" replace="Czech Republic"/>
<Typo word="Dahomey" find="\bdahomey\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Dahomey"/>
<Typo word="Danish" find="\bdan+ish\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Danish"/>
<Typo word="Democratic People's Republic of Korea" find="\b[Dd]emocratic\s*people['′]?s\s*republic\s*of\s*[kK]orea\b" replace="Democratic People's Republic of Korea"/>
<Typo word="Democratic Republic of Congo" find="\b[Dd]emocratic\s+republic\s+of\s+[Cc]ongo\b" replace="Democratic Republic of Congo"/>
<Typo word="Denmark" find="\bdenmark\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Denmark"/>
<Typo word="Dhekelia" find="\bdhekeli(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Dhekeli$1"/>
<Typo word="Djibouti" find="\bdjibouti\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Djibouti"/>
<Typo word="Dominica" find="\bdomin+ici?(a|ans?)\b(?!'')(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Dominic$1"/><!--don't match when scientific name-->
<Typo word="Dominican Republic" find="\bdominican\s*[rR]epublic\b" replace="Dominican Republic"/>
<Typo word="East Timor" find="\beast\s*timor\b" replace="East Timor"/>
<Typo word="Ecuador" find="\becua?d+or(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ecuador$1"/>
<Typo word="Egypt" find="\beg[yi]pt(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Egypt$1"/>
<Typo word="El Salvador" find="\bel\s*[Ss]alvado(r|rians?)\b" replace="El Salvado$1"/>
<Typo word="Equatorial Guinea" find="\bequatorial\s*[Gg]uinea\b" replace="Equatorial Guinea"/>
<Typo word="Eritrea" find="\beritrea(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Eritrea$1"/>
<Typo word="Estonia" find="\bestonia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Estonia$1"/>
<Typo word="Ethiopia" find="\beth[ie]opia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ethiopia$1"/>
<Typo word="Falkland Islands" find="\b[Ff]au?lkland\s*islands\b" replace="Falkland Islands"/>
<Typo word="Falkland" find="\bfau?lkland(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Falkland$1"/>
<Typo word="Faroe Islands" find="\b[Ff]aroe\s*islands\b" replace="Faroe Islands"/>
<Typo word="Fehnerbaçe" find="\b(?:[fF]ehnerbac|fehnerbaç)e\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Fehnerbahçe"/>
<Typo word="Fiji" find="\bfiji(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Fiji$1"/>
<Typo word="Filipino" find="\b(?:(?:[Pp]h|f)il+ip+inoe?|Filipinoe)(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Filipino$1"/>
<Typo word="Finland" find="\bfin(land(ia)?|nish)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Fin$1"/>
<Typo word="France" find="\bfrance\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="France"/>
<Typo word="French Polynesia" find="\b[Ff]rench\s*polynesia\b" replace="French Polynesia"/>
<Typo word="Gabon" find="\bgabon\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Gabon"/>
<Typo word="Gambia" find="\bgambia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Gambia$1"/>
<Typo word="Georgia" find="\bgeorgia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Georgia$1"/>
<Typo word="Germany" find="\bgerman(s?|y|ic|is[mt]s?|i[sz]e[sdr]?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})(?<!cousin[- ]german)" replace="German$1"/><!-- don't match [[wikt:cousin-german]] -->
<Typo word="Ghana" find="\bghan(a(n?|ian)s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ghan$1"/>
<Typo word="Gibraltar" find="\bgibraltar(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Gibraltar$1"/>
<Typo word="Greece" find="\bgre(ece|eks?|cian)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Gre$1"/>
<Typo word="Greenland" find="\bgreenland(ic|ers?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Greenland$1"/>
<Typo word="Grenad(a/ines)" find="\bgrenad(an?s?|ines)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Grenad$1"/>
<Typo word="Guatemala" find="\bguatemala(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Guatemala$1"/>
<Typo word="Guinea-Bissau" find="\b[Gg]uinea-bissau\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Guinea-Bissau"/>
<Typo word="Guinean" find="\bguinea(ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Guinea$1"/>
<Typo word="Guyana" find="\bguyana(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Guyana$1"/>
<Typo word="Haiti" find="\bhaiti(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Haiti$1"/>
<Typo word="Herzegovina" find="\bherzegovin(a|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Herzegovin$1"/>
<Typo word="Honduras" find="\bhondura(n?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Hondura$1"/>
<Typo word="Hong Kong_" find="\b(?!Hongkong [Ll]and\b)[Hh]ong[-\s]*kong\b" replace="Hong Kong"/><!--avoid [[Hongkong Land]]-->
<Typo word="Hungary" find="\bhungar(y|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Hungar$1"/>
<Typo word="I(c/r)eland" find="\bi([cr])eland(ers?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="I$1eland$2"/>
<Typo word="Icelandic" find="\biceland(ic|ers?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Iceland$1"/>
<Typo word="India" find="\bindia(n?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})(?![\s-]rubber)" replace="India$1"/><!--don't match india rubber-->
<Typo word="Indonesia" find="\bindonesia(ns?)?\b(?<!indonesia(ns?)?)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Indonesia$1"/><!--not in urls or domains-->
<Typo word="Ira(n/q)_" find="\bira(n|nians?|qi?s?)\b(?<!Ira(n|nians?|qi?s?))(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ira$1"/><!--Avoid match on domains and URLs-->
<Typo word="Islas Malvinas" find="\bislas\s+[Mm]alvinas\b" replace="Islas Malvinas"/>
<Typo word="Italy" find="\bital+(y|ian?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ital$1"/>
<Typo word="Ivory Coast" find="\b[Ii]vory\s*coast\b" replace="Ivory Coast"/>
<Typo word="Jamaica" find="\bjam+ai?ca(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Jamaica$1"/>
<Typo word="Japan" find="\bjapan\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Japan"/>
<Typo word="Japanese" find="\bjapan+es+e\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Japanese"/>
<Typo word="Jordan" find="\bjordan(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Jordan$1"/>
<Typo word="Kazak(h)" find="\bka[sz]ak(h?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kazak$1"/>
<Typo word="Kazakhstan" find="\bka[sz]akh?stan\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kazakhstan"/>
<Typo word="Kenya" find="\bkenya(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kenya$1"/>
<Typo word="Kirg(h)iz(stan/ia)" find="\bkir(gh?)iz(ia|stan)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kir$1iz$2"/>
<Typo word="Kiribati" find="\bkiribati(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kiribati$1"/>
<Typo word="Korea" find="\bkorea(n?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Korea$1"/>
<Typo word="Kosovo" find="\bkos+ov(o|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kosov$1"/>
<Typo word="Kuwait" find="\bkuwait(is?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kuwait$1"/>
<Typo word="Kyrgyzstan" find="\b(?:Kyrgy|kyrgyz)stan(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kyrgyzstan$1"/>
<Typo word="Laos" find="\blao(s|tians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Lao$1"/>
<Typo word="Latvia" find="\blatvia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Latvia$1"/>
<Typo word="Lebanese" find="\bleb[ae]n?nes+e\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Lebanese"/>
<Typo word="Lebanon" find="\bleb[ae]n(on|ese)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Leban$1"/>
<Typo word="Lesotho" find="\blesoth(o|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Lesoth$1"/>
<Typo word="Liberia" find="\bliberia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Liberia$1"/>
<Typo word="Libya" find="\blib[yi]a(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Libya$1"/>
<Typo word="Liechtenstein" find="\bliechtenstein\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Liechtenstein"/>
<Typo word="Lithuania" find="\blithuania(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Lithuania$1"/>
<Typo word="Luxembourg" find="\bluxembourg\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Luxembourg"/>
<Typo word="Maca(o/u)" find="\bmaca([ou])\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Maca$1"/>
<Typo word="Macedon" find="\bmac[ae]don(ian?s?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Macedon$1"/>
<Typo word="Madagascar" find="\bmad[ae]gasca(r|ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Madagasca$1"/>
<Typo word="Malawi" find="\bmal+awi(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Malawi$1"/>
<Typo word="Malay(sia)" find="\bmal+ay(alam|ali|an?s?|s|sian?s?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Malay$1"/>
<Typo word="Maldives" find="\bmald[ei]v(es|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Maldiv$1"/>
<Typo word="Mali" find="\bmali\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mali"/>
<Typo word="Malta" find="\bmal+t(a|ese)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Malt$1"/>
<Typo word="Marshall Islands" find="\b[Mm]arshal+\s+islands\b" replace="Marshall Islands"/>
<Typo word="Mauritania" find="\bmauritania(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mauritania$1"/>
<Typo word="Mauritius" find="\bmauriti(us|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mauriti$1"/>
<Typo word="Mayotte" find="\bmayotte\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mayotte"/>
<Typo word="Mexico" find="\bmexic(o|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mexic$1"/>
<Typo word="Micronesia" find="\bmicronesia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Micronesia$1"/>
<Typo word="Moldova" find="\bmoldov(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Moldov$1"/>
<Typo word="Monaco" find="\bmon(aco|acans?|egasques?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mon$1"/>
<Typo word="Mongolia" find="\bmongol+(s?|ian?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mongol$1"/>
<Typo word="Montenegro" find="\bmontenegr(o|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Montenegr$1"/>
<Typo word="Montserrat" find="\b(?:mont?ser+|Montser)a(ti?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Montserra$1"/><!--Don't fix name Monserrat-->
<Typo word="Morocco" find="\bmor+oc+(o|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Morocc$1"/>
<Typo word="Mozambique" find="\bmozambique\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mozambique"/>
<Typo word="Myanmar" find="\bmyanmar\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Myanmar"/>
<Typo word="Nagorno-Karabakh" find="\b[Nn]agorno-karabakh\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Nagorno-Karabakh"/>
<Typo word="Namibia" find="\bnamibi(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Namibi$1"/>
<Typo word="Nauru" find="\bnauru\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Nauru"/>
<Typo word="Nepal" find="\bnepal\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Nepal"/>
<Typo word="Nepalese" find="\bnep[ae]l?les?se\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Nepalese"/>
<Typo word="Netherlands" find="\bnetherlands\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Netherlands"/>
<Typo word="New Caledonia" find="\b[Nn]ew\s+caledonia(ns?)?\b" replace="New Caledonia$1"/>
<Typo word="New Zealand" find="\b[Nn]ew\s+(?:zea|Ze)land(ers?)?\b" replace="New Zealand$1"/>
<Typo word="Nicaragua" find="\bnicaragua(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Nicaragua$1"/>
<Typo word="Niger(ia)" find="\bniger(i[ae]n?s?|ois|\b(?!''))\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Niger$1"/><!--don't match scientific names-->
<Typo word="Niue" find="\bniue\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Niue"/>
<Typo word="Norfolk Island" find="\b[Nn]orfolk\s+island\b" replace="Norfolk Island"/>
<Typo word="North Korea" find="\bnorth\s+kore(a|ans?)\b" replace="North Kore$1"/>
<Typo word="Northern Cyprus" find="\bnorthern cyprus\b" replace="Northern Cyprus"/>
<Typo word="Northern Mariana Islands" find="\bnorthern\s+[Mm]ariana\s+islands\b" replace="Northern Mariana Islands"/>
<Typo word="Nor(way/wegian/se/man(dy)/folk)" find="\bnor(way|wegians?|se|sem[ae]n|dic|mans?|mandy|folk)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Nor$1"/>
<Typo word="Oman" find="\boma(ni?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Oma$1"/>
<Typo word="Pakistan" find="\bpakist(ani?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Pakist$1"/>
<Typo word="Palau" find="\bpalau\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Palau"/>
<Typo word="Palestine" find="\b(?:pale|[Pp]ali)stin(e|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Palestin$1"/>
<Typo word="Palestinian" find="\b[Pp]al[ei]stian(s)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Palestinian$1"/>
<Typo word="Panama" find="\bpanam+a(nians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Panama$1"/>
<Typo word="Papua New Guinea" find="\b[Pp]apua new [Gg]uinea\b" replace="Papua New Guinea"/>
<Typo word="Paraguay" find="\bparagua[yi](ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Paraguay$1"/>
<Typo word="People's Republic of China" find="\b[Pp]eople['′]s\s+republic\s+of\s+[Cc]hina\b" replace="People's Republic of China"/>
<Typo word="Per(sia/u)" find="\bper(sian?s?|u|uvians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Per$1"/>
<Typo word="Philippin(e/o)" find="\bphil?lip?pino([eo]s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Philippin$1"/>
<Typo word="Philippine" find="\b(?:phil+ip+|Phil+ip)ine(s)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Philippine$1"/>
<Typo word="Pitcairn Islands" find="\b[Pp]itcairn\s+islands\b" replace="Pitcairn Islands"/>
<Typo word="Poland" find="\bpoland\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Poland"/>
<Typo word="Portugal" find="\bportugal\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Portugal"/>
<Typo word="Portuguese" find="\bportug+u?eu?s+e\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Portuguese"/>
<Typo word="Pridnestrovie" find="\bpridnestrovie\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Pridnestrovie"/>
<Typo word="Punjab(i)" find="\bpunjab(i?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Punjab$1"/>
<Typo word="Qatar" find="\bqu?ata(ri?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Qata$1"/>
<Typo word="Republic of China/Congo" find="\brepublic\s+of\s+[Cc](hina|ongo)\b" replace="Republic of C$1"/>
<Typo word="Republic of Korea" find="\brepublic\s+of\s+[kK]orea\b" replace="Republic of Korea"/>
<Typo word="Romania" find="\bromani(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Romani$1"/>
<Typo word="Russia" find="\brus+i(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Russi$1"/>
<Typo word="Rwanda" find="\brwanda(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Rwanda$1"/>
<Typo word="Saint Helena" find="\bsaint\s+[Hh]elena\b" replace="Saint Helena"/>
<Typo word="Saint Kitts and Nevis" find="\bsaint\s+[Kk]itts\s+and\s+[Nn]evis\b" replace="Saint Kitts and Nevis"/>
<Typo word="Saint Lucia" find="\bsaint [Ll]ucia\b" replace="Saint Lucia"/>
<Typo word="Saint Pierre and Miquelon" find="\bsaint\s+[Pp]ierre\s+and\s+[Mm]iquelon\b" replace="Saint Pierre and Miquelon"/>
<Typo word="Saint Vincent and the Grenadines" find="\bsaint\s+[Vv]incent\s+and\s+the\s+[Gg]renadines\b" replace="Saint Vincent and the Grenadines"/>
<Typo word="Samoa" find="\bsamoa(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Samoa$1"/>
<Typo word="San Marino" find="\b[Ss]an\s+marino\b" replace="San Marino"/>
<Typo word="São Paulo" find="\b[Ss](?:ã[uõ]\s+[Pp]a[uo]|a[ouõ]\s+[Pp]a[uo]|ão\s+[Pp]ao|ão\s+pa[ou])lo\b" replace="São Paulo"/>
<Typo word="São Tomé and Príncipe" find="\b[Ss][ãa]o\s+[Tt]om[ée]\s+and\s+pr[íi]ncipe\b" replace="São Tomé and Príncipe"/>
<Typo word="São Tomé and Príncipe" find="\b[Ss]ao\s+[Tt]ome\s+and\s+Principe\b" replace="São Tomé and Príncipe"/>
<Typo word="Sardinia" find="\bsardini(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Sardini$1"/>
<Typo word="Saud(i)" find="\bsaud(i?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Saud$1"/>
<Typo word="Scandinavia" find="\b(?:scand[ai]|Scanda)navia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Scandinavia$1"/>
<Typo word="Senegal" find="\bsen[ae]gal\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Senegal"/>
<Typo word="Senegalese" find="\bsen[ae]gal+[ae]s?se\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Senegalese"/>
<Typo word="Serbia" find="\bserbi(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Serbi$1"/>
<Typo word="Sèvres" find="\bSevres\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Sèvres"/>
<Typo word="Seychelles" find="\bseychel+es\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Seychelles"/>
<Typo word="Sierra Leone" find="\bsier+a\s+[Ll]eone(ans?)?\b" replace="Sierra Leone$1"/>
<Typo word="Sierra Leonese" find="\bsier+a\s+[Ll]eones+e\b" replace="Sierra Leonese"/>
<Typo word="Singapore" find="\bsingap+or[ei](ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Singapore$1"/>
<Typo word="Slav(on)ic" find="\bslav(on)?ic\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Slav$1ic"/>
<Typo word="Slov(ak/en)ia" find="\bslov(ak|en)ia(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Slov$1ia$2"/>
<Typo word="Solomon Islands" find="\b[Ss]olomon\s+islands\b" replace="Solomon Islands"/>
<Typo word="Somali(a/land)" find="\bsomali(a?|s|ans?|land)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Somali$1"/>
<Typo word="South Africa" find="\bsouth\s+[Aa]frica(ns?)?\b" replace="South Africa$1"/>
<Typo word="South Korea" find="\bsouth\s+[Kk]ore(a|ans?)\b" replace="South Kore$1"/>
<Typo word="South Ossetia" find="\bsouth\s+[Oo]ssetia\b" replace="South Ossetia"/>
<Typo word="Spain" find="\bspa(in|ni(?:sh|ards?))\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Spa$1"/>
<Typo word="Sri Lanka" find="\b[Ss]ri\s*lank(a|ans?)\b" replace="Sri Lank$1"/>
<Typo word="Sudan" find="\bsudan\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Sudan"/>
<Typo word="Sudanese" find="\bsudan+es+e\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Sudanese"/>
<Typo word="Suriname" find="\bsuriname(rs?|se)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Suriname$1"/>
<Typo word="Svalbard" find="\bsvalbard\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Svalbard"/>
<Typo word="Swaziland" find="\bswaziland\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Swaziland"/>
<Typo word="Sweden" find="\bswed(en|ish)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Swed$1"/>
<Typo word="Switzerland" find="\bswi(tzerland|ss)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Swi$1"/>
<Typo word="Syria" find="\bsyri(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Syri$1"/>
<Typo word="Taiwan" find="\btaiwan(ese)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Taiwan$1"/>
<Typo word="Tajikistan" find="\btajikistan(i?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tajikistan$1"/>
<Typo word="Tanzania" find="\btanzania(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tanzania$1"/>
<Typo word="Thailand" find="\bthailand\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Thailand"/>
<Typo word="Timor" find="\btimor(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Timor$1"/>
<Typo word="Timor-Leste" find="\b[Tt]imor-leste\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Timor-Leste"/>
<Typo word="Tobago" find="\btobag(o|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tobag$1"/>
<Typo word="Togan(s)" find="\btogan(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Togan$1"/><!-- do not capitalize "togo", as it might mean "to go" -->
<Typo word="Tokelau" find="\btokelau\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tokelau"/>
<Typo word="Tonga" find="\btonga(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tonga$1"/>
<Typo word="Transnistria" find="\btransnistria(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Transnistria$1"/>
<Typo word="Trinidad" find="\btrin+idad(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Trinidad$1"/>
<Typo word="Tristan da Cunha" find="\b[Tt]ristan da cunha\b" replace="Tristan da Cunha"/>
<Typo word="Tunisia" find="\btunisi(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tunisi$1"/>
<Typo word="Turk(men)istan" find="\bt(ur[ck]o?)(m[ea]n)?(s?|ic|[ei]stan)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="T$1$2$3"/>
<Typo word="Turkish" find="\bturkis([hm])\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Turkis$1"/>
<Typo word="Turks and Caicos Islands" find="\b[Tt]urks\s+and\s+[Cc]aicos\s+islands\b" replace="Turks and Caicos Islands"/>
<Typo word="Tuvalu" find="\btuvalu(vians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tuvalu$1"/>
<Typo word="Uganda" find="\buganda(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Uganda$1"/>
<Typo word="Ukraine" find="\b(?:Ukra|ukrai?)n(e|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ukrain$1"/>
<Typo word="United Arab Emirates" find="\b[Uu]nited\s+[Aa]rab\s+emirates\b" replace="United Arab Emirates"/>
<Typo word="Uruguay" find="\burugua[yi](ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Uruguay$1"/>
<Typo word="Uzbekistan" find="\bu[sz]be[ck]istan(i?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Uzbekistan$1"/>
<Typo word="Vanuatu" find="\bvanuatu\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Vanuatu"/>
<Typo word="Vatican City" find="\b[Vv]atican\s+city\b" replace="Vatican City"/>
<Typo word="Venezuela" find="\bvenez+uel+(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Venezuel$1"/>
<Typo word="Vietnam" find="\bviet\s*[Nn]am\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Vietnam"/>
<Typo word="Vietnamese" find="\bvietnames+e\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Vietnamese"/>
<Typo word="Virgin Islands" find="\b[Vv]irgin islands\b" replace="Virgin Islands"/>
<Typo word="Wallis and Futuna" find="\b[Ww]allis\s+and\s+futuna\b" replace="Wallis and Futuna"/>
<Typo word="Western Sahara" find="\bwestern\s+sahara\b" replace="Western Sahara"/>
<Typo word="Württemberg" find="\bw[uü]rt+emberg\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Württemberg"/>
<Typo word="Yemen" find="\byem+en(is?|ites?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Yemen$1"/>
<Typo word="Yugoslavia" find="\byugoslavi(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Yugoslavi$1"/>
<Typo word="Zambia" find="\bzambi(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Zambi$1"/>
<Typo word="Zimbabwe" find="\bzimbabw[ei](ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Zimbabwe$1"/>
</source>

=====Canada=====
<source lang="xml">
<Typo word="Alberta" find="\balberta(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Alberta$1"/>
<Typo word="Klondike" find="\bklondike\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Klondike"/>
<Typo word="Labrador" find="\blabrador([ie]ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Labrador$1"/>
<Typo word="Manitoba" find="\bmanitoba(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Manitoba$1"/>
<Typo word="Montr(e/é)al" find="\bmontr([eé])al(ers?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Montr$1al$2"/>
<Typo word="Newfoundland" find="\bnewfoundland(ers?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Newfoundland$1"/>
<Typo word="Ontario" find="\bontari(o|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ontari$1"/>
<Typo word="Qu(e/é)bec" find="\bqu([eé])bec(ois|k?ers?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Qu$1bec$2"/>
<Typo disabled="Saskat(chewa/oo)n" find="\bsaskat(chewa|oo)n\b" replace="Saskat$2n"/><!--Disabled due to multiple meanings-->
<Typo word="Toronto" find="\btoront(o|onians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Toront$1"/>
<Typo word="Vancouver" find="\bvancouve(r|rites?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Vancouve$1"/>
<Typo word="Vancouver" find="\b[Vv]ancove(r|rites?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Vancouve$1"/>
<Typo word="Winnipeg" find="\bwin+[iea]peg\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Winnipeg"/>
<Typo word="Yukon Territory" find="\b[Yy]ukon\s*territory\b" replace="Yukon Territory"/>
<Typo word="Yukon" find="\byukon\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Yukon"/>
</source>

=====United Kingdom=====
<source lang="xml">
<Typo word="Britain" find="\b(?:br(?:it?|ri)?t(ains?|ons?|ish(ers?|isms?|ly|ness)?|icisms?|ney|pop|tany)|[Bb]rist(ish)(ers|ness)?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Brit$1$3$4"/>
<Typo word="Engl(and/ish)" find="\b(?:eng?|En)(land|lish((wo)?m[ae]n)?)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Eng$1"/>
<Typo word="Great Britain" find="\bgreat\s+[Bb]ritain(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Great Britain"/>
<Typo word="Isle of Man" find="\b[Ii]sle\s+of\s+man" replace="Isle of Man"/>
<Typo word="Manx((wo)man)" find="\bmanx((wo)?m[ae]n)?(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Manx$1"/>
<Typo word="Scot(land/s/sman/swoman/tish)" find="\bscot?(lands?|s(?:(?:wo)?m[ae]ns?)?|tish)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Scot$1"/><!--No domains, URLs nor scotch-->
<Typo word="Welsh" find="\bwelsh(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Welsh"/>
</source>

=====United States – States=====
<source lang="xml">
<Typo word="Ala(bam/sk)a" find="\bala(bam|sk)(a|i?ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ala$1$2"/>
<Typo word="Arizona" find="\barizon(a|i?ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Arizon$1"/><!--Not domains and URLs-->
<Typo word="Arkansas" find="\barkans(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Arkans$1"/>
<Typo word="California" find="\bcaliforni(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Californi$1"/>
<Typo word="Carolina" find="\bcarolin(an?s?)\b(?!'')(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Carolin$1"/><!--don't match when part of scientific name of an organism-->
<Typo word="Colorado" find="\bcolorad(o|ans?)\b(?!'')(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Colorad$1"/><!--don't match when scientific name-->
<Typo word="Connecticut" find="\b(con+|Con)ecticut\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Connecticut"/>
<Typo word="Delaware" find="\bdelawar(es?|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Delawar$1"/>
<Typo word="Florida" find="\bflorid(a|ians?)\b(?!'')(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Florid$1"/><!--don't match when part of scientific name of an organism-->
<Typo word="Guam" find="\bguam\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Guam"/>
<Typo word="Hawaii" find="\bhawaii(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Hawaii$1"/>
<Typo word="Idaho" find="\bidaho(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Idaho$1"/>
<Typo word="Indiana(polis)" find="\bindian(a|i?ans?|apolis|town)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Indian$1"/><!--Not domains and URLs-->
<Typo word="Iowa" find="\biow(an?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Iow$1"/>
<Typo word="Kansas" find="\bkansa(ns?|s)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kansa$1"/>
<Typo word="Kentucky" find="\bkentuck(y|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Kentuck$1"/>
<Typo word="Louisiana" find="\blouisian(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Louisian$1"/>
<Typo word="Maine" find="\bmaine\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Maine"/>
<Typo word="Maryland" find="\bmarylan(d|ders?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Marylan$1"/>
<Typo word="Massachusetts" find="\b(?:massachusetts|[Mm](?:as+achuse|asachuset?|as+achusset?)ts+)(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Massachusetts$1"/>
<Typo word="Michigan" find="\bmichigan(ders?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Michigan$1"/>
<Typo word="Minnesota" find="\bminnesot(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Minnesot$1"/>
<Typo word="Mississippi" find="\b(?:mississippi|[Mm]is(?:issip|sisip|sissi)pi)(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mississippi$1"/>
<Typo word="Missouri" find="\bmissour(i|ians?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Missour$1"/>
<Typo word="Montana" find="\bmontan(a|ans?)\b(?!'')(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Montan$1"/><!--don't match when part of scientific name of an organism-->
<Typo word="Nebraska" find="\bnebrask(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Nebrask$1"/>
<Typo word="Nevada" find="\bnevad(a|i?ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Nevad$1"/>
<Typo word="New England_" find="\b[Nn]ew\s{0,9}[Ee]ngland(ers?)?\b(?<!new\s{0,9}England\b|New\sEngland(ers?)?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="New England$1"/><!--exclude 'new England' and self match --->
<Typo word="New Jersey" find="\bnew\s*[Jj]ersey(ites?)?\b" replace="New Jersey$1"/>
<Typo word="New Hampshire_" find="\bhampsh?ire\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Hampshire"/><!--not 'new =>New' as Hampshire UK-->
<Typo word="New Mexico_" find="\b[Nn]ew\s{0,9}[Mm]exic(o|ans?)\b(?<!new\s{0,9}Mexicans?\b|New\sMexic(o|ans?)\b)(?<!\.[^\s\.]{0,999})" replace="New Mexic$1"/><!--exclude 'new Mexican(s)' and self match-->
<Typo word="New Netherland" find="\bNew\s*[Nn]etherlands\b" replace="New Netherland"/>
<Typo word="New York" find="\bnew\s*[Yy]ork(ers?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="New York$1"/><!--Not domains and URLs-->
<Typo word="North Carolina/Dakota" find="\bnorth\s*([Cc]arolin|[Dd]akot)a(n?s?)\b" replace="North $1a$2"/>
<Typo word="Ohio" find="\bohio(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Ohio$1"/>
<Typo word="Oklahoma" find="\boklahoma(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Oklahoma$1"/>
<Typo word="Oregon" find="\boregon(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Oregon$1"/>
<Typo word="Pennsylvania" find="\bpennsylvania(ns?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Pennsylvania$1"/>
<Typo word="Puerto Rico" find="\bpuerto\s+ric(o|ans?)\b" replace="Puerto Ric$1"/>
<Typo word="South Carolina/Dakota" find="\bsouth\s*([Cc]arolin|[Dd]akot)a(n?s?)\b" replace="South $1a$2"/>
<Typo word="Rhode Island" find="\b(?:Rhode\s*i|rhode\s*[Ii])sland(ers?)?\b" replace="Rhode Island$1"/>
<Typo word="Tennessee" find="\btennesse(e|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tennesse$1"/>
<Typo word="Texas" find="\btexa(s|ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Texa$1"/>
<Typo word="United States" find="\b[Uu]nited\s*states\b" replace="United States"/>
<Typo word="United States" find="\b[Uu]nite[ds][sS]tates\b" replace="United States"/>
<Typo word="Utah" find="\butah(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Utah$1"/><!--Not domains and URLs-->
<Typo word="Vermont" find="\bvermont(ers?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Vermont$1"/>
<Typo word="Virginia_" find="\b(?:Vi|vir)gini?(a|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Virgini$1"/><!--Not domains and URLs-->
<Typo word="Washington" find="\bwashington(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Washington$1"/><!--Not domains and URLs-->
<Typo word="West Virginia" find="\bwest\s*[Vv]irginia(ns?)?\b" replace="West Virginia$1"/>
<Typo word="Wyoming" find="\bwyoming\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Wyoming"/>
</source>

=====United States – Cities=====
<source lang="xml">
<Typo word="Albuquerque" find="\b([Aa])lb(er?qu?erqu?|u?quequ|uqueru?q|uequerqu|uqerqu|aquerq)e\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Albuquerque"/>
<Typo word="Chicago" find="\bchicago(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Chicago$1"/>
<Typo word="Chattanooga" find="\b[Cc]hat+[ae]no+ga(n?s?)\b(?!\.\w|-\w)(?<!Chattanooga(n?s?))(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Chattanooga$1"/><!--not in urls or domains-->
<Typo word="Cincinnati" find="\b[Cc]in+c[ai]n+at+(i|ians?|us)\b(?<!Cincinnat(i|ians?|us))(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cincinnat$1"/>
<Typo word="Cleveland" find="\bcleveland\b(?<!(\.|-)cleveland)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Cleveland"/><!--not in urls or domains-->
<Typo word="Fort Worth" find="\bForth?\s+[Ww]orth?\b(?<!Fort Worth)" replace="Fort Worth"/>
<Typo word="Las Vegas" find="\b(?:las\s*[Vv]egas|[Ll]as\s*vegas)\b" replace="Las Vegas"/>
<Typo word="Los Angeles" find="\b[Ll]os\s{0,9}[Aa]ng(el|le)[eo]?se?\b(?<!Los Angeles)(?<!\b[Dd]e\s{0,9}[Ll]os\s{0,9}[Aa]ng(el|le)[eo]?se?)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Los Angeles"/><!--avoid the common Spanish phrase "de los Angeles" through use of lookbehind-->
<Typo word="Manhattan" find="\b([Mm])anhatten\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1anhattan"/><!--"manhattan" can be lowercase; don't force to uppercase-->
<Typo word="Milwaukee" find="\b(milwau|[Mm]ilwu?a)kee\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Milwaukee"/>
<Typo word="New Orleans_" find="\b[Nn]ew\s*orleans\b" replace="New Orleans"/>
<Typo word="Phoenix," find="\b([Pp]oenix|[Pp](?:e|eo+)nix)\,\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Phoenix,"/><!--, added to avoid non place instances-->
<Typo word="Philadelphia" find="\b(?:[Pp]hil(?:i?delph|adelp|adeph)|philadelph)ia(ns?)?\b(?!'')(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Philadelphia$1"/><!--avoid match when bird name-->
<Typo word="Portland" find="\bportlan(d|ders?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Portlan$1"/>
<Typo word="Springfield" find="\bspringfield\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Springfield"/>\
<Typo word="Tallahassee" find="\b([Tt]alahas+e+|[Tt]allahasee|[Tt]allahasse)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tallahassee"/>
<Typo word="Tucson" find="\b([Tt])uscon\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="$1ucson"/>
</source>

====Epochs, ages and dynasties====
<source lang="xml">
<Typo word="Abbassid" find="\babbassid(e?s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Abbassid$1"/>
<Typo word="Bronze Age" find="\b(?:bronze\s+[Aa]|[Bb]ronze\s+a)(ges?)\b" replace="Bronze A$1"/>
<Typo word="Capet" find="\bcapet(ians?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Capet$1"/>
<Typo word="Car(ol/lov)ingian" find="\bcar(ol|lov)ingia(ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Car$1ingia$2"/>
<Typo word="Dark Ages" find="\b(?:[Dd]ark\s+a|dark\s+[Aa])(ges)\b" replace="Dark A$1"/>
<Typo word="Edwardian" find="\bedwardia(ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Edwardia$1"/>
<Typo word="Elizabeth(an)" find="\belizabeth(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Elizabeth$1"/>
<Typo word="Fatimid" find="\bfatim(ids?|ites?|ah?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Fatim$1"/>
<Typo word="Iron Age" find="\b(?:iron\s+[Aa]|[Ii]ron\s+a)(ges?)\b" replace="Iron A$1"/>
<Typo word="Merovingian" find="\bmerovingia(ns?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Merovingia$1"/>
<Typo word="Middle Ages" find="\b(?:midd?le\s+[Aa]|[Mm]idd?le\s+a)ges\b" replace="Middle Ages"/>
<Typo word="Napoleon(ic)" find="\b(napole[ao]|Napolea)n(ic)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Napoleon$2"/>
<Typo word="Norman" find="\bnorman(s?|dy)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Norman$1"/>
<Typo word="Romano(v/ff)" find="\bromano(vs?|ffs?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Romano$1"/>
<Typo word="Sassanid" find="\bsassani(de?s?|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Sassani$1"/>
<Typo word="Sel(juk/eucid)" find="\bsel(juk|euc(ids?|us))\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Sel$1"/>
<Typo word="Stuart" find="\bstuart(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Stuart$1"/>
<Typo word="Tudor" find="\btudor(s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tudor$1"/>
<Typo word="Valois" find="\bvalois\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Valois"/>
<Typo word="Victorian" find="\bvictoria(n[as]?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Victoria$1"/>
<Typo word="Windsor" find="\bwindso(rs?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Windso$1"/>
</source>

====Calendrical proper nouns====
<source lang="xml">
<!--Month name errors-->
<Typo word="(Jan/Febr)uary" find="\b(Jan|Febr)(?:aur|ura?)y\b" replace="$1uary"/> 
<Typo word="January" find="\b(?:[Jj]anur|janu|[Jj]aun|[Jj]ua?nu)ar(y|ies)\b" replace="Januar$1"/>
<Typo word="February" find="\b[Ff]eb(?:ur?[ae]|ru(?:r[ae]|e)|ry?a|raua|erua)r(y|ies)\b" replace="Februar$1"/>
<Typo word="September" find="\b[Ss]e(?:pte(?:meb|nb|rmb|mp)?|mp?temb)er(s?)\b" replace="September$1"/>
<Typo word="November" find="\b[Nn](?:ov(?:e?me|en|erm)|o[bc]em)(bers?)\b" replace="Novem$1"/>
<Typo word="December" find="\b[Dd](?:ecemem?|e[bv]em|ecen|ecerm|ecme|[ei]sem)(bers?)\b" replace="Decem$1"/>
<Typo word="April" find="\b[Aa]p(?:i?r|ria|ti)l(s?)\b" replace="April$1"/>
<!--Month name capitalisation-->
<Typo word="February" find="\b(?:fe|Fer|Fre)br?uary(s?)\b(?!\s&\sheavenly)(?<!Tommy\sfebruary)" replace="February$1"/>
<Typo disabled="March" find="\b([0123]?\d)\s+march\b" replace="$1 March"/><!--part replaced by new rule, partly false positive 'a 2/4 march written'[[Clan little]] -->
<Typo word="April" find="\bapril(s?)\b" replace="April$1"/>
<Typo disabled="May" find="\bmay\s+(\d{1,4})\b" replace="May $1"/><!--replaced by new rule-->
<Typo word="June/July" find="\bju(ne|ly)(s?)\b" replace="Ju$1$2"/>
<Typo word="August" find="\b([123]?\d)\s+august\b" replace="$1 August"/>
<Typo disabled="August" find="\baugust\s+(\d{1,4})\b" replace="August $1"/><!--replaced by new rule-->
<Typo word="September" find="\bseptember(s?)\b" replace="September$1"/>
<Typo word="October" find="\b(?:octob|[Oo]ctov|[Oo]ctorb)(ers?)\b" replace="Octob$1"/>
<Typo word="November" find="\bnovember(s?)\b" replace="November$1"/>
<Typo word="December" find="\bdecember(s?)\b" replace="December$1"/>
<!--Day name errors-->
<Typo word="Tuesday" find="\b[Tt]eu(sdays?)\b" replace="Tue$1"/>
<Typo word="Wednesday" find="\b(?:[Ww]e(?:nd?e?sd?|dnessd|desd)|wednesd)a(ys?)\b" replace="Wednesda$1"/>
<Typo word="Thursday" find="\b[Tt]hru(sdays?)\b" replace="Thur$1"/>
<Typo word="Saturday" find="\b(?:[Ss]ate|satu)(rdays?)\b" replace="Satu$1"/>
<!--Day name capitalisation only-->
<Typo word="Sunday" find="\bsunda(ys?)\b" replace="Sunda$1"/>
<Typo word="Monday" find="\bmonda(ys?)\b" replace="Monda$1"/>
<Typo word="Friday" find="\bfrida(ys?)\b" replace="Frida$1"/>
<Typo word="T(ue/hur)sday" find="\bt(ue|hur)(sdays?)\b" replace="T$1$2"/>
<!--Special days-->
<Typo word="Michaelmas" find="\bmich[ae]*lmas+\b" replace="Michaelmas"/>
<Typo word="Easter" find="\beaster(?!\s+egg)(?<![Nn]or['’]easter)\b" replace="Easter"/>
</source>

====Miscellaneous proper nouns====
<source lang="xml">
<Typo word="Anglican" find="\banglican(s?|ism)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Anglican$1"/>
<Typo word="Baptist_" find="\bbaptist(\s+(?:[Cc]hurch|minister|preacher|college|school|university)s?|(?<=John\s{1,9}[Tt]he\s{1,9}baptist))\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Baptist$1"/><!--look around for key terms to avoid FPs-->
<Typo word="Calvinism" find="\bcalvinis([mt][a-z]*)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Calvinis$1"/>
<Typo word="Christ(mas/ian_/endom/)" find="(?!\bCristian\b)\b(?:christ|[Cc](?:hirst|hris(?=\w)|rist|hrsit))(ian(?:ity|dom|i[sz](?:e[ds]?|ing|ation)|sted)|mas(?:es|ti[md]es?|s?y|days?)?|endom)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Christ$1"/>
<Typo word="Disney(land)" find="\bdisney(land)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Disney$1"/>
<Typo word="DreamWorks" find="\b[Dd]ream(\sW|w)orks\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="DreamWorks"/>
<Typo word="Facebook" find="\b(?:face[Bb]|FaceB)ook\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Facebook"/><!--don't match "facebook.com"-->
<Typo word="Firefox" find="\bfirefox\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Firefox"/>
<Typo word="Francisco" find="\b[Ff]ran(?:sisc|[sc]ics)(o|ans?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Francisc$1"/>
<Typo word="GameSpot" find="\b[Gg]amespot\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="GameSpot"/><!--Not domains and URLs-->
<!--word="Internet" find="\binternet\b" replace="Internet"/> see talk page-->
<Typo word="iPad/iPod/iPhone" find="\b[Ii]p((?:[ao]d|hone)s?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="iP$1"/>
<Typo word="iTunes" find="\b[Ii]tunes\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="iTunes"/>
<Typo word="Lutheran" find="\b[Ll]ut(?:era|h?eria)n(s?|ism)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Lutheran$1"/>
<Typo word="Lutheran" find="\blutheran(s?|ism)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Lutheran$1"/>
<Typo word="Methodist" find="\bmethodis(m|ts?|tic)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Methodis$1"/>
<Typo word="Mormon" find="\bmormon(s?|ism)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Mormon$1"/>
<Typo word="Muhammad etc." find="\bm([ou]ham+[ae][dt])(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="M$1$2"/>  
<Typo word="Muslim/Moslem" find="\bm(usli|osle)(ms?)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="M$1$2"/>  
<Typo word="Myspace" find="\bmyspace\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Myspace"/><!--don't match "myspace.com"-->
<Typo word="NASCAR" find="\b[Nn]ascar\b(?!\s(JF|Motorsport)\b)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="NASCAR"/>
<Typo word="Pentecost" find="\b(?:pente|[Pp]enta)cost(s?|als?|alism)\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Pentecost$1"/>
<Typo word="SpongeBob" find="\b[Ss]ponge(\sB|b)ob\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="SpongeBob"/>
<Typo word="SquarePants" find="\b[Ss]quare(\sP|p)ants\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="SquarePants"/>
<Typo word="Telugu" find="\btelugu\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Telugu"/>
<Typo word="Tibet(an)" find="\btibet(ans?)?\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="Tibet$1"/>
<Typo word="TV_" find="\b[Tt]v\b(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})(?<!WE\stv)" replace="TV"/><!--Avoid match on .tv (domain name) and WE tv-->
<Typo word="YouTube" find="\b(?:Yout|you[-\s]?[Tt]|You[-\s][Tt])ube\b(?<!</?youtube)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="YouTube"/><!--don't match youtube.com, nor <youtube></youtube> tags from Wikia"-->
</source>

===Grammar===
====Articles====
<source lang="xml">
<Typo word="A …" find="\b(?<!')([Aa])n\s+([Ee]u[A-Za-z]+|Ukrain[eians]+|[Uu](nanim[a-z]+|ni(form|on|later[a-z]+|que[a-z]*|ty?|ted|vers[a-z]+)|ra[a-z]+|ser|s(?:ua|efu)l|til[a-z]+)(ly)?)(?<!Euler[a-z]{0,99})\b" replace="$1 $2"/><!--don't match Xi'an-->
<Typo word="A h-" find="\b(?<!')([Aa])n\s+(?<!(?:\]\]|⌊)an\s)h(alf|a[nr]dy?|[aio]t|e(ad|lp|avy)[a-z]*|igh[a-z]*|oax|omo?e[a-z]*|ouse|uge|uman)\b(?<!\]an\b)" replace="$1 h$2"/><!--don't match [[Europe]]an higher..., Xi'a high etc.-->
<Typo word="An h-" find="\b([Aa])\s+h(eir(ess|loom)?|our(ly)?|onest|onou?r(abl[ey]|ary)?)\b" replace="$1n h$2"/>
<Typo word="An 8th/11th/18th" find="\ba\s+(8|11|18)th([-\s])" replace="an $1th$2"/>
</source>

====Contractions====
<source lang="xml">
<Typo word="(C/Sh/W)ouldn't" find="\b([CcWw]|[Ss]h)ou(dln[’'`]?|ldnt)t\b" replace="$1ouldn't"/>
<Typo word="e.g." find="\b([Ee]\.g)(,|\s)" replace="$1.$2"/>
<Typo word="(H/Sh/W)e'(d/ll/s)" find="\b([Ss]?[HhWw]e);(d|ll|s)\b" replace="$1'$2"/>
<Typo word="(T/W)Here'(d/ll/s/ve)" find="\b(H|[TtWw]h)ere;(d|ll|s|ve)\b" replace="$1ere'$2"/>
<Typo word="I(t)'(d/m/s/ll)" find="\b([Ii]t?);([dms]|ll)\b" replace="$1'$2"/>
<Typo word="Its (after)" find="\b([Aa](?:round|[lm]ong(?:st)?|bove|t|re)|[Bb](?:eyond|[ey]|etween|elow|oth)|[Cc]elebrat(?:e[ds]?|ing)|[Dd]uring|[Ff]rom|[Ii]n(?:to)?|[Kk]eep|[Mm]ade|[Oo](?:[fn]|ver|nto)|[Tt](?:hrough(?:out)?|o)|[Uu](?:p(?:on)?|nder(?:neath)?)|[Ww]ith(?:in|out)?)\s+it[’'`]s\b" replace="$1 its"/>
<Typo word="Its (before)" find="\b([Ii])t[’'`]s\s+(apex|causes?|doors|downfall|founders?|inceptions?|origins?|own|pinnacle|policies|reasons?|zenith)\b" replace="$1ts $2"/>
<Typo word="-en't" find="\b([Aa]r|[Hh]av|[Ww]er)n[’'`;]t\b" replace="$1en't"/>
<Typo word="-n't" find="\b([Cc]a|([CcWw]|[Ss]h)ould|[DdWw]o|[Dd](id|oes)|[Hh]a(s|d|ve)|[Ww](as|ere))(?:[’'`]n|n;)t\b" replace="$1n't"/>
<Typo word="there's" find="\btheres\b" replace="there's"/><!--don't find place name Theres-->
<Typo word="They'll" find="\b([Tt])(?:yhe|ehy|hey)(?:ll|;l+)\b" replace="$1hey'll"/>
<Typo word="They'(r/v)e" find="\b([Tt])hey;?([rv])e?\b" replace="$1hey'$2e"/>
<Typo word="W(as/ere)n't" find="\b([Ww])(as|ere)[’'`]?nt\b" replace="$1$2n't"/>
<Typo word="Weren't" find="\b([Ww])er[en][’'`]?n?t\b" replace="$1eren't"/>
<Typo word="Wh(at/en/o/y)'(d/ll/re/s/ve)" find="\b([Ww])h(at|en|o|y);(d|ll|[rv]e|s)\b" replace="$1h$2'$3"/>
<Typo word="Y'all" find="\b([Yy])a[’'`]ll\b" replace="$1'all"/>
</source>

====Joined words====
<source lang="xml">
<Typo word="(Left/Right) field" find="\b(left|[Rr]ight)f(?:ie|ei)ld(ers?)?\b" replace="$1 field$2"/>
<Typo word="More/Less/etc. than_" find="\b([Mm]ore|[Ll]ess(?:er)?|[Ww]orse|(?:[Gg]reat|[Bb]ett|(?:[Yy]ou|[Ll]o)ng|[Oo]ld|(?:[Ss]m|T|t)all|[Bb]igg|[Ll]arg|[Ss](?:ho|ma)rt|[Hh]igh|[Ll]ow|[Tt]hick|[Tt]hinn|([Rr])ath)er)\s+then\s+(?!than\b)" replace="$1 than "/><!--don't match at the end of a sentence, e.g., "Life was better then."; too many false postives for "other then" -->
<Typo word="A unique" find="\b([Aa])n\s+unique(ly)?" replace="$1 unique$2"/>
<Typo word="As well" find="\baswell\b" replace="as well"/>
<Typo word="At least" find="\b([Aa])tleast\b" replace="$1t least"/>
<Typo word="Close by" find="\b([Cc])loseby\b" replace="$1lose by"/>
<Typo word="In (fact/the/some/many/any/spite/particular/between)" find="\b([Ii])n(fact|them?|some|m?any|spite|particular|between)\b" replace="$1n $2"/>
<Typo word="(Crime/Drug) lord" find="\b([Cc]rime|[Dd]rug)-?lord(s?)\b" replace="$1 lord$2"/>
<Typo word="Other hand" find="\b([Oo])therhand\b" replace="$1ther hand"/>
<Typo word="Super Bowl" find="\b[Ss]uper[Bb]owl(s?)\b" replace="Super Bowl$1"/>
</source>

====Duplicated words====
<source lang="xml">
<Typo word="it is" find="\b([Ii])t\s+it\b" replace="$1t is"/>
<Typo word="Duplicated words" find="\b(a[mns]?|and|are|b(?:ecome|[ey])|did|[dgnt]o|for|h(?:ave|im|ow)|i[fst]s?|m(or)?e|o[fr]|other|s?he|the(?:ir|[mny]|se)?|th[iu]s|[hw]as|were|wh(?:at|ere|en|ich|om?|y)|with|(?:c|sh|w)ould|made)\s+\1\b" replace="$1"/><!--don't add "in", per talk in Archive 3-->
</source>

====Preposition usage====
<source lang="xml">
<Typo word="Comprises" find="\b([Cc])omprises of\b" replace="$1omprises"/>
</source>

====Punctuation====
<source lang="xml">
<Typo word="'s" find="(\w);s\b(?<!&[#\w]{1,99};s)" replace="$1's"/><!--semicolon for apostrophe; allow &xxx; (HTML entities)-->
<Typo word="Hers/Ours\Theirs/Yours" find="\b([Hh]e|Ou|[Tt]hei|[Yy]?ou)r's\b" replace="$1rs"/>
<Typo word="e.g." find="\b([Ee])(?:g\.?|\.\s*g)([\s,:;-]|'')(?!White|veit|River)" replace="$1.g.$2"/>
</source>

====Other====
<source lang="xml">
<Typo word="Between ... and" find="\b([Bb]etween (?:[0-9,.]+|zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|(?:twen|thir|four|for|fif|six|seven|eigh|nine)(?:teen|ty)) )to\b" replace="$1and"/>
</source>

===Band names===
<source lang="xml">
<Typo word="Mötley Crüe" find="\b[Mm]otley\s+[Cc]rue\b" replace="Mötley Crüe"/>
<Typo word="AC/DC" find="\b[Aa][Cc]-[Dd][Cc]\b" replace="AC/DC"/>
<Typo word="Metallica" find="\b[Mm]ettal+ica\b" replace="Metallica"/>
</source>

===General rules===
These have to come last, so that special cases (which these might transform into an unanticipated error) get treated first.
<source lang="xml">
<Typo DISABLED="Triple letters" find="(?!\b(?:Eisschnelllauf|Killlai|(?:Pya|G|g)rrrl?|[Rr]sssf|[Oo]ooh|[A-Za-z]+([a-z])\1\1\1[a-z]*|[a-fw]+)\b)\b([A-Za-z]+)([a-gj-wyz])\3\3([a-z]+)\b" replace="$2$3$3$4"/><!--Replace triple letters within a word (except h, x, i) with double letters; don't match some exceptions, quadruple letters, hexadecimal colours like #ccc, Roman numerals iii, web www.-->
</source>

====Beginnings====
<source lang="xml">
<Typo word="Ac-" find="\b([Aa])cc+(hiev|oustic|rimon[iy]|ronym|tiv[aei]|tual|upunctur|ute)([a-z]*)\b" replace="$1c$2$3"/>
<Typo word="Acc-" find="\b([IiUu]na|A|a)c(?:|cc+)(ept[a-z]*|ess[a-z]*|ident[a-z]*|omp(?:an(ie[ds]|y)|lish[a-z]*)|ord[a-z]+|ount[a-z]*|ura[ct][a-z]+)\b" replace="$1cc$2"/>
<Typo word="(Re)Acqu-" find="\b([Rr]ea|A|a)(?:cc+|d?)qu(aint[a-z]*|ir[ei][a-z]*|isiti(ons?|ve)|its?|itt(ed|als?|ing))\b" replace="$1cqu$2"/>
<Typo word="Add-" find="\b([Nn]ona|A|a)d(?:|dd+)(ic?ti[ov][a-z]*|ress[a-z]*)\b" replace="$1dd$2"/>
<Typo word="Aff-" find="\b([Aa])f(?:|ff)((?:e|li)ct(?:|ed|ing|ion)s?|iliat[ei][a-z]*|init(?:y|ies)|irmati[a-z]+|luen(?:t(ly)?|ce))\b" replace="$1ff$2"/>
<Typo word="After-" find="\b([Aa])f(?:et|te|er)(math|noon|ward)(s?)\b" replace="$1fter$2$3"/>
<Typo word="Al-" find="\b([Aa])ll+(beit|most|ong|ready|though|together|(?<!All)ways)\b" replace="$1l$2"/><!--avoid false positive Allways-->
<Typo word="Alle-" find="\b([Aa])le(g(?:e[ds]?|ing|edly|iances?|ory|ori[a-z]*)|viat(?:e[ds]?|ing|ion|or))\b" replace="$1lle$2"/>
<Typo word="Allo-" find="\b([Aa])lo(c[au]t|morph|path|phon|trop|w)(e?[ds]?|ing|ments?|abl[ey]|ances?|ics?|ion|y|ies)\b" replace="$1llo$2$3"/>
<Typo word="Allu-" find="\b([Aa])lu([dr](e[ds]?|ing(ly)?|ments?)|s(ions?|ive(ly)?|ory))\b(?<!Alured)" replace="$1llu$2"/>
<Typo word="Am-" find="\b([Uu]na|A|a)mm+(ass[a-z]*|end[a-z]*|enit[a-z]*|ong(st)?|ount[a-z]*|us(e[ds]?|ing|ements?))\b(?<![Dd]'[Aa]mmassa)" replace="$1m$2"/>
<!--avoid false positives: [Dd]'[Aa]mmassa -->
<Typo word="Amphi-" find="\b([Aa])mp(?:ih?|h)(bi(ans?|ous(ly)?)|theat(re|er)s?)\b" replace="$1mphi$2"/>
<Typo word="Ann-" find="\b([Aa])n(ihilat[a-z]+|ounc[ei][a-z]*|ually|ua?ls?|ull(ed|ing)|ular|iversar[a-z]+)\b(?<!\b[Aa]niversario)" replace="$1nn$2"/>
<Typo word="Ap-" find="\b([Aa])pp+(art(ments?)?|titudes?)\b" replace="$1p$2"/>
<Typo word="App-" find="\b(A|a|[DdMm]isa)p(all(s?|ed|ing[a-z]*)|are(l|nt(ly)?)|aritions?|ea[lr][a-z]*|ellat[a-z]+|end[a-z]*|li[ace][adns][a-z]*|ly|oint(s?|ed|ing|ments?)|rehen[ds][a-z]*|roach[a-z]*|rov(e[ds]?|als?|ing[a-z]*))\b(?<![Aa]plicada)" replace="$1pp$2"/><!--Don't fix French word (A/a)plicada/>-->
<Typo word="Aqua-" find="\b([Aa])cqua(ri(an?|um?)s?|tics?)\b" replace="$1qua$2"/>
<Typo word="Arr-" find="\b(A|a|[Rr]ea)r(ang(e[sdr]?|ing|ements?)|iv(als?|es?|ed|ing))\b" replace="$1rr$2"/>
<Typo word="Att-" find="(?!\bAtack\b)\b(A|a|[Uu]na)t(ack(e[dr]|ing)?s?|ain(ed|ing|ment|able)?s?|orneys?|r(ac|ibu)t(ed?|ing|ion|or|ive)?s?)\b" replace="$1tt$2"/><!--Don't fix surname Atack-->
<Typo word="Ball-" find="\b([Bb])al(istic(s?|ally|ian)|oon(?!\s+Yoka)(s?|ed|ing|ist))\b" replace="$1all$2"/>
<Typo word="Biblio-" find="\b([Bb])ib(?:i?lo|li)(graph[a-z]+|th?eques?)\b" replace="$1iblio$2"/>
<Typo word="Canoni-" find="\b([Cc])annoni(cal(s?|ly)|ze[ds]?|zing|zations?|sts?)\b" replace="$1anoni$2"/>
<Typo word="Chair-" find="\b([Cc])hari(lifts?|(wo)?m[ae]n(ships?)?|persons?)\b" replace="$1hair$2"/>
<Typo word="(Dis)Colour-" find="\b([Dd]isc|C|c)olou([a-ln-qs-y][a-z]*)\b" replace="$1olour$2"/><!--Don't match Coloumb or Colouz Uv Sound-->
<Typo word="Corr-" find="\b([Cc])or(ect[a-z]*|espond[a-z]*|osi(ons?|ve[a-z]*))\b" replace="$1orr$2"/>
<Typo word="Diphth-" find="\b([Dd])ip(?:ht|th)(eria|ongs?)\b" replace="$1iphth$2"/>
<Typo word="(In)Def-" find="\b(D|d|[Ii]nd)eff(ici(en|t)[a-z]+|init[ie][a-z]*|en[cs][ie][a-z]*|end[a-z]*)\b" replace="$1ef$2"/>
<Typo word="Desp-" find="\b([Dd])isp(air[a-z]*|icabl[ey]|is(es?|ed|ing)|ite|onden[a-z]+)\b" replace="$1esp$2"/>
<Typo word="Dis-" find="\b([Dd])(?:e|is)s(agree[a-z]*|appear[a-z]*|array[a-z]*|ease[a-z]*|integrat[a-z]+|miss[a-z]*|o(?:bed|r)ien[a-z]+|order[a-z]*)\b" replace="$1is$2"/>
<Typo word="Diss-" find="\b([Dd])is(atisf[a-z]+|olution[a-z]*|olv(e[ds]?|ing)|uad[ei][a-z]*)\b" replace="$1iss$2"/> 
<Typo word="Disse-" find="\b([Dd])ise([cnr]t|mbl|minat|nsion|rtat|rv|rvic|ver)(e?[ds]?|[eo]rs?|ing|ions?)\b" replace="$1isse$2$3"/>
<Typo word="Dissi-" find="\b([Dd])isi([abe-ko-ru-z]|m[a-nq-z]|s[a-km-z]|t[a-gi-z])([a-z]+)\b" replace="$1issi$2$3"/>
<!--avoid false positives: disidentification, disillusion, Disimone, disimprove, disimpaction, Disini, disinfect, disinter, Disislava, Disith, etc.,--> 
<Typo word="Down-" find="\b([Dd])ow(falls?|load[a-z]*|stairs?|stream|town|wards?)\b" replace="$1own$2"/>
<Typo word="Eff-" find="\b(E|e|[Ii]ne)f(ect[a-z]*|icien[a-z]*|ort(s?|less[a-z]*))\b" replace="$1ff$2"/>
<Typo word="Emi-" find="\b(E|e|[Pp]ree)mmi(grat[a-z]+|nen[ct][a-z]*|ssar[iy][a-z]*)\b" replace="$1mi$2"/>
<Typo word="Emb-" find="\b([Ee])nb([a-z]+)\b(?<!\bEnb(?:an|aqom|arr?|as|ee|ekshi[a-z]{0,99}|ergs?|etsu|ilulu|ise|lend|om|oth|orne|rel|ridge|ukan|ulufushi|un)\b)(?<!Bir Enba)" replace="$1mb$2"/>
<!--avoid false positives: Enbergs?, Enban, Enbaqom, Enbar(r), Enbas, Enbee, Enbekshi..., Enbetsu, Enbilulu, Enbise, Enblend, Enbom, Enboth, Enbrel, Enbridge, Enbukan, Enbulufushi, Enbun, Bir Enba-->
<Typo word="Emm-" find="\b([Ee])nm([a-z][a-z]*)\b(?<!\bEnm(?:a|ei)|Enmakaje|Enmann?(?:sche)?|Enmass|Enmore|[Ee]nm(?:esh|atter)[a-z]*|[Ee]nmit(?:y|ies)|Enmax|Enmund|[Ee]nm[aá]scarados?|Enmao)" replace="$1mm$2"/>
<!--avoid false positives: Enma, Enmakaje, Enman, Enmann(sche), Enmass, Enmore, enmesh, enmatter, enmity, Enmax, Enmund, enmáscarado, Enmao -->
<Typo disabled="Emp-" find="\b([Ee])n(p[a-z][a-z]*)\b(?<!\b[Ee]np(?:hytot[a-z]+|i|ing|lan[a-z]+|ower|rostil|uku)\b)" replace="$1m$2"/>
<!--avoid false positives: enphytotic, enplane, enpi, Enping, Enpower, Enprostil, Enpuku-->
<Typo word="Err-" find="\b([Ee])r(ands?|atic(ally)?|oneous(ly)?|ors?)\b" replace="$1rr$2"/>
<Typo word="Exc-" find="\b([Ee])xe(ed[a-z]*|r?pt(s?|ed|ing|ional(ly)?)|llen[ct][a-z]*|lled|ssive[lynes]*)\b" replace="$1xce$2"/>
<Typo word="(Un)Fore-" find="\b([Uu]nf|F|f)or(see(n|able|ing|r?s?)|saw|(cast|doom|stall|tell|warn)(s?|ers?|ing)|(bod|clos)(es?|ing(ly)?)|(brain|castle|court|deck|face|finger|front|ground|hand|head|leg|lock|mast|name|noon|paw|quarter|runner|sail|stay|taste|word)s?|foot|feet|most|told)\b(?<!\bFor(?:see|stall)\b)" replace="$1ore$2"/><!--don't catch Forsee, Forstall, common names-->
<Typo word="Giu-" find="\b[Gg]ui(li(?:a|o|ani)|seppe)\b" replace="Giu$1"/>
<Typo word="Ill-" find="\b([Ii])l(egal[a-z]*\b(?<!\bEl Ilegal)|ness[a-z]*|ogical(ly)?|uminat(e[ds]?|ion|ing)|us(ions?|ive(ly)?|ory))\b" replace="$1ll$2"/><!--Allow El Ilegal-->
<!--avoid false positives: inboard, inborn, inbound, inbreathe, inbreed, inbuilt-->
<Typo word="Imb-" find="\b([Ii])nb(alanc[ei][a-z]*|ecil[ei][a-z]*|ed[a-z]*|ib[ei][a-z]*|ue[a-z]*)\b" replace="$1mb$2"/>
<Typo word="Imm-" find="\b([Ii])n?m(atur[ei][a-z]*|ediate[a-z]*|ense[a-z]*|inen[ct][a-z]*|un[io][a-z]+|une[a-z]*)\b" replace="$1mm$2"/>
<Typo word="Imp-" find="\b([Ii])np(artial[a-z]*|enetrab([a-z]+)|ersonat[a-z]+|ortan[a-z]+|ossib[a-z]+|rov[ei][a-z]+)" replace="$1mp$2"/>
<!--avoid false positives: inpatient, inphase, input, inmate, inmost, inmigrante-->
<Typo DISABLED="Imp-/Imm-" find="(?!\b[Ii]nmigrante\b)\b([Ii])n(p[b-gi-tv-z]|m[b-np-z])([a-z]+)\b" replace="$1m$2$3"/>
<Typo word="In-" find="\bEn(duc|flam)(e[ds]?|ing|ements?|tive(ly)?)\b" replace="In$1$2"/><!--don't match "Enduction"-->
<Typo word="in-" find="\ben(duc|flam)(es?|ed|ing|ements?|tions?|tive(ly)?)\b" replace="in$1$2"/>
<Typo word="In-" find="\bUn(ability|(?:e|su)fficien(?:t|tly|cy)|effect([a-z]+)|equalit(?:ies|y))\b" replace="In$1"/>
<Typo word="in-" find="\bun(ability|(?:e|su)fficien(?:t|tly|cy)|effect([a-z]+)|equalit(?:ies|y))\b" replace="in$1"/>
<Typo word="Inco(m/n)-" find="\b([Ii])mco(m[beimp]|n[cdfgstv])" replace="$1nco$2"/>
<Typo word="Inn-" find="\b([Ii])(?:n|nnn)(ate(ly)?|ocent[a-z]*|ocuous[a-z]*|ovat[ei][a-z]*|uendo(es)?|umer[ao][a-z]+)\b" replace="$1nn$2"/>
<Typo word="(Mis/Re/Un)Inter-" find="\b(I|i|[Mm]isi|[Rr]ei|[Uu]ni)nte(fer[a-z]+|pret[a-z]*|relat(e[ds]?|ions?)|rupt[a-z]*|ven[eit][a-z]*|view[a-z]*)\b" replace="$1nter$2"/>
<Typo word="Irr-" find="\b([Ii])(?:r|rrr)(ation[a-z]*|elevant|eplaceable|esistibl[ey]|i[gt]at[ei][a-z]*)\b" replace="$1rr$2"/>
<Typo word="(Uno/O)ff-" find="\b([Uu]no|[Oo](?!fer\b|ficial\b))f(?:|ff)(er(?:ed|ings?)|ice(?:r?|holder)s?|icia(l(?:s?|ly|dom|ism)|te[ds]?|ting))\b" replace="$1ff$2"/><!--don't match (O/o)fer, (O/o)ficial-->  
<Typo word="Op" find="\b([Oo])pp+(en(s?|ed|ings?|ly|ness)|erat[a-z]+|inion[a-z]*)\b(?<!\bOppen)" replace="$1p$2"/><!--don't match surname Oppen-->
<Typo word="Opp-" find="\b([Oo])p(onents?|ortun[a-z]+|ose[ds]?|osi[a-z]+|ress[a-z]*)\b" replace="$1pp$2"/>
<Typo word="Per-" find="\b(P|p|[Rr]ep)re(cussi(?:ons?|ve[a-z]*)|haps|missi(?:ons?|ve)|sonal[a-z]*|spectives?|vers(e|ely|ions?))\b" replace="$1er$2"/>
<Typo DISABLED="Pre-" find="\b([Pp])er?(rogative[ds]?|scri(?:ber?[ds]?|bing|pti[a-z]+)|siden[ct][a-z]*)\b" replace="$1re$2"/><!--ran slowly, modified since-->
<Typo word="Pro-" find="\b([Pp])or(babi?l|blem|[cf]ess|duc|gress|vi[ds])([a-z]*)\b" replace="$1ro$2$3"/>
<Typo word="Pseudo-" find="\b([Pp])suedo([a-z]*)\b" replace="$1seudo$2"/>
<Typo word="Quatern-" find="\b([Qq])uartern([ai][a-z]+)\b" replace="$1uatern$2"/>
<Typo word="Ree-" find="\b([Rr])e(lect(s?|ed)|nact[a-z]*|stablish[a-z]*)\b" replace="$1ee$2"/>
<Typo word="Sch-" find="\b([Ss])hc(edul[a-z]+|em[ae][a-z]*|is[mt]s?|[mn][ou][a-z]+|olar[a-z]*|ool[a-z]*)\b" replace="$1ch$2"/>
<Typo word="Sea- (no hyphen)" find="\b([Ss])ea-(board?|foods?|m[ae]n|ports?|planes?|wards?|weeds?|worth(?:y|iness))\b" replace="$1ea$2"/><!--No other sea- words should be corrected; see talk page (Wikipedia_talk:AutoWikiBrowser/Typos#Sea-)-->
<Typo word="und-/unn-/unt-/unv-" find="\bum([dntv][a-z]+)\b(?<!umtv)(?![^\s\.]*\.\w)(?<!\.[^\s\.]{0,999})" replace="un$1"/><!--[[3GPP]] is domain false positive not umtv and proper nouns by only matching lower case--> 
<Typo word="Unn-" find="\b([Uu])(?:n|nnn)(amed|avigable|ecessar(il)?y|eeded|(?:atural|otice|umber)[a-z]*)\b" replace="$1nn$2"/>
<Typo word="Wh-" find="\b([Ww])(ere(?:abouts|by)|isker(?:s|ed)|istl(?:er?s?|ed|ing))\b" replace="$1h$2"/>
<Typo word="Xiph-" find="\b([Xx])yph([io][a-z]+)\b" replace="$1iph$2"/><!--don't match Xyphus-->
</source>

====Endings====
<source lang="xml">
<Typo word="-XXX(ed/er/ing/ive)" find="\b([A-Za-z]+[aeiou])([bdfgklmnprstvz])\2{2,}(ed|[eo]rs?|i(ng|ve|on)s?)\b" replace="$1$2$2$3"/>
<Typo word="-able (1)" find="\b([IiUu]n)?([Aa]ccept|[Aa]rgu|[Cc]ap|[Cc]onfigur|[Ff]orgiv|[Hh]ospit|[Mm]istak|[Nn]ot|[Oo]ppos|[Ss]cal|[Tt]ranslat|[Uu]s|[Vv]alu|[Vv]ulner)(?:ea?|[eiu]a?)b(l[ey]|ilit(?:y|ies))\b" replace="$1$2ab$3"/>
<Typo word="-able (2)" find="\b((?:[IiUu]n)?[Dd]e)(bat|cid|fin|form|grad|[lt]ect|not|pend|plor|p?riv|sir|spi[cs])(?:ea|i)bl([ey])\b" replace="$1$2abl$3"/>
<Typo word="-able (3)" find="\b((?:[IiUu]n)?[Rr]e)(ad|ason|charge|cogni[sz]|concil|cover|cycl|deem|mark|mov|new|pai?r|pea[lt]|place|put|view|voc)(?:ea?|[eiu]a?)b(l[ey]|ility)\b" replace="$1$2ab$3"/>
<Typo word="-acious" find="\b([A-Za-z]+)acitous(?<!anthracitous)(ness(?:es)?|ly)?\b" replace="$1acious$2"/>
<Typo word="-acity" find="\b([A-Za-z]+)act?iy\b" replace="$1acity"/>
<Typo word="-ail(ed/ing)" find="\b([BbFfHhJjmNnRrSsTtw]?|[Tt]r)aill(ed|ing)\b" replace="$1ail$2"/><!--don't find surnames "(M/W)ailling"-->
<Typo word="-aking" find="\b([Mm]is|[Rr]e)?([BbFfMmRrTtWw]|[LlPp]e|[BbCcFfWw]re|[Ss](?:[hlnot]|[np]e|[ct]re))kaing(s)?\b" replace="$1$2aking$3"/>
<Typo word="-ality" find="\b([DdQq]u|[Ee]qu|[FfNn]at|[FfNn]orm|[LlRr]eg|[Ll]oc|[Rr]e|[Tt]o[nt]|[Vv]it)all+it(y|ies)\b" replace="$1alit$2"/>
<Typo word="-ally (1)" find="\b([A-Za-z]+(?:[cdglntv]i|nt|ic|io?n|er|ot|son))aly\b(?<!Finaly|qualy)" replace="$1ally"/>
<!--Don't match B(r)ialy, Castaly, Finaly, qualy--><!--see also "-ically", "-ually"-->
<Typo word="-ally (2)" find="\b([A-Za-z-]+(?:ic?|[enu]))alyl?\b(?<!(?:Ann?|Ballyhe|[Bb]r?i|Bon|Conne|Cre|De|Don|Dou|Fe|Fin|Glene|Gre|He|Kenn?e|Kan|Ke|Kilte|Kinn?s?e|McNealy|[Mm]e|Nan|Ne|Que?|Se|She|Sme|Spezi|Whe|Vit)aly|(?:[Ss]i|[Ll]in)alyl)" replace="$1ally"/><!--Don't match many proper names-->
<Typo word="-alty" find="\b([Aa]dmir|[Cc]asu|[Dd]isloy|[LlRr]oy|[Mm]ayor|[Pp]en)(?:alit|atl|lat)(y|ies)\b" replace="$1alt$2"/><!--see also "-lty"-->
<Typo word="-ament" find="\b([Ff]il|[Ll]ig|[Tt]est|[Tt]ourn)ia?ment(s?|ary)\b" replace="$1ament$2"/>
<Typo word="-anging" find="\b((?:[Pp]?[Rr]e)?[Aa]rr|(?:[Ee]x|[Ii]nter|[Ss]hort|[Uu]n)?[Cc]h|[Dd]er|R|r)an(?:gei|egi)?ng\b" replace="$1anging"/>
<Typo word="-anical" find="\b([Bb]ot|[Mm]ech|[Pp]urit|[Ss]at)annical(s?|ly)\b" replace="$1anical$2"/>
<!--"-ance" & "-ant" errors, some separated rules for convenience, grouped together here-->
<Typo word="-an(ce/t)" find="\b([Aa]dam|[Aa](?:bu|tte)nd|(?:[Dd]is|[Rr]e)?[Aa]ppear|(?:[Rr]e)?[Cc]ogni[sz]|(?:[Aa]s|[Cc]on|[Dd]is)son|[Dd]efend|[Ii]gnor|[Mm]erch|[Oo]xid|[Ss]erv|[Vv]ac)(?:en|and)(ts?|tly|ci?es?|cy)\b" replace="$1an$2"/>
<Typo word="-(t)an(ce/t)" find="\b([Aa](?:ccep|cqu(?:ain|it)|dmit)|[Bb]la|(?:[Nn]on)?[Cc]omba|[Ee]xpec|(?:[Ii]n)?[Hh](?:ab|e[rs])i|[Ii]mp[ao]r|[Mm]ili|[Pp]it|[Rr]e(?:luc|mit|pen))t[ei]n((?:c[eiy]|t(?<!\b[Rr]emittent))[a-z]*)\b" replace="$1tan$2"/><!--allow remittent-->
<Typo word="-(st)ance" find="\b([Aa]ssi|[Cc]on|[Dd]i|[Ii]n|[DdRr]esi|[Ss]ub)st[ei]n(ci?[ey][ds]?|t[a-z]*)\b(?<!\b[Dd]istention\b)" replace="$1stan$2"/>
<Typo word="-(st)ant" find="\b([Aa]ssi|[Cc]on|[Ii]ncon|[Dd]i|[Ii]n|[Rr]esi)st(?:atn|ent)(s?|ly)\b" replace="$1stant$2"/>
<Typo word="-ard(s/ian/son)" find="\b([Ee]dw|[Hh]ow|[Rr]ich)rad((son)?s?|ians?)\b" replace="$1ard$2"/>
<Typo word="-ary" find="\b([Bb]ound|[Dd]iction|[Ll]egend|[Pp]rim|[Ss](?:al|econd)|[Tt]ern)e?r(y|ies)\b" replace="$1ar$2"/>
<Typo word="-asion" find="\b([Aa]br|[Ee]v|[Ii]nv|[Oo]cc|[Pp]ersu)ation(s?|al(ly)?)\b" replace="$1asion$2"/>
<Typo word="-ately_" find="\b([A-Za-z]+[bcdgimstv])atly\b" replace="$1ately"/>
<Typo word="-athlon" find="\b([Bb]i|[Dd]ec|[Hh]ept|[Pp]ent|[Tt]ri)ath[ae]l(ons?|etes?)\b" replace="$1athl$2"/>
<Typo word="-atian" find="\b(Als|Dalm|Gal)atio(ns?)\b" replace="$1atia$2"/>
<Typo word="-atile" find="\b(V|v|[Nn]onv)(ers|ol)itile(ly|ness)?\b" replace="$1$2atile$3"/>
<Typo word="-atility" find="\b([Vv])(ers|ol)it(?:ila|i?li)t(y|ies)\b" replace="$1$2atilit$3"/>
<Typo word="-ation" find="\b([A-Za-z]+)ati?oin(s?|al(ly)?|ed|ing)\b" replace="$1ation$2"/>
<Typo word="-atious" find="\b([Ff]lirt|[Oo]stent|[Vv]ex)ac(ious[a-z]*)\b" replace="$1at$2"/>
<Typo word="-atoes" find="\b([Pp]ot|[Tt]om)atos\b" replace="$1atoes"/>
<Typo word="-berg" find="\b([Hh]eidel|[Nn]urem|[Ww][uü]rt+em|[Tt]?[Aa]nnen)bo?urg\b" replace="$1berg"/><!--don't match Gutenburg-->
<Typo word="-burg" find="\b([Gg]ettys|[Gg]othen|[Hh]a[bp]s|[Ll]ynch|[Vv]icks)b(?:e|ou)rg\b" replace="$1burg"/>
<Typo word="-bility" find="\b([A-Za-z]+)b(?:il|li)(?:li?)?t(y|ies)\b" replace="$1bilit$2"/>
<Typo word="-builder" find="\b([Bb]ody|[Hh]ome|[Ss]hip)[d\-]build(ers?|ing)\b" replace="$1build$2"/>
<Typo word="-cede (1)" find="\b([RrSs]ec|[Pp]rec|[Cc]onc|[Ii]nterc|[Aa]ntec|c|C)eed(e[ds]?|ers?|ing|ents?)\b" replace="$1ed$2"/>
<Typo word="-cede (2)" find="\b([RrSs]ec|[Pp]rec|[Cc]onc|[Ii]nterc|[Aa]ntec|c|C)eed(s?)\b" replace="$1ede$2"/>
<Typo word="-cedent" find="\b([Pp]r|[Uu]npr|[Aa]nt)ec(?:en|i)den(t(s?|ed(ly|ness)?|less|ial)|c[ey])\b" replace="$1eceden$2"/>
<Typo word="-cei(p)t" find="\b([Cc]on|[DdRr]e)cie(p?t)(s?|ed|ful|fully)\b" replace="$1cei$2$3"/>
<Typo word="-ceive" find="\b([DdRr]e|[AIMRUaeimnprsu]*[Pp]er|[IMPRUaeilmnprsu]*[Cc]on|[Tt]rans)c(?:e?ie|i?e?)v(e[ds]?|ers?|ing|ership|ables?)\b" replace="$1ceiv$2"/>
<Typo word="-ceiving" find="\b([RrDd]e|[AIMRUaeimnprsu]*[Pp]er|[IMPRUaeilmnprsu]*[Cc]on|[Tt]rans)c(?:ie|ei)ve(ing|ables?)" replace="$1ceiv$2"/>
<Typo word="-ceps" find="\b([Qq]uadr|[Tt]r)icep(ts?)?\b" replace="$1iceps"/>
<Typo word="-cidental(ly)" find="\b([Aa]c|(?:[Cc]o)?[Ii]n)c(?:ident(?:a|ial)|edenti?al?)(s?|ly)\b" replace="$1cidental$2"/>
<Typo word="-cious" find="\b([Cc]ons|[Gg]ra|[Jj]udi|[Ll]us|[Mm]ali|[Pp]re(?:|co|da)|[Ss]p[ae]|[Ss]uspi|[Vv][eo]ra|[Vv]i)(?:ci?oui|ci?oiu|ciuo|sciou)s(ly|ness)?\b" replace="$1cious$2"/>
<Typo word="-(c/l/t)ious" find="\b([A-Za-z]+[clt])ioous([a-z]*)\b" replace="$1ious$2"/>
<Typo word="-cipient" find="\b([Rr]e|[Ee]x|[Ii]n|[Pp]er)c(?:epie|ipia)n(ts?|c[ey]|tly)\b" replace="$1cipien$2"/>
<Typo word="-claim" find="\b([Aa]c|[DdRr]e|[Dd]is|[Ee]x|[Pp]ro)cliam((er)?s?|ed|ing)\b" replace="$1claim$2"/>
<Typo word="-clamation" find="\b([DdRr]e|[Ee]x|[Pp]ro)cl(?:ai|o)mat(ions?|ory)\b" replace="$1clamat$2"/>
<Typo word="-clude" find="\b([Cc]on|[Ee]x|[Ii]n|[Oo]c|[Pp]re|[Ss]e)culd(e[ds]?|ing)\b" replace="$1clud$2"/>
<Typo word="-clusion" find="\b([Cc]on|[Ee]x|[Ii]n|[Oo]c)lu(de[ds]?|ding|sions?|sive(ly)?)\b" replace="$1clu$2"/>
<Typo word="-comer" find="\b([Ii]n|[Ll]ate|[Nn]ew|[Ww]el)commer(s?)\b" replace="$1comer$2"/>
<Typo word="-courage" find="\b([Ee]n|[Dd]is)co(?:urge?|urage|rage?)(e(d|r?s?)|ing(ly)?)\b" replace="$1courag$2"/>
<Typo word="-covered" find="\b([DRUdeinrsu]*[Cc])overd\b" replace="$1overed"/>
<Typo word="-crease" find="\b([Ii]n|[Dd]e)cres(e[drs]?|ing(ly)?|able)\b" replace="$1creas$2"/>
<Typo word="-cumbent" find="\b([Ii]n|[RrDd]e)cumban(ts?|cy|cies|tly)\b" replace="$1cumben$2"/>
<Typo word="-current" find="\b([Cc]on|[Rr]eoc|[Oo]c|[Rr]e)cur(?:e|r?a)n(t(ly)?|ces?)\b" replace="$1curren$2"/>
<Typo word="-cycle" find="\b([Bb]i|[Tt]ri|[Uu]ni|[Mm]otor|[Rr]e|[Ee]pi)(?:cylc?|cicl)([aei][a-z]*)\b(?<!Tricicle|icicleta)" replace="$1cycl$2"/><!--excludes Tricicle theatre group-->
<Typo word="-dition" find="\b([Aa][du]|[Cc]on|E|e|[Ee]xpe|[DdSs]e|[Pp]er|[Rr]en?|[Tt]ra)(?:d?idtio|dit[io]|[di]tio|dt?io|dition|dititio)n(s?|al(ly)?|ed|ing|ary)\b(?<![Aa]udions?)" replace="$1dition$2"/><!--don't match Audion-->
<Typo word="-dolence" find="\b([Cc]on|[Ii]n|[Rr]e)dolan(ces?|t(ly)?)\b" replace="$1dolen$2"/>
<Typo word="-dth" find="\b([Bb]andwi|[Hh]a(?:ir|nds?)brea|[Hh]undre|[Tt]housan)th(s?)\b" replace="$1dth$2"/>
<Typo word="-ducible" find="\b([Cc]on|[DdRrSs]e|[Ii]n|(?:[Ii]r)?[Rr]e(?:pro)?|[Pp]ro)duce?ab(l[ey]|ility)\b" replace="$1ducib$2"/>
<Typo word="-ductible" find="\b([Dd]e|[Nn]onde|[Cc]on|[Ii]n)ductab(l[ey]|ility)\b" replace="$1ductib$2"/>
<Typo word="-duction" find="\b([Aa](?:[bd]|utopro)|[Cc]o(?:n|pro)|[Dd]e(?:|xtro)|[Hh]yperpro|[Kk]inopro|[Ii]n(?:|tro)|[Nn]onpre|[Oo]verpre|[Pp](?:ostpre|r[eo])|[Rr]e(?:pro|tro|intro|d?)|[Ss](?:u(?:perpro|rpro)|e)|[Uu]nderpro|[Yy]pro)du(?:ci|ct|ti)on(s)?\b" replace="$1duction$2"/>
<Typo word="-ductor" find="\b([Aa][bd]|[Cc]on|[Dd]e|[Ii]n)ducte(rs?)\b" replace="$1ducto$2"/>
<Typo word="-eable" find="\b([Uu]n|[Ii]r)?([Cc]halleng|[Kk]nowledg|[Nn]otic|[Rr]eplac)[ai]bl([ey])\b" replace="$1$2eabl$3"/>
<Typo word="-eaning" find="\b([A-Za-z]+)ea(?:nin|nni)ng\b" replace="$1eaning"/>
<Typo word="-ecession" find="\b([RrSs]|[Pp]r)ec(?:c?e|ces)sion(s?|al|ists?|ism)\b" replace="$1ecession$2"/>
<Typo word="-elie(f/ve)" find="\b([BbRr]|[DdMm]isb|[Nn]onb|[Uu]nb)eleie?(fs?|ver?[ds]?|ving|vabl[ey])\b" replace="$1elie$2"/>
<Typo word="-ely" find="\b([IiUu]n)?([Aa]ctiv|[Cc]los|[Dd]ens|[Ee]ntir|[Ff]als|[Ff]ierc|[Ii]mmens|[Ll](?:arg|at|i[kv]|on)|loos|[Nn]am|[Pp]recis|[Ss](?:ev|inc)er|[Ss]pars|[Ww]id)l+e?y\b(?<!Densley)" replace="$1$2ely"/>
<!--"-ence" & "-ent" errors, grouped here-->
<Typo word="-en(ce/t)" find="\b([Aa]ccid|[Cc]li|[Ee]xcell|[Ii]ngredi|[Ll]eni|(?:[Dd]is)?[Oo]bedi|[Ss]uperintend|[Tt]ranscend|[Vv]iol)an(c[ey]|t[a-z]*)\b(?<!Violant[ae])" replace="$1en$2"/><!--don't match the name Violante/Violanta-->
<Typo word="-ently" find="\b([Aa]ppar|[Cc]urr|[DdRr]ec|[Ss]il|[Ii]nt|[Ee]vid|[Pp]res)enlty\b" replace="$1ently"/><!--see also "-equently"-->
<Typo word="-(t)ence" find="\b((?:|[Ii]n)(?:[Aa]dver|[Cc]ompe)|[Ll]a|(?:|[Ii]m)[Pp](?:eni|o|re)|sen)tan(ts?|tly|tial|ci?es?|cy|ced)\b" replace="$1ten$2"/>
<Typo word="-(ist)ence" find="\b((?:|[Ii]n)[Cc]ons|(?:|[Cc]o|[Nn]on|[Pp]re)[Ee]x|[Ii]ns|[Ss]ubs)ist[ai]n(ci?[ey]s?|t[a-z]*)\b" replace="$1isten$2"/>
<!--end "-ence" errors-->
<Typo word="-enness" find="\b([Dd]runk|[Ee]v|[Kk]e|[Oo]p|[Ss][ou](?:dd|ll))eness\b" replace="$1enness"/>
<Typo word="-ennial" find="\b([Pp]er|(?:[Bb]i|[Tt]ri|[Ss]e(?:m|squ)i|[Qq]uadri?)(?:cent)?|[Qq]uin(?:t|qu)|[Cc]ent|[Mm]ill)e(?:nte|)nial([a-z]*)\b" replace="$1ennial$2"/>
<Typo word="-eous" find="\b([Dd]is|[Ss]ub|[Uu]n)?([Cc](?:ourt|rustac|utan)|[Gg]as|[Gg]org|[Hh]erbac|[Ii]gn|[Ii]nstantan|[Pp]roteinac|[Rr]ight|[Ss]pontan|[Vv]itr)(?:e?uo|iou)(s[a-z]*)\b" replace="$1$2eou$3"/><!--see also "-geneous"-->
<Typo word="-equently" find="\b([Cc]ons|[Ff]r|[Ii]nfr|[Ss]ubs)en?qu(?:enlt|antl|entil+|entual+)y\b" replace="$1equently"/>
<Typo word="-ereal" find="\b([Ee]th|[Ss]id|[Vv]en)eri?al(ly)?\b" replace="$1ereal$2"/>
<Typo word="-ertain" find="\b(C|c|[Ee]nt|[Uu]nc)ertia(n[a-z]*)\b" replace="$1ertai$2"/>
<Typo word="-escent" find="\b([Aa](?:cqui|dol)|[Cc]o(?:|nv)al|[Cc]r|[Ee](?:fferv|van)|[Ii](?:ncan|ri)d|[Oo]bsol)e(?:cs?e|se|sca)n(ts?|ce)\b" replace="$1escen$2"/>
<Typo word="-ese" find="\b([Cc]hin|[Dd]ioc|[Jj]a[pv]an|[Ll]eban|[Mm]alt|[Pp]ortugu|[Ss]iam)e[aes]se\b" replace="$1ese"/>
<Typo word="-esident" find="\b([Pp]?r|R|[Nn]onp?r|[Cc]op?r)(?:ei?s|si)di?en(te?s?|c[ey]|[ct]ial(?:ly)?|cies|tiary|tships?)\b" replace="$1esiden$2"/>
<Typo word="-etary" find="\b([Dd]i|[Mm]on||[Pp](?:lan|rol|ropri)|[Ss]ecr)(?:at[ae]|et[eo])r((il)?y|is[mt]s?|ies|ium?|ia[lt]?)\b(?<![Ss]ecretory|[Pp]roprietorial)" replace="$1etar$2"/>
<Typo word="-ever" find="\b([Ff]or|[Hh]ow|[Ww]her)eever\b" replace="$1ever"/>
<Typo word="-exper-" find="([Ee])pxer([a-z]+)\b" replace="$1xper$2"/> 
<Typo word="-eys" find="\b([Aa]ttorn|[Cc]himn|[Dd]onk|[Jj]ers|[Jj]ourn|[Pp]ull|[Tt]urk)(?:ie|y)s\b" replace="$1eys"/>
<Typo word="-fered" find="\b([Dd]if|[Oo]f|[Pp](?:il|rof)|[Ss]uf|[Ww]a)ferr(ed|ings?)\b" replace="$1fer$2"/>
<Typo word="-ference" find="\b([Pp]?[RrDd]e|[A-Za-z]*[Cc]on|[Dd]if|[Ii]n(?:|dif|ter)|[A-Za-z]*[Tt]rans|[Cc]ircum)f(?:era?n|r[ae]n|f?ere?r[ae]n|f?erem|erne)(ce[drs]?|cing|t(ial)?(s?|ly))\b(?<!Defrance)" replace="$1feren$2"/>
<Typo word="-fering" find="\b([A-Za-z]+fer)eing(s)?\b" replace="$1ing$2"/> 
<Typo word="-ferred" find="\b([Cc]on|[Pp]?[DdRr]e|[Ii]n|[Tt]rans)f(?:e|fer?)r(ing|e[dr]|als?)\b" replace="$1ferr$2"/>
<Typo word="-ficent" find="\b([Mm](?:ag|u)ni|[Bb]ene)f(?:ica|[ae]ce|icie)n(t(ly)?|ce)\b" replace="$1ficen$2"/>
<Typo word="-ficial" find="\b([Ss](?:acri|uper)|[Uu]nof|[Oo]f|[Aa]rti)fical(s?|ly|ity)\b" replace="$1ficial$2"/>
<Typo word="-field" find="\b([Aa]|[Aa]ir|[Bb]a(?:ck|ttle)|[Bb][lr]oo[km]|[Cc](?:an|hester|oal|orn)|[Dd]own|[Gg]a[rs]|[Hh]ome|[Ii]n|[Mm](?:a(?:ns|[ks]e)|id|ine)|[Oo]ut|[Oo]il|[Ss](?:cho||hef|now|pring)|[Uu]p)?feild([a-z]*)\b" replace="$1field$2"/><!--Don't match surname Feild-->
<Typo word="-fifth" find="\b([Tt](?:wen|hir)|[Ff](?:or|if)|[Ss](?:ix|even)|[Ee]igh|[Nn]ine)ty-([Ff])ith\b" replace="$1ty-$2ifth"/>
<Typo word="-finite" find="\b([Ii]n(?:de)?f|[Dd]ef|[Aa]ff)(?:finite?|f?in[ae]te?|f?init(?<!\bSRK Infinit)|ianite)(s?|ly|ness)\b" replace="$1inite$2"/><!--Not 'SRK Infinit'-->
<Typo word="-finit(iv)e" find="\b([Dd]e|[Ii]n|[Ii]nde)f+inat([ei][a-z]*)\b" replace="$1finit$2"/>
<Typo word="-first" find="\b([Tt](?:wen|hir)|[Ff](?:or|if)|[Ss](?:ix|even)|[Ee]igh|[Nn]ine)ty-([Ff])r?ist\b" replace="$1ty-$2irst"/>
<Typo word="-flict" find="\b([Aa]f|[Cc]on|[Ii]n)fil?ct(s?|ing(ly)?|ed)\b" replace="$1flict$2"/>
<Typo word="-fluent" find="\b([AaEe]f|[Cc]on|[Ii]n|[Ss]uper)f(?:ule|lua)n(c[ei][a-z]*|ti[a-z]+|ts?|tly)\b" replace="$1fluen$2"/>
<Typo word="T(wo/hree/en/welve/wenty/hirty/housand)fold" find="\b([Tt])(wo|hree|en|welve|wenty|hirt(?:y|een)|housand)[\s]+fold(?!-)\b" replace="$1$2fold"/><!-- Don't match "two fold-out maps" -->
<Typo word="(Four/Five/...)fold" find="\b([Ff](our|ive|orty|ift(y|een))|[Ss](ix|even)(teen|ty)?|[Ee](ight(y?|een)|leven)|[Nn]ine(teen|ty)?|[Hh]undred)[\s]+fold\b" replace="$1fold"/>
<Typo word="-form" find="\b([Cc]on|[DdRr]e|[Pp]er|[Un]ni|[Pp]lat|[Ii]n)fr?om(s?|ed|ing|ati(ons?|ve(ly)?)|ly|ances?|ity)\b" replace="$1form$2"/>
<Typo word="-fourth" find="\b([Tt](?:wen|hir)|[Ff](?:or|if)|[Ss](?:ix|even)|[Ee]igh|[Nn]ine)ty-([Ff])orth\b" replace="$1ty-$2ourth"/>
<Typo word="-friend" find="\b([Bb]oy|[Gg]irl|[Bb]e|[Uu]n)freind(s?|ed|ly)\b" replace="$1friend$2"/>
<Typo word="-ful" find="\b([Dd]is|[Uu]n)?([Bb]eauti|[Cc](?:are|heer)|[Ee]vent|[Gg]ra[ct]e|[Hh]elp|[Pp](?:eace|ower)|[Ss](?:poon|uccess)|[Uu]se|[Ww]onder)full(s?|ly|ness)\b" replace="$1$2ful$3"/>
<Typo word="-fully" find="\b([A-Za-z]+ful)y\b" replace="$1ly"/>
<Typo word="-gement" find="\b((?:A|a|[Rr]ea)rran|(?:E|e|[Dd]ise)nga|[Ee]n(?:go|la)r|[Ii](?:mp|nfr)in)gment(s?)\b" replace="$1gement$2"/>
<Typo word="-geneity" find="\b(H|(?:[Ii]n)?h)(eter|om)ogenit(y|ies)\b" replace="$1$2ogeneit$3"/>
<Typo word="-geneous" find="\b(H|(?:[Ii]n)?h)(eter|om)ogeni(ous[a-z]*)\b" replace="$1$2ogene$3"/>
<Typo word="-geni(s/z)e" find="\b([A-Za-z]+gen)ei([sz][a-z]+)\b" replace="$1i$2"/>
<Typo word="-gest" find="\b([Cc]on|[Dd]i|[Ii]n)jest(s?|ed|ing|ion|ives?)\b" replace="$1gest$2"/>
<Typo word="-goes" find="\b([Ee]mbar|[JjLl]in|[Uu]nder)gos\b" replace="$1goes"/>
<Typo word="-gogue" find="\b([Dd]em|[Ee]?m?[Mm]en|[Pp]ed|[Ss]yn)(?:agoug|ogogu?)e(s?)\b" replace="$1agogue$2"/>
<Typo word="-grade" find="\b([Dd]e|[Dd]own|[Uu]p)gradd(e[ds]?|ing)\b" replace="$1grad$2"/>
<Typo word="-(g/p)ressive" find="\b([A-Za-z]+[gp]res)i(ve[a-z]*|ons?)\b" replace="$1si$2"/>
<Typo word="-ground" find="\b([Aa]bove|[Bb](?:ack|attle|elow)|[Cc]amp|[Ff](?:air|ore)|[Pp]lay|[Uu]nder)(?:gorun|roun|grou|goun)(d[a-z]*)\b" replace="$1groun$2"/>
<Typo disabled="-handed" find="\b([Ll]ef|[Rr]igh)t\s*hande(d|rs?)\b" replace="$1t-hande$2"/><!--nothing wrong with separate words-->
<Typo word="-herent" find="\b([Aa]d|[Cc]o|[Ii]n|[Ii]nco)he(?:a?ra|are)n(t[a-z]*|c[ey])\b" replace="$1heren$2"/>
<Typo word="-hibition_" find="\b([Ee]x|[Ii]n|[Pp]ro)habiti(ons?|ve(ly)?)\b" replace="$1hibiti$2"/>
<Typo word="-ian" find="\b(As|Christ|[Cc]ivil|Egypt|Ind|[Mm]usic|[Pp]edestr)ain(s?|ism|s?ity)\b" replace="$1ian$2"/>
<Typo word="-ian(ce/t)" find="\b([Aa]lleg|[Bb]rill|[Rr]ad|Rel(?!ient\s+K)|rel|(?:V|v|[Ii]nv)ar)(?:ai|ie)n(ts?|ces?)\b" replace="$1ian$2"/><!--avoid false positive Relient K (band)-->
<Typo word="-iation" find="\b([Aa](?:bbr|ll)ev|[Aa]ssoc|[Dd]ev|[Hh]umil|[Ii]nit|[Rr]ad|[Vv]ar)ati(ons?|ve)\b" replace="$1iati$2"/>
<Typo word="-ible" find="\b([Ii][nr])?([Aa]ud|[Cc]r(?:ed|uc)|[Ee]d|[Ee]lig|[Ff]lex|[Hh]orr|[Tt]ang|[Tt]err|[Vv]inc)ab(l[ey]s?|ility)\b" replace="$1$2ib$3"/>
<Typo word="-(s)ible" find="\b([Ii][mnr])?([Aa]dmis|[Dd]efen|[Dd]ivi|[Ff]ea|mer|[Oo]sten|[Pp](?:os|lau)|[Rr]ever|[SsTt]en|[Vv]i)sab(l[ey]|ility)\b" replace="$1$2sib$3"/>
<Typo word="-(t)ible" find="\b([IiUu][mnr])?([Cc]o(?:rrup|nver|mpa)|[Pp]ercep|[Rr]esis|[Ss]ugges)tab(l[ey]|ility)\b" replace="$1$2tib$3"/>
<Typo word="-ical" find="\b([Cc](?:lin|rit)|[Ee]lectr|(?:[Gg]eo|[Pp]ho[nt]o|[Tt]ele)[Gg]raph|[Ii]dent|[Ll]og|[Mm](?:ag|etaphor)|mus|[Pp](?:oli|rac)t|[Tt]echn|[Aa]?[Tt]r?[oy]p)(?:i?c|)ial(s?|ly)\b" replace="$1ical$2"/><!--Don't match Stan Musial-->
<Typo word="-ically" find="\b([Aa]utomat|[Bb]as|[Cc](?:o[mn]|rit)|[Ee]lectr|[Ii]ron|[Mm](?:ag|us)|[Pp](?:rac|oli)t|[Ss]pecif)i(?:al|ca?)ly\b" replace="$1ically"/>
<Typo word="-ictive" find="\b([A-Za-z]+)icitve(ly|s)?\b" replace="$1ictive$2"/>
<Typo word="-iddle" find="\b([Gg]r|[FfMmRr])idle(s?|d)\b" replace="$1iddle$2"/>
<Typo word="-idential" find="\b([Pp]?r(?:es|ov)|Res|[Cc]onf)identai?l(ly|ity)?\b" replace="$1idential$2"/>
<Typo word="-iduous" find="\b([Dd]ec|[Aa]ss)idi?ous(ly)?\b" replace="$1iduous$2"/>
<Typo word="-ield" find="\b([fWwYy]|[Uu]n[fwy]|[Ww]indsh)eild(s?|y|ed|ing|ers?|able)\b" replace="$1ield$2"/>
<Typo word="-ification" find="\b([DdMm]is|[DdRr]e|)([Cc]ert|[Cc]lass|[Ee]lectr|[Ff]ort|[Ii]dent|[Mm]agn|[Mm]od|[Nn]ot|[Pp]erson|[Pp]ur|[Qq]ual|[Ss]pec|[Uu]n|[Vv]er)(?:fici?ati?|ifcati?|ificiati?|ificat)on(s)?\b" replace="$1$2ification$3"/>
<Typo word="-ify" find="\b([DdMm]is)?([Hh]orr|[Ii]dent|[Qq]ual|[Rr]at|[Ss]pec|[Tt]err|[Vv]er)(?:[ao]f|i?fi)y(ing)?\b" replace="$1$2ify$3"/>
<Typo word="-ight" find="\b([BbWw]?[Rr]|[FfSs]l?|[Kk]?[Nn])igth?(s?|ed|ing|er|l?y|life|hoods?)\b(?<!Sligting)" replace="$1ight$2"/>
<Typo word="-ilities" find="\b([A-Za-z]+il)l+ities\b" replace="$1ities"/>
<Typo word="-ily" find="\b([Uu]n)?([Aa]ngr|[Ee]as|[Hh]eav|[Ll]uck|[Mm]ight|[Pp]rimar|[Ss]atisfactor|[Ss]tead)(?:il|i?al?|)ly\b" replace="$1$2ily"/>
<Typo word="-iness" find="\b((?:[Cc]r|[HhLl])az|[HhNnTt]ast|[FfSs]unn[DdFfGgLlMmRr]ust|[HhSs]ill|[Ll]o(?:[nv]e|rd|w)l|(?:(?:T|t|[Uu]nt)rustw|W|w)orth)yness\b" replace="$1iness"/>
<Typo word="-ing" find="\b([Ee]n|[DdMm]is)?([CcDd]ar|[Cc]ontinu|[DdLl]anc|[Dd]r?iv|[Ff]eatur|[Ff]orc|[GgLl]iv|[HhRrSsWw]av|[BbCcFfMmRrTtWw]ak|[Nn]otic|[SsWw]hin|[Ss][kh]a[rtv]|[Uu]s)eing(s?)\b" replace="$1$2ing$3"/>
<Typo word="-ining" find="\b([A-Za-z]+)inig(s?|ly)\b(?<!\b(?:(?:Br|Kl|M|H|St|W)e|Nar|Kurt|Lap|[Tt])inig\b)" replace="$1ining$2"/><!--Don't match (Br/Kl/M/H/St/W)einig, (Nar/Kurt/Lap/T)inig. 'ing' typos can be false positive i.e 'paintinig'-->
<Typo word="-ionship" find="\b([Rr]elat|[Cc]hamp|[Cc]ompan)(?:ionsih?|oinshi)p(s?)\b" replace="$1ionship$2"/>
<Typo word="-ish" find="\b([A-Za-z]+?)i?sih(ing(?:ly)?|e[ds]|ers?|ly)?\b(?<![AaersT]sih|Aisih|ingsih|Tlaksih|Mirajoucsih|Sumbangsih|Yingtsih)" replace="$1ish$2"/><!--Don't match proper names with -asih -esih -rsih -ssih, e.g., Bersih, Finarsih, Kasih, Kosasih, Madrasih, Masih, Massih, Messih, Nesih, Sukaesih, Nurnaningsih, Ningsih, Ariningsih, Yulianingsih, Asih, Tsih, Aisih, Tlaksih, Mirajoucsih, Sumbangsih, Yingtsih,-->
<Typo word="-ism" find="\b([Aa]narch|[Cc]ritic|[Oo]rgan|[Pp]lagiar|[Tt]our)s?i(?:st)?m(s?)\b" replace="$1ism$2"/>
<Typo word="-istry" find="([Aa]rt|[Cc]hem|[Dd]ent|[Mm]in|[Rr]eg)ist(ies|y)\b" replace="$1istr$2"/>
<Typo word="-itch_" find="\b([DdHhPpWw]|[Ss][tw]|[Tt]w)ict?h(e[ds]|ing|(?<![Ww]ich)ers?)\b(?<!Picher)" replace="$1itch$2"/><!--don't find "swich", "wicher", "Picher"-->
<Typo word="-itely" find="\b([A-Za-z]+[lnst])itly\b" replace="$1itely"/>
<Typo word="-ition" find="\b([Aa][du]d|[Aa]mb|[Cc]o(?:al|nd)|[Dd]emol|[Ee]d|(?:[Ee]x|[Ii]n|[Pp]ro)hib|[Ii]ntu|[Ii]g?n|[Pp]os|[Tt]rad|[Tt]u)it(?:oi?|ioi)n(s?|al(ly)?|is[mt]s?)\b" replace="$1ition$2"/>
<Typo word="-itious" find="\b([Aa]mb|[Cc]ement|[Ff]ict|[Nn]utr|[Ss]ed)ic(ious[a-z]*)\b" replace="$1it$2"/>
<Typo word="-itous" find="\b([Ff]ort|[Gg]rat|[Uu]biq)ui?tious(ly|ness)?\b" replace="$1uitous$2"/>
<Typo word="-ively" find="\b([A-Za-z]+)ivly\b" replace="$1ively"/>
<Typo word="-ives" find="\b([Aa]fterl|[Ll]|(?:[Aa]le|[Ee]x-|[Hh]ouse)?[Ww])ifes\b(?<!\b(?:(?:[Hh]alf-|[Ll]ow-|[Ss]till(?:-|\s+))[Ll]|Readers W)ifes)" replace="$1ives"/><!--Exclude FPs "half-lifes", "low-lifes", "still lifes", "Readers Wifes" (also knifes and midwifes are valid as verbs)-->
<Typo word="-junction" find="\b([Cc]on|[Dd]is|[Ii]n|[Ss]ub)ju[cn]n?ti(ons?|ves?|vitis)\b" replace="$1juncti$2"/>
<Typo word="-kel" find="\b([Ss]he|[Ss]nor|[Yy]o)kle(s?|ing)\b" replace="$1kel$2"/> 
<Typo word="-keted" find="\b([Bb]lan|[Bb]rac|[JjPp]ac|[Mm]ar|[DdPpRrSs]oc)kett(ed|ing|s)\b" replace="$1ket$2"/>
<Typo word="-king" find="\b([BbCcFfMmRrTtWw]a|([BbHhLlVv]|[Ss]tr)i)keing\b" replace="$1king"/>
<Typo word="-(a/e/i/o/u)(c/n/o/r/s)king" find="\b([A-Za-z]+[aeiou][cnors])kign\b" replace="$1king"/>
<Typo word="-licate" find="\b([Ee]xp|[Ii]mp)lict(e[ds]?|ing|ions?)\b" replace="$1licat$2"/>
<Typo word="-licit (verb)" find="\b(E|e|[Ss]o)lic(?:id|t)(ors?|s?|ed|ing|ations?)\b" replace="$1licit$2"/>
<Typo word="-licit (adjective)" find="\b([IiUu]?n?[Ee]xp|[Ii]mp|[Ii]l)lic(?:id|t)(ly)?\b" replace="$1licit$2"/>
<Typo word="-lingual" find="\b(B|b|[Tt]r|[Uu]n|[Mm]ult)illingual([a-z]*)\b" replace="$1ilingual$2"/>
<Typo word="-lithic" find="\b([Mm]ega|[Mm]ono|[Nn]?[Ee]o|]Pp]ala?eo)litic\b" replace="$1lithic"/>
<Typo word="-lled" find="\b([Ii]nsta|[BbCcFfKkMmWw][ai])leld\b" replace="$1lled"/>
<Typo word="-logue" find="\b([Mm]ono|[Dd]ia|[Ee]c|[Ee]pi|[Aa]na|[Pp]ro|[Ii]de[ao]|[Cc]ata)lou?g(e(?:[ds]?|rs?))\b(?<![Cc]ataloge(?:[ds]|rs?))(?<![Ee]piloges?)" replace="$1logu$2"/><!--don't convert cataloged, cataloges, cataloger, epiloge(s)-->
<Typo word="-lty" find="\b([Cc]rue|[Dd]ifficu|[Ff]ac?u|[Gg]ui|[Nn]ove|[Ss]pecia|[Ss]ubt[ei])tl(y|ier|iest?|iness)\b" replace="$1lt$2"/><!--see also "-alty"-->
<Typo word="-lytic" find="\b((?:[Pp]sycho)?[Aa]na|(?:[Aa]uto)?[Cc]ata|[Ee]lectro)litic(s?|al(ly)?)\b" replace="$1lytic$2"/>
<Typo word="-men's" find="\b([Cc]hair|[Ff]ore|[Gg]entle|[Ww]o)men(?:s['′’]s?['′’]?|;?s['′’]?)\b(?:['′’](?!'))?" replace="$1men's"/>
<Typo word="-ment" find="\b([A-Za-z]*(?:[Aa](?:gree|rma|rrange)|[Dd]ocu|[Pp]ay)|[Aa](?:mend|rgu)|[Ee](?:nviron|xperi)|[Ii]mprove|[Ss](?:eg|tate))m(?:a?n|etn|emt|net)(s?|ed|a[lr][a-z]*)\b(?<!Segman)" replace="$1ment$2"/><!--do not match surname Segman-->
<Typo word="-mentaries" find="\b([Cc]om|[Dd]ocu)mentare?ys\b" replace="$1mentaries"/>
<Typo word="-mentary" find="\b([Aa]li|[Cc]om(?:pl[ei])?|[Dd]ocu|[Ee]le|[Ff]rag|[Mm]o|[Pp]arlia|[Rr]udi|[Ss]edi|[Ss]upple)men(?:atr|te?r|ta)(y|ies|ily|ians?)\b" replace="$1mentar$2"/>
<Typo word="-mina(nt/te)" find="\b([Cc]onta|[Dd]eter|[DdNn]o|[GgSs]e|[Pp]redo|[LlRr]u)min(?:e|ia)(nt(ly)?|nces?|te[ds]?|ting|tions?|tors?)\b" replace="$1mina$2"/>
<Typo word="-minent" find="\b(E|e|[Ii]m|[Pp]ro|[Pp]ree)m(?:ina|mine)n(ces?|cy|t(ly)?)\b" replace="$1minen$2"/>
<Typo word="-missible" find="\b([Aa]d|[Pp]er|[Tt]rans)mis+ab(le|ility)\b" replace="$1missib$2"/>
<Typo word="-mitted" find="\b([Pp]er|[Rr]e|[EeOo]|(?:[Rr]e)?(?:[Aa]d|[Cc]om|[Ss]ub|[Tt]rans))mit(ed|edly|ing)\b" replace="$1mitt$2"/>
<Typo word="-mity" find="\b([Cc]ala|[De]efor|[Ii]nfir|[Pp]roxi)mat(y|ies)\b" replace="$1mit$2"/>
<Typo word="-nace" find="\b([Mm]e|[Ff]ur)nanc(e[ds]?|ing)\b" replace="$1nac$2"/>
<Typo word="-nally" find="\b([A-Za-z]+[a-mo-z])(?:nalyl|anlly)\b" replace="$1nally"/><!--avoid incorrect to incorrect change on -nanlly-->
<Typo word="-nance" find="\b([Ii]ndig|[Mm]a(?:lig|inte)|[Pp](?:e|oig|reg)|[Rr]e(?:pug|so)|[Ss]usti)nen(cy|ci?es?|t[a-z]*)\b" replace="$1nan$2"/><!--see also "-mina(nt/te)"-->
<Typo word="-nf(i/o)rm" find="\b([Cc]o|I|i|[DdMm]isi|[IiUu]nco|[Rr]eco)mf([io])rm(s?|ed|ing|ati(ons?|ve(ly)?)|abl[ey]|al(ity)?)\b" replace="$1nf$2rm$3"/>
<Typo word="-nment" find="\b([Aa](?:l|ss)ig|[Ee]n(?:tertai|viro)|[Gg]over)(?:nem|me)nt(s?|al[a-z]*)\b" replace="$1nment$2"/><!--see also "-ment"-->
<Typo word="-nomial" find="\b([Mm]o|[Pp]oly|[Tt]ri)nomina(ls?)\b" replace="$1nomia$2"/><!--Don't match binominal-->
<Typo word="-nounce" find="\b([Aa]n|[DdRr]e|[Pp]ro|[Mm]ispro)(?:nou|nuo?n|oun)cn?(e[a-z]*|ings?)\b" replace="$1nounc$2"/>
<Typo word="-oid" find="\b([Aa]n[de]r|[AaOo]v|[Cc]ub|[Dd]ev|[Hh]uman|[Pp]aran|[Ss]ter|[Tt](?:abl|ac|or|yph))iod(s?|ed|ing|ance|al)\b" replace="$1oid$2"/>
<Typo word="-ology" find="\b([A-Za-z]+)ol(?:[ai]?|ol)g(y(?<![Vv]olgy\b)|ic[a-z]*|ies|ists?)\b" replace="$1olog$2"/>
<Typo word="-ong" find="\b([Aa][lm]|[GgLlSsTt]|[Ww]r)omg(s?)\b" replace="$1ong$2"/>
<Typo word="-onym" find="\b([Aa]cr|[Aa]n|[Ee]p|[Hh]om|[Pp]seud|[Ss]yn)(?:yn[oy]m|on[aio]m|onym?n)(s?|ous|ously|ity|y)\b" replace="$1onym$2"/>
<Typo word="-ormally" find="\b([FfNn]|[Ii]nf|[Aa]bn)ormaly\b" replace="$1ormally"/>
<Typo word="-orous" find="\b([Aa]m|[Pp]|[Rr]anc|[RrVv]ig)o(?:urou|u?ro)s(ly|ness|\b(?<!Poros))\b" replace="$1orous$2"/><!--allowing humourous per talk page, see also "-vorous"-->
<Typo word="-osion" find="\b([Cc]orr|[Ee]r|[Ee]xpl|[Ii]mpl)otion(s?)\b" replace="$1osion$2"/>
<Typo word="-otten" find="\b(g|r|[Ff]org|[Bb]eg|[Mm]isg)ot(?:|tt)en(er|est|stones?)?\b" replace="$1otten$2"/>
<Typo word="-oughly" find="\b([RrTt]|[Tt]hor)ougly\b" replace="$1oughly"/>
<Typo word="-ought" find="\b([BbfSs]|[BbWw]r|[Tt]h)(?:aught|ougth)(s?)\b" replace="$1ought$2"/><!--Faught is a surname-->
<Typo word="-ound-" find="([bcfghmprswzCDFGKMPRSTVWYZ])uond([a-z]{0,})" replace="$1ound$2"/>
<Typo word="-paration" find="\b([Pp]r|[RrSs])ep(?:e?r?a|ar)t(ions?|or[ys]?|orily|ive(s?|ly))\b" replace="$1eparat$2"/>
<Typo word="-partment" find="\b(A|a|[Dd]e|[Cc]om)pa[rt]ment(s?|al[a-z]*)\b" replace="$1partment$2"/>
<Typo word="-pel" find="\b([Cc]om|[Dd]is|[Ee]x|[Ii]m|[Pp]ro|[Rr]e)pell(s?)\b" replace="$1pel$2"/>
<Typo word="-pelled" find="\b([Cc]om|[Dd]is|[Ee]x|[Ii]m|[Pp]ro|[Rr]e)pel(ed|ing|[eo]rs?)\b" replace="$1pell$2"/>
<Typo word="-pensable" find="\b([Ii]ndis|[Dd]is|[Cc]om)pensib(l[ey]|ility|leness)\b" replace="$1pensab$2"/>
<Typo word="-pensation" find="\b([Cc]om|[Dd]is)pensantio(ns?|nal)\b" replace="$1pensatio$2"/>
<Typo word="-pense" find="\b([Ii]n)?([Dd]is|[Ee]x|[Ss]us)penc(e[ds]?|ing|ive(?:ly|ness)?|ers?|ful|abl[ey]|ations?|ary|aries)\b" replace="$1$2pens$3"/>
<Typo word="-petiti(on/ve)" find="\b([Nn]on|[Uu]n)?([Cc]om|[Rr]e)p(?:[ie]tit|ei?ti|pet[ae]ti|atiti)(ons?|ve[a-z]*)\b" replace="$1$2petiti$3"/>
<Typo word="-phone" find="\b([Mm](?:ega|icro|ono)|[Ss](?:axo|tereo|ym)|[Tt]ele)pon(e[ds]?|ing|y|ic(ally)?)\b" replace="$1phon$2"/>
<Typo word="-ployment" find="\b([Ee]m|[Uu]nem|[Rr]ede|[Dd]e)ployement(s?)\b" replace="$1ployment$2"/>
<Typo word="-politan" find="\b([Cc]osmo|[Mm]etro|[Nn]ea)polit(?:ia?|ai)n(s?|ism)\b" replace="$1politan$2"/>
<Typo word="-ponent" find="\b([Cc]om|[Dd]e|[Ex]x|[Oo]p|[Pp]ro)ponan(ts?)\b" replace="$1ponen$2"/>
<Typo word="-press" find="\b([Ii]m|(?:[Ii]n|[DdRr]e)?(?:[Cc]om|[Ee]x)|[DdRr]e|[Oo]p|[Ss]up)pres(e[ds]?|ing|ion[a-z]*|ive(ly)?)?\b" replace="$1press$2"/>
<Typo word="-pulation" find="\b([Mm]ani|[PpCc]o|[Ss]ti)puati([a-z]+)\b" replace="$1pulati$2"/>
<Typo word="-putable" find="\b([Ii]n(?:com|dis)|[Dd]is(?:re)?|[Rr]e|[Ii]m|[Cc]om)put(?:e?i|ea)b(l[ey]|ilit[a-z]+)\b" replace="$1putab$2"/>
<Typo word="-putation" find="\b([Cc]om|[RrDd]e|[AaIi]m)puation([alys]*)\b" replace="$1putation$2"/>
<Typo word="-quarter" find="\b([Hh](?:ea|in)d|[Ff]ore)qu[ar]ter(s?|ed|ing)\b" replace="$1quarter$2"/>
<Typo word="-quisition" find="\b([Aa]c|[Ii]n|[Rr]e)quis(?:tio|itoi?)n(s?)\b" replace="$1quisition$2"/>
<Typo word="-rance" find="\b([Aa]ppea|(?:[Aa]s|[Ii]n)su|[Cc]lea|[Dd]elive|[Ee]n(?:du|t)|[Ff][lr]ag|[Hh]ind|[Ii]gno|[Pp]erseve|[Rr]ememb|[Ss]eve|[Tt](?:emp|ol)e)e?rea?n([ct][a-gi-z][a-z]*)\b(?<![Ii]nsurency\b)" replace="$1ran$2"/><!--Not Insur[g]ency-->
<Typo word="-rector" find="\b([Cc]or|[Dd]i|[Cc]odi)recte(r[a-z]*)\b" replace="$1recto$2"/>
<Typo word="-rien(ce/t)" find="\b([Ii]n|[Dd]is|[Rr]e)?([Ee]xpe|[Nn]ut|O|o|[Pp]ru)r(?:ei|ia|ite)n(ce[ds]?|cing|t[a-z]*)\b" replace="$1$2rien$3"/>
<Typo word="-rious" find="\b([CcVv]a|[CcFf]u|[Dd]eli|[Hh]ila|[Ii](?:ll|nd)ust|[Ii]nju|[Ll]abou?|[Ll]uxu|[Mm]yste|[Nn]oto|[Pp]reca|[Ss]e|[Vv]icto)r(?:i?oui|i?oiu|iuo|ou|riou)s(ly|ness)?\b(?<!\b[Ss]erous\b)" replace="$1rious$2"/>
<Typo word="-roid" find="\b([Aa]n[de]|(?:As|a?s|S)te|[Cc]ent|[Ff]ib|[Mm]eteo|[Ss]phe|[Tt]hy)riod(s?|al)\b" replace="$1roid$2"/>
<Typo word="-sage" find="\b(U|u|[Dd]o)seage(s?)\b" replace="$1sage$2"/>
<Typo word="-scend" find="\b(A|a|[Dd]e|[Tt]ran|[Cc]onde)c?[cs]end(s?|ed|ing)\b" replace="$1scend$2"/>
<Typo word="-scend(a/e)nt" find="\b(A|a|[Dd]e|[Tt]ran|[Cc]onde)c?[cs]end([ae])n[td](s?)\b" replace="$1scend$2nt$3"/>
<Typo word="-science" find="\b([Cc]on|[Pp]re|[Nn]e|[Oo]mni|[Bb]io|[Gg]eo|[Nn]euro|[Pp]seudo)[cs]ien(ces?|t(ious)?(ly)?|tific(ally)?)\b" replace="$1scien$2"/>
<Typo word="-scribe" find="\b([Dd]e|[Ii]n|[Pp]r[eo]|[Ss]ub)sri([bp][a-z]+)\b" replace="$1scri$2"/>
<Typo word="-scripti(on\ve)" find="\b([Cc]ircum|[Cc]on|[DdRr]e|[Ii]n|[Pp]r[eo]|[Ss]ub|[Tt]ran)scr?ip?(?:t|iti?)(ons?|ve(ly)?)\b" replace="$1scripti$2"/>
<Typo word="-sequence" find="\b([A-Za-z]*s|S)equesece([ds])?\b" replace="$1equence$2"/>
<Typo word="-sequent" find="\b([Cc]on|[Ii]ncon|[Ss]ub)(?:si?qu|equ|senqu|seq)en(ces?|t[a-z]*)\b" replace="$1sequen$2"/>
<Typo word="-solutely" find="\b([A-Za-z]+)solutly\b" replace="$1solutely"/>
<Typo word="-soning" find="\b([A-Za-z]+son)inig\b" replace="$1ing"/>
<Typo word="-source" find="\b([Rr]e|[Oo]ut)(?:ssour|so[ru])c(e[ds]?|ing|eful(ly|ness)?)\b(?<![Rr]essources?)" replace="$1sourc$2"/><!--not the French word '(R/r)essource(s)' used in name i.e. [[Euro Ressources]]-->
<Typo word="-sphere" find="\b([Aa]tmo|[Bb]logo|[Hh]emi|[Ss]trato)-?s(?:h?pere|phe+r)(s)?\b" replace="$1sphere$2"/>
<Typo word="-stitute" find="\b([Cc]on|[DdRr]e(?:con)|[Ii]n|[Pp]ro|[Ss]ub)s(?:i?tut|titu[dr]?|tutit|tutut)(es?|ed|ing|ion[a-z]*)\b" replace="$1stitut$2"/>
<Typo word="-strict" find="\b([Cc]on|[Rr]e(?:|di))stict(s?|ed|ing|ions?|ive)\b" replace="$1strict$2"/>
<Typo word="-struct" find="\b((?:[RrDd]e|[Mm]is)?[Cc]on|(?:[Ii]n|[Nn]on)?[DdRr]e|[Ii]n(?:fra)?|[Mm][ai]cro|[Oo]b|[Ss]u(?:b|per))(?:stuct|[st]ruct|sttruct|sruct|struc)(s?|ed|ing|ionis[tm]s?|ions?|ures?|ors?|ivis[tm]s?|(ive|ural)(?:ly)?)\b" replace="$1struct$2"/><!--Error 'Instruction(s) => Instructtions' but maybe a hidden control character-->
<Typo word="-surrect" find="\b([Rr]e|[Ii]n)s(?:sur+e|ure|ur+u)ct(s?|ed|ing|ion[a-z]*)\b" replace="$1surrect$2"/>
<Typo word="-tally" find="\b([A-Za-z]+[b-eghj-z])talyl?\b" replace="$1tally"/><!--Don't match names Naftaly, Nataly-->
<Typo word="-teenth" find="\b([Tt]hir|[Ff]our|[Ff]if|[Ss]ix|[Ss]even|[Ee]igh|[Nn]ine)t(?:e[en]|the+n)th?(s?)\b" replace="$1teenth$2"/>
<Typo word="-thèque" find="\b([Bb]ibli|[Dd]isc)oth?[eéê]que(s?)\b" replace="$1othèque$2"/>
<Typo word="-thing" find="\b([Aa]ny|[Ee]very|[Ss]ome|[Nn]o)t(?:hign|ing)\b(?<![Nn]oting)" replace="$1thing"/>
<Typo word="-tience" find="\b([Ii][mn]|[Oo]ut)?([Pp]a|[Qq]uo|[Ss]en)t(?:ia|ei)n(ces?|t[a-z]*)\b" replace="$1$2tien$3"/>
<Typo word="-tified" find="\b([Bb]eau?|[Cc]er|[FfMm]or|[Ii]den|[Jj]us|[Nn]o|[Qq]uan|[Rr]a|[Rr]ec|[Tt]es)ta?fi(e[ds]|abl[ey]|cat(e|ion)s?)\b" replace="$1tifi$2"/><!--see also "-tifie(d/s)"-->
<Typo word="-tifie(d/s)" find="\b([Rr]e|[Uu]n|)([Bb]eau?|[Cc]er|[FfMm]or|[Ii]den|[Jj]us|[Nn]o|[Qq]uan|[Rr]a|[Rr]ec|[Tt]es)tife([ds])\b" replace="$1$2tifie$3"/><!--see also "-tified"-->
<Typo word="-tility" find="\b([Ii]n)?([Dd]uc|[Ff](?:er|u)|[Hh]os|[Mm]o|[Uu]|[Vv](?:ersa|ola))t(?:ila|il?|illi)t(y|ies|arian)\b" replace="$1$2tilit$3"/>
<Typo word="-timately" find="\b([Ii]n|[Uu]l)(?:i?ti?mate?le|(i|t|iti)mate?le?)y\b" replace="$1timately"/>
<Typo word="-tinct" find="\b([Ii]n(?:dis)?|[Dd]is|[Ee]x)(?:ctinc|ti[cn]|ticnt)(s?|(ive)?(ly)?|ions?)\b(?<!\bDistin)" replace="$1tinct$2"/>
<Typo word="-tion(s)" find="\b([A-Za-z]+)tio(?:i|(s))n\b" replace="$1tion$2"/>
<Typo word="-tion" find="\b([DdNn]omina|(?:[Ee]n|[Dd]e)crypt|[Ss]?[Ee]lec|[Ee]mo|[Ss]ec)t(?:oi?|iio)n(s?|al[a-z]*)\b" replace="$1tion$2"/>
<Typo word="-tional(ly)" find="\b([A-Za-z]+tion)nal(ly)?\b" replace="$1al$2"/>
<Typo word="-tionally" find="\b([A-Za-z]+tion)aly\b" replace="$1ally"/>
<Typo word="-tionary" find="\b([DdP]ic|[Rr]?[Ee]volu|[Ee]xpedi|[Ii]nfla|[Rr]eac)tionay\b" replace="$1tionary"/>
<Typo word="-tious" find="\b([Aa]mbi|[Cc]a[pu]|[Ff][ai]cti|[Ii]nfec|[Nn]utri|[Rr]epeti)t(?:i?oui|oiu|iuo)s(ly|ness)?\b" replace="$1tious$2"/>
<Typo word="-tivities" find="\b([Aa]c|[Ff]es|[Nn]a|[Rr]eac|(?:[Ii]n)?[Ss]ensi)tivit?es\b" replace="$1tivities"/>
<Typo word="-tor" find="\b([Aa]nces|[Cc]onspira|[Ee]di|[Ii]nven|[Mm]oni|[Rr]eac|[Tt]ransla)t+er(s?|ed|ing|i?al[a-z]*)\b" replace="$1tor$2"/>
<Typo word="-trate" find="\b([Cc]oncen|[Ii]nfil)tar?t(e[ds]?|ing|ions?|ors?)\b" replace="$1trat$2"/>
<Typo word="-(s)trate" find="\b([Aa]dmini|[DdRr]emon|[Ff]ru|[Ii]llu|[Mm]agi|[Oo]rche)star?t(es?|ed|ing|ions?|ive(s?|ly)|ors?)\b" replace="$1strat$2"/>
<Typo word="-tributor" find="\b([Cc]on|[Dd]is|[Aa]t)tribute(rs?)\b" replace="$1tributo$2"/>
<Typo word="-tting" find="\b([BbGgJjLlPpSsVvWw]e|[BbCcGgPpRr]u|[Ff]orge)ting\b(?<!Guting)" replace="$1tting"/>
<Typo word="-tude" find="\b([Aa][lpt]t|[Ff]ort|[Gg]rat|[Ll]at|[Ll]ong|[Mm]agn|[Mm]ult|[Ss]ol)i(?:tut|dud)(es?|inal(ly)?)\b" replace="$1itud$2"/>
<Typo word="-ture" find="\b([Cc]ap|[Ff]ea|[Ll]ec|[Pp]ic|[Ss]culp|[Tt]or)tur(s?)\b" replace="$1ture$2"/><!--don't find surname "Pastur"-->
<Typo word="-ually" find="\b([FfTt][Aa]ct|[Cc]as|[Ee](q|vent)|[Gg]rad|[Mm](an|ut)|[Aa]?[Ss]ex|(?:[Uu]n)?[Uu]s|[Vv]is)(?:u[al]?|al?)ly\b" replace="$1ually"/><!--Don't match Annaly-->
<Typo word="-vel" find="\b([BbLlRr]e|[Dd]ri|[GgNnRr]a|[GgTt]r[ao]|[HhNn]o|[Mm]ar|[Ss](?:ho|hri|[nw]i))vle(s?)\b" replace="$1vel$2"/>
<Typo word="-vele(d/r)" find="\b([BbLl]e|[Dd]ri|[Rr]a|[GgTt]r[ao]|[Mm]ar|[Ss](?:ho|hri|[nw]i))va?le(d|rs?)\b" replace="$1vele$2"/>
<Typo word="-veling" find="\b([BbLlRr]e|[Dd]ri|[Rr]a|[GgTt]r[ao]|[Mm]ar|[Ss](?:ho|hri|[nw]i))vle?ing\b" replace="$1veling"/>
<Typo word="-vement" find="\b([A-Za-z]+)vment(s?|al|ed|ing)\b" replace="$1vement$2"/>
<Typo word="-venge" find="\b(A|a|[Rr]e|[Ss]ca)vang(er?s?|ed|ing)\b" replace="$1veng$2"/>
<Typo word="-versary" find="\b([Aa]nni|[Aa]d)v(?:erse|r?esa)r(y|ies|ial)\b" replace="$1versar$2"/>
<Typo word="-versity" find="\b([Aa]d|[Dd]i|[Uu]ni)veristy\b" replace="$1versity"/>
<Typo word="-view" find="\b([Ii]nter|[Oo]ver|[Pp]?[Rr]e)(?:vei|vi|ve|wie|ive)w(s?|ed|ing|ers?|able)\b" replace="$1view$2"/>
<Typo word="-vious" find="\b([Dd]e|[Ee]n|[Oo]b(?:li)?|[Pp]re)v(?:ouse?|iosu?|iou?su|u?ose?)(ly)?\b(?<!Devos)" replace="$1vious$2"/>
<Typo word="-vorous" find="\b([Cc]arn|[Hh]erb|[Ii]nsect|[Oo]mn)iv[aeiu]r(ous(?:ly)?|es?)\b" replace="$1ivor$2"/>
<Typo word="-wed/-wing" find="\b([A-Za-z]+)ww(ed|ing|s)\b" replace="$1w$2"/>
<Typo word="-where" find="\b([Aa]ny|[Ee]lse|[Ee]very|[Nn]o|[Ss]ome)h?were\b" replace="$1where"/>
</source>

===Incorrect phrases===
<source lang="xml">
<!--Do NOT extend the below rule to "based around".
Regardless of the FP rate, an incorrect change could render text nonsensical.-->
<Typo word="Based (off) of" find="\b([Bb])ased\s+(?<!-[Bb]ased)(off\s+)?of\b" replace="$1ased on"/>
<Typo word="et al." find="\bet(\.\s*al\b\.?|\s+al\b(?!\.))" replace="et al."/>
<Typo word="known as" find="\b(is|w?as|are|were|became|or|but|perhaps|been|(?:usual|wide|normal|general|common|most)ly|well|better|best|often|[Aa]lso)\s+know(?:s|ed)?\s+(as|for)\b" replace="$1 known $2"/>
<Typo word="the first time" find="\b([Tt])he\s+(very\s+)?fr?ist\s+time\b" replace="$1he $2first time"/>
<Typo word="per se" find="\bper\s+say\b" replace="per se"/>
</source>
"""
