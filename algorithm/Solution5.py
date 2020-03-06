from collections import Counter
import operator


class Solution(object):
    def __init__(self):
        self.result = []

    def findSubstring(self, s, words):
        if not s or not words: return []
        le = len(words[0])
        wordsLen = len(words)
        wordsArrayLen = wordsLen * le
        sle = len(s)
        newlen = len(words)
        for i in range(0, sle):
            if i + wordsArrayLen <= sle:
                newstr = s[i:i + wordsArrayLen]
                # 将字符串数组转换为字符串列表
                wordsList = list(words)
                otherWords = []
                for j in range(0, newlen):
                    my = newstr[le * j:le * (j + 1)]
                    otherWords.append(my)
                otherWords = Counter(otherWords)
                wordsList = Counter(wordsList)
                if operator.eq(wordsList, otherWords):
                    self.result.append(i)
        return self.result


so = Solution()

s = "barfoothefoobarman"
words = ["foo", "bar"]
ss1 = "cxksvbkmmlkwviteqccjhsedjmoyimskmeehhovubiszsodiqhtyaxdlktmuiggukldubzqdjiebyjkpqfpqdsepmqluwrqictcguslddphdyrsowjhbcnsqddmbvclzvqhsksxnhethvnyuxfxzsqpxvdasflscbzumssbbwuluijqhqngkfxhdahvhunjwpgkjylmwixssgizyyhifepigyenttyriebtcogbwftqmcpmcwvhcmsklyxgryxccyvhodiljbbxftjhrerurleejekacheehclvfviqxmnefzowdhswsxcbdmdfvilekzcrukityxyfwmcctwanvdoyptfnbtrnsthoepieoiklwmppkpegssgknmxpfoezilnocxsrfcebqtsdkwjfqppedmvkczjmnzcpwxiebofujyxuwgzpxotdcqnerzteyvwwseauvgoeglyctzrspmvrcjyuiraimwehdfbalretcfxxeppwdnniwnegeeotdsaixdikuodytbxasmwxzlfxzldfstaxmcflfpybdbzzewzylxwmidkjrprjjtgxwnideifjkeiqdjpogncrsmcjetsnnamlpwotftdranhdxytfnvwgkzroukdjmpucnjxscajcqtfptaujwtrguiwouzyhqulddiygjjkbesqyskjofawzisqdrqkjkvnodlwowgrbyhzruihzkezsyrvshhbreqhkbfaymsbmzaftkpvutwotnklutnnydxihcihqcidckkxwzssuogodszzmopmumwbogkhjukleukcufuqvcezxgylunxobvrsbbzkvlxbhiddnzuieyhbeimbxlpzghthksugdrjkznoomkzsiitpqhqquhraqkkbcgjhxstzhjpwtoocxirprjfmqwmhgyikgtrellftwupqldsinlzfwfrmdfvmgfwmyqsmdxhzuwpfbjprwowsvphzuelckjrkbjwejdgdbxkdhzwfnsaljjkdnxixizikigqrmwwnugsdhokxikirtuxjtfibgslozeilagywptbwhmvqwdjszgbsnjutchkdluooaompjooraljypusobvjohdklmuqyogoquaigqwxsjiryclpfjywsdgdpctpqzdivgqbwoapykiypvpuepswsybkcwzsxfbvntylibcglmeciuzojrnesqounppmwshjlgxtjzzumgzwcymlpbrjsfehxtttldfwlcsudrqpzpnbnapfbgovoucnnygadnzqrrkvkckkuanjaeodnfzbzdqpdypgmoydhiysnlehnrsnwjsloropxeeacwjomhuusuohhsqulihjrcuhvixsmdvpbefqnbmhwaodueafnjpellmhulbiqwzscfiqiuxgwomqsmxfvmmhyaqunrcdocvqjfirbiyzwmpoypwtdkcdksxzkacaeasnhbgjlgkhsaxqrvmufoyrjxqvztxdvpscszndfymaamqrhelnvleejxbiqyonpgpihdnpbcpbohuvmfkhtrncoqmgqatfjkpqnffqjutxenuqvhzoyosogeuwhpdqzvipaofjkbiooeejlfzjvrzbytxhidxkyfzavglghtuyzbhlgjwcawdardhcigmgonijvtpdokdnlmatvzxyvdymggqqmcyargmnbbqpnveahhudgtbdwzrehiuwmsyeykrbojqbexelgaomtrrqtiucspyfhxjijajxjcbpbfahfrvyimodwjgpyewhdfrphbmsfnhguhpzakalyoowzunzbjhgqyvxbkrgzyouidtinttnkkkjezjhjsqbslzuvqcvrrrzwkjkgdzsnldtlmdwgtxzewvcpxzgqqhncqzkvackmgexujtbcqcipxmgwlopdvcgndqjdvtpbzoxijamacvrzjxyvnnykpgxuxixucpvddumpvapxxizhhxeukcebjdvimucqjztpvheqivqfdpokosgyxkbipwsbqurcvltquzjcwzkzqyletteqffaubswtonxjasbvrkznljodkbhfunvzsxwvpsrdhqokjpfcceqnqgrckaheoegibceqwvvdljnwyuzcbrsrxlthlcobgwkhyqzwlubyfrvflwimnafknauacickeoteeucrodrvuobikjwxlckyeeyjoctusnawhcpyfhtcvukifgfskpspvrylvtfogfmqhcqpjlrgidopjwiunalltjwpccflhrdrvtgegznocdgnzohposakdwbgagtkxwbtrjzxkoomuuzvkjkadkkhjlpjtittewoxfpwpemdygftsqgttqfcbtrlmbefhbteijbapnfpwkkqcslwjramkuxyveeffzlpkopbevsahdskveigvivhesfcwlhdnstxhkblhtnpyfbwljegrzpysxaqihwxzrxibyvjriasqbobmskfsbdmydejkagmrdutdqevagpsjduvxgarhefihkrukzgcdcxguddvlsnuxjrxrrozvuhfgazqzhuejtlgyqdllsfiewhvqwunsdsydtqfanjmiwujpxuapcktysrqoleirwiwsabupngajcjyzdarflmgddwtradizletninfvwfgyohathrbsdhxjfsaivkjiqcyypdvniemylmrufspkbmthhvpcfanwclwtouhwavunjnhogwyhluqsphwxhjvjutfkpoipjecusmiaiijvcapujmrrxocshhexxnmgrraldklntxlxzarimkzkyceglkfjxtrrkucpeqfznqxmqqufbwrbaxhnhoyfiqwumakqsrsfhrtzhqekoxmouvdckchsufmghyyarqhyhbartebhenxylaavcjnwobeycdytthudiuudavkeljdwkdtopindjrdnudjqlftvznzbklgxvlthqmvfuklgcovysgodlhakwzmjnugifcpvqmbnzovdcqbwzsbkbcvydjhqdpakrphkeixdwuibmjxlbzwddtdgcmxhbxtvpafvleajyikkrkyvluaondwrptastvnivufiafsanengqldbfdrugonxjnqckfkfcrocwiflosufdxikbaejqthzgzcqeoxggnlexqqmkktpjbzkbfwtydtgcvyilxrrlewkwowgapvjruwubsozxjhzgfjrcalpejaazyizodihzedaytbveiwkpgesgphnajpziyyybihdpkfnghlkrhvhnzbwqkjquareyrcczjfqvkebtpmnyjwmkxkajvsfvljucnwbybsunyxjplwnusbgrlicgaieltynjwrhzlbmlzvamtphntngeyjnytrmorbxnufmfiasjwswrkdfdsljqwwrppfgggdtdkhktidcgxyxhdcmyqwqosjekomqxpmaatkvbpxhnyhwdljdbfuszfwjukctzovbjhwnxwwkwdgzppdswzkweihasjtuzoxjywwvsuhoynppfujdvwzaghcbsyxsoubmqzhitoyteqklmwoisqkaxmbpkyhztklllvwhjuapmnazjrhbhrbgffvqdfryrckdzgkjcmapzdqiuzldspjxugpxlgydliikouvsgyjgbzqxacasrjslphkdqiidsqniklbsjkymmpjmtlfkuxxlghowsyzkopvaawtlitzukijdtqppnoavyrsqptcgixgkvbxgxwcjglpzbeqqvrmtigjzbnfknowkrwqostybgnaktraokohuwstyibkvpihgeyxztvabkcldvosfcbbbuxzcajzptgxygwzbrzddbohzcbgheiiyhhchsdylmvlsukuljxrnnymqbsxfchgjoksiqqtcohwirqvdpmsfmevpyuxbbdmrpfzfvujldgtvypaqdsvqwsfwoczrhmiztjgqfqcjyvewmeoqwjiudnqrssizesazdhpjxrsxpytdektctbwzroslgbmmvnlzubitucqjalnevigrmeqfuiqblcnhrbilcqgyuwiukxafhgwtmoagxqhkvxtmabaetgcnfkjpjjurrtmdhnkgfttasmpuqpyjxbzcnirxsoojjcpspbbvuuxpimjydikbjjdwrxvlnlvwokqflrchlaywokussetdnybhxzsmkpkybbgosiwgiwcxgwradmfsmhzkguwsjhtlizbchziswmrcjifowkgitisbcrunanakocmxbxpxjicushiotpxnxrobikoixpunrhlsgcsrlwmdfusylplkgclrmcbkrwzkfkelnyeyuqdznvyamllvnymacnmvllfqymdlkilfaognmgqysbvfbjhextbkhhdftgsfqdmrttgfbwgtzdbdnijmekwntzsoikuypiridaqfyyaybbdommasyxfsyxggjchylyiqayvzywxazcolordookgmhpvstcqgcbxdzseaqbaqfqdvhjjvtqkbhhtajmhnneqoyuopxqhehkzotjmnbyqiflkoztdmzwdaqtpqkyuriwhefvtgtjqywcowyskxonxghoytovmxrtdypwgihyjdazzytkyjzxqioqbcnnbgheeyakihitnltmlmyjwyjogxeizuxbaghfeirprcienbtyqrkmrvaasgktchwdoekuobjffsmsvftlyfxqazquiankjkpxozucddjixxdtcweddevffnznpoayypyopssuxecxbfqgdwjgaglgtmvibvibngseakyaqaxuipalllsorfwksrutpcuelminzgnriklqzlcnwwbpbxzvqvohylllztyaboskadccrgppcsfgrgbhcsrcfcngynhbbbncgqexyvpbnujeamneeegljtsjhbkkcamissiqnxrarcetpsyvyehhabqjcbtgdiovawlqtfqmhxgwrgupmdxoepxistovdeqfdcvyhmloltnczhrnkqcqgzayuquxumfzoayxolozeddfkxswnuovwowqeqqaevctxasmlgnpjrwvootdjhzhxvzdnpgrmimmifavnnkxgiuwwoahxbovwqalhgcworiwyitlxdkenfakvatsbkpzaqkhwpdnillgvfrtkexyjzigcdydnqfpgrxegcroqduliogssfqdfalhglmtbrjjjiormhgckcqsswnmcfrhgcqoochrusbfcrwpyerjjhdbgsqiyhrgmhucjdtfwwmanjpopjxasceyvugvdzbpgvtsapxwlkzbvopmxonqsrqplxkqwlgfibxjquheggfdxwqwmfoewfujegzcuhhclenbbxfjfmncifbumpbiuxtadudxekcprrquqyfwksatzbpltsvnpqovltspdwgwqysgwyehsfcsitfbmdrdthygatxfrdchcuoysshlzlfifmltpcyljxrlsprjuttwpjxkbexdsenzqysidqtopmajbrvwmoudxrpaymdqsspjtjtwbomtameefzctpwxoqmpobugtnxeiizelnqeofjskkugasdoirfyucgqpfuznudzjvfxaqrnbntdiyrqrzrmbxcsdyrsuwterzdurxjskcvscpltqchrbjlgkczgyumrtqlnnufzyduauhwklddmpotbsuhsoulkmxxbtcauhwwbdsnqysdniyoasvugrgqdfneashubftdjnsblneyvcoyumsddatjhjnidueeaxjllemyrtxmxnkszfxfhqopbbxeydladunoybopwlcubooavlfddvsfxrlxuwzxrmnrpchmpliqbwtxhyckuuptldshzrfsfukwwtiogqehoxgvyigucxppahzcygwfaibzbmnjetrttzoriwnmucewldaljxqjfrkjdxsitldmlrfvoshkwnghqhszgilnbvwhvrroeuaplhmbzulxhueabybjimwjkvqhmjvqdxireuufqgcaaiadgbmoqkzafshtbemhduahquohasjcajfimryccxejpndtrpcwlcdbwtkzltbnchxpavtevyqmltffkjbvlhwkajjocmdhvbywyrctpsidnpixzlsksrwvaflcuojprhlqbqlqivtwldtkpowjftefaphugtkxcxpdndwyyrujvpvmdsxklcpntzibusbwpqcdvybupxfmobautyegcwtxvbzpvanlspqoptkhspviswclwjtafnxcqytmaiztarjpmtygkuodstqockqjznnpmgdmqehqxqgjlgrwagbuzrkdbaocobscjxqzeyqbqynegechmddnuosyogaejuiuuzuyzmzrmovutxbfchvzvnzjuzqfwyaqxwqykrqygnsznwgpddoyrnjnpzsnysdxqvyamqysdttqpcgsfwswkbjzdemdyrcpoaraqstulomcquuwroudrgcumqzkjcbxctzvlsryhdazawxrksubayy"
words1 = ["otftdranhdxytfnvwgkzroukdj", "iflkoztdmzwdaqtpqkyuriwhef", "lbsjkymmpjmtlfkuxxlghowsyz",
          "cddjixxdtcweddevffnznpoayy", "snjutchkdluooaompjooraljyp", "fuszfwjukctzovbjhwnxwwkwdg",
          "frmdfvmgfwmyqsmdxhzuwpfbjp", "ukityxyfwmcctwanvdoyptfnbt", "mhnneqoyuopxqhehkzotjmnbyq",
          "vtgtjqywcowyskxonxghoytovm", "wouzyhqulddiygjjkbesqyskjo", "mfiasjwswrkdfdsljqwwrppfgg",
          "zruihzkezsyrvshhbreqhkbfay", "rsxpytdektctbwzroslgbmmvnl", "jdwrxvlnlvwokqflrchlaywoku",
          "xhnhoyfiqwumakqsrsfhrtzhqe", "gtbdwzrehiuwmsyeykrbojqbex", "tpcyljxrlsprjuttwpjxkbexds",
          "tsjhbkkcamissiqnxrarcetpsy", "keiqdjpogncrsmcjetsnnamlpw", "rquqyfwksatzbpltsvnpqovlts",
          "tdgcmxhbxtvpafvleajyikkrky", "qvrmtigjzbnfknowkrwqostybg", "vluaondwrptastvnivufiafsan",
          "rnsthoepieoiklwmppkpegssgk", "cyypdvniemylmrufspkbmthhvp", "ihcihqcidckkxwzssuogodszzm",
          "chrusbfcrwpyerjjhdbgsqiyhr", "wmeoqwjiudnqrssizesazdhpjx", "ommasyxfsyxggjchylyiqayvzy",
          "kwntzsoikuypiridaqfyyaybbd", "cwjomhuusuohhsqulihjrcuhvi", "wxazcolordookgmhpvstcqgcbx",
          "nusbgrlicgaieltynjwrhzlbml", "xrtdypwgihyjdazzytkyjzxqio", "xfvmmhyaqunrcdocvqjfirbiyz",
          "fuklgcovysgodlhakwzmjnugif", "hzhxvzdnpgrmimmifavnnkxgiu", "xsmdvpbefqnbmhwaodueafnjpe",
          "xfbvntylibcglmeciuzojrnesq", "cnhrbilcqgyuwiukxafhgwtmoa", "xkajvsfvljucnwbybsunyxjplw",
          "zuieyhbeimbxlpzghthksugdrj", "gbzqxacasrjslphkdqiidsqnik", "jxtrrkucpeqfznqxmqqufbwrba",
          "chziswmrcjifowkgitisbcruna", "jyzdarflmgddwtradizletninf", "pcktysrqoleirwiwsabupngajc",
          "dkenfakvatsbkpzaqkhwpdnill", "kbiooeejlfzjvrzbytxhidxkyf", "wlopdvcgndqjdvtpbzoxijamac",
          "xsoojjcpspbbvuuxpimjydikbj", "faubswtonxjasbvrkznljodkbh", "uqsphwxhjvjutfkpoipjecusmi",
          "nawhcpyfhtcvukifgfskpspvry", "xkdhzwfnsaljjkdnxixizikigq", "zxgylunxobvrsbbzkvlxbhiddn",
          "alltjwpccflhrdrvtgegznocdg", "gffvqdfryrckdzgkjcmapzdqiu", "hzedaytbveiwkpgesgphnajpzi",
          "wmpoypwtdkcdksxzkacaeasnhb", "hsdylmvlsukuljxrnnymqbsxfc", "bbbncgqexyvpbnujeamneeeglj",
          "bjhgqyvxbkrgzyouidtinttnkk", "pyuxbbdmrpfzfvujldgtvypaqd", "cfanwclwtouhwavunjnhogwyhl",
          "plkgclrmcbkrwzkfkelnyeyuqd", "ugvdzbpgvtsapxwlkzbvopmxon", "msbmzaftkpvutwotnklutnnydx",
          "pdwgwqysgwyehsfcsitfbmdrdt", "elgaomtrrqtiucspyfhxjijajx", "biqyonpgpihdnpbcpbohuvmfkh",
          "llmhulbiqwzscfiqiuxgwomqsm", "mpucnjxscajcqtfptaujwtrgui", "gdzsnldtlmdwgtxzewvcpxzgqq",
          "gdtdkhktidcgxyxhdcmyqwqosj", "zubitucqjalnevigrmeqfuiqbl", "aymdqsspjtjtwbomtameefzctp",
          "kjezjhjsqbslzuvqcvrrrzwkjk", "zavglghtuyzbhlgjwcawdardhc", "fawzisqdrqkjkvnodlwowgrbyh",
          "vrzjxyvnnykpgxuxixucpvddum", "rdutdqevagpsjduvxgarhefihk", "ydhiysnlehnrsnwjsloropxeea",
          "hgjoksiqqtcohwirqvdpmsfmev", "jyxuwgzpxotdcqnerzteyvwwse", "sozxjhzgfjrcalpejaazyizodi",
          "usobvjohdklmuqyogoquaigqwx", "tmdhnkgfttasmpuqpyjxbzcnir", "quareyrcczjfqvkebtpmnyjwmk",
          "rmwwnugsdhokxikirtuxjtfibg", "qsrqplxkqwlgfibxjquheggfdx", "rukzgcdcxguddvlsnuxjrxrroz",
          "oomuuzvkjkadkkhjlpjtittewo", "wqwmfoewfujegzcuhhclenbbxf", "yjogxeizuxbaghfeirprcienbt",
          "qbwoapykiypvpuepswsybkcwzs", "lvtfogfmqhcqpjlrgidopjwiun", "rwowsvphzuelckjrkbjwejdgdb",
          "jfqppedmvkczjmnzcpwxiebofu", "hygatxfrdchcuoysshlzlfifml", "gxqhkvxtmabaetgcnfkjpjjurr",
          "zppdswzkweihasjtuzoxjywwvs", "hgyikgtrellftwupqldsinlzfw", "kckkuanjaeodnfzbzdqpdypgmo",
          "aiijvcapujmrrxocshhexxnmgr", "sjiryclpfjywsdgdpctpqzdivg", "kuxyveeffzlpkopbevsahdskve",
          "uqvhzoyosogeuwhpdqzvipaofj", "gjhxstzhjpwtoocxirprjfmqwm", "cwiflosufdxikbaejqthzgzcqe",
          "qeqqaevctxasmlgnpjrwvootdj", "ymggqqmcyargmnbbqpnveahhud", "ekomqxpmaatkvbpxhnyhwdljdb",
          "zvamtphntngeyjnytrmorbxnuf", "uhoynppfujdvwzaghcbsyxsoub", "efhbteijbapnfpwkkqcslwjram",
          "koxmouvdckchsufmghyyarqhyh", "tthudiuudavkeljdwkdtopindj", "nwwbpbxzvqvohylllztyaboska",
          "dccrgppcsfgrgbhcsrcfcngynh", "qdpakrphkeixdwuibmjxlbzwdd", "ftgsfqdmrttgfbwgtzdbdnijme",
          "ounppmwshjlgxtjzzumgzwcyml", "cpvqmbnzovdcqbwzsbkbcvydjh", "pbrjsfehxtttldfwlcsudrqpzp",
          "qbcnnbgheeyakihitnltmlmyjw", "ztvabkcldvosfcbbbuxzcajzpt", "xfpwpemdygftsqgttqfcbtrlmb",
          "hncqzkvackmgexujtbcqcipxmg", "ilfaognmgqysbvfbjhextbkhhd", "hvqwunsdsydtqfanjmiwujpxua",
          "yqrkmrvaasgktchwdoekuobjff", "egeeotdsaixdikuodytbxasmwx", "jfmncifbumpbiuxtadudxekcpr",
          "slozeilagywptbwhmvqwdjszgb", "kkugasdoirfyucgqpfuznudzjv", "pvapxxizhhxeukcebjdvimucqj",
          "bqurcvltquzjcwzkzqyletteqf", "cbrsrxlthlcobgwkhyqzwlubyf", "mqzhitoyteqklmwoisqkaxmbpk",
          "nbnapfbgovoucnnygadnzqrrkv", "ztpvheqivqfdpokosgyxkbipws", "auvgoeglyctzrspmvrcjyuirai",
          "yhmloltnczhrnkqcqgzayuquxu", "funvzsxwvpsrdhqokjpfcceqnq", "vuhfgazqzhuejtlgyqdllsfiew",
          "gmhucjdtfwwmanjpopjxasceyv", "vpscszndfymaamqrhelnvleejx", "dzseaqbaqfqdvhjjvtqkbhhtaj",
          "zylxwmidkjrprjjtgxwnideifj", "nzohposakdwbgagtkxwbtrjzxk", "igvivhesfcwlhdnstxhkblhtnp",
          "trncoqmgqatfjkpqnffqjutxen", "vwfgyohathrbsdhxjfsaivkjiq", "rdnudjqlftvznzbklgxvlthqmv",
          "kopvaawtlitzukijdtqppnoavy", "raldklntxlxzarimkzkyceglkf", "nakocmxbxpxjicushiotpxnxro",
          "wxoqmpobugtnxeiizelnqeofjs", "smsvftlyfxqazquiankjkpxozu", "fwksrutpcuelminzgnriklqzlc",
          "nefzowdhswsxcbdmdfvilekzcr", "ibvibngseakyaqaxuipalllsor", "znvyamllvnymacnmvllfqymdlk",
          "gcvyilxrrlewkwowgapvjruwub", "mwehdfbalretcfxxeppwdnniwn", "wwoahxbovwqalhgcworiwyitlx",
          "nmxpfoezilnocxsrfcebqtsdkw", "engqldbfdrugonxjnqckfkfcro", "grckaheoegibceqwvvdljnwyuz",
          "jcbpbfahfrvyimodwjgpyewhdf", "rvflwimnafknauacickeoteeuc", "gxygwzbrzddbohzcbgheiiyhhc",
          "wcxgwradmfsmhzkguwsjhtlizb", "bikoixpunrhlsgcsrlwmdfusyl", "ssetdnybhxzsmkpkybbgosiwgi",
          "vyehhabqjcbtgdiovawlqtfqmh", "opmumwbogkhjukleukcufuqvce", "vjriasqbobmskfsbdmydejkagm",
          "gjlgkhsaxqrvmufoyrjxqvztxd", "yyybihdpkfnghlkrhvhnzbwqkj", "kznoomkzsiitpqhqquhraqkkbc",
          "yhztklllvwhjuapmnazjrhbhrb", "jjiormhgckcqsswnmcfrhgcqoo", "rphbmsfnhguhpzakalyoowzunz",
          "igmgonijvtpdokdnlmatvzxyvd", "rsqptcgixgkvbxgxwcjglpzbeq", "zldspjxugpxlgydliikouvsgyj",
          "enzqysidqtopmajbrvwmoudxrp", "naktraokohuwstyibkvpihgeyx", "zlfxzldfstaxmcflfpybdbzzew",
          "mfzoayxolozeddfkxswnuovwow", "rodrvuobikjwxlckyeeyjoctus", "yfbwljegrzpysxaqihwxzrxiby",
          "croqduliogssfqdfalhglmtbrj", "gvfrtkexyjzigcdydnqfpgrxeg", "xgwrgupmdxoepxistovdeqfdcv",
          "oxggnlexqqmkktpjbzkbfwtydt", "pyopssuxecxbfqgdwjgaglgtmv", "svqwsfwoczrhmiztjgqfqcjyve",
          "bartebhenxylaavcjnwobeycdy"]
