# Task: dycrypt text with Visioner cipher r = 2,3,4,5 and r in [10, 20]


def list_to_string(Y):
    Y_str = ""
    for i in Y:
        Y_str += chr(i + 1072)
    return Y_str

def to_Z_ring(text):
    X = list()
    for i in text:
        X.append(ord(i)-1072)
    return X

def Encryption(X,K):
    X = to_Z_ring(X)
    K = to_Z_ring(K)
    Y = list()
    r = len(K)
    for i in range(len(X)):
        Y.append((X[i] + K[i % r]) % 32)

    print(list_to_string(Y))


##########################################################

def Sorting(d):
    sorted_values = sorted(d.values()) 
    sorted_dict = {}
    for i in sorted_values:
        for k in d.keys():
            if d[k] == i:
                sorted_dict[k] = d[k]
                break
    return sorted_dict

# Y - block of text - количество появление букви t в Y
def Nt(Y,t):
    count = 0
    for i in Y:
        if i == t:
            count += 1
    return count
    

# Index I(Y) - индекс соответствия
def I_Y(Y):
    n = len(Y)
    I = 0 
    N = 0
    choosen = ""    
        
    for i in Y:
        if i not in choosen:
            N = Nt(Y,i)
            I += N * (N - 1)
            choosen += i
    I /= n * (n - 1)
    return I


#################################################################
# (*) Function that finds length of key (r) for given CT:
def Index_for_r(text, r):
    # key_len = 0
    # max_I = 0
    d = dict()
    I_avarage = 0
    for i in range(len(text)):
        if i < r:
            d[i] = text[i]
            continue
        d[i % r] += text[i]
    print(f'r = {r}:\n---------------')    
    for key in d.keys():
        I_avarage += I_Y(d[key])
        print(f'I_{key} = {I_Y(d[key])}')
    print(f'---------------\nI_average = {I_avarage / r}\n---------------')        
    I_avarage = 0

    d = dict()





