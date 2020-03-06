import time


class Solution(object):
    def __init__(self):
        self.strlist = []
        self.result = []

    def findSubstring(self, s, words):
        # result = []
        beginTime = time.time()
        if len(words) > 0:
            le = len(words[0])
        wordsLen = len(words)
        sle = len(s)
        if len(words) == 0:
            return []
        for i in range(0, sle):
            # print("第", i, "次")
            if i + wordsLen * le <= sle:
                newstr = s[i:i + wordsLen * le]
                mylist = []
                newlen = len(newstr) / le
                for j in range(0, int(newlen)):
                    my = newstr[le * j:le * (j + 1)]
                    mylist.append(my)
                # print("newstr= ", newstr)
                # print("mylsit :  ", mylist)
                # print("chang= ", i + len(words) * len(words[0]))
                for str in words:
                    # print("str-->", str)
                    if str in mylist:
                        # print("replaced str", str)
                        mylist.remove(str)
                        # newstr = newstr.replace(str, "", 1)
                    # print("myList  ", mylist)
                if len(mylist) == 0:
                    # print("appendi-->", i)
                    self.result.append(i)
                    # print("self.result:",self.result)
        endTime = time.time()
        print("used time:  ", endTime - beginTime)
        return self.result


ss = 'barfoothefoobarman'
words = ["foo", "bar"]
ss1 = "barfoofoobarthefoobarman"
words1 = ["bar", "foo", "the"]
ss2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "good"]
ss3 = "foobarfoobar"
words3 = ["foo", "bar"]
so = Solution()
ss4 = "a"
words4 = []
ss5 = "ababaab"
words5 = ["ab", "ba", "ba"]
ss6 = "cxksvbkmmlkwviteqccjhsedjmoyimskmeehhovubiszsodiqhtyaxdlktmuiggukldubzqdjiebyjkpqfpqdsepmqluwrqictcguslddphdyrsowjhbcnsqddmbvclzvqhsksxnhethvnyuxfxzsqpxvdasflscbzumssbbwuluijqhqngkfxhdahvhunjwpgkjylmwixssgizyyhifepigyenttyriebtcogbwftqmcpmcwvhcmsklyxgryxccyvhodiljbbxftjhrerurleejekacheehclvfviqxmnefzowdhswsxcbdmdfvilekzcrukityxyfwmcctwanvdoyptfnbtrnsthoepieoiklwmppkpegssgknmxpfoezilnocxsrfcebqtsdkwjfqppedmvkczjmnzcpwxiebofujyxuwgzpxotdcqnerzteyvwwseauvgoeglyctzrspmvrcjyuiraimwehdfbalretcfxxeppwdnniwnegeeotdsaixdikuodytbxasmwxzlfxzldfstaxmcflfpybdbzzewzylxwmidkjrprjjtgxwnideifjkeiqdjpogncrsmcjetsnnamlpwotftdranhdxytfnvwgkzroukdjmpucnjxscajcqtfptaujwtrguiwouzyhqulddiygjjkbesqyskjofawzisqdrqkjkvnodlwowgrbyhzruihzkezsyrvshhbreqhkbfaymsbmzaftkpvutwotnklutnnydxihcihqcidckkxwzssuogodszzmopmumwbogkhjukleukcufuqvcezxgylunxobvrsbbzkvlxbhiddnzuieyhbeimbxlpzghthksugdrjkznoomkzsiitpqhqquhraqkkbcgjhxstzhjpwtoocxirprjfmqwmhgyikgtrellftwupqldsinlzfwfrmdfvmgfwmyqsmdxhzuwpfbjprwowsvphzuelckjrkbjwejdgdbxkdhzwfnsaljjkdnxixizikigqrmwwnugsdhokxikirtuxjtfibgslozeilagywptbwhmvqwdjszgbsnjutchkdluooaompjooraljypusobvjohdklmuqyogoquaigqwxsjiryclpfjywsdgdpctpqzdivgqbwoapykiypvpuepswsybkcwzsxfbvntylibcglmeciuzojrnesqounppmwshjlgxtjzzumgzwcymlpbrjsfehxtttldfwlcsudrqpzpnbnapfbgovoucnnygadnzqrrkvkckkuanjaeodnfzbzdqpdypgmoydhiysnlehnrsnwjsloropxeeacwjomhuusuohhsqulihjrcuhvixsmdvpbefqnbmhwaodueafnjpellmhulbiqwzscfiqiuxgwomqsmxfvmmhyaqunrcdocvqjfirbiyzwmpoypwtdkcdksxzkacaeasnhbgjlgkhsaxqrvmufoyrjxqvztxdvpscszndfymaamqrhelnvleejxbiqyonpgpihdnpbcpbohuvmfkhtrncoqmgqatfjkpqnffqjutxenuqvhzoyosogeuwhpdqzvipaofjkbiooeejlfzjvrzbytxhidxkyfzavglghtuyzbhlgjwcawdardhcigmgonijvtpdokdnlmatvzxyvdymggqqmcyargmnbbqpnveahhudgtbdwzrehiuwmsyeykrbojqbexelgaomtrrqtiucspyfhxjijajxjcbpbfahfrvyimodwjgpyewhdfrphbmsfnhguhpzakalyoowzunzbjhgqyvxbkrgzyouidtinttnkkkjezjhjsqbslzuvqcvrrrzwkjkgdzsnldtlmdwgtxzewvcpxzgqqhncqzkvackmgexujtbcqcipxmgwlopdvcgndqjdvtpbzoxijamacvrzjxyvnnykpgxuxixucpvddumpvapxxizhhxeukcebjdvimucqjztpvheqivqfdpokosgyxkbipwsbqurcvltquzjcwzkzqyletteqffaubswtonxjasbvrkznljodkbhfunvzsxwvpsrdhqokjpfcceqnqgrckaheoegibceqwvvdljnwyuzcbrsrxlthlcobgwkhyqzwlubyfrvflwimnafknauacickeoteeucrodrvuobikjwxlckyeeyjoctusnawhcpyfhtcvukifgfskpspvrylvtfogfmqhcqpjlrgidopjwiunalltjwpccflhrdrvtgegznocdgnzohposakdwbgagtkxwbtrjzxkoomuuzvkjkadkkhjlpjtittewoxfpwpemdygftsqgttqfcbtrlmbefhbteijbapnfpwkkqcslwjramkuxyveeffzlpkopbevsahdskveigvivhesfcwlhdnstxhkblhtnpyfbwljegrzpysxaqihwxzrxibyvjriasqbobmskfsbdmydejkagmrdutdqevagpsjduvxgarhefihkrukzgcdcxguddvlsnuxjrxrrozvuhfgazqzhuejtlgyqdllsfiewhvqwunsdsydtqfanjmiwujpxuapcktysrqoleirwiwsabupngajcjyzdarflmgddwtradizletninfvwfgyohathrbsdhxjfsaivkjiqcyypdvniemylmrufspkbmthhvpcfanwclwtouhwavunjnhogwyhluqsphwxhjvjutfkpoipjecusmiaiijvcapujmrrxocshhexxnmgrraldklntxlxzarimkzkyceglkfjxtrrkucpeqfznqxmqqufbwrbaxhnhoyfiqwumakqsrsfhrtzhqekoxmouvdckchsufmghyyarqhyhbartebhenxylaavcjnwobeycdytthudiuudavkeljdwkdtopindjrdnudjqlftvznzbklgxvlthqmvfuklgcovysgodlhakwzmjnugifcpvqmbnzovdcqbwzsbkbcvydjhqdpakrphkeixdwuibmjxlbzwddtdgcmxhbxtvpafvleajyikkrkyvluaondwrptastvnivufiafsanengqldbfdrugonxjnqckfkfcrocwiflosufdxikbaejqthzgzcqeoxggnlexqqmkktpjbzkbfwtydtgcvyilxrrlewkwowgapvjruwubsozxjhzgfjrcalpejaazyizodihzedaytbveiwkpgesgphnajpziyyybihdpkfnghlkrhvhnzbwqkjquareyrcczjfqvkebtpmnyjwmkxkajvsfvljucnwbybsunyxjplwnusbgrlicgaieltynjwrhzlbmlzvamtphntngeyjnytrmorbxnufmfiasjwswrkdfdsljqwwrppfgggdtdkhktidcgxyxhdcmyqwqosjekomqxpmaatkvbpxhnyhwdljdbfuszfwjukctzovbjhwnxwwkwdgzppdswzkweihasjtuzoxjywwvsuhoynppfujdvwzaghcbsyxsoubmqzhitoyteqklmwoisqkaxmbpkyhztklllvwhjuapmnazjrhbhrbgffvqdfryrckdzgkjcmapzdqiuzldspjxugpxlgydliikouvsgyjgbzqxacasrjslphkdqiidsqniklbsjkymmpjmtlfkuxxlghowsyzkopvaawtlitzukijdtqppnoavyrsqptcgixgkvbxgxwcjglpzbeqqvrmtigjzbnfknowkrwqostybgnaktraokohuwstyibkvpihgeyxztvabkcldvosfcbbbuxzcajzptgxygwzbrzddbohzcbgheiiyhhchsdylmvlsukuljxrnnymqbsxfchgjoksiqqtcohwirqvdpmsfmevpyuxbbdmrpfzfvujldgtvypaqdsvqwsfwoczrhmiztjgqfqcjyvewmeoqwjiudnqrssizesazdhpjxrsxpytdektctbwzroslgbmmvnlzubitucqjalnevigrmeqfuiqblcnhrbilcqgyuwiukxafhgwtmoagxqhkvxtmabaetgcnfkjpjjurrtmdhnkgfttasmpuqpyjxbzcnirxsoojjcpspbbvuuxpimjydikbjjdwrxvlnlvwokqflrchlaywokussetdnybhxzsmkpkybbgosiwgiwcxgwradmfsmhzkguwsjhtlizbchziswmrcjifowkgitisbcrunanakocmxbxpxjicushiotpxnxrobikoixpunrhlsgcsrlwmdfusylplkgclrmcbkrwzkfkelnyeyuqdznvyamllvnymacnmvllfqymdlkilfaognmgqysbvfbjhextbkhhdftgsfqdmrttgfbwgtzdbdnijmekwntzsoikuypiridaqfyyaybbdommasyxfsyxggjchylyiqayvzywxazcolordookgmhpvstcqgcbxdzseaqbaqfqdvhjjvtqkbhhtajmhnneqoyuopxqhehkzotjmnbyqiflkoztdmzwdaqtpqkyuriwhefvtgtjqywcowyskxonxghoytovmxrtdypwgihyjdazzytkyjzxqioqbcnnbgheeyakihitnltmlmyjwyjogxeizuxbaghfeirprcienbtyqrkmrvaasgktchwdoekuobjffsmsvftlyfxqazquiankjkpxozucddjixxdtcweddevffnznpoayypyopssuxecxbfqgdwjgaglgtmvibvibngseakyaqaxuipalllsorfwksrutpcuelminzgnriklqzlcnwwbpbxzvqvohylllztyaboskadccrgppcsfgrgbhcsrcfcngynhbbbncgqexyvpbnujeamneeegljtsjhbkkcamissiqnxrarcetpsyvyehhabqjcbtgdiovawlqtfqmhxgwrgupmdxoepxistovdeqfdcvyhmloltnczhrnkqcqgzayuquxumfzoayxolozeddfkxswnuovwowqeqqaevctxasmlgnpjrwvootdjhzhxvzdnpgrmimmifavnnkxgiuwwoahxbovwqalhgcworiwyitlxdkenfakvatsbkpzaqkhwpdnillgvfrtkexyjzigcdydnqfpgrxegcroqduliogssfqdfalhglmtbrjjjiormhgckcqsswnmcfrhgcqoochrusbfcrwpyerjjhdbgsqiyhrgmhucjdtfwwmanjpopjxasceyvugvdzbpgvtsapxwlkzbvopmxonqsrqplxkqwlgfibxjquheggfdxwqwmfoewfujegzcuhhclenbbxfjfmncifbumpbiuxtadudxekcprrquqyfwksatzbpltsvnpqovltspdwgwqysgwyehsfcsitfbmdrdthygatxfrdchcuoysshlzlfifmltpcyljxrlsprjuttwpjxkbexdsenzqysidqtopmajbrvwmoudxrpaymdqsspjtjtwbomtameefzctpwxoqmpobugtnxeiizelnqeofjskkugasdoirfyucgqpfuznudzjvfxaqrnbntdiyrqrzrmbxcsdyrsuwterzdurxjskcvscpltqchrbjlgkczgyumrtqlnnufzyduauhwklddmpotbsuhsoulkmxxbtcauhwwbdsnqysdniyoasvugrgqdfneashubftdjnsblneyvcoyumsddatjhjnidueeaxjllemyrtxmxnkszfxfhqopbbxeydladunoybopwlcubooavlfddvsfxrlxuwzxrmnrpchmpliqbwtxhyckuuptldshzrfsfukwwtiogqehoxgvyigucxppahzcygwfaibzbmnjetrttzoriwnmucewldaljxqjfrkjdxsitldmlrfvoshkwnghqhszgilnbvwhvrroeuaplhmbzulxhueabybjimwjkvqhmjvqdxireuufqgcaaiadgbmoqkzafshtbemhduahquohasjcajfimryccxejpndtrpcwlcdbwtkzltbnchxpavtevyqmltffkjbvlhwkajjocmdhvbywyrctpsidnpixzlsksrwvaflcuojprhlqbqlqivtwldtkpowjftefaphugtkxcxpdndwyyrujvpvmdsxklcpntzibusbwpqcdvybupxfmobautyegcwtxvbzpvanlspqoptkhspviswclwjtafnxcqytmaiztarjpmtygkuodstqockqjznnpmgdmqehqxqgjlgrwagbuzrkdbaocobscjxqzeyqbqynegechmddnuosyogaejuiuuzuyzmzrmovutxbfchvzvnzjuzqfwyaqxwqykrqygnsznwgpddoyrnjnpzsnysdxqvyamqysdttqpcgsfwswkbjzdemdyrcpoaraqstulomcquuwroudrgcumqzkjcbxctzvlsryhdazawxrksubayy"
words6 = ["otftdranhdxytfnvwgkzroukdj", "iflkoztdmzwdaqtpqkyuriwhef", "lbsjkymmpjmtlfkuxxlghowsyz",
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

ss7 = ""
words7 = []
ret = so.findSubstring(ss6, words6)
for str in so.strlist:
    print("str---->", str)
for i in ret:
    print("ret i--->", i)


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        timeused = 0;
        for i in range(0, len(points)):
            if i + 1 < len(points):
                newi = abs(points[i + 1][1] - points[i][1])
                newj = abs(points[i + 1][0] - points[i][0])
                timeused += newi if newi > newj else newj
        return timeused