# superStringLen = len(ss1)
# print("superStringLen--->", superStringLen)
# ret = so.findSubstring(ss1, words1)
# for i in ret:
#     print("reti :  ", i)

# class Test():
#     def __init__(self):
#         self.words = []
#
#     def transfer(self, words, otherWords):
#         if words == otherWords:
#             return True


import operator


# from collections import Counter
# t = Test()
#
# words = ["foo", "bar"]
# words= Counter(words)
# otherWords = [ "bar","foo"]
# otherWords = Counter(otherWords)
#
# print(words)
# ll = t.transfer(words,otherWords)
# if operator.eq(words,otherWords):
#     print ("right")
#
# print(ll)

#
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         from collections import Counter
#         if not s or not words:return []
#         one_word = len(words[0])
#         all_len = len(words) * one_word
#         n = len(s)
#         words = Counter(words)
#         res = []
#         for i in range(0, n - all_len + 1):
#             tmp = s[i:i+all_len]
#             c_tmp = []
#             for j in range(0, all_len, one_word):
#                 c_tmp.append(tmp[j:j+one_word])
#             if Counter(c_tmp) == words:
#                 res.append(i)
#         return res


class Solution(object):
    def search(self, nums, target):
        # 时间复杂度为log(n)则循环次数为logn
        # 数组长度为0 或者为1的情况
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        minValue = 0
        bigValue = len(nums) - 1
        if target == nums[minValue]:
            return minValue
        if target == nums[bigValue]:
            return bigValue
        i = 0
        while (minValue < bigValue):

            midValue = int((minValue + bigValue) / 2)
            if (i == 0 and target > nums[bigValue] and target < nums[midValue]):
                minValue = 0
                bigValue = midValue
            if (i == 0 and target > nums[bigValue] and target > nums[midValue]):
                bigValue = bigValue
                minValue = midValue
            if (i == 0 and target < nums[bigValue] and target < nums[midValue] and nums[midValue] > nums[bigValue]):
                bigValue = bigValue
                minValue = midValue
            if (i == 0 and target < nums[bigValue] and target < nums[midValue] and nums[midValue] < nums[bigValue]):
                bigValue = bigValue
                minValue = int((midValue + 0) / 2)
            if (i == 0 and target < nums[bigValue] and target > nums[midValue] and nums[midValue] < nums[bigValue]):
                bigValue = bigValue
                minValue = midValue
            if (i >= 0):
                if nums[midValue] < target:
                    minValue = midValue + 1
                elif nums[midValue] > target:
                    bigValue = midValue - 1
                else:
                    return midValue
            i += 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]

target = 0
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 3
nums2 = [1]
target2 = 1
nums3 = [1, 3]
target3 = 3
nums4 = [4, 5, 6, 7, 8, 1, 2, 3]
target4 = 8
so = Solution()
ret = so.search(nums4, target4)
print(ret)