def main():    
    text = "вэтойстатьеприведемнебольшуюсоднойсторонышутливуюносдругойстороныполностьюнаучнуютеориюспомощьюкоторойможнооправдатьсебявтемоментыкогданадвамивзялаверхленьделовтомчтовфизикесуществуеттакаятермодинамическаявеличинакакэнтропияеенаучноезначениеопределяетмерунеобратимогорассеиванияэнергиивдругихслучаяхонажеможетопределятьвероятностьосуществлениякакоголибомакроскопическогосостоянияоднакоскажемтаквбытупрощепонятьзначениеэнтропиикакмерынеупорядоченностисистемычемменьшеэлементысистемыподчиненыкакомулибопорядкутемвышеэнтропияздесьсделаемнебольшоеуточняющеезамечаниеотомчтотакоепорядокэтооченьважнопотомучтоситуациюкогдачтоторавномернораспределеноподоступномупространствуможноназватьбеспорядкомилихаосомеслинапримерречьидетомусореравномернонакиданномнаполвкомнатеноподобнуюситуациюможноназватьипорядкомеслиречьидетнапримерокачественноиравномерноокрашеннойстенетутужкомучтоиукогокакиеассоциацииоднакомыдоговоримсядлянуждэтойстатьичтокакивсефизикиидругиеученыебудемпониматьподпорядкомналичиенекоторойвыраженнойструктурывсистеменапримерсуществованиеконкретныхпредметоввопределенныхточкахпространствааподбеспорядкомравномерноераспределениевсехвидовматериивпространствевтакомслучаеэнтропияэтомерабеспорядка"
    print(f'X = \n-------------------------------------------------\n{text}\n-------------------------------------------------')


    # keys
    k_2 = 'ня'
    k_3 = 'три'
    k_4 = 'шифр'
    k_5 = 'цезар'
    k_17 = 'гиперболоидгарина'
    keys_array = [k_2, k_3, k_4, k_5, k_17]

    text = "пьянцряяяытоэзпдсдщмтаыкйчаэюнсмыиюсыпымичасшзптлмырспавыиюсыпымиоыкънюсйэъяацътлстнэзлрьнщнжылйысыпыищнумыньпнбсяяыюдоюпстлылтмяъчнргнмнгпящзпжмкнбтпвктмйгткыбянщцянпухжхйтраштрябадяснйнюядэлыгхмнлхцтрчямбткхцхмнйнйкмяпыохютдъяацънтжъяддъзтньптгткмдялтпамтнопнсхлывыпнрюдхбнмхюкмтпрзхбспавхфюкацнювнъяудщнудяньптгткмсйбтпыюямыряыыраштрябшдъзмйнйывыкхаылнйэнюйыохцтрчнрнюнюсыюъзмнсмнйырчяудщснйпаисаоэнждьнъюяыфмнцтмхдкмяпыохзчячлтпимттьнэюснддъмырязюзюстлицтлщдъыедкктлтмяъюзюстлиоыгдзъдъъчячнщтшзоньнэюсйастлпъедкмяпыохюфгтрйрсдшятлъдоншыенттяндммэждтжнлтцнмхдысылдсыснйыдьнэюснчьяныцтмйбнеъньнянщтдсырхсаягзлйывсядсысыпнбънщдэмыпнрьптгтктмыоыгырятьмылаоэнюсэяърябалыеънъяфбнсйатрьнэюсйылхкхфннюнщдюкхмноэзщдэптцйзсдянщтюнэдэяпмылтпънъячзсяъмылъяьншбчнщмнстмыоыгыаътлрхсаягзллыеънъяфбнсйзьнэюсйылтршзэддыхгтсъяьпхлтпыйнцтрябтмънхпнбънщдэмынчпнчтмънцрядъдятятуйылацянхтчнрнчячзтяюрыххягзхнсмнйылигывыбыпхлююскммаесьянцряяяыхцянчячзпртухжхйхзспавхдацтмидотсдщоымхлнсйоыгьнэюсйылъяшздзтмтйысыпыипъэяудъмыиюсэтчсапибюзюстлтмноэзщдэраштрябыбнмхдчнъйэдямифьптгщдянпбыоэдсдшдъмифяндйнфьпыряпнмюспяноыгодюоыпмгчнщпнбънщдэмыдэяюоэдсдшдъзтбюдвбхгыбщяядэзхбьпыряпнмюспдпснйылюкацндкмяпыохюксылтпнатрьнэюсйн"
    print(f'for r = 2:')
    print(I_Y(text))

    text = "фнъащщдръохчвшкчфнюэнуюуоиырбццэцыбъаацялаевуътырэцгфшеуцыбъаацялчаыхабъоохтгяягждхцвшжгяцююбоотавцвюсююояюцбаиффидмщчсзфвнююфчэънъцхфиярмфрфътпсыифхшзыняммчыцфвцюзъатьъчрьхщейнгвкехъдрттпъчафафрярфъзнгъистнэшяъэиьртпэъвючъпнчэиезхахпярячэрчючвхмчызчвфчаыяхцуаидшфауцврщгхрфрхъпеяхшхшрффшеурзбуезисецярочьцшхъаяшчфнэпъотнвюздэцгвдабылхщдтучэрсъиьюлаыруюфтъшабтаярйхщьюлабцгвцсэрсюмяртабттцнювиьтйнвыбацлхчаэздмпярячэрчнхдацбшрьртюхшнэнеяцвпмазняэцгвргшщдхфнзнюьнямачнучьнявггшщдхфняццзряххнъиьюфеыруючаазцъыдхффлачнхдацбшзщфнгмщцхутхфяхйаыдкюневцйэзрйнччиюхятэрчюъаьядюътъцчяцвпмаъедюцйххотишэцбюъаьыйвцгшъерюъотаумтзъавцвркяюфчахааигяшчфнэххаяццющдгчяюфеяшабъврхгвкеьцшэцярпфръоснгяцвпмьюфъырзрцгюфчбуъэибарюхшвхяошмчвцюгщаанвркяюфчахаэиьшмтэхаьхтяцэттаьхтвняючафцуэырбрдгиишжююояюхтчктвдъяцвпмьюфчбуъанймрцхъярчвшфчацьрячбъфххяюрвркяюфчахаютврачэхащщдххчвыдгоьюфезъашыьюлаъиьшнтбщажртжръюмяртаьгцюлатцвшфгпмэпхецмпвцыбътвдъзъаъиьшкгхьъчрьшрцаыхшнезнялнугмчьчаэрюръояццяцвпмьюфяруъзрчэньюъаацытгврочэхащщдаыьвывлкгшщдхфчэибарюхшггбчбъфюктэрчъцяъшчвхнечвхмюхъаткаяшчфнэххялэдюяьрэбацгвштэщдтитяццснгяцвпмьюфвркяюфчахахштбчвхмчыняшнфбнзтрцюкюръчарътчвющдаиябъфхкдртаьщэгятхеявшаярснъаьнврйчбчаазцъи"
    print(f'for r = 3:')
    print(I_Y(text))

    text = "ъежюбщжркдщяирцхьнаээйвыфазойцшэжсевжшвэуазвгрцгцхвбьшзужсевжшвэучвыецевфжбрлябгцъщюиртбзцаюсдтъжъважсаююхвюзшфтьижмйнхпъъщьжфщэкгююымфэшмцрдрцччуфтэшйыэхрфэувткцазкццдапьъэщзйэщжтлнжвштфпкндьжмьэшфьзэщюрчкщыаяьэштфъххжажчьпэнбрлябюэпбрпнбшэцгаэмщычнжьэшзээцхашъььжлвашщехакфэазсээшчшакшалльейуззшзйюеиъхдцъхкцгаэмщычъртэшвпкхвбкдвблбщбккяхеруъштвужуьсжффъицеъжчьзэщююыцеюйъвперуюьхфъжщюрюнавштцсуъзяицнхзцбпкдыэшящэансэкшвяарюрвфщаухщгзцдпьцлхехвбкрешйъщьуящьднбмрнсыэфщэкгешйъщьучвфпрбхегюрвцаггрхюзцдпьтзвэфцлрнсэкшвяазыфэщрбьнярэфбхщцямрцщгкцлэчжнхэпфьэяфэанввжфлвжъфъжнгюизшювежюжящэфкфцецгюкцагпъвбаъзрортъжлшрпъввжшфтецахихвашщгаэмщыэхвяжмвбкыгэжфзяицевииббккзьжобюеиытшърсэщгюизшъжфьыаэфюйцахйуьэшчдшдндаэяршьнжюдыеюиндръхвьэшбюеиюшьибэжфбрзцятвцаэшъщэжчвфжйбгцщьвликшцфвцецбрякфвфргюизшъжфщбгрдхпдьфэъбрзшььэшвъшящбккщэецьашкбюдндэжцюашащэецэбкнбхкыжгютвьляжюаыююыцюрврщрйщвжаикшацшэштвьумвужкваафепьууэлошнкцэбкижмаяжювиюшъщщдапьъаршалльхлящэунхгьнаяжхььшъряжмгюизшъжфбргрлшэхщъжъважсцлииъхехвщйъдгвъзаукешйъщьэхфяирахищзйэщжтжкфэанююетдхкхпезшщфднжюъквяиншхгнбэуэжюптфезшвбкшфэйъцршчвфщнеяжшуфвцаашкбюдндэжндрйчдхьняхерщтйнйтамвтдижхирьтзшвбкшфэйъцхъъфъжфеыляфхххжажчьпхъвьэшфсэщгюизшъш"
    print(f'for r = 4:')
    print(I_Y(text))

    text = "швщощзчзтмыфчитыйммэыжхлмошесюътхйбиучоэсэътыюзъюэдцлргщурсвдххнлеутнюзчгюэцшюнгфчмоаюгшпювуаьоаущоадоуоцгухпацзлавтцмбпшчммювкфтлаукдргелврвнйзпбейеалрмнмъктотиуучвдзыичюпмсгпкшттйкщтраежтхжсхдшгеуизыцсапшктизютзкравфтадфпяхытзузгумзэцьмншыуцрхъктяхисмрггкхбацчпмющучабзкпвргнжээыхкишшйчууюъшлгнежхюгенеьдлмтюехмдхбдщьтыххявгуштмдцъщхзчйлхгнжкраукоыюжхмраххсъдфпчхзпхгюзуштюхтпяюътзкюзпзжхвчзктчащуяжуаеядтжтмэтзчхгнмээиххпшюпзкьыхвнхйфхрпъуюеэгуштшзнштхваюеьвкфьиывтеьытщыбюцщеьсфхдзютмнлаесоьйрпбюеучяфашщеьшаяенгччояюдодхзбшдхбеммэыжхлмоумувдьфяопкмзрвкюаэюкхтювьщовцпхеядхждюавщоюнкфьтцлфоядчхмгнчхсшишзцшфпхгфцьщовдхзвэдсмрэдхзсяжклеыытхпюъуштгетхмгеххсвжефсвшшуоцгуфачшещьсыццоахйсоьюрпхрдцхмхзрпнрехпмхжхмчмюймтювшшоаыхзвэдсмрэдтзкшъефнювтзпюбзсоьгещеэдфхдючтъюбючъажюгуоцгуфачшещьшеучяфаууеббнчезтнлевгецршвкчоъцьмсвшкфнююхзвэдсмрэдусррокфнюяцщеэычътгьпхмгнчхигаукоъцпперзцхцшцыпиюътзкювалоудзхршвцждыхтъжфучхйбиещьшнчхкранйсхкноиъюнлргщнмузытвесййммядтпмрибцофеучяфауунрбнюихгксовдххйтсхзжхгтхйбихъквйхввбюцщеьытзпаюсмрбйюмсвшуйаэюксоэахмтэсъцрхъсмтюшзхпаыймлхгтвхвдьсаееххсвжефсвшезпюъжмсядхждъдсчатгууеагумррзфчефырмншызшеешнлотвещеаюнйпадцщрргцщвхшчзкювцтузцкднвжуципучхмхжеиебеучяфае"
    print(f'for r = 5:')
    print(I_Y(text))

    text = "еебущталадйтршктдифькспщзжывфофхыйфъэхюойгбъплвгжъофмяшупчьацфснлчылрцачмяылбясцювнырлжафюньдкжостюшыйпцхтюпэыокигтмщтбвкбкьпърыъяноумннгмсеьйртнудееаэшердукыпрэьфыхотьхзлтфцгъуьакчитвичавъфхьптуыирлчхщчавкфршшцшотднээъэотрокхооюехтизэидеррфуясупуугитьнэурнэжабауъцзсррщюелкптшалшушзлитмэужрдцыфелнэтрацнщойнбуясупуугхьтнэовъьубукщяыэисвкшерропрльоьумдоьичрсщщуяйеряттжобцютсзьнпптшоттфкротмхищзсьаюэштьеяцъяхдцтршушцнбртацьилтппьжюжынчтоазсоъньтютауярххеьгдепффтмщуищнринвгюифъфслрьперсинлтнксфвршвьъьшгзкгътмегзкноаыьчмвзфнюьфмфрржъшуйтоьицтухцжтпязрупдпезиъиицбуьшащаиосеяцэязцщввпьвухаеацхыпсъэсгшащярццажрлкслуезуьэьшденюфтррцяебрюртнпинючыдсщбшяоьчбчфссвшннфъсшьпфшьхдквръйбищюуаатхьфмоиеиыссффцыйылэшмпеаштчяруквпъюяцфирркъопнятюоохцмдрнюфъатцъзъпъшоъйрояцсодхвгбйаюоюмбмюоъорицзрукуэцфвдъцщефучххшкутнцраяшхмишэпршуьакйрнюрэаехэсхсыщьтфгшххъомщбкэжаюаыкноьыдтсрвпюдьхотмиабщыцлиеншптшоттпыфцроецяньтнпщзсцжфеяомщбевэцвацогкшкюечрцнъйцпюызлегятнюнршфжъъьхмпавдьозчэхпешщъхдоизртнитэчюсьфргфгжххъомщбхглаююгжфибътмихпфайърющчьебъпоеиьнхльшшшйхнлэьримыквпрньчфидхутнргдчюшшлгчфссвшннфъсеррьппнхтоазсксфяетоьчушссеаиюпунукыжыуукхихтрсоефпчхсцурчфссвшннфъсктуохьфхоузитэръяуяйниацриррйтстцядфло"
    print(f'for r = 17:')
    print(I_Y(text))

    
    for k in keys_array:
        print(f'-------------------\n------ {k} ------\n-------------------')
        r = len(k)

        C_text = "" # Cipher Text

        # # Convert characters to Z-ring
        # X = to_Z_ring(text)
        # K = to_Z_ring(k)
            
        # Y = list()
        # for i in range(len(X)):
        #     Y.append((X[i] + K[i % r]) % 32)

        print(f'Y = \n-------------------------------------------------\n{Encryption(text, k)}\n-------------------------------------------------') 


        print(f"Сonformity Index for r = {r}")
        # Index_for_r(text, r)
        print()

if __name__ == "__main__":
    main()






# Clearing 'dirty' text
    # text_dirty = "В этой статье приведем небольшую, с одной стороны шутливую, но с другой стороны полностью научную теорию с помощью которой можно оправдать себя в те моменты, когда над Вами взяла верх лень. Дело в том, что в физике существует такая термодинамическая величина как энтропия. Её научное значение определяет меру необратимого рассеивания энергии. В других случаях она же может определять вероятность осуществления какого-либо макроскопического состояния. Однако, скажем так, «в быту» проще понять значение энтропии как меры неупорядоченности системы: чем меньше элементы системы подчинены какому-либо порядку, тем выше энтропия. Здесь сделаем небольшое уточняющее замечание о том, что такое порядок. Это очень важно, потому что ситуацию, когда что-то равномерно распределено по доступному пространству можно назвать беспорядком или хаосом (если, например, речь идет о мусоре, равномерно накиданном на пол в комнате). Но подобную ситуацию можно назвать и порядком (если речь идет, например, о качественно и равномерно окрашенной стене), тут уж кому что, и у кого какие ассоциации... Однако мы договоримся для нужд этой статьи, что, как и все физики и другие ученые, будем понимать под порядком наличие некоторой выраженной структуры в системе (например, существование конкретных предметов в определенных точках пространства), а под беспорядком – равномерное распределение всех видов материи в пространстве. В таком случае, энтропия – это мера беспорядка."
    # print(len(text_dirty))
    # text_dirty = text_dirty.lower() # make all characters lowercase
    # text = ''.join(e for e in text_dirty if e.isalnum())
    # text = text.replace('ё','е') # raplace 'ё' on 'e'




